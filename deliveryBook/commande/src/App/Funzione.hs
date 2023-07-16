module App.Funzione where 


import Domain.Commandes
import Infra.BdCommandes
import Data.Time
import Data.List 

-- fonction au niveau applicatiif qui appelle le dommaine et l'infra pour sauvegarder une commande
-- a ce niveau les entrees sont les String 

type NomDuClient = String 
type Quantite    = String 
type LeCalibre   = String 
type Prix_Unitaire = String 


funzioneCommande :: NomDuClient -> Quantite -> LeCalibre -> Prix_Unitaire -> IO ()
funzioneCommande nameClient qte calibre prix  = do
    -- verifie si les champs ne sont pas vides.
    if null nameClient || null qte || null calibre || null prix 
        then fail "impossible de creer une commande sans les elements requis"
    else do
        let toIntQte = read qte :: Int 
            toIntPrix = read prix :: Int 
        case toIntQte > 0 && toIntPrix > 0 of 
            False -> fail "le prix et/ou le calibre ne peuvent etre nuls ou negatifs"
            True -> do 
                -- je recupere la date du systeme 
                date <- utctDay <$> getCurrentTime 
                 -- je fais la facture 
                let facture = toIntQte*toIntPrix 
                -- je verifie le calibre 
                case (verifCalibre calibre) of 
                    Left _ -> fail "le calibre ne correspond pas. il en existe trois : P, M , G"
                    Right someRightCalibre -> do 
                        -- je construis une nouvelle commande 
                        let someCommande = 
                                newCommande nameClient toIntQte someRightCalibre toIntPrix facture date
                        saveCommande someCommande

   
