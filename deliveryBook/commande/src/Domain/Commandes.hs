
{-# LANGUAGE TemplateHaskell #-}

module Domain.Commandes where 

import Data.Time
import Data.Aeson
import Data.Aeson.TH
import Text.ParserCombinators.Parsec



{- un calibre est soit: M pour moyen, P pour petit , G pour gros -}

data Calibre  = P | M | G deriving (Read, Show , Eq)
$(deriveJSON defaultOptions ''Calibre)

-- data Quantite = Alveoles Int | Cartons Int deriving (Show, Eq, Read)
-- $(deriveJSON defaultOptions ''Quantite)


{- une commande est definie par : le nom du client qui passe le commande , la qte commandee, le calibre, 
    la date de commandee prix unitaire de l'aleveole, la facture totale du client -}

-- le type Commande est un entity

data Commande = MkCommande {
    nomClient :: String,
    quantite :: Int,
    calibre :: Calibre,
    prixUnitaireAlveole :: Int,
    facture :: Int,
    dateCommande :: Day
    } deriving (Show, Eq, Read)
$(deriveJSON defaultOptions ''Commande)


-- fonction pour creer une commande : la facture du client est calcule pas 


type Qte = Int
type PrixUnitAlveole = Int
type DateCommande = Day
type NomClient = String
type Facture = Int 


newCommande ::  NomClient -> Qte -> Calibre -> PrixUnitAlveole -> Facture -> DateCommande -> Commande 
newCommande = MkCommande


-- parser d'un element de type Calibre 

parserCalibre :: Parser Calibre 
parserCalibre = do
    (char 'P' <|> char 'M' <|> char 'G') >>= (\x -> return $ (read [x] :: Calibre))
    -- linea seguente : altra possibilità
    --(\x -> read [x] :: Calibre) <$> (char 'P' <|> char 'M' <|> char 'G') >>= return 

verifCalibre :: String -> Either ParseError Calibre 
verifCalibre = parse parserCalibre "il n'existe que trois calibres: P , M et G"