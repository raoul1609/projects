
{-# LANGUAGE TemplateHaskell #-}

module Domain.Commandes where 

import Data.Time
import Data.Aeson
import Data.Aeson.TH



{- un calibre est soit: M pour moyen, P pour petit , G pour gros -}

data Calibre  = P | M | G deriving (Read, Show , Eq)
$(deriveJSON defaultOptions ''Calibre)

{- une commande est identifiee par : le nom du client qui passe le commande , la qte commandee, le calibre, 
    la date de commandee prix unitaire de l'aleveole, la facture totale du client -}

-- le type Commande est un entity

data Commande = Commande {
    idCommande :: String,
    nomClient :: String,
    quantite :: Int,
    calibre :: Calibre,
    prixUnitaireAlveole :: Int,
    facture :: Int,
    dateCommande :: Day
    } deriving (Show, Eq, Read)
$(deriveJSON defaultOptions ''Commande)