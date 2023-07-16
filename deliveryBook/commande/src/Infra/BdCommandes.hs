
{-# LANGUAGE OverloadedStrings #-}
{-# LANGUAGE BangPatterns #-}

module Infra.BdCommandes where 


import Database.MySQL.Simple
import Database.MySQL.Simple.QueryResults
import Database.MySQL.Simple.Result 
import Database.MySQL.Base.Types
import qualified Data.ByteString.Char8 as B
import Domain.Commandes (Calibre , Commande(..), verifCalibre) -- Commande(..) veut dire import ele type Commande avec tout ce qui va avec


instance Result Calibre 

-- This class performs automatic extraction and type conversion of rows from a query result.
instance QueryResults Commande where 
        convertResults [fa,fb,fc,fd,fe,ff] [va,vb,vc,vd,ve,vf] = 
                MkCommande a b c d e f
            where   !a = convert fa va
                    !b = convert fb vb 
                    !c = convert fc vc
                    !d = convert fd vd
                    !e = convert fe ve 
                    !f = convert ff vf
        convertResults fs vs = convertError fs vs 6

-- FramField : classe des types qui peuvent etre convertis a parti d'un byteString
instance FromField Calibre where 
    -- fromField est un tuple, le premier correspond a Type dans le bd, le deuxieme est une fonction :: BytesTring -> Either String a
    fromField = ([VarChar], \someval -> do       
        case (B.unpack someval) of
            something -> do 
                -- j'analyse le calibre venant de la bd 
                let parsedCalibre = verifCalibre something
                case parsedCalibre of 
                    Right x -> Right x 
                    Left _ -> Left "un element de type calibre est soit P, M ou G"
            _         -> Left "erreur de convertion du type Calibre") 



request :: Query 
request = "INSERT into commande (nomClient, quantite, calibre, prixUnitaireAlveole, facture, date) Values (?,?,?,?,?,?)" 

-- fonction pour sauvegarder une commande dans la table commande, qui est dans la bd nommee commande.

saveCommande :: Commande -> IO () 
saveCommande uneCommande = do
    connectionToDB <- connect defaultConnectInfo {connectHost = "localhost", connectPort = 3306, connectUser = "nkalla",
         connectPassword = "Ange1308!!", connectDatabase = "commande"} 
    responseToRequest <- execute connectionToDB request (nomClient uneCommande, 
        show $ quantite uneCommande, show $ calibre uneCommande , show $ prixUnitaireAlveole uneCommande, 
        show $ facture uneCommande, show $ dateCommande uneCommande)
    close connectionToDB >> print responseToRequest



    
                    
