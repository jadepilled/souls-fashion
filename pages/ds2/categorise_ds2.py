import json

# Your JSON data as a list of dictionaries
data = [
    {
        "name": "Agdayne's Cuffs",
        "image": "Arms/Agdayne's Cuffs.png",
        "primaryColor": "#9c989a",
        "secondaryColors": [
            "#645d5b",
            "#5a4436"
        ]
    },
    {
        "name": "Alonne Knight Gauntlets",
        "image": "Arms/Alonne Knight Gauntlets.png",
        "primaryColor": "#d0cfd3",
        "secondaryColors": [
            "#9d9aa2",
            "#707286"
        ]
    },
    {
        "name": "Alva Gauntlets",
        "image": "Arms/Alva Gauntlets.png",
        "primaryColor": "#979695",
        "secondaryColors": [
            "#605c5a",
            "#4f423b"
        ]
    },
    {
        "name": "Archdrake Gloves",
        "image": "Arms/Archdrake Gloves.png",
        "primaryColor": "#959a98",
        "secondaryColors": [
            "#575a52",
            "#565a54"
        ]
    },
    {
        "name": "Astrologist's Gauntlets",
        "image": "Arms/Astrologist's Gauntlets.png",
        "primaryColor": "#a28d69",
        "secondaryColors": [
            "#544f4a",
            "#4f4737"
        ]
    },
    {
        "name": "Bandit Gauntlets",
        "image": "Arms/Bandit Gauntlets.png",
        "primaryColor": "#9c9b99",
        "secondaryColors": [
            "#666256",
            "#514936"
        ]
    },
    {
        "name": "Bell Keeper Cuffs",
        "image": "Arms/Bell Keeper Cuffs.png",
        "primaryColor": "#635b4e",
        "secondaryColors": [
            "#5f5850",
            "#4c443a"
        ]
    },
    {
        "name": "Benhart's Gauntlets",
        "image": "Arms/Benhart's Gauntlets.png",
        "primaryColor": "#5a5149",
        "secondaryColors": [
            "#535034",
            "#4d443a"
        ]
    },
    {
        "name": "Black Dragon Gauntlets",
        "image": "Arms/Black Dragon Gauntlets.png",
        "primaryColor": "#9d9b99",
        "secondaryColors": [
            "#5e6153",
            "#615e54"
        ]
    },
    {
        "name": "Black Gloves",
        "image": "Arms/Black Gloves.png",
        "primaryColor": "#8e9696",
        "secondaryColors": [
            "#5c6362",
            "#5b645c"
        ]
    },
    {
        "name": "Black Leather Gloves",
        "image": "Arms/Black Leather Gloves.png",
        "primaryColor": "#8e8c8c",
        "secondaryColors": [
            "#656a65",
            "#636565"
        ]
    },
    {
        "name": "Black Witch Gloves",
        "image": "Arms/Black Witch Gloves.png",
        "primaryColor": "#918e92",
        "secondaryColors": [
            "#5d5663",
            "#5e5468"
        ]
    },
    {
        "name": "Bone King Cuffs",
        "image": "Arms/Bone King Cuffs.png",
        "primaryColor": "#6c685b",
        "secondaryColors": [
            "#565249",
            "#484539"
        ]
    },
    {
        "name": "Brigand Gauntlets",
        "image": "Arms/Brigand Gauntlets.png",
        "primaryColor": "#c7b190",
        "secondaryColors": [
            "#b5a48a",
            "#a6906f"
        ]
    },
    {
        "name": "Catarina Gauntlets",
        "image": "Arms/Catarina Gauntlets.png",
        "primaryColor": "#d0c6b2",
        "secondaryColors": [
            "#c4b9a2",
            "#b1a48d"
        ]
    },
    {
        "name": "Chaos Gloves",
        "image": "Arms/Chaos Gloves.png",
        "primaryColor": "#585550",
        "secondaryColors": [
            "#4e552e",
            "#494538"
        ]
    },
    {
        "name": "Creighton's Chain Gloves",
        "image": "Arms/Creighton's Chain Gloves.png",
        "primaryColor": "#5f6359",
        "secondaryColors": [
            "#605f56",
            "#605e58"
        ]
    },
    {
        "name": "Dark Gauntlets",
        "image": "Arms/Dark Gauntlets.png",
        "primaryColor": "#cfd0d2",
        "secondaryColors": [
            "#959799",
            "#6a706b"
        ]
    },
    {
        "name": "Desert Sorceress Gloves",
        "image": "Arms/Desert Sorceress Gloves.png",
        "primaryColor": "#525132",
        "secondaryColors": [
            "#514744",
            "#4a413d"
        ]
    },
    {
        "name": "Dingy Cuffs",
        "image": "Arms/Dingy Cuffs.png",
        "primaryColor": "#9c938c",
        "secondaryColors": [
            "#867466",
            "#695c53"
        ]
    },
    {
        "name": "Dragon Acolyte Gloves",
        "image": "Arms/Dragon Acolyte Gloves.png",
        "primaryColor": "#949394",
        "secondaryColors": [
            "#67676b",
            "#656868"
        ]
    },
    {
        "name": "Dragonrider Gauntlets",
        "image": "Arms/Dragonrider Gauntlets.png",
        "primaryColor": "#d6d7d8",
        "secondaryColors": [
            "#97989a",
            "#56585b"
        ]
    },
    {
        "name": "Drakekeeper Gauntlets",
        "image": "Arms/Drakekeeper Gauntlets.png",
        "primaryColor": "#5b5b5b",
        "secondaryColors": [
            "#535355",
            "#4d4f4e"
        ]
    },
    {
        "name": "Drangleic Gauntlets",
        "image": "Arms/Drangleic Gauntlets.png",
        "primaryColor": "#8a6f61",
        "secondaryColors": [
            "#585450",
            "#5e463a"
        ]
    },
    {
        "name": "Elite Knight Gloves",
        "image": "Arms/Elite Knight Gloves.png",
        "primaryColor": "#ad8a6d",
        "secondaryColors": [
            "#916d52",
            "#795b43"
        ]
    },
    {
        "name": "Engraved Gauntlets",
        "image": "Arms/Engraved Gauntlets.png",
        "primaryColor": "#a2a090",
        "secondaryColors": [
            "#8a8876",
            "#636052"
        ]
    },
    {
        "name": "Executioner Gauntlets",
        "image": "Arms/Executioner Gauntlets.png",
        "primaryColor": "#8c8f90",
        "secondaryColors": [
            "#5a5d56",
            "#585a5b"
        ]
    },
    {
        "name": "Falconer Gloves",
        "image": "Arms/Falconer Gloves.png",
        "primaryColor": "#87735b",
        "secondaryColors": [
            "#6f5d49",
            "#5b4835"
        ]
    },
    {
        "name": "Faraam Gauntlets",
        "image": "Arms/Faraam Gauntlets.png",
        "primaryColor": "#dbdbdc",
        "secondaryColors": [
            "#919294",
            "#7a7b82"
        ]
    },
    {
        "name": "Gauntlets of Aurous (Invisible)",
        "image": "Arms/Gauntlets of Aurous (Invisible).png",
        "primaryColor": "#9097a9",
        "secondaryColors": [
            "#8690a9",
            "#7684a0"
        ]
    },
    {
        "name": "Gauntlets of Aurous",
        "image": "Arms/Gauntlets of Aurous.png",
        "primaryColor": "#696655",
        "secondaryColors": [
            "#5d514e",
            "#4f4638"
        ]
    },
    {
        "name": "Grave Warden Cuffs",
        "image": "Arms/Grave Warden Cuffs.png",
        "primaryColor": "#616457",
        "secondaryColors": [
            "#5e5f50",
            "#585826"
        ]
    },
    {
        "name": "Gyrm Gloves",
        "image": "Arms/Gyrm Gloves.png",
        "primaryColor": "#867353",
        "secondaryColors": [
            "#766748",
            "#655635"
        ]
    },
    {
        "name": "Gyrm Warrior Gloves",
        "image": "Arms/Gyrm Warrior Gloves.png",
        "primaryColor": "#87694f",
        "secondaryColors": [
            "#775d46",
            "#6a5832"
        ]
    },
    {
        "name": "Hard Leather Gauntlets",
        "image": "Arms/Hard Leather Gauntlets.png",
        "primaryColor": "#67564b",
        "secondaryColors": [
            "#5c5733",
            "#564538"
        ]
    },
    {
        "name": "Havel's Gauntlets",
        "image": "Arms/Havel's Gauntlets.png",
        "primaryColor": "#999a9b",
        "secondaryColors": [
            "#5c5e5c",
            "#3a4449"
        ]
    },
    {
        "name": "Heide Knight Gauntlets",
        "image": "Arms/Heide Knight Gauntlets.png",
        "primaryColor": "#d8d8d9",
        "secondaryColors": [
            "#9d9c9d",
            "#616660"
        ]
    },
    {
        "name": "Hexer's Gloves",
        "image": "Arms/Hexer's Gloves.png",
        "primaryColor": "#a99e8e",
        "secondaryColors": [
            "#948676",
            "#87786b"
        ]
    },
    {
        "name": "Hollow Infantry Gloves",
        "image": "Arms/Hollow Infantry Gloves.png",
        "primaryColor": "#6a6a6a",
        "secondaryColors": [
            "#524e1b",
            "#0c5e0c"
        ]
    },
    {
        "name": "Hollow Soldier Gauntlets",
        "image": "Arms/Hollow Soldier Gauntlets.png",
        "primaryColor": "#867563",
        "secondaryColors": [
            "#6d5f4f",
            "#625e53"
        ]
    },
    {
        "name": "Imperious Gloves",
        "image": "Arms/Imperious Gloves.png",
        "primaryColor": "#a09997",
        "secondaryColors": [
            "#8a7268",
            "#6b5952"
        ]
    },
    {
        "name": "Imported Manchettes",
        "image": "Arms/Imported Manchettes.png",
        "primaryColor": "#646255",
        "secondaryColors": [
            "#5e6130",
            "#5a4f49"
        ]
    },
    {
        "name": "Infantry Gloves",
        "image": "Arms/Infantry Gloves.png",
        "primaryColor": "#524f13",
        "secondaryColors": [
            "#484848",
            "#50342f"
        ]
    },
    {
        "name": "Insolent Gloves",
        "image": "Arms/Insolent Gloves.png",
        "primaryColor": "#9f928d",
        "secondaryColors": [
            "#887269",
            "#70594f"
        ]
    },
    {
        "name": "Ironclad Gauntlets",
        "image": "Arms/Ironclad Gauntlets.png",
        "primaryColor": "#cdcdcd",
        "secondaryColors": [
            "#9c9d9c",
            "#6d7068"
        ]
    },
    {
        "name": "Jester's Gloves",
        "image": "Arms/Jester's Gloves.png",
        "primaryColor": "#6f5743",
        "secondaryColors": [
            "#5b5029",
            "#634833"
        ]
    },
    {
        "name": "King's Gauntlets",
        "image": "Arms/King's Gauntlets.png",
        "primaryColor": "#9a9999",
        "secondaryColors": [
            "#595755",
            "#47413c"
        ]
    },
    {
        "name": "Knight Gauntlets",
        "image": "Arms/Knight Gauntlets.png",
        "primaryColor": "#ab9b92",
        "secondaryColors": [
            "#a18974",
            "#897364"
        ]
    },
    {
        "name": "Leather Gloves",
        "image": "Arms/Leather Gloves.png",
        "primaryColor": "#857063",
        "secondaryColors": [
            "#6e5c50",
            "#5e4637"
        ]
    },
    {
        "name": "Leydia Gauntlets",
        "image": "Arms/Leydia Gauntlets.png",
        "primaryColor": "#a99d90",
        "secondaryColors": [
            "#998a74",
            "#85796b"
        ]
    },
    {
        "name": "Lion Mage Cuffs",
        "image": "Arms/Lion Mage Cuffs.png",
        "primaryColor": "#aa915e",
        "secondaryColors": [
            "#937647",
            "#8a6b36"
        ]
    },
    {
        "name": "Lion Warrior Cuffs",
        "image": "Arms/Lion Warrior Cuffs.png",
        "primaryColor": "#897351",
        "secondaryColors": [
            "#615032",
            "#5e5329"
        ]
    },
    {
        "name": "Llewellyn Gloves",
        "image": "Arms/Llewellyn Gloves.png",
        "primaryColor": "#646752",
        "secondaryColors": [
            "#4b4a49",
            "#43413c"
        ]
    },
    {
        "name": "Looking Glass Gauntlets",
        "image": "Arms/Looking Glass Gauntlets.png",
        "primaryColor": "#9ea0a0",
        "secondaryColors": [
            "#9da19a",
            "#636864"
        ]
    },
    {
        "name": "Lucatiel's Gloves",
        "image": "Arms/Lucatiel's Gloves.png",
        "primaryColor": "#5c5125",
        "secondaryColors": [
            "#5f4734",
            "#4b3424"
        ]
    },
    {
        "name": "Mad Warrior Gauntlets",
        "image": "Arms/Mad Warrior Gauntlets.png",
        "primaryColor": "#98999a",
        "secondaryColors": [
            "#5c6657",
            "#555e31"
        ]
    },
    {
        "name": "Manchettes of Judgment",
        "image": "Arms/Manchettes of Judgment.png",
        "primaryColor": "#898d8e",
        "secondaryColors": [
            "#646a65",
            "#55595a"
        ]
    },
    {
        "name": "Manikin Gloves",
        "image": "Arms/Manikin Gloves.png",
        "primaryColor": "#6c5d58",
        "secondaryColors": [
            "#5a4339",
            "#4b372e"
        ]
    },
    {
        "name": "Mastodon Gauntlets",
        "image": "Arms/Mastodon Gauntlets.png",
        "primaryColor": "#aca08d",
        "secondaryColors": [
            "#998969",
            "#887554"
        ]
    },
    {
        "name": "Monastery Long Gloves",
        "image": "Arms/Monastery Long Gloves.png",
        "primaryColor": "#c3b6a6",
        "secondaryColors": [
            "#b2a28f",
            "#9c8a76"
        ]
    },
    {
        "name": "Moon Butterfly Cuffs",
        "image": "Arms/Moon Butterfly Cuffs.png",
        "primaryColor": "#dad4ce",
        "secondaryColors": [
            "#c3bab1",
            "#aba297"
        ]
    },
    {
        "name": "Old Ironclad Gauntlets",
        "image": "Arms/Old Ironclad Gauntlets.png",
        "primaryColor": "#686760",
        "secondaryColors": [
            "#635f56",
            "#4f4832"
        ]
    },
    {
        "name": "Old Knight Gauntlets",
        "image": "Arms/Old Knight Gauntlets.png",
        "primaryColor": "#4e5653",
        "secondaryColors": [
            "#3a4544",
            "#37423c"
        ]
    },
    {
        "name": "Pate's Gloves",
        "image": "Arms/Pate's Gloves.png",
        "primaryColor": "#cbad91",
        "secondaryColors": [
            "#b99d89",
            "#b18a6e"
        ]
    },
    {
        "name": "Peasant Long Gloves",
        "image": "Arms/Peasant Long Gloves.png",
        "primaryColor": "#555555",
        "secondaryColors": [
            "#494139",
            "#483d3c"
        ]
    },
    {
        "name": "Penal Handcuffs",
        "image": "Arms/Penal Handcuffs.png",
        "primaryColor": "#5f5c53",
        "secondaryColors": [
            "#4f4943",
            "#48423b"
        ]
    },
    {
        "name": "Priestess Gloves",
        "image": "Arms/Priestess Gloves.png",
        "primaryColor": "#968d96",
        "secondaryColors": [
            "#847b84",
            "#665f66"
        ]
    },
    {
        "name": "Prisoner's Gloves",
        "image": "Arms/Prisoner's Gloves.png",
        "primaryColor": "#876b58",
        "secondaryColors": [
            "#6b5749",
            "#59473a"
        ]
    },
    {
        "name": "Rogue Gauntlets",
        "image": "Arms/Rogue Gauntlets.png",
        "primaryColor": "#dddddc",
        "secondaryColors": [
            "#999895",
            "#625f56"
        ]
    },
    {
        "name": "Royal Soldier Gauntlets",
        "image": "Arms/Royal Soldier Gauntlets.png",
        "primaryColor": "#99978f",
        "secondaryColors": [
            "#898478",
            "#82796d"
        ]
    },
    {
        "name": "Royal Swordsman Gloves",
        "image": "Arms/Royal Swordsman Gloves.png",
        "primaryColor": "#959695",
        "secondaryColors": [
            "#575a57",
            "#545453"
        ]
    },
    {
        "name": "Ruin Gauntlets",
        "image": "Arms/Ruin Gauntlets.png",
        "primaryColor": "#9a9995",
        "secondaryColors": [
            "#626756",
            "#625f56"
        ]
    },
    {
        "name": "Rusted Mastodon Gauntlets",
        "image": "Arms/Rusted Mastodon Gauntlets.png",
        "primaryColor": "#a79e8e",
        "secondaryColors": [
            "#948874",
            "#877662"
        ]
    },
    {
        "name": "Saint's Long Gloves",
        "image": "Arms/Saint's Long Gloves.png",
        "primaryColor": "#968987",
        "secondaryColors": [
            "#86736d",
            "#6b6051"
        ]
    },
    {
        "name": "Shadow Gauntlets",
        "image": "Arms/Shadow Gauntlets.png",
        "primaryColor": "#959799",
        "secondaryColors": [
            "#55595a",
            "#3c4244"
        ]
    },
    {
        "name": "Smelter Demon Gauntlets",
        "image": "Arms/Smelter Demon Gauntlets.png",
        "primaryColor": "#909296",
        "secondaryColors": [
            "#666a63",
            "#5a5b5a"
        ]
    },
    {
        "name": "Steel Gauntlets",
        "image": "Arms/Steel Gauntlets.png",
        "primaryColor": "#939896",
        "secondaryColors": [
            "#5c6460",
            "#576060"
        ]
    },
    {
        "name": "Syan's Gauntlets",
        "image": "Arms/Syan's Gauntlets.png",
        "primaryColor": "#a7a096",
        "secondaryColors": [
            "#928771",
            "#857864"
        ]
    },
    {
        "name": "Targray's Manifers",
        "image": "Arms/Targray's Manifers.png",
        "primaryColor": "#9da19b",
        "secondaryColors": [
            "#8c8874",
            "#83785f"
        ]
    },
    {
        "name": "Tattered Cloth Manchettes",
        "image": "Arms/Tattered Cloth Manchettes.png",
        "primaryColor": "#9c896d",
        "secondaryColors": [
            "#8b765d",
            "#97582a"
        ]
    },
    {
        "name": "Throne Defender Gauntlets",
        "image": "Arms/Throne Defender Gauntlets.png",
        "primaryColor": "#959493",
        "secondaryColors": [
            "#5b5f56",
            "#5c5c5a"
        ]
    },
    {
        "name": "Throne Watcher Gauntlets",
        "image": "Arms/Throne Watcher Gauntlets.png",
        "primaryColor": "#949793",
        "secondaryColors": [
            "#8f938d",
            "#7c817c"
        ]
    },
    {
        "name": "Traveling Merchant Gloves",
        "image": "Arms/Traveling Merchant Gloves.png",
        "primaryColor": "#85766e",
        "secondaryColors": [
            "#675852",
            "#605a4d"
        ]
    },
    {
        "name": "Tseldora Manchettes",
        "image": "Arms/Tseldora Manchettes.png",
        "primaryColor": "#9f8b68",
        "secondaryColors": [
            "#887451",
            "#736448"
        ]
    },
    {
        "name": "Varangian Cuffs",
        "image": "Arms/Varangian Cuffs.png",
        "primaryColor": "#e0dfe0",
        "secondaryColors": [
            "#9f9d9f",
            "#585557"
        ]
    },
    {
        "name": "Velstadt's Gauntlets",
        "image": "Arms/Velstadt's Gauntlets.png",
        "primaryColor": "#dfdddb",
        "secondaryColors": [
            "#a9a196",
            "#928776"
        ]
    },
    {
        "name": "Vengarl's Gloves",
        "image": "Arms/Vengarl's Gloves.png",
        "primaryColor": "#897672",
        "secondaryColors": [
            "#695e59",
            "#615655"
        ]
    },
    {
        "name": "Wanderer Manchettes",
        "image": "Arms/Wanderer Manchettes.png",
        "primaryColor": "#a1a38d",
        "secondaryColors": [
            "#64584f",
            "#5c4639"
        ]
    },
    {
        "name": "White Priest Gloves",
        "image": "Arms/White Priest Gloves.png",
        "primaryColor": "#a7a090",
        "secondaryColors": [
            "#938976",
            "#857a65"
        ]
    },
    {
        "name": "Xanthous Gloves",
        "image": "Arms/Xanthous Gloves.png",
        "primaryColor": "#dfce99",
        "secondaryColors": [
            "#e0ca5f",
            "#cfb35b"
        ]
    },
    {
        "name": "Agdayne's Black Robe",
        "image": "Chest/Agdayne's Black Robe.png",
        "primaryColor": "#949597",
        "secondaryColors": [
            "#797c82",
            "#5d5f60"
        ]
    },
    {
        "name": "Alonne Captain Armor",
        "image": "Chest/Alonne Captain Armor.png",
        "primaryColor": "#9a959a",
        "secondaryColors": [
            "#5b5a62",
            "#575864"
        ]
    },
    {
        "name": "Alonne Knight Armor",
        "image": "Chest/Alonne Knight Armor.png",
        "primaryColor": "#949296",
        "secondaryColors": [
            "#5a5b5f",
            "#59585e"
        ]
    },
    {
        "name": "Alva Armor",
        "image": "Chest/Alva Armor.png",
        "primaryColor": "#8b6a62",
        "secondaryColors": [
            "#5d5651",
            "#4c433b"
        ]
    },
    {
        "name": "Archdrake Robes",
        "image": "Chest/Archdrake Robes.png",
        "primaryColor": "#d0d5d4",
        "secondaryColors": [
            "#bcc4c4",
            "#9ca3a2"
        ]
    },
    {
        "name": "Armor of Aurous (Invisible)",
        "image": "Chest/Armor of Aurous (Invisible).png",
        "primaryColor": "#8c9ab3",
        "secondaryColors": [
            "#708ea6",
            "#7187a6"
        ]
    },
    {
        "name": "Armor of Aurous",
        "image": "Chest/Armor of Aurous.png",
        "primaryColor": "#626262",
        "secondaryColors": [
            "#605753",
            "#4e453a"
        ]
    },
    {
        "name": "Astrologist's Robe",
        "image": "Chest/Astrologist's Robe.png",
        "primaryColor": "#a9a695",
        "secondaryColors": [
            "#a09464",
            "#85794e"
        ]
    },
    {
        "name": "Bandit Armor",
        "image": "Chest/Bandit Armor.png",
        "primaryColor": "#925d55",
        "secondaryColors": [
            "#5f5952",
            "#504438"
        ]
    },
    {
        "name": "Bell Keeper Bellyband",
        "image": "Chest/Bell Keeper Bellyband.png",
        "primaryColor": "#a0968d",
        "secondaryColors": [
            "#9c8773",
            "#8d6d59"
        ]
    },
    {
        "name": "Benhart's Armor",
        "image": "Chest/Benhart's Armor.png",
        "primaryColor": "#504f4f",
        "secondaryColors": [
            "#494339",
            "#423c34"
        ]
    },
    {
        "name": "Black Dragon Armor",
        "image": "Chest/Black Dragon Armor.png",
        "primaryColor": "#847759",
        "secondaryColors": [
            "#655e4e",
            "#554b33"
        ]
    },
    {
        "name": "Black Hollow Mage Robe",
        "image": "Chest/Black Hollow Mage Robe.png",
        "primaryColor": "#54544c",
        "secondaryColors": [
            "#424339",
            "#353d41"
        ]
    },
    {
        "name": "Black Leather Armor",
        "image": "Chest/Black Leather Armor.png",
        "primaryColor": "#a38b69",
        "secondaryColors": [
            "#8d7354",
            "#635b52"
        ]
    },
    {
        "name": "Black Robes",
        "image": "Chest/Black Robes.png",
        "primaryColor": "#585c5c",
        "secondaryColors": [
            "#4d5251",
            "#4d4e4e"
        ]
    },
    {
        "name": "Black Witch Robe",
        "image": "Chest/Black Witch Robe.png",
        "primaryColor": "#9095a9",
        "secondaryColors": [
            "#717489",
            "#595062"
        ]
    },
    {
        "name": "Bone King Robe",
        "image": "Chest/Bone King Robe.png",
        "primaryColor": "#676660",
        "secondaryColors": [
            "#656058",
            "#615c53"
        ]
    },
    {
        "name": "Brigand Armor",
        "image": "Chest/Brigand Armor.png",
        "primaryColor": "#b3a78b",
        "secondaryColors": [
            "#a2916e",
            "#87755b"
        ]
    },
    {
        "name": "Cale's Leather Armor",
        "image": "Chest/Cale's Leather Armor.png",
        "primaryColor": "#8b8a72",
        "secondaryColors": [
            "#5e625a",
            "#5e6256"
        ]
    },
    {
        "name": "Catarina Armor",
        "image": "Chest/Catarina Armor.png",
        "primaryColor": "#cfc5b0",
        "secondaryColors": [
            "#c4b9a2",
            "#afa48f"
        ]
    },
    {
        "name": "Chaos Robe",
        "image": "Chest/Chaos Robe.png",
        "primaryColor": "#a39b8c",
        "secondaryColors": [
            "#928772",
            "#857762"
        ]
    },
    {
        "name": "Creighton's Chainmail",
        "image": "Chest/Creighton's Chainmail.png",
        "primaryColor": "#585d5b",
        "secondaryColors": [
            "#58564f",
            "#474338"
        ]
    },
    {
        "name": "Dark Armor",
        "image": "Chest/Dark Armor.png",
        "primaryColor": "#949396",
        "secondaryColors": [
            "#7a7c82",
            "#5e6268"
        ]
    },
    {
        "name": "Desert Sorceress Top",
        "image": "Chest/Desert Sorceress Top.png",
        "primaryColor": "#d5cecb",
        "secondaryColors": [
            "#a79691",
            "#8c7168"
        ]
    },
    {
        "name": "Dingy Robe",
        "image": "Chest/Dingy Robe.png",
        "primaryColor": "#9b9a8e",
        "secondaryColors": [
            "#8f8a71",
            "#636156"
        ]
    },
    {
        "name": "Dragon Acolyte Robe",
        "image": "Chest/Dragon Acolyte Robe.png",
        "primaryColor": "#c9c8c9",
        "secondaryColors": [
            "#a2a1a0",
            "#676662"
        ]
    },
    {
        "name": "Dragonrider Armor",
        "image": "Chest/Dragonrider Armor.png",
        "primaryColor": "#5c5f61",
        "secondaryColors": [
            "#565452",
            "#4c453a"
        ]
    },
    {
        "name": "Drakekeeper Armor",
        "image": "Chest/Drakekeeper Armor.png",
        "primaryColor": "#585e5d",
        "secondaryColors": [
            "#4c4f4f",
            "#3d4244"
        ]
    },
    {
        "name": "Drangleic Mail",
        "image": "Chest/Drangleic Mail.png",
        "primaryColor": "#8b8a89",
        "secondaryColors": [
            "#5a5855",
            "#48423b"
        ]
    },
    {
        "name": "Elite Knight Armor",
        "image": "Chest/Elite Knight Armor.png",
        "primaryColor": "#a0998e",
        "secondaryColors": [
            "#9e8d74",
            "#8a7662"
        ]
    },
    {
        "name": "Executioner Armor",
        "image": "Chest/Executioner Armor.png",
        "primaryColor": "#585a5c",
        "secondaryColors": [
            "#4d5052",
            "#3b434b"
        ]
    },
    {
        "name": "Falconer Armor",
        "image": "Chest/Falconer Armor.png",
        "primaryColor": "#86695f",
        "secondaryColors": [
            "#6c5c50",
            "#5c4738"
        ]
    },
    {
        "name": "Faraam Armor",
        "image": "Chest/Faraam Armor.png",
        "primaryColor": "#9c9d9d",
        "secondaryColors": [
            "#616666",
            "#565859"
        ]
    },
    {
        "name": "Grave Warden Top",
        "image": "Chest/Grave Warden Top.png",
        "primaryColor": "#969692",
        "secondaryColors": [
            "#85837c",
            "#73888b"
        ]
    },
    {
        "name": "Gyrm Armor",
        "image": "Chest/Gyrm Armor.png",
        "primaryColor": "#9d9b96",
        "secondaryColors": [
            "#605e5a",
            "#584933"
        ]
    },
    {
        "name": "Gyrm Warrior Armor",
        "image": "Chest/Gyrm Warrior Armor.png",
        "primaryColor": "#847566",
        "secondaryColors": [
            "#655c50",
            "#5f584f"
        ]
    },
    {
        "name": "Hard Leather Armor",
        "image": "Chest/Hard Leather Armor.png",
        "primaryColor": "#9e9590",
        "secondaryColors": [
            "#998577",
            "#887366"
        ]
    },
    {
        "name": "Havel's Armor",
        "image": "Chest/Havel's Armor.png",
        "primaryColor": "#d2d1d2",
        "secondaryColors": [
            "#a2a1a0",
            "#9a9b9b"
        ]
    },
    {
        "name": "Heide Knight Chainmail",
        "image": "Chest/Heide Knight Chainmail.png",
        "primaryColor": "#d1cec9",
        "secondaryColors": [
            "#a6a096",
            "#a49e97"
        ]
    },
    {
        "name": "Hexer's Robes",
        "image": "Chest/Hexer's Robes.png",
        "primaryColor": "#636661",
        "secondaryColors": [
            "#5b5851",
            "#585951"
        ]
    },
    {
        "name": "Hollow Infantry Armor",
        "image": "Chest/Hollow Infantry Armor.png",
        "primaryColor": "#575a5a",
        "secondaryColors": [
            "#4b4a47",
            "#574433"
        ]
    },
    {
        "name": "Hollow Soldier Armor",
        "image": "Chest/Hollow Soldier Armor.png",
        "primaryColor": "#8c6863",
        "secondaryColors": [
            "#675b57",
            "#534539"
        ]
    },
    {
        "name": "Imperious Armor",
        "image": "Chest/Imperious Armor.png",
        "primaryColor": "#565755",
        "secondaryColors": [
            "#45423c",
            "#3b4346"
        ]
    },
    {
        "name": "Imported Tunic",
        "image": "Chest/Imported Tunic.png",
        "primaryColor": "#9f8a71",
        "secondaryColors": [
            "#896f5e",
            "#66574c"
        ]
    },
    {
        "name": "Infantry Armor",
        "image": "Chest/Infantry Armor.png",
        "primaryColor": "#5c5e5f",
        "secondaryColors": [
            "#4e4c4a",
            "#564534"
        ]
    },
    {
        "name": "Insolent Armor",
        "image": "Chest/Insolent Armor.png",
        "primaryColor": "#99948d",
        "secondaryColors": [
            "#8b847a",
            "#837a70"
        ]
    },
    {
        "name": "Ironclad Armor",
        "image": "Chest/Ironclad Armor.png",
        "primaryColor": "#cecece",
        "secondaryColors": [
            "#9a9b9a",
            "#636865"
        ]
    },
    {
        "name": "Jester's Robes",
        "image": "Chest/Jester's Robes.png",
        "primaryColor": "#886f4c",
        "secondaryColors": [
            "#85663a",
            "#6d604d"
        ]
    },
    {
        "name": "King's Armor",
        "image": "Chest/King's Armor.png",
        "primaryColor": "#989591",
        "secondaryColors": [
            "#595b58",
            "#5b5953"
        ]
    },
    {
        "name": "Knight Armor",
        "image": "Chest/Knight Armor.png",
        "primaryColor": "#dfdfdf",
        "secondaryColors": [
            "#9a9999",
            "#887261"
        ]
    },
    {
        "name": "Leather Armor",
        "image": "Chest/Leather Armor.png",
        "primaryColor": "#c7b28a",
        "secondaryColors": [
            "#a8926c",
            "#897456"
        ]
    },
    {
        "name": "Leydia Black Robe",
        "image": "Chest/Leydia Black Robe.png",
        "primaryColor": "#87878d",
        "secondaryColors": [
            "#626665",
            "#5a5a5f"
        ]
    },
    {
        "name": "Leydia White Robe",
        "image": "Chest/Leydia White Robe.png",
        "primaryColor": "#b0b6c5",
        "secondaryColors": [
            "#9399aa",
            "#7b8395"
        ]
    },
    {
        "name": "Lion Mage Robe",
        "image": "Chest/Lion Mage Robe.png",
        "primaryColor": "#5a5a5a",
        "secondaryColors": [
            "#5a5751",
            "#524833"
        ]
    },
    {
        "name": "Lion Warrior Cape",
        "image": "Chest/Lion Warrior Cape.png",
        "primaryColor": "#574b33",
        "secondaryColors": [
            "#564b31",
            "#453a29"
        ]
    },
    {
        "name": "Llwellyn Armor",
        "image": "Chest/Llwellyn Armor.png",
        "primaryColor": "#5d6163",
        "secondaryColors": [
            "#5a5651",
            "#45413d"
        ]
    },
    {
        "name": "Looking Glass Armor",
        "image": "Chest/Looking Glass Armor.png",
        "primaryColor": "#dddede",
        "secondaryColors": [
            "#969999",
            "#949899"
        ]
    },
    {
        "name": "Lucatiel's Vest",
        "image": "Chest/Lucatiel's Vest.png",
        "primaryColor": "#a7a39a",
        "secondaryColors": [
            "#5a5b5b",
            "#575b5f"
        ]
    },
    {
        "name": "Mad Warrior Armor",
        "image": "Chest/Mad Warrior Armor.png",
        "primaryColor": "#94969b",
        "secondaryColors": [
            "#54575b",
            "#3c4248"
        ]
    },
    {
        "name": "Manikin Top",
        "image": "Chest/Manikin Top.png",
        "primaryColor": "#675f64",
        "secondaryColors": [
            "#585454",
            "#52453a"
        ]
    },
    {
        "name": "Mastodon Armor",
        "image": "Chest/Mastodon Armor.png",
        "primaryColor": "#9e886b",
        "secondaryColors": [
            "#897050",
            "#746148"
        ]
    },
    {
        "name": "Monastery Longshirt",
        "image": "Chest/Monastery Longshirt.png",
        "primaryColor": "#dfd8cf",
        "secondaryColors": [
            "#ccc5ba",
            "#c3bbb0"
        ]
    },
    {
        "name": "Moon Butterfly Wings",
        "image": "Chest/Moon Butterfly Wings.png",
        "primaryColor": "#f3d35a",
        "secondaryColors": [
            "#f2cf24",
            "#e09d58"
        ]
    },
    {
        "name": "Nahr Alma Robes",
        "image": "Chest/Nahr Alma Robes.png",
        "primaryColor": "#645f58",
        "secondaryColors": [
            "#5e5951",
            "#49443a"
        ]
    },
    {
        "name": "Old Ironclad Armor",
        "image": "Chest/Old Ironclad Armor.png",
        "primaryColor": "#9b9894",
        "secondaryColors": [
            "#898478",
            "#83796c"
        ]
    },
    {
        "name": "Old Knight Armor",
        "image": "Chest/Old Knight Armor.png",
        "primaryColor": "#4d5a57",
        "secondaryColors": [
            "#384746",
            "#35413c"
        ]
    },
    {
        "name": "Pate's Armor",
        "image": "Chest/Pate's Armor.png",
        "primaryColor": "#a5a19c",
        "secondaryColors": [
            "#ad8c6b",
            "#977253"
        ]
    },
    {
        "name": "Peasant Attire",
        "image": "Chest/Peasant Attire.png",
        "primaryColor": "#746243",
        "secondaryColors": [
            "#5e4b2e",
            "#584d33"
        ]
    },
    {
        "name": "Penal Straightjacket",
        "image": "Chest/Penal Straightjacket.png",
        "primaryColor": "#968f88",
        "secondaryColors": [
            "#8b8379",
            "#827a72"
        ]
    },
    {
        "name": "Priestess Robe",
        "image": "Chest/Priestess Robe.png",
        "primaryColor": "#ced0cd",
        "secondaryColors": [
            "#c3c3ba",
            "#a3a39c"
        ]
    },
    {
        "name": "Prisoner's Tatters 2",
        "image": "Chest/Prisoner's Tatters 2.png",
        "primaryColor": "#6e6248",
        "secondaryColors": [
            "#584d34",
            "#584c32"
        ]
    },
    {
        "name": "Prisoner's Tatters",
        "image": "Chest/Prisoner's Tatters.png",
        "primaryColor": "#656252",
        "secondaryColors": [
            "#574d35",
            "#52482f"
        ]
    },
    {
        "name": "Red Lion Warrior Cape",
        "image": "Chest/Red Lion Warrior Cape.png",
        "primaryColor": "#686257",
        "secondaryColors": [
            "#564b33",
            "#47251b"
        ]
    },
    {
        "name": "Robe of Judgment",
        "image": "Chest/Robe of Judgment.png",
        "primaryColor": "#5e5e60",
        "secondaryColors": [
            "#4a4b4d",
            "#284c4e"
        ]
    },
    {
        "name": "Rogue Armor",
        "image": "Chest/Rogue Armor.png",
        "primaryColor": "#5f5f5f",
        "secondaryColors": [
            "#5d5547",
            "#4f4638"
        ]
    },
    {
        "name": "Royal Soldier Armor",
        "image": "Chest/Royal Soldier Armor.png",
        "primaryColor": "#afa38e",
        "secondaryColors": [
            "#5d5855",
            "#544837"
        ]
    },
    {
        "name": "Royal Swordsman Armor",
        "image": "Chest/Royal Swordsman Armor.png",
        "primaryColor": "#5b5e61",
        "secondaryColors": [
            "#555454",
            "#4a423c"
        ]
    },
    {
        "name": "Ruin Armor",
        "image": "Chest/Ruin Armor.png",
        "primaryColor": "#9c9994",
        "secondaryColors": [
            "#62645f",
            "#615d54"
        ]
    },
    {
        "name": "Rusted Mastodon Armor",
        "image": "Chest/Rusted Mastodon Armor.png",
        "primaryColor": "#86735d",
        "secondaryColors": [
            "#685c4d",
            "#554838"
        ]
    },
    {
        "name": "Saint's Dress",
        "image": "Chest/Saint's Dress.png",
        "primaryColor": "#89745f",
        "secondaryColors": [
            "#6c5b4c",
            "#5a4837"
        ]
    },
    {
        "name": "Shadow Top",
        "image": "Chest/Shadow Top.png",
        "primaryColor": "#5b5c54",
        "secondaryColors": [
            "#525450",
            "#42433a"
        ]
    },
    {
        "name": "Singer's Dress",
        "image": "Chest/Singer's Dress.png",
        "primaryColor": "#929c91",
        "secondaryColors": [
            "#798578",
            "#5f6559"
        ]
    },
    {
        "name": "Smelter Demon Armor",
        "image": "Chest/Smelter Demon Armor.png",
        "primaryColor": "#5a5d60",
        "secondaryColors": [
            "#51565a",
            "#515255"
        ]
    },
    {
        "name": "Steel Armor",
        "image": "Chest/Steel Armor.png",
        "primaryColor": "#999c9d",
        "secondaryColors": [
            "#51605e",
            "#545b5a"
        ]
    },
    {
        "name": "Syan's Armor",
        "image": "Chest/Syan's Armor.png",
        "primaryColor": "#a0968b",
        "secondaryColors": [
            "#918575",
            "#847869"
        ]
    },
    {
        "name": "Targray's Armor",
        "image": "Chest/Targray's Armor.png",
        "primaryColor": "#969491",
        "secondaryColors": [
            "#63615c",
            "#524b39"
        ]
    },
    {
        "name": "Tattered Cloth Robe",
        "image": "Chest/Tattered Cloth Robe.png",
        "primaryColor": "#a28b62",
        "secondaryColors": [
            "#8e7651",
            "#8f6630"
        ]
    },
    {
        "name": "Throne Defender Armor",
        "image": "Chest/Throne Defender Armor.png",
        "primaryColor": "#878889",
        "secondaryColors": [
            "#5b5a59",
            "#49433b"
        ]
    },
    {
        "name": "Throne Watcher Armor",
        "image": "Chest/Throne Watcher Armor.png",
        "primaryColor": "#c3c3c3",
        "secondaryColors": [
            "#a4a5a4",
            "#9c9e9d"
        ]
    },
    {
        "name": "Traveling Merchant Coat",
        "image": "Chest/Traveling Merchant Coat.png",
        "primaryColor": "#a29a8b",
        "secondaryColors": [
            "#908776",
            "#867361"
        ]
    },
    {
        "name": "Tseldora Robe",
        "image": "Chest/Tseldora Robe.png",
        "primaryColor": "#9d8b6e",
        "secondaryColors": [
            "#8a7459",
            "#665b4d"
        ]
    },
    {
        "name": "Varangian Armor",
        "image": "Chest/Varangian Armor.png",
        "primaryColor": "#5d5550",
        "secondaryColors": [
            "#4f5355",
            "#614833"
        ]
    },
    {
        "name": "Velstadt's Armor",
        "image": "Chest/Velstadt's Armor.png",
        "primaryColor": "#a19c97",
        "secondaryColors": [
            "#605950",
            "#4d4539"
        ]
    },
    {
        "name": "Vengarl's Armor",
        "image": "Chest/Vengarl's Armor.png",
        "primaryColor": "#615d5f",
        "secondaryColors": [
            "#595b60",
            "#5a4f51"
        ]
    },
    {
        "name": "Wanderer Coat",
        "image": "Chest/Wanderer Coat.png",
        "primaryColor": "#908a6b",
        "secondaryColors": [
            "#87735e",
            "#675e50"
        ]
    },
    {
        "name": "White Hollow Mage Robe",
        "image": "Chest/White Hollow Mage Robe.png",
        "primaryColor": "#c9cecd",
        "secondaryColors": [
            "#9ba19d",
            "#7a8485"
        ]
    },
    {
        "name": "White Priest Robe",
        "image": "Chest/White Priest Robe.png",
        "primaryColor": "#9d9c99",
        "secondaryColors": [
            "#8a8474",
            "#857661"
        ]
    },
    {
        "name": "Xanthous Overcoat",
        "image": "Chest/Xanthous Overcoat.png",
        "primaryColor": "#ebcb16",
        "secondaryColors": [
            "#d4ac0c",
            "#946d0d"
        ]
    },
    {
        "name": "Alonne Captain Helm",
        "image": "Head/Alonne Captain Helm.png",
        "primaryColor": "#949099",
        "secondaryColors": [
            "#5a5e6a",
            "#555360"
        ]
    },
    {
        "name": "Alonne Knight Helm",
        "image": "Head/Alonne Knight Helm.png",
        "primaryColor": "#9493a6",
        "secondaryColors": [
            "#7c829b",
            "#70728c"
        ]
    },
    {
        "name": "Alva Helm",
        "image": "Head/Alva Helm.png",
        "primaryColor": "#96999c",
        "secondaryColors": [
            "#5b5958",
            "#4e5051"
        ]
    },
    {
        "name": "Archdrake Helm",
        "image": "Head/Archdrake Helm.png",
        "primaryColor": "#889499",
        "secondaryColors": [
            "#586160",
            "#555d5d"
        ]
    },
    {
        "name": "Bell Keeper Helmet",
        "image": "Head/Bell Keeper Helmet.png",
        "primaryColor": "#8a6f50",
        "secondaryColors": [
            "#6a5e50",
            "#5d4b33"
        ]
    },
    {
        "name": "Benhart's Knight Helm",
        "image": "Head/Benhart's Knight Helm.png",
        "primaryColor": "#9e9a97",
        "secondaryColors": [
            "#666158",
            "#5c5955"
        ]
    },
    {
        "name": "Black Dragon Helm",
        "image": "Head/Black Dragon Helm.png",
        "primaryColor": "#86795b",
        "secondaryColors": [
            "#686453",
            "#5d5f57"
        ]
    },
    {
        "name": "Black Hollow Mage Hood",
        "image": "Head/Black Hollow Mage Hood.png",
        "primaryColor": "#a09b91",
        "secondaryColors": [
            "#5b605f",
            "#5d5d57"
        ]
    },
    {
        "name": "Black Hood",
        "image": "Head/Black Hood.png",
        "primaryColor": "#626965",
        "secondaryColors": [
            "#50514e",
            "#3c4144"
        ]
    },
    {
        "name": "Black Witch Domino Mask",
        "image": "Head/Black Witch Domino Mask.png",
        "primaryColor": "#cccedd",
        "secondaryColors": [
            "#acafc7",
            "#9197ae"
        ]
    },
    {
        "name": "Black Witch Hat",
        "image": "Head/Black Witch Hat.png",
        "primaryColor": "#525153",
        "secondaryColors": [
            "#484749",
            "#484648"
        ]
    },
    {
        "name": "Black Witch Veil",
        "image": "Head/Black Witch Veil.png",
        "primaryColor": "#5e635e",
        "secondaryColors": [
            "#5e615c",
            "#575360"
        ]
    },
    {
        "name": "Bone Crown",
        "image": "Head/Bone Crown.png",
        "primaryColor": "#6f6856",
        "secondaryColors": [
            "#6b6858",
            "#70644c"
        ]
    },
    {
        "name": "Brigand Hood",
        "image": "Head/Brigand Hood.png",
        "primaryColor": "#b1a794",
        "secondaryColors": [
            "#9a8a6f",
            "#866d54"
        ]
    },
    {
        "name": "Cale's Helm",
        "image": "Head/Cale's Helm.png",
        "primaryColor": "#555a5a",
        "secondaryColors": [
            "#4e5154",
            "#3a4349"
        ]
    },
    {
        "name": "Catarina Helm",
        "image": "Head/Catarina Helm.png",
        "primaryColor": "#cec3ac",
        "secondaryColors": [
            "#c5b89f",
            "#b4a78e"
        ]
    },
    {
        "name": "Chaos Hood",
        "image": "Head/Chaos Hood.png",
        "primaryColor": "#676755",
        "secondaryColors": [
            "#5a564f",
            "#494637"
        ]
    },
    {
        "name": "Creighton's Steel Mask",
        "image": "Head/Creighton's Steel Mask.png",
        "primaryColor": "#9e9d96",
        "secondaryColors": [
            "#595a52",
            "#565a56"
        ]
    },
    {
        "name": "Dark Mask",
        "image": "Head/Dark Mask.png",
        "primaryColor": "#cacbcb",
        "secondaryColors": [
            "#a1a09f",
            "#5a5b5b"
        ]
    },
    {
        "name": "Desert Sorceress Hood",
        "image": "Head/Desert Sorceress Hood.png",
        "primaryColor": "#946558",
        "secondaryColors": [
            "#926253",
            "#8d6355"
        ]
    },
    {
        "name": "Dingy Hood",
        "image": "Head/Dingy Hood.png",
        "primaryColor": "#94948d",
        "secondaryColors": [
            "#85837b",
            "#66665f"
        ]
    },
    {
        "name": "Dragon Acolyte Mask",
        "image": "Head/Dragon Acolyte Mask.png",
        "primaryColor": "#cfcfd0",
        "secondaryColors": [
            "#a3a2a3",
            "#a1a2a3"
        ]
    },
    {
        "name": "Dragon Sage Hood",
        "image": "Head/Dragon Sage Hood.png",
        "primaryColor": "#cacac8",
        "secondaryColors": [
            "#c1c0be",
            "#abaaa8"
        ]
    },
    {
        "name": "Dragonrider Helm",
        "image": "Head/Dragonrider Helm.png",
        "primaryColor": "#626464",
        "secondaryColors": [
            "#535755",
            "#4f5153"
        ]
    },
    {
        "name": "Drakekeeper Helm",
        "image": "Head/Drakekeeper Helm.png",
        "primaryColor": "#4f5155",
        "secondaryColors": [
            "#4b4e52",
            "#4c4b4d"
        ]
    },
    {
        "name": "Drangleic Helm",
        "image": "Head/Drangleic Helm.png",
        "primaryColor": "#5c6960",
        "secondaryColors": [
            "#4b5658",
            "#3b454b"
        ]
    },
    {
        "name": "Durgo's Hat",
        "image": "Head/Durgo's Hat.png",
        "primaryColor": "#9f9d98",
        "secondaryColors": [
            "#646117",
            "#4c452c"
        ]
    },
    {
        "name": "Elite Knight Helm",
        "image": "Head/Elite Knight Helm.png",
        "primaryColor": "#959aa1",
        "secondaryColors": [
            "#5f645e",
            "#5d6261"
        ]
    },
    {
        "name": "Executioner Helm",
        "image": "Head/Executioner Helm.png",
        "primaryColor": "#585e5a",
        "secondaryColors": [
            "#565453",
            "#49443b"
        ]
    },
    {
        "name": "Falconer Helm",
        "image": "Head/Falconer Helm.png",
        "primaryColor": "#919396",
        "secondaryColors": [
            "#646868",
            "#606367"
        ]
    },
    {
        "name": "Faraam Helm",
        "image": "Head/Faraam Helm.png",
        "primaryColor": "#8c95a0",
        "secondaryColors": [
            "#909296",
            "#7d8286"
        ]
    },
    {
        "name": "Grave Warden Mask",
        "image": "Head/Grave Warden Mask.png",
        "primaryColor": "#9a9992",
        "secondaryColors": [
            "#85837b",
            "#6a6960"
        ]
    },
    {
        "name": "Gyrm Helm",
        "image": "Head/Gyrm Helm.png",
        "primaryColor": "#e1ded7",
        "secondaryColors": [
            "#a09f97",
            "#9a8d6a"
        ]
    },
    {
        "name": "Gyrm Warrior Greathelm",
        "image": "Head/Gyrm Warrior Greathelm.png",
        "primaryColor": "#938670",
        "secondaryColors": [
            "#87765d",
            "#6c675a"
        ]
    },
    {
        "name": "Gyrm Warrior Helm",
        "image": "Head/Gyrm Warrior Helm.png",
        "primaryColor": "#908674",
        "secondaryColors": [
            "#857761",
            "#6f6857"
        ]
    },
    {
        "name": "Havel's Helm",
        "image": "Head/Havel's Helm.png",
        "primaryColor": "#9a9b9a",
        "secondaryColors": [
            "#586462",
            "#5a645c"
        ]
    },
    {
        "name": "Heide Knight Greathelm",
        "image": "Head/Heide Knight Greathelm.png",
        "primaryColor": "#d0cfcc",
        "secondaryColors": [
            "#cec4b2",
            "#c5b79e"
        ]
    },
    {
        "name": "Heide Knight Iron Mask",
        "image": "Head/Heide Knight Iron Mask.png",
        "primaryColor": "#969494",
        "secondaryColors": [
            "#656563",
            "#645958"
        ]
    },
    {
        "name": "Helm of Aurous (Invisible)",
        "image": "Head/Helm of Aurous (Invisible).png",
        "primaryColor": "#9093ac",
        "secondaryColors": [
            "#8d8faa",
            "#7982a0"
        ]
    },
    {
        "name": "Helm of Aurous",
        "image": "Head/Helm of Aurous.png",
        "primaryColor": "#876a5f",
        "secondaryColors": [
            "#6e554a",
            "#6e5349"
        ]
    },
    {
        "name": "Hexer's Hood",
        "image": "Head/Hexer's Hood.png",
        "primaryColor": "#959593",
        "secondaryColors": [
            "#5d5c5b",
            "#555656"
        ]
    },
    {
        "name": "Hollow Infantry Helm",
        "image": "Head/Hollow Infantry Helm.png",
        "primaryColor": "#989a97",
        "secondaryColors": [
            "#5b5d57",
            "#4c5b56"
        ]
    },
    {
        "name": "Hollow Soldier Helmet",
        "image": "Head/Hollow Soldier Helmet.png",
        "primaryColor": "#999995",
        "secondaryColors": [
            "#98886e",
            "#8a705a"
        ]
    },
    {
        "name": "Hunter's Hat",
        "image": "Head/Hunter's Hat.png",
        "primaryColor": "#9b928f",
        "secondaryColors": [
            "#64554f",
            "#5d4336"
        ]
    },
    {
        "name": "Imperious Helm",
        "image": "Head/Imperious Helm.png",
        "primaryColor": "#d3d4d4",
        "secondaryColors": [
            "#959698",
            "#787c82"
        ]
    },
    {
        "name": "Imported Hood",
        "image": "Head/Imported Hood.png",
        "primaryColor": "#9b896e",
        "secondaryColors": [
            "#877159",
            "#6e5948"
        ]
    },
    {
        "name": "Infantry Helm",
        "image": "Head/Infantry Helm.png",
        "primaryColor": "#dcdcdb",
        "secondaryColors": [
            "#999b98",
            "#5b6555"
        ]
    },
    {
        "name": "Insolent Helm",
        "image": "Head/Insolent Helm.png",
        "primaryColor": "#d8d9d9",
        "secondaryColors": [
            "#939598",
            "#5f6668"
        ]
    },
    {
        "name": "Ironclad Helm",
        "image": "Head/Ironclad Helm.png",
        "primaryColor": "#949493",
        "secondaryColors": [
            "#636561",
            "#616560"
        ]
    },
    {
        "name": "Jester's Cap",
        "image": "Head/Jester's Cap.png",
        "primaryColor": "#a4a19a",
        "secondaryColors": [
            "#a48e62",
            "#8b744c"
        ]
    },
    {
        "name": "King's Crown",
        "image": "Head/King's Crown.png",
        "primaryColor": "#919491",
        "secondaryColors": [
            "#5b6157",
            "#5b605a"
        ]
    },
    {
        "name": "Knight Helm",
        "image": "Head/Knight Helm.png",
        "primaryColor": "#8e9291",
        "secondaryColors": [
            "#5d645d",
            "#585e58"
        ]
    },
    {
        "name": "Leydia Black Hood",
        "image": "Head/Leydia Black Hood.png",
        "primaryColor": "#9a9695",
        "secondaryColors": [
            "#5f6267",
            "#58555a"
        ]
    },
    {
        "name": "Leydia White Hood",
        "image": "Head/Leydia White Hood.png",
        "primaryColor": "#ccd1dd",
        "secondaryColors": [
            "#bcc2d1",
            "#b0b6c6"
        ]
    },
    {
        "name": "Lion Warrior Helm",
        "image": "Head/Lion Warrior Helm.png",
        "primaryColor": "#616560",
        "secondaryColors": [
            "#596260",
            "#536267"
        ]
    },
    {
        "name": "Looking Glass Helm",
        "image": "Head/Looking Glass Helm.png",
        "primaryColor": "#d7d8da",
        "secondaryColors": [
            "#9d9fa1",
            "#969b9b"
        ]
    },
    {
        "name": "Lucatiel's Mask",
        "image": "Head/Lucatiel's Mask.png",
        "primaryColor": "#9b9595",
        "secondaryColors": [
            "#89704f",
            "#6d6151"
        ]
    },
    {
        "name": "Mad Warrior Mask",
        "image": "Head/Mad Warrior Mask.png",
        "primaryColor": "#515b58",
        "secondaryColors": [
            "#505558",
            "#3b4347"
        ]
    },
    {
        "name": "Manikin Mask",
        "image": "Head/Manikin Mask.png",
        "primaryColor": "#d8cfcb",
        "secondaryColors": [
            "#c5b8b2",
            "#a79d98"
        ]
    },
    {
        "name": "Mask of Judgment",
        "image": "Head/Mask of Judgment.png",
        "primaryColor": "#615d52",
        "secondaryColors": [
            "#5c5a51",
            "#494737"
        ]
    },
    {
        "name": "Mastodon Helm",
        "image": "Head/Mastodon Helm.png",
        "primaryColor": "#88765b",
        "secondaryColors": [
            "#6b5e4b",
            "#574a35"
        ]
    },
    {
        "name": "Monastery Headcloth",
        "image": "Head/Monastery Headcloth.png",
        "primaryColor": "#ded7cd",
        "secondaryColors": [
            "#cfc5b7",
            "#c3b9ab"
        ]
    },
    {
        "name": "Moon Butterfly Hat",
        "image": "Head/Moon Butterfly Hat.png",
        "primaryColor": "#d6cec7",
        "secondaryColors": [
            "#cec4b6",
            "#c7b8a6"
        ]
    },
    {
        "name": "Moon Hat",
        "image": "Head/Moon Hat.png",
        "primaryColor": "#d9cc96",
        "secondaryColors": [
            "#9c9b95",
            "#a2976b"
        ]
    },
    {
        "name": "Nahr Alma Hood",
        "image": "Head/Nahr Alma Hood.png",
        "primaryColor": "#4c4b47",
        "secondaryColors": [
            "#4a443b",
            "#3c3d40"
        ]
    },
    {
        "name": "Old Ironclad Helm",
        "image": "Head/Old Ironclad Helm.png",
        "primaryColor": "#9a9791",
        "secondaryColors": [
            "#88837a",
            "#645e53"
        ]
    },
    {
        "name": "Old Knight Helm",
        "image": "Head/Old Knight Helm.png",
        "primaryColor": "#4d5a55",
        "secondaryColors": [
            "#394846",
            "#374645"
        ]
    },
    {
        "name": "Pate's Helm",
        "image": "Head/Pate's Helm.png",
        "primaryColor": "#d6d5d5",
        "secondaryColors": [
            "#a39f9c",
            "#8a8577"
        ]
    },
    {
        "name": "Peasant Hat",
        "image": "Head/Peasant Hat.png",
        "primaryColor": "#706445",
        "secondaryColors": [
            "#5a4b29",
            "#47371a"
        ]
    },
    {
        "name": "Penal Mask",
        "image": "Head/Penal Mask.png",
        "primaryColor": "#4b4a4a",
        "secondaryColors": [
            "#3c4246",
            "#423d3a"
        ]
    },
    {
        "name": "Priestess Headpiece",
        "image": "Head/Priestess Headpiece.png",
        "primaryColor": "#d1d0c3",
        "secondaryColors": [
            "#cac7b7",
            "#aaa899"
        ]
    },
    {
        "name": "Prisoner's Hood 2",
        "image": "Head/Prisoner's Hood 2.png",
        "primaryColor": "#8b6f4f",
        "secondaryColors": [
            "#5f5c4e",
            "#5c4b34"
        ]
    },
    {
        "name": "Prisoner's Hood",
        "image": "Head/Prisoner's Hood.png",
        "primaryColor": "#897154",
        "secondaryColors": [
            "#6a604f",
            "#6c5c47"
        ]
    },
    {
        "name": "Rogue Hood",
        "image": "Head/Rogue Hood.png",
        "primaryColor": "#99918a",
        "secondaryColors": [
            "#8b837b",
            "#867a71"
        ]
    },
    {
        "name": "Royal Soldier Helmet",
        "image": "Head/Royal Soldier Helmet.png",
        "primaryColor": "#909391",
        "secondaryColors": [
            "#86745e",
            "#5f5d57"
        ]
    },
    {
        "name": "Royal Swordman Helm",
        "image": "Head/Royal Swordman Helm.png",
        "primaryColor": "#969797",
        "secondaryColors": [
            "#5b5f5f",
            "#585857"
        ]
    },
    {
        "name": "Ruin Helm",
        "image": "Head/Ruin Helm.png",
        "primaryColor": "#909091",
        "secondaryColors": [
            "#837b6f",
            "#615e4e"
        ]
    },
    {
        "name": "Rusted Mastodon Helm",
        "image": "Head/Rusted Mastodon Helm.png",
        "primaryColor": "#837561",
        "secondaryColors": [
            "#64594e",
            "#504639"
        ]
    },
    {
        "name": "Saint's Hood",
        "image": "Head/Saint's Hood.png",
        "primaryColor": "#8b6d61",
        "secondaryColors": [
            "#705c51",
            "#6f5c50"
        ]
    },
    {
        "name": "Shadow Mask",
        "image": "Head/Shadow Mask.png",
        "primaryColor": "#9a9a9a",
        "secondaryColors": [
            "#576266",
            "#525b5f"
        ]
    },
    {
        "name": "Smelter Demon Helm",
        "image": "Head/Smelter Demon Helm.png",
        "primaryColor": "#596063",
        "secondaryColors": [
            "#565c5e",
            "#555658"
        ]
    },
    {
        "name": "Spiked Bandit Helm",
        "image": "Head/Spiked Bandit Helm.png",
        "primaryColor": "#a5a19a",
        "secondaryColors": [
            "#89857a",
            "#66655a"
        ]
    },
    {
        "name": "Standard Helm",
        "image": "Head/Standard Helm.png",
        "primaryColor": "#9b9b9b",
        "secondaryColors": [
            "#626664",
            "#606562"
        ]
    },
    {
        "name": "Steel Helm",
        "image": "Head/Steel Helm.png",
        "primaryColor": "#969b9a",
        "secondaryColors": [
            "#535d62",
            "#535d5e"
        ]
    },
    {
        "name": "Syan's Helm",
        "image": "Head/Syan's Helm.png",
        "primaryColor": "#a69d92",
        "secondaryColors": [
            "#928675",
            "#857867"
        ]
    },
    {
        "name": "Targray's Helm",
        "image": "Head/Targray's Helm.png",
        "primaryColor": "#94928e",
        "secondaryColors": [
            "#585e5f",
            "#565956"
        ]
    },
    {
        "name": "Tattered Cloth Hood",
        "image": "Head/Tattered Cloth Hood.png",
        "primaryColor": "#a08c5f",
        "secondaryColors": [
            "#8b764b",
            "#6c6148"
        ]
    },
    {
        "name": "Thief Mask",
        "image": "Head/Thief Mask.png",
        "primaryColor": "#958c8a",
        "secondaryColors": [
            "#89776e",
            "#646161"
        ]
    },
    {
        "name": "Throne Defender Helm",
        "image": "Head/Throne Defender Helm.png",
        "primaryColor": "#8d8d8b",
        "secondaryColors": [
            "#5d5e5d",
            "#5d5c57"
        ]
    },
    {
        "name": "Throne Watcher Helm",
        "image": "Head/Throne Watcher Helm.png",
        "primaryColor": "#c9cccc",
        "secondaryColors": [
            "#bbc3c3",
            "#a5a7a7"
        ]
    },
    {
        "name": "Traveling Merchant Hat",
        "image": "Head/Traveling Merchant Hat.png",
        "primaryColor": "#5a5350",
        "secondaryColors": [
            "#4f433a",
            "#453a32"
        ]
    },
    {
        "name": "Tseldora Cap",
        "image": "Head/Tseldora Cap.png",
        "primaryColor": "#a1885c",
        "secondaryColors": [
            "#8d7449",
            "#88642a"
        ]
    },
    {
        "name": "Varangian Helm",
        "image": "Head/Varangian Helm.png",
        "primaryColor": "#dbdcdc",
        "secondaryColors": [
            "#98999b",
            "#5f6160"
        ]
    },
    {
        "name": "Velstadt's Helm",
        "image": "Head/Velstadt's Helm.png",
        "primaryColor": "#655a4e",
        "secondaryColors": [
            "#5e5230",
            "#514538"
        ]
    },
    {
        "name": "Vengarl's Helm",
        "image": "Head/Vengarl's Helm.png",
        "primaryColor": "#5a5a5f",
        "secondaryColors": [
            "#574f58",
            "#4b3b43"
        ]
    },
    {
        "name": "Wanderer Hood",
        "image": "Head/Wanderer Hood.png",
        "primaryColor": "#928e84",
        "secondaryColors": [
            "#8c8578",
            "#837a6b"
        ]
    },
    {
        "name": "Warlock Mask",
        "image": "Head/Warlock Mask.png",
        "primaryColor": "#97999e",
        "secondaryColors": [
            "#5d635d",
            "#595e5a"
        ]
    },
    {
        "name": "White Hollow Mage Hood",
        "image": "Head/White Hollow Mage Hood.png",
        "primaryColor": "#a0a49f",
        "secondaryColors": [
            "#98998f",
            "#908f73"
        ]
    },
    {
        "name": "White Priest Headpiece",
        "image": "Head/White Priest Headpiece.png",
        "primaryColor": "#aaa798",
        "secondaryColors": [
            "#9f9063",
            "#af8a34"
        ]
    },
    {
        "name": "Xanthous Crown",
        "image": "Head/Xanthous Crown.png",
        "primaryColor": "#ede09a",
        "secondaryColors": [
            "#ebd75e",
            "#e9cc26"
        ]
    },
    {
        "name": "Agdayne's Kilt",
        "image": "Legs/Agdayne's Kilt.png",
        "primaryColor": "#979796",
        "secondaryColors": [
            "#606466",
            "#636363"
        ]
    },
    {
        "name": "Alonne Knight Leggings",
        "image": "Legs/Alonne Knight Leggings.png",
        "primaryColor": "#97979d",
        "secondaryColors": [
            "#52535f",
            "#3c4250"
        ]
    },
    {
        "name": "Alva Leggings",
        "image": "Legs/Alva Leggings.png",
        "primaryColor": "#5b5754",
        "secondaryColors": [
            "#5c534e",
            "#49423c"
        ]
    },
    {
        "name": "Archdrake Boots",
        "image": "Legs/Archdrake Boots.png",
        "primaryColor": "#798485",
        "secondaryColors": [
            "#5e6462",
            "#5b6160"
        ]
    },
    {
        "name": "Astrologist's Bottoms",
        "image": "Legs/Astrologist's Bottoms.png",
        "primaryColor": "#a79967",
        "secondaryColors": [
            "#5d5854",
            "#5d5231"
        ]
    },
    {
        "name": "Bandit Boots",
        "image": "Legs/Bandit Boots.png",
        "primaryColor": "#65625f",
        "secondaryColors": [
            "#565248",
            "#4b4538"
        ]
    },
    {
        "name": "Bell Keeper Trousers",
        "image": "Legs/Bell Keeper Trousers.png",
        "primaryColor": "#837974",
        "secondaryColors": [
            "#605853",
            "#4c423a"
        ]
    },
    {
        "name": "Benhart's Boots",
        "image": "Legs/Benhart's Boots.png",
        "primaryColor": "#5c5f5c",
        "secondaryColors": [
            "#4e4b45",
            "#4b4338"
        ]
    },
    {
        "name": "Black Boots",
        "image": "Legs/Black Boots.png",
        "primaryColor": "#605e5e",
        "secondaryColors": [
            "#4c4d4c",
            "#514b47"
        ]
    },
    {
        "name": "Black Dragon Leggings",
        "image": "Legs/Black Dragon Leggings.png",
        "primaryColor": "#5c5a4e",
        "secondaryColors": [
            "#5e594b",
            "#524b36"
        ]
    },
    {
        "name": "Black Leather Boots",
        "image": "Legs/Black Leather Boots.png",
        "primaryColor": "#5c5e5e",
        "secondaryColors": [
            "#5a524a",
            "#54463a"
        ]
    },
    {
        "name": "Black Witch Trousers",
        "image": "Legs/Black Witch Trousers.png",
        "primaryColor": "#b0b6c9",
        "secondaryColors": [
            "#9b9cab",
            "#524c5f"
        ]
    },
    {
        "name": "Blood Stained Skirt",
        "image": "Legs/Blood Stained Skirt.png",
        "primaryColor": "#aca691",
        "secondaryColors": [
            "#9a8c72",
            "#675b4f"
        ]
    },
    {
        "name": "Bone King Skirt",
        "image": "Legs/Bone King Skirt.png",
        "primaryColor": "#96938f",
        "secondaryColors": [
            "#5b574f",
            "#47443b"
        ]
    },
    {
        "name": "Brigand Trousers",
        "image": "Legs/Brigand Trousers.png",
        "primaryColor": "#988867",
        "secondaryColors": [
            "#857557",
            "#6d5f4a"
        ]
    },
    {
        "name": "Cale's Shoes",
        "image": "Legs/Cale's Shoes.png",
        "primaryColor": "#636668",
        "secondaryColors": [
            "#524f47",
            "#4e4f4a"
        ]
    },
    {
        "name": "Catarina Leggings",
        "image": "Legs/Catarina Leggings.png",
        "primaryColor": "#afa891",
        "secondaryColors": [
            "#8f8a73",
            "#877361"
        ]
    },
    {
        "name": "Chaos Boots",
        "image": "Legs/Chaos Boots.png",
        "primaryColor": "#58534c",
        "secondaryColors": [
            "#4f535f",
            "#484239"
        ]
    },
    {
        "name": "Creighton's Chain Leggings",
        "image": "Legs/Creighton's Chain Leggings.png",
        "primaryColor": "#595e5e",
        "secondaryColors": [
            "#505655",
            "#515456"
        ]
    },
    {
        "name": "Dark Leggings",
        "image": "Legs/Dark Leggings.png",
        "primaryColor": "#979796",
        "secondaryColors": [
            "#5d6161",
            "#5c5e5d"
        ]
    },
    {
        "name": "Desert Sorceress Skirt",
        "image": "Legs/Desert Sorceress Skirt.png",
        "primaryColor": "#b1876e",
        "secondaryColors": [
            "#94685e",
            "#6f4f48"
        ]
    },
    {
        "name": "Dragon Acolyte Boots",
        "image": "Legs/Dragon Acolyte Boots.png",
        "primaryColor": "#676450",
        "secondaryColors": [
            "#5f5f56",
            "#4e4a38"
        ]
    },
    {
        "name": "Dragonrider Leggings",
        "image": "Legs/Dragonrider Leggings.png",
        "primaryColor": "#4d4e51",
        "secondaryColors": [
            "#354c4f",
            "#3d4044"
        ]
    },
    {
        "name": "Drakekeeper Boots",
        "image": "Legs/Drakekeeper Boots.png",
        "primaryColor": "#4f5154",
        "secondaryColors": [
            "#494a4f",
            "#4a494c"
        ]
    },
    {
        "name": "Drangleic Leggings",
        "image": "Legs/Drangleic Leggings.png",
        "primaryColor": "#545754",
        "secondaryColors": [
            "#4c4a48",
            "#524739"
        ]
    },
    {
        "name": "Elite Knight Leggings",
        "image": "Legs/Elite Knight Leggings.png",
        "primaryColor": "#919393",
        "secondaryColors": [
            "#5f5d59",
            "#575e61"
        ]
    },
    {
        "name": "Executioner Leggings",
        "image": "Legs/Executioner Leggings.png",
        "primaryColor": "#5e6162",
        "secondaryColors": [
            "#595e62",
            "#595856"
        ]
    },
    {
        "name": "Falconer Boots",
        "image": "Legs/Falconer Boots.png",
        "primaryColor": "#5f5f56",
        "secondaryColors": [
            "#595758",
            "#504536"
        ]
    },
    {
        "name": "Faraam Boots",
        "image": "Legs/Faraam Boots.png",
        "primaryColor": "#666460",
        "secondaryColors": [
            "#57514f",
            "#53443a"
        ]
    },
    {
        "name": "Flying Feline Boots",
        "image": "Legs/Flying Feline Boots.png",
        "primaryColor": "#a99e96",
        "secondaryColors": [
            "#957053",
            "#8d5a34"
        ]
    },
    {
        "name": "Grave Warden Bottoms",
        "image": "Legs/Grave Warden Bottoms.png",
        "primaryColor": "#929392",
        "secondaryColors": [
            "#5d6163",
            "#545553"
        ]
    },
    {
        "name": "Gyrm Boots",
        "image": "Legs/Gyrm Boots.png",
        "primaryColor": "#68685d",
        "secondaryColors": [
            "#676851",
            "#4e4e38"
        ]
    },
    {
        "name": "Gyrm Warrior Boots",
        "image": "Legs/Gyrm Warrior Boots.png",
        "primaryColor": "#978a6f",
        "secondaryColors": [
            "#86785f",
            "#6f634d"
        ]
    },
    {
        "name": "Hard Leather Boots",
        "image": "Legs/Hard Leather Boots.png",
        "primaryColor": "#5e5b56",
        "secondaryColors": [
            "#565b57",
            "#4f504d"
        ]
    },
    {
        "name": "Havel's Leggings",
        "image": "Legs/Havel's Leggings.png",
        "primaryColor": "#8e8f8c",
        "secondaryColors": [
            "#61645f",
            "#5a605d"
        ]
    },
    {
        "name": "Heavy Boots",
        "image": "Legs/Heavy Boots.png",
        "primaryColor": "#a08c73",
        "secondaryColors": [
            "#89765f",
            "#6b5f4e"
        ]
    },
    {
        "name": "Heide Knight Leggings",
        "image": "Legs/Heide Knight Leggings.png",
        "primaryColor": "#9e9b98",
        "secondaryColors": [
            "#9a9999",
            "#8d847a"
        ]
    },
    {
        "name": "Hexer's Boots",
        "image": "Legs/Hexer's Boots.png",
        "primaryColor": "#575b5b",
        "secondaryColors": [
            "#504c46",
            "#4d4439"
        ]
    },
    {
        "name": "Hollow Infantry Boots",
        "image": "Legs/Hollow Infantry Boots.png",
        "primaryColor": "#9e9c9c",
        "secondaryColors": [
            "#696762",
            "#555553"
        ]
    },
    {
        "name": "Hollow Soldier Leggings",
        "image": "Legs/Hollow Soldier Leggings.png",
        "primaryColor": "#867360",
        "secondaryColors": [
            "#6e5e4e",
            "#5b4935"
        ]
    },
    {
        "name": "Imperious Leggings",
        "image": "Legs/Imperious Leggings.png",
        "primaryColor": "#565c5d",
        "secondaryColors": [
            "#575b5b",
            "#575a57"
        ]
    },
    {
        "name": "Imported Trousers",
        "image": "Legs/Imported Trousers.png",
        "primaryColor": "#605c5a",
        "secondaryColors": [
            "#585349",
            "#4d453b"
        ]
    },
    {
        "name": "Infantry Boots",
        "image": "Legs/Infantry Boots.png",
        "primaryColor": "#9b9c9a",
        "secondaryColors": [
            "#6a6960",
            "#525553"
        ]
    },
    {
        "name": "Insolent Boots",
        "image": "Legs/Insolent Boots.png",
        "primaryColor": "#52565b",
        "secondaryColors": [
            "#484848",
            "#45403e"
        ]
    },
    {
        "name": "Ironclad Leggings",
        "image": "Legs/Ironclad Leggings.png",
        "primaryColor": "#929392",
        "secondaryColors": [
            "#616566",
            "#5d5d5a"
        ]
    },
    {
        "name": "Jester's Tights",
        "image": "Legs/Jester's Tights.png",
        "primaryColor": "#a58c5e",
        "secondaryColors": [
            "#8b754d",
            "#654e31"
        ]
    },
    {
        "name": "King's Leggings",
        "image": "Legs/King's Leggings.png",
        "primaryColor": "#4f5659",
        "secondaryColors": [
            "#555350",
            "#494d4e"
        ]
    },
    {
        "name": "Knight Leggings",
        "image": "Legs/Knight Leggings.png",
        "primaryColor": "#9b978f",
        "secondaryColors": [
            "#948777",
            "#87786a"
        ]
    },
    {
        "name": "Leather Boots",
        "image": "Legs/Leather Boots.png",
        "primaryColor": "#887261",
        "secondaryColors": [
            "#725c4b",
            "#654632"
        ]
    },
    {
        "name": "Leggings of Aurous (Invisible)",
        "image": "Legs/Leggings of Aurous (Invisible).png",
        "primaryColor": "#8e90ae",
        "secondaryColors": [
            "#6e8ea4",
            "#7585a3"
        ]
    },
    {
        "name": "Leggings of Aurous",
        "image": "Legs/Leggings of Aurous.png",
        "primaryColor": "#8e4f51",
        "secondaryColors": [
            "#674c49",
            "#554539"
        ]
    },
    {
        "name": "Lion Mage Skirt",
        "image": "Legs/Lion Mage Skirt.png",
        "primaryColor": "#a18e5d",
        "secondaryColors": [
            "#706346",
            "#5d5033"
        ]
    },
    {
        "name": "Lion Warrior Skirt",
        "image": "Legs/Lion Warrior Skirt.png",
        "primaryColor": "#555953",
        "secondaryColors": [
            "#5a522d",
            "#4a4538"
        ]
    },
    {
        "name": "Llwellyn Shoes",
        "image": "Legs/Llwellyn Shoes.png",
        "primaryColor": "#5b5e5e",
        "secondaryColors": [
            "#2d5e5e",
            "#3c4449"
        ]
    },
    {
        "name": "Looking Glass Leggings",
        "image": "Legs/Looking Glass Leggings.png",
        "primaryColor": "#959896",
        "secondaryColors": [
            "#8e9290",
            "#5e6664"
        ]
    },
    {
        "name": "Lucatiel's Trousers",
        "image": "Legs/Lucatiel's Trousers.png",
        "primaryColor": "#554d48",
        "secondaryColors": [
            "#4f493b",
            "#514439"
        ]
    },
    {
        "name": "Mad Warrior Leggings",
        "image": "Legs/Mad Warrior Leggings.png",
        "primaryColor": "#585b5f",
        "secondaryColors": [
            "#4c4d4e",
            "#3b4249"
        ]
    },
    {
        "name": "Manikin Boots",
        "image": "Legs/Manikin Boots.png",
        "primaryColor": "#565258",
        "secondaryColors": [
            "#574d4c",
            "#463938"
        ]
    },
    {
        "name": "Mastodon Leggings",
        "image": "Legs/Mastodon Leggings.png",
        "primaryColor": "#958673",
        "secondaryColors": [
            "#86745c",
            "#70604b"
        ]
    },
    {
        "name": "Monastery Skirt",
        "image": "Legs/Monastery Skirt.png",
        "primaryColor": "#dfdad4",
        "secondaryColors": [
            "#ddd8d0",
            "#cdc5ba"
        ]
    },
    {
        "name": "Moon Butterfly Skirt",
        "image": "Legs/Moon Butterfly Skirt.png",
        "primaryColor": "#c95f23",
        "secondaryColors": [
            "#9d6b4b",
            "#9f5627"
        ]
    },
    {
        "name": "Old Ironclad Leggings",
        "image": "Legs/Old Ironclad Leggings.png",
        "primaryColor": "#898575",
        "secondaryColors": [
            "#62615c",
            "#655f51"
        ]
    },
    {
        "name": "Old Knight Leggings",
        "image": "Legs/Old Knight Leggings.png",
        "primaryColor": "#4c4d4a",
        "secondaryColors": [
            "#42423d",
            "#3a413b"
        ]
    },
    {
        "name": "Pate's Trousers",
        "image": "Legs/Pate's Trousers.png",
        "primaryColor": "#a39f98",
        "secondaryColors": [
            "#a78a6c",
            "#937153"
        ]
    },
    {
        "name": "Peasant Trousers",
        "image": "Legs/Peasant Trousers.png",
        "primaryColor": "#626661",
        "secondaryColors": [
            "#4d462e",
            "#3a4334"
        ]
    },
    {
        "name": "Penal Skirt",
        "image": "Legs/Penal Skirt.png",
        "primaryColor": "#585554",
        "secondaryColors": [
            "#5a514a",
            "#4c423a"
        ]
    },
    {
        "name": "Priestess Skirt",
        "image": "Legs/Priestess Skirt.png",
        "primaryColor": "#908a91",
        "secondaryColors": [
            "#837c83",
            "#827875"
        ]
    },
    {
        "name": "Prisoner's Waistcloth",
        "image": "Legs/Prisoner's Waistcloth.png",
        "primaryColor": "#5f592d",
        "secondaryColors": [
            "#59462d",
            "#4b3320"
        ]
    },
    {
        "name": "Rogue Leggings",
        "image": "Legs/Rogue Leggings.png",
        "primaryColor": "#585f59",
        "secondaryColors": [
            "#585852",
            "#4b4537"
        ]
    },
    {
        "name": "Royal Soldier Leggings",
        "image": "Legs/Royal Soldier Leggings.png",
        "primaryColor": "#5b5e5a",
        "secondaryColors": [
            "#575550",
            "#48443a"
        ]
    },
    {
        "name": "Royal Swordsman Leggings",
        "image": "Legs/Royal Swordsman Leggings.png",
        "primaryColor": "#555658",
        "secondaryColors": [
            "#53504e",
            "#49423c"
        ]
    },
    {
        "name": "Ruin Leggings",
        "image": "Legs/Ruin Leggings.png",
        "primaryColor": "#5c5b5a",
        "secondaryColors": [
            "#5b574d",
            "#4d4738"
        ]
    },
    {
        "name": "Rusted Mastodon Leggings",
        "image": "Legs/Rusted Mastodon Leggings.png",
        "primaryColor": "#a3998f",
        "secondaryColors": [
            "#887664",
            "#685b50"
        ]
    },
    {
        "name": "Saint's Trousers",
        "image": "Legs/Saint's Trousers.png",
        "primaryColor": "#515b60",
        "secondaryColors": [
            "#4b4b4b",
            "#46413c"
        ]
    },
    {
        "name": "Shadow Leggings",
        "image": "Legs/Shadow Leggings.png",
        "primaryColor": "#525a58",
        "secondaryColors": [
            "#4c5453",
            "#424d44"
        ]
    },
    {
        "name": "Smelter Demon Leggings",
        "image": "Legs/Smelter Demon Leggings.png",
        "primaryColor": "#595f60",
        "secondaryColors": [
            "#545b5d",
            "#53595a"
        ]
    },
    {
        "name": "Steel Leggings",
        "image": "Legs/Steel Leggings.png",
        "primaryColor": "#595f5d",
        "secondaryColors": [
            "#545d5c",
            "#535857"
        ]
    },
    {
        "name": "Syan's Leggings",
        "image": "Legs/Syan's Leggings.png",
        "primaryColor": "#a69b92",
        "secondaryColors": [
            "#867565",
            "#6a5f52"
        ]
    },
    {
        "name": "Targray's Leggings",
        "image": "Legs/Targray's Leggings.png",
        "primaryColor": "#9a978f",
        "secondaryColors": [
            "#827b74",
            "#68635b"
        ]
    },
    {
        "name": "Throne Defender Leggings",
        "image": "Legs/Throne Defender Leggings.png",
        "primaryColor": "#5e5f5a",
        "secondaryColors": [
            "#565753",
            "#51514b"
        ]
    },
    {
        "name": "Throne Watcher Leggings",
        "image": "Legs/Throne Watcher Leggings.png",
        "primaryColor": "#6c6a6a",
        "secondaryColors": [
            "#656464",
            "#626362"
        ]
    },
    {
        "name": "Tights of Judgment",
        "image": "Legs/Tights of Judgment.png",
        "primaryColor": "#525758",
        "secondaryColors": [
            "#535555",
            "#535553"
        ]
    },
    {
        "name": "Traveling Merchan Boots",
        "image": "Legs/Traveling Merchan Boots.png",
        "primaryColor": "#87714a",
        "secondaryColors": [
            "#6c5e47",
            "#655232"
        ]
    },
    {
        "name": "Tseldora Trousers",
        "image": "Legs/Tseldora Trousers.png",
        "primaryColor": "#635a4a",
        "secondaryColors": [
            "#5a4c2e",
            "#463921"
        ]
    },
    {
        "name": "Varangian Leggings",
        "image": "Legs/Varangian Leggings.png",
        "primaryColor": "#5b5456",
        "secondaryColors": [
            "#584f4c",
            "#51433b"
        ]
    },
    {
        "name": "Velstadt's Leggings",
        "image": "Legs/Velstadt's Leggings.png",
        "primaryColor": "#5a5c59",
        "secondaryColors": [
            "#56514b",
            "#4c4538"
        ]
    },
    {
        "name": "Vengarl's Boots",
        "image": "Legs/Vengarl's Boots.png",
        "primaryColor": "#595758",
        "secondaryColors": [
            "#595253",
            "#383c41"
        ]
    },
    {
        "name": "Wanderer Boots",
        "image": "Legs/Wanderer Boots.png",
        "primaryColor": "#8c715c",
        "secondaryColors": [
            "#675f54",
            "#5c4937"
        ]
    },
    {
        "name": "White Priest Skirt",
        "image": "Legs/White Priest Skirt.png",
        "primaryColor": "#97958a",
        "secondaryColors": [
            "#898577",
            "#827b6a"
        ]
    },
    {
        "name": "Xanthous Waistcloth",
        "image": "Legs/Xanthous Waistcloth.png",
        "primaryColor": "#e7d99e",
        "secondaryColors": [
            "#e8c928",
            "#d3ab13"
        ]
    },
    {
        "name": "Dragonrider Greatshield",
        "image": "Shields\\Greatshields/Dragonrider Greatshield.png",
        "primaryColor": "#575653",
        "secondaryColors": [
            "#51555b",
            "#4b4539"
        ]
    },
    {
        "name": "Drakekeeper's Greatshield",
        "image": "Shields\\Greatshields/Drakekeeper's Greatshield.png",
        "primaryColor": "#565f61",
        "secondaryColors": [
            "#51585a",
            "#505555"
        ]
    },
    {
        "name": "Greatshield of Glory",
        "image": "Shields\\Greatshields/Greatshield of Glory.png",
        "primaryColor": "#5a5f60",
        "secondaryColors": [
            "#47484a",
            "#3d4144"
        ]
    },
    {
        "name": "Gyrm Greatshield",
        "image": "Shields\\Greatshields/Gyrm Greatshield.png",
        "primaryColor": "#a6aead",
        "secondaryColors": [
            "#9ba09c",
            "#606257"
        ]
    },
    {
        "name": "Havel's Greatshield",
        "image": "Shields\\Greatshields/Havel's Greatshield.png",
        "primaryColor": "#8d8a88",
        "secondaryColors": [
            "#817c78",
            "#5f5e5f"
        ]
    },
    {
        "name": "King's Mirror",
        "image": "Shields\\Greatshields/King's Mirror.png",
        "primaryColor": "#cccece",
        "secondaryColors": [
            "#bec1c1",
            "#bbbec0"
        ]
    },
    {
        "name": "Mastodon Greatshield",
        "image": "Shields\\Greatshields/Mastodon Greatshield.png",
        "primaryColor": "#a48f6b",
        "secondaryColors": [
            "#887454",
            "#766448"
        ]
    },
    {
        "name": "Old Knight Greatshield",
        "image": "Shields\\Greatshields/Old Knight Greatshield.png",
        "primaryColor": "#929998",
        "secondaryColors": [
            "#7a8483",
            "#57605f"
        ]
    },
    {
        "name": "Orma's Greatshield",
        "image": "Shields\\Greatshields/Orma's Greatshield.png",
        "primaryColor": "#939595",
        "secondaryColors": [
            "#616261",
            "#535656"
        ]
    },
    {
        "name": "Pate's Shield",
        "image": "Shields\\Greatshields/Pate's Shield.png",
        "primaryColor": "#9a9a9b",
        "secondaryColors": [
            "#5c6165",
            "#575555"
        ]
    },
    {
        "name": "Pursuer's Greatshield",
        "image": "Shields\\Greatshields/Pursuer's Greatshield.png",
        "primaryColor": "#90949c",
        "secondaryColors": [
            "#737987",
            "#565a5c"
        ]
    },
    {
        "name": "Rebel's Greatshield",
        "image": "Shields\\Greatshields/Rebel's Greatshield.png",
        "primaryColor": "#a79e95",
        "secondaryColors": [
            "#979593",
            "#89847a"
        ]
    },
    {
        "name": "Reeve's Greatshield",
        "image": "Shields\\Greatshields/Reeve's Greatshield.png",
        "primaryColor": "#949494",
        "secondaryColors": [
            "#616363",
            "#616361"
        ]
    },
    {
        "name": "Tower Shield",
        "image": "Shields\\Greatshields/Tower Shield.png",
        "primaryColor": "#9a9b9c",
        "secondaryColors": [
            "#575957",
            "#464439"
        ]
    },
    {
        "name": "Twin Dragon Shield",
        "image": "Shields\\Greatshields/Twin Dragon Shield.png",
        "primaryColor": "#a29b94",
        "secondaryColors": [
            "#958776",
            "#877767"
        ]
    },
    {
        "name": "Wicked Eye Greatshield",
        "image": "Shields\\Greatshields/Wicked Eye Greatshield.png",
        "primaryColor": "#e0dbd6",
        "secondaryColors": [
            "#cdc3ba",
            "#c5b7af"
        ]
    },
    {
        "name": "Archdrake Shield",
        "image": "Shields\\Shields/Archdrake Shield.png",
        "primaryColor": "#cfd0d0",
        "secondaryColors": [
            "#9b9d9c",
            "#5c6467"
        ]
    },
    {
        "name": "Bell Keeper Shield",
        "image": "Shields\\Shields/Bell Keeper Shield.png",
        "primaryColor": "#989393",
        "secondaryColors": [
            "#8e817d",
            "#857873"
        ]
    },
    {
        "name": "Black Dragon Shield",
        "image": "Shields\\Shields/Black Dragon Shield.png",
        "primaryColor": "#606467",
        "secondaryColors": [
            "#605c53",
            "#5a5c5b"
        ]
    },
    {
        "name": "Black Flamestone Parma",
        "image": "Shields\\Shields/Black Flamestone Parma.png",
        "primaryColor": "#979c9b",
        "secondaryColors": [
            "#798487",
            "#585f5d"
        ]
    },
    {
        "name": "Blossom Kite Shield",
        "image": "Shields\\Shields/Blossom Kite Shield.png",
        "primaryColor": "#cda79a",
        "secondaryColors": [
            "#a79c94",
            "#976a5c"
        ]
    },
    {
        "name": "Blue Wooden Shield",
        "image": "Shields\\Shields/Blue Wooden Shield.png",
        "primaryColor": "#c8cbcd",
        "secondaryColors": [
            "#a6a8a8",
            "#567386"
        ]
    },
    {
        "name": "Bone Shield",
        "image": "Shields\\Shields/Bone Shield.png",
        "primaryColor": "#9c9ea2",
        "secondaryColors": [
            "#9a9b9e",
            "#999899"
        ]
    },
    {
        "name": "Bound Wooden Shield",
        "image": "Shields\\Shields/Bound Wooden Shield.png",
        "primaryColor": "#9c958f",
        "secondaryColors": [
            "#847a75",
            "#625b58"
        ]
    },
    {
        "name": "Chaos Shield",
        "image": "Shields\\Shields/Chaos Shield.png",
        "primaryColor": "#979797",
        "secondaryColors": [
            "#605957",
            "#545a63"
        ]
    },
    {
        "name": "Defender's Shield",
        "image": "Shields\\Shields/Defender's Shield.png",
        "primaryColor": "#8d8e89",
        "secondaryColors": [
            "#5e6869",
            "#595b57"
        ]
    },
    {
        "name": "Drakekeeper's Shield",
        "image": "Shields\\Shields/Drakekeeper's Shield.png",
        "primaryColor": "#94989b",
        "secondaryColors": [
            "#7c8187",
            "#555a5c"
        ]
    },
    {
        "name": "Drangleic Shield",
        "image": "Shields\\Shields/Drangleic Shield.png",
        "primaryColor": "#d9d8d8",
        "secondaryColors": [
            "#9d9d9a",
            "#878379"
        ]
    },
    {
        "name": "Golden Wing Shield",
        "image": "Shields\\Shields/Golden Wing Shield.png",
        "primaryColor": "#9d8871",
        "secondaryColors": [
            "#897259",
            "#636156"
        ]
    },
    {
        "name": "Grand Spirit Tree Shield",
        "image": "Shields\\Shields/Grand Spirit Tree Shield.png",
        "primaryColor": "#969ba2",
        "secondaryColors": [
            "#898b8d",
            "#57616c"
        ]
    },
    {
        "name": "Hollow Soldier Shield",
        "image": "Shields\\Shields/Hollow Soldier Shield.png",
        "primaryColor": "#ab9f92",
        "secondaryColors": [
            "#978774",
            "#88745d"
        ]
    },
    {
        "name": "Homunculus Wooden Shield",
        "image": "Shields\\Shields/Homunculus Wooden Shield.png",
        "primaryColor": "#ac9f90",
        "secondaryColors": [
            "#a08b70",
            "#8b755a"
        ]
    },
    {
        "name": "King's Shield",
        "image": "Shields\\Shields/King's Shield.png",
        "primaryColor": "#989794",
        "secondaryColors": [
            "#5f5f5c",
            "#4b4439"
        ]
    },
    {
        "name": "Large Leather Shield",
        "image": "Shields\\Shields/Large Leather Shield.png",
        "primaryColor": "#e7e4d6",
        "secondaryColors": [
            "#e7e4d6",
            "#e0dbc8"
        ]
    },
    {
        "name": "Lion Clan Shield",
        "image": "Shields\\Shields/Lion Clan Shield.png",
        "primaryColor": "#68635e",
        "secondaryColors": [
            "#5f584d",
            "#534535"
        ]
    },
    {
        "name": "Mirrah Shield",
        "image": "Shields\\Shields/Mirrah Shield.png",
        "primaryColor": "#d2d2d0",
        "secondaryColors": [
            "#a09e9b",
            "#8a837a"
        ]
    },
    {
        "name": "Moon Butterfly Shield",
        "image": "Shields\\Shields/Moon Butterfly Shield.png",
        "primaryColor": "#d39d55",
        "secondaryColors": [
            "#da9b27",
            "#a15d1d"
        ]
    },
    {
        "name": "Old Knight's Shield",
        "image": "Shields\\Shields/Old Knight's Shield.png",
        "primaryColor": "#929a98",
        "secondaryColors": [
            "#7a8584",
            "#586563"
        ]
    },
    {
        "name": "Porcine Shield",
        "image": "Shields\\Shields/Porcine Shield.png",
        "primaryColor": "#aca194",
        "secondaryColors": [
            "#9e8d68",
            "#88765d"
        ]
    },
    {
        "name": "Red Rust Shield",
        "image": "Shields\\Shields/Red Rust Shield.png",
        "primaryColor": "#939395",
        "secondaryColors": [
            "#585659",
            "#463d40"
        ]
    },
    {
        "name": "Royal Kite Shield",
        "image": "Shields\\Shields/Royal Kite Shield.png",
        "primaryColor": "#959392",
        "secondaryColors": [
            "#847b75",
            "#605f5d"
        ]
    },
    {
        "name": "Shield of the Insolent",
        "image": "Shields\\Shields/Shield of the Insolent.png",
        "primaryColor": "#d4d4d5",
        "secondaryColors": [
            "#9a9c9d",
            "#7b838a"
        ]
    },
    {
        "name": "Silver Eagle Kite Shield",
        "image": "Shields\\Shields/Silver Eagle Kite Shield.png",
        "primaryColor": "#d1d1d1",
        "secondaryColors": [
            "#9ca1aa",
            "#93969b"
        ]
    },
    {
        "name": "Silverblack Shield",
        "image": "Shields\\Shields/Silverblack Shield.png",
        "primaryColor": "#8da1ac",
        "secondaryColors": [
            "#949da0",
            "#798488"
        ]
    },
    {
        "name": "Slumbering Dragon Shield",
        "image": "Shields\\Shields/Slumbering Dragon Shield.png",
        "primaryColor": "#8e9499",
        "secondaryColors": [
            "#717a85",
            "#575d62"
        ]
    },
    {
        "name": "Spirit Tree Shield",
        "image": "Shields\\Shields/Spirit Tree Shield.png",
        "primaryColor": "#919295",
        "secondaryColors": [
            "#5a5d61",
            "#53595e"
        ]
    },
    {
        "name": "Stone Parma",
        "image": "Shields\\Shields/Stone Parma.png",
        "primaryColor": "#585e65",
        "secondaryColors": [
            "#535556",
            "#3e4143"
        ]
    },
    {
        "name": "Watchdragon Parma",
        "image": "Shields\\Shields/Watchdragon Parma.png",
        "primaryColor": "#dadcdb",
        "secondaryColors": [
            "#bac6c8",
            "#9ea7a5"
        ]
    },
    {
        "name": "Wooden Shield",
        "image": "Shields\\Shields/Wooden Shield.png",
        "primaryColor": "#a6a196",
        "secondaryColors": [
            "#8f8679",
            "#85796d"
        ]
    },
    {
        "name": "Yellow Quartz Shield",
        "image": "Shields\\Shields/Yellow Quartz Shield.png",
        "primaryColor": "#c9b45b",
        "secondaryColors": [
            "#a99557",
            "#aa912b"
        ]
    },
    {
        "name": "Benhart's Parma",
        "image": "Shields\\Small Shields/Benhart's Parma.png",
        "primaryColor": "#9f9d96",
        "secondaryColors": [
            "#8c8577",
            "#5e5d56"
        ]
    },
    {
        "name": "Buckler",
        "image": "Shields\\Small Shields/Buckler.png",
        "primaryColor": "#d1cfcc",
        "secondaryColors": [
            "#9a9998",
            "#5d5a58"
        ]
    },
    {
        "name": "Cleric's Parma",
        "image": "Shields\\Small Shields/Cleric's Parma.png",
        "primaryColor": "#d8ccaf",
        "secondaryColors": [
            "#a08f6f",
            "#88785a"
        ]
    },
    {
        "name": "Cleric's Small Shield",
        "image": "Shields\\Small Shields/Cleric's Small Shield.png",
        "primaryColor": "#d8ccad",
        "secondaryColors": [
            "#9f8e6c",
            "#897857"
        ]
    },
    {
        "name": "Crimson Parma",
        "image": "Shields\\Small Shields/Crimson Parma.png",
        "primaryColor": "#dfe0e1",
        "secondaryColors": [
            "#93979b",
            "#625d5c"
        ]
    },
    {
        "name": "Cursed Bone Shield",
        "image": "Shields\\Small Shields/Cursed Bone Shield.png",
        "primaryColor": "#dadedf",
        "secondaryColors": [
            "#d4d7d8",
            "#989fa0"
        ]
    },
    {
        "name": "Foot Soldier Shield",
        "image": "Shields\\Small Shields/Foot Soldier Shield.png",
        "primaryColor": "#dddcda",
        "secondaryColors": [
            "#a4a39b",
            "#886f56"
        ]
    },
    {
        "name": "Golden Falcon Shield",
        "image": "Shields\\Small Shields/Golden Falcon Shield.png",
        "primaryColor": "#b3a48d",
        "secondaryColors": [
            "#a08d70",
            "#8b7355"
        ]
    },
    {
        "name": "Iron Parma",
        "image": "Shields\\Small Shields/Iron Parma.png",
        "primaryColor": "#d3d3d3",
        "secondaryColors": [
            "#969897",
            "#646869"
        ]
    },
    {
        "name": "Llewelyn Shield",
        "image": "Shields\\Small Shields/Llewelyn Shield.png",
        "primaryColor": "#cdcdce",
        "secondaryColors": [
            "#979a9b",
            "#595c5b"
        ]
    },
    {
        "name": "Magic Shield",
        "image": "Shields\\Small Shields/Magic Shield.png",
        "primaryColor": "#bdc0c4",
        "secondaryColors": [
            "#b6bac3",
            "#a5a8a9"
        ]
    },
    {
        "name": "Manikin Shield",
        "image": "Shields\\Small Shields/Manikin Shield.png",
        "primaryColor": "#999b94",
        "secondaryColors": [
            "#8a8876",
            "#5e5f54"
        ]
    },
    {
        "name": "Phoenix Parma",
        "image": "Shields\\Small Shields/Phoenix Parma.png",
        "primaryColor": "#dbdbda",
        "secondaryColors": [
            "#a1a09b",
            "#8a8676"
        ]
    },
    {
        "name": "Small Leather Shield",
        "image": "Shields\\Small Shields/Small Leather Shield.png",
        "primaryColor": "#d1c8b3",
        "secondaryColors": [
            "#a9a393",
            "#9a8f6f"
        ]
    },
    {
        "name": "Sunlight Parma",
        "image": "Shields\\Small Shields/Sunlight Parma.png",
        "primaryColor": "#a49751",
        "secondaryColors": [
            "#a7952e",
            "#8a7327"
        ]
    },
    {
        "name": "Target Shield",
        "image": "Shields\\Small Shields/Target Shield.png",
        "primaryColor": "#a29d95",
        "secondaryColors": [
            "#968777",
            "#8b725f"
        ]
    },
    {
        "name": "Transgressor's Leather Shield",
        "image": "Shields\\Small Shields/Transgressor's Leather Shield.png",
        "primaryColor": "#9e9f98",
        "secondaryColors": [
            "#9a8e71",
            "#5c5e59"
        ]
    },
    {
        "name": "Varangian Shield",
        "image": "Shields\\Small Shields/Varangian Shield.png",
        "primaryColor": "#dfdede",
        "secondaryColors": [
            "#9e9c9c",
            "#847872"
        ]
    },
    {
        "name": "Watcher's Shield",
        "image": "Shields\\Small Shields/Watcher's Shield.png",
        "primaryColor": "#979896",
        "secondaryColors": [
            "#85847b",
            "#5d5f5b"
        ]
    },
    {
        "name": "Aldia Hammer",
        "image": "Weapons/Aldia Hammer.png",
        "primaryColor": "#98989a",
        "secondaryColors": [
            "#949291",
            "#686463"
        ]
    },
    {
        "name": "Alonne Greatbow",
        "image": "Weapons/Alonne Greatbow.png",
        "primaryColor": "#9ea4a9",
        "secondaryColors": [
            "#9b9fa2",
            "#969b9f"
        ]
    },
    {
        "name": "Arced Sword",
        "image": "Weapons/Arced Sword.png",
        "primaryColor": "#a2a39a",
        "secondaryColors": [
            "#a2a09a",
            "#9c9c95"
        ]
    },
    {
        "name": "Archdrake Chime",
        "image": "Weapons/Archdrake Chime.png",
        "primaryColor": "#c6c3b9",
        "secondaryColors": [
            "#a8a49a",
            "#8c8578"
        ]
    },
    {
        "name": "Archdrake Mace",
        "image": "Weapons/Archdrake Mace.png",
        "primaryColor": "#a6a69d",
        "secondaryColors": [
            "#5c6163",
            "#555958"
        ]
    },
    {
        "name": "Archdrake Staff",
        "image": "Weapons/Archdrake Staff.png",
        "primaryColor": "#a0a296",
        "secondaryColors": [
            "#a19f92",
            "#716e64"
        ]
    },
    {
        "name": "Avelyn",
        "image": "Weapons/Avelyn.png",
        "primaryColor": "#88755c",
        "secondaryColors": [
            "#656159",
            "#645f55"
        ]
    },
    {
        "name": "Bandit Axe",
        "image": "Weapons/Bandit Axe.png",
        "primaryColor": "#a09b97",
        "secondaryColors": [
            "#606a6a",
            "#61615c"
        ]
    },
    {
        "name": "Bandit Greataxe",
        "image": "Weapons/Bandit Greataxe.png",
        "primaryColor": "#a7a19b",
        "secondaryColors": [
            "#85786e",
            "#665b4f"
        ]
    },
    {
        "name": "Bandit's Knife",
        "image": "Weapons/Bandit's Knife.png",
        "primaryColor": "#cdc4b8",
        "secondaryColors": [
            "#c4b9ab",
            "#b0a493"
        ]
    },
    {
        "name": "Barbed Club",
        "image": "Weapons/Barbed Club.png",
        "primaryColor": "#5f6162",
        "secondaryColors": [
            "#585a58",
            "#545a5b"
        ]
    },
    {
        "name": "Bastard Sword",
        "image": "Weapons/Bastard Sword.png",
        "primaryColor": "#9f9f9b",
        "secondaryColors": [
            "#9c9e9f",
            "#626561"
        ]
    },
    {
        "name": "Bat Staff",
        "image": "Weapons/Bat Staff.png",
        "primaryColor": "#897867",
        "secondaryColors": [
            "#6b6256",
            "#6c5e50"
        ]
    },
    {
        "name": "Battle Axe",
        "image": "Weapons/Battle Axe.png",
        "primaryColor": "#dcdceb",
        "secondaryColors": [
            "#9b9e9b",
            "#626763"
        ]
    },
    {
        "name": "Bell Keeper Bow",
        "image": "Weapons/Bell Keeper Bow.png",
        "primaryColor": "#696962",
        "secondaryColors": [
            "#63655c",
            "#5e5d51"
        ]
    },
    {
        "name": "Berserker Blade",
        "image": "Weapons/Berserker Blade.png",
        "primaryColor": "#999ca1",
        "secondaryColors": [
            "#8e9ba7",
            "#5e6466"
        ]
    },
    {
        "name": "Binoculars",
        "image": "Weapons/Binoculars.png",
        "primaryColor": "#d8d2a0",
        "secondaryColors": [
            "#a7a592",
            "#9f9760"
        ]
    },
    {
        "name": "Black Dragon Greataxe",
        "image": "Weapons/Black Dragon Greataxe.png",
        "primaryColor": "#988b66",
        "secondaryColors": [
            "#565d5d",
            "#5d5b52"
        ]
    },
    {
        "name": "Black Dragon Greatsword",
        "image": "Weapons/Black Dragon Greatsword.png",
        "primaryColor": "#625d4e",
        "secondaryColors": [
            "#554e38",
            "#4b4e4c"
        ]
    },
    {
        "name": "Black Dragon Sword",
        "image": "Weapons/Black Dragon Sword.png",
        "primaryColor": "#9d8e64",
        "secondaryColors": [
            "#867856",
            "#696351"
        ]
    },
    {
        "name": "Black Dragon Warpick",
        "image": "Weapons/Black Dragon Warpick.png",
        "primaryColor": "#5f5e59",
        "secondaryColors": [
            "#605c4e",
            "#55564b"
        ]
    },
    {
        "name": "Black Flamestone Dagger",
        "image": "Weapons/Black Flamestone Dagger.png",
        "primaryColor": "#939d9b",
        "secondaryColors": [
            "#536361",
            "#526064"
        ]
    },
    {
        "name": "Black Knight Greataxe",
        "image": "Weapons/Black Knight Greataxe.png",
        "primaryColor": "#9a9794",
        "secondaryColors": [
            "#847b76",
            "#68605b"
        ]
    },
    {
        "name": "Black Knight Greatsword",
        "image": "Weapons/Black Knight Greatsword.png",
        "primaryColor": "#b1aea3",
        "secondaryColors": [
            "#a19b8f",
            "#8e8578"
        ]
    },
    {
        "name": "Black Knight Hablerd",
        "image": "Weapons/Black Knight Hablerd.png",
        "primaryColor": "#87795b",
        "secondaryColors": [
            "#6a6a66",
            "#6c6354"
        ]
    },
    {
        "name": "Black Knight Ultra Greatsword",
        "image": "Weapons/Black Knight Ultra Greatsword.png",
        "primaryColor": "#98948f",
        "secondaryColors": [
            "#655d57",
            "#564b34"
        ]
    },
    {
        "name": "Black Scorpion Stinger",
        "image": "Weapons/Black Scorpion Stinger.png",
        "primaryColor": "#5b6460",
        "secondaryColors": [
            "#585f58",
            "#50554f"
        ]
    },
    {
        "name": "Black Witch's Staff",
        "image": "Weapons/Black Witch's Staff.png",
        "primaryColor": "#50565c",
        "secondaryColors": [
            "#4e5259",
            "#373d44"
        ]
    },
    {
        "name": "Blacksmith's Hammer",
        "image": "Weapons/Blacksmith's Hammer.png",
        "primaryColor": "#9fa09f",
        "secondaryColors": [
            "#555654",
            "#504735"
        ]
    },
    {
        "name": "Blacksteel Katana",
        "image": "Weapons/Blacksteel Katana.png",
        "primaryColor": "#565e64",
        "secondaryColors": [
            "#585b5c",
            "#565a5e"
        ]
    },
    {
        "name": "Bloodied Whip",
        "image": "Weapons/Bloodied Whip.png",
        "primaryColor": "#9f8763",
        "secondaryColors": [
            "#8e7250",
            "#756347"
        ]
    },
    {
        "name": "Blue Flame",
        "image": "Weapons/Blue Flame.png",
        "primaryColor": "#dfe0e0",
        "secondaryColors": [
            "#d3d4d2",
            "#d0d1d0"
        ]
    },
    {
        "name": "Blue Knight's Halberd",
        "image": "Weapons/Blue Knight's Halberd.png",
        "primaryColor": "#dddedd",
        "secondaryColors": [
            "#989c97",
            "#636461"
        ]
    },
    {
        "name": "Bluemoon Greatsword",
        "image": "Weapons/Bluemoon Greatsword.png",
        "primaryColor": "#9ca198",
        "secondaryColors": [
            "#76adb0",
            "#699796"
        ]
    },
    {
        "name": "Bone Scythe",
        "image": "Weapons/Bone Scythe.png",
        "primaryColor": "#928d88",
        "secondaryColors": [
            "#61605e",
            "#615f58"
        ]
    },
    {
        "name": "Bone Staff",
        "image": "Weapons/Bone Staff.png",
        "primaryColor": "#887558",
        "secondaryColors": [
            "#6d5d4b",
            "#6a5c56"
        ]
    },
    {
        "name": "Bound Hand Axe",
        "image": "Weapons/Bound Hand Axe.png",
        "primaryColor": "#595c5e",
        "secondaryColors": [
            "#575a5c",
            "#565152"
        ]
    },
    {
        "name": "Bow of Want",
        "image": "Weapons/Bow of Want.png",
        "primaryColor": "#8a7557",
        "secondaryColors": [
            "#6e5f4a",
            "#53544b"
        ]
    },
    {
        "name": "Broadsword",
        "image": "Weapons/Broadsword.png",
        "primaryColor": "#9b9e9b",
        "secondaryColors": [
            "#9a9c93",
            "#97988f"
        ]
    },
    {
        "name": "Broken Straight Sword",
        "image": "Weapons/Broken Straight Sword.png",
        "primaryColor": "#616363",
        "secondaryColors": [
            "#5f5958",
            "#575554"
        ]
    },
    {
        "name": "Broken Thief Sword",
        "image": "Weapons/Broken Thief Sword.png",
        "primaryColor": "#94968c",
        "secondaryColors": [
            "#868579",
            "#5e625b"
        ]
    },
    {
        "name": "Butcher's Knife",
        "image": "Weapons/Butcher's Knife.png",
        "primaryColor": "#95918e",
        "secondaryColors": [
            "#87817d",
            "#847a75"
        ]
    },
    {
        "name": "Caestus",
        "image": "Weapons/Caestus.png",
        "primaryColor": "#a6a095",
        "secondaryColors": [
            "#958c71",
            "#86725e"
        ]
    },
    {
        "name": "Caitha's Chime",
        "image": "Weapons/Caitha's Chime.png",
        "primaryColor": "#876f66",
        "secondaryColors": [
            "#675b54",
            "#69534d"
        ]
    },
    {
        "name": "Channeler's Trident",
        "image": "Weapons/Channeler's Trident.png",
        "primaryColor": "#a8a092",
        "secondaryColors": [
            "#a29669",
            "#6d634c"
        ]
    },
    {
        "name": "Chaos Blade",
        "image": "Weapons/Chaos Blade.png",
        "primaryColor": "#cccdca",
        "secondaryColors": [
            "#a6a5a0",
            "#a4a5a1"
        ]
    },
    {
        "name": "Chaos Rapier",
        "image": "Weapons/Chaos Rapier.png",
        "primaryColor": "#a19f9d",
        "secondaryColors": [
            "#9c9c97",
            "#6c6862"
        ]
    },
    {
        "name": "Chariot Lance",
        "image": "Weapons/Chariot Lance.png",
        "primaryColor": "#a9a4a2",
        "secondaryColors": [
            "#68635f",
            "#66625b"
        ]
    },
    {
        "name": "Chime of Want",
        "image": "Weapons/Chime of Want.png",
        "primaryColor": "#5a5855",
        "secondaryColors": [
            "#55524e",
            "#504e4b"
        ]
    },
    {
        "name": "Claws",
        "image": "Weapons/Claws.png",
        "primaryColor": "#949d9b",
        "secondaryColors": [
            "#8c9795",
            "#73898a"
        ]
    },
    {
        "name": "Claymore",
        "image": "Weapons/Claymore.png",
        "primaryColor": "#dddedd",
        "secondaryColors": [
            "#cecdc9",
            "#aeada4"
        ]
    },
    {
        "name": "Cleric's Sacred Chime",
        "image": "Weapons/Cleric's Sacred Chime.png",
        "primaryColor": "#a89d8f",
        "secondaryColors": [
            "#988870",
            "#87775e"
        ]
    },
    {
        "name": "Club",
        "image": "Weapons/Club.png",
        "primaryColor": "#6a5f56",
        "secondaryColors": [
            "#6e5b48",
            "#614a33"
        ]
    },
    {
        "name": "Composite Bow",
        "image": "Weapons/Composite Bow.png",
        "primaryColor": "#9b9475",
        "secondaryColors": [
            "#6c614d",
            "#67605a"
        ]
    },
    {
        "name": "Craftsman's Hammer",
        "image": "Weapons/Craftsman's Hammer.png",
        "primaryColor": "#64645d",
        "secondaryColors": [
            "#625e56",
            "#504538"
        ]
    },
    {
        "name": "Crescent Axe",
        "image": "Weapons/Crescent Axe.png",
        "primaryColor": "#a89b8f",
        "secondaryColors": [
            "#9a8873",
            "#89745d"
        ]
    },
    {
        "name": "Crescent Sickle",
        "image": "Weapons/Crescent Sickle.png",
        "primaryColor": "#616463",
        "secondaryColors": [
            "#61625f",
            "#5e5f5f"
        ]
    },
    {
        "name": "Crypt Blacksword",
        "image": "Weapons/Crypt Blacksword.png",
        "primaryColor": "#51534f",
        "secondaryColors": [
            "#4e524f",
            "#48453a"
        ]
    },
    {
        "name": "Curved Dragon Greatsword",
        "image": "Weapons/Curved Dragon Greatsword.png",
        "primaryColor": "#969697",
        "secondaryColors": [
            "#5b5e61",
            "#575859"
        ]
    },
    {
        "name": "Curved Twinblade",
        "image": "Weapons/Curved Twinblade.png",
        "primaryColor": "#e1e3dd",
        "secondaryColors": [
            "#a7a89d",
            "#646358"
        ]
    },
    {
        "name": "Dagger",
        "image": "Weapons/Dagger.png",
        "primaryColor": "#aaa39d",
        "secondaryColors": [
            "#9c9b9b",
            "#9d745f"
        ]
    },
    {
        "name": "Dark Pyromancy Flame",
        "image": "Weapons/Dark Pyromancy Flame.png",
        "primaryColor": "#fca20a",
        "secondaryColors": [
            "#ef5708",
            "#d62706"
        ]
    },
    {
        "name": "Darkdrift",
        "image": "Weapons/Darkdrift.png",
        "primaryColor": "#99acc9",
        "secondaryColors": [
            "#738db4",
            "#575454"
        ]
    },
    {
        "name": "Defender Greatsword",
        "image": "Weapons/Defender Greatsword.png",
        "primaryColor": "#636562",
        "secondaryColors": [
            "#5a5e57",
            "#595d55"
        ]
    },
    {
        "name": "Demon's Great Hammer",
        "image": "Weapons/Demon's Great Hammer.png",
        "primaryColor": "#6d675b",
        "secondaryColors": [
            "#63594b",
            "#4e4539"
        ]
    },
    {
        "name": "Disc Chime",
        "image": "Weapons/Disc Chime.png",
        "primaryColor": "#ac9f89",
        "secondaryColors": [
            "#988a70",
            "#867960"
        ]
    },
    {
        "name": "Dragon Chime",
        "image": "Weapons/Dragon Chime.png",
        "primaryColor": "#c3b990",
        "secondaryColors": [
            "#a4a291",
            "#a89c6f"
        ]
    },
    {
        "name": "Dragon Tooth",
        "image": "Weapons/Dragon Tooth.png",
        "primaryColor": "#949595",
        "secondaryColors": [
            "#656a64",
            "#5a5e5b"
        ]
    },
    {
        "name": "Dragonrider Bow",
        "image": "Weapons/Dragonrider Bow.png",
        "primaryColor": "#5c594e",
        "secondaryColors": [
            "#5c5751",
            "#574b39"
        ]
    },
    {
        "name": "Dragonrider Twinblade",
        "image": "Weapons/Dragonrider Twinblade.png",
        "primaryColor": "#92948f",
        "secondaryColors": [
            "#626660",
            "#5c615d"
        ]
    },
    {
        "name": "Dragonrider's Halberd",
        "image": "Weapons/Dragonrider's Halberd.png",
        "primaryColor": "#999996",
        "secondaryColors": [
            "#63655f",
            "#62635f"
        ]
    },
    {
        "name": "Dragonslayer Greatbow",
        "image": "Weapons/Dragonslayer Greatbow.png",
        "primaryColor": "#aba19a",
        "secondaryColors": [
            "#9c9072",
            "#968976"
        ]
    },
    {
        "name": "Dragonslayer Spear",
        "image": "Weapons/Dragonslayer Spear.png",
        "primaryColor": "#9fa0a0",
        "secondaryColors": [
            "#8d8a66",
            "#636353"
        ]
    },
    {
        "name": "Dragonslayer's Crescent Axe",
        "image": "Weapons/Dragonslayer's Crescent Axe.png",
        "primaryColor": "#a5a5a1",
        "secondaryColors": [
            "#555250",
            "#4e433b"
        ]
    },
    {
        "name": "Drakekeeper's Great Hammer",
        "image": "Weapons/Drakekeeper's Great Hammer.png",
        "primaryColor": "#5c6161",
        "secondaryColors": [
            "#565755",
            "#3c4347"
        ]
    },
    {
        "name": "Drakekeeper's Greataxe",
        "image": "Weapons/Drakekeeper's Greataxe.png",
        "primaryColor": "#5b5d5d",
        "secondaryColors": [
            "#4c4e4d",
            "#4a4c4a"
        ]
    },
    {
        "name": "Drakekeeper's Sword",
        "image": "Weapons/Drakekeeper's Sword.png",
        "primaryColor": "#a2a4a3",
        "secondaryColors": [
            "#616261",
            "#5c5c5c"
        ]
    },
    {
        "name": "Drakekeeper's Ultra Greatsword",
        "image": "Weapons/Drakekeeper's Ultra Greatsword.png",
        "primaryColor": "#5a5b5a",
        "secondaryColors": [
            "#515250",
            "#4c4c47"
        ]
    },
    {
        "name": "Drakekeeper's Warpick",
        "image": "Weapons/Drakekeeper's Warpick.png",
        "primaryColor": "#5f605e",
        "secondaryColors": [
            "#535555",
            "#515152"
        ]
    },
    {
        "name": "Drakewing Ultra Greatsword",
        "image": "Weapons/Drakewing Ultra Greatsword.png",
        "primaryColor": "#9299aa",
        "secondaryColors": [
            "#8d95a7",
            "#8b92a5"
        ]
    },
    {
        "name": "Drangleic Sword",
        "image": "Weapons/Drangleic Sword.png",
        "primaryColor": "#666c64",
        "secondaryColors": [
            "#5f625a",
            "#605f5a"
        ]
    },
    {
        "name": "Espada Ropera",
        "image": "Weapons/Espada Ropera.png",
        "primaryColor": "#a0a29b",
        "secondaryColors": [
            "#6b685f",
            "#686865"
        ]
    },
    {
        "name": "Estoc",
        "image": "Weapons/Estoc.png",
        "primaryColor": "#9fa19f",
        "secondaryColors": [
            "#989b97",
            "#969992"
        ]
    },
    {
        "name": "Falchion",
        "image": "Weapons/Falchion.png",
        "primaryColor": "#91908d",
        "secondaryColors": [
            "#656960",
            "#636159"
        ]
    },
    {
        "name": "Flamberge",
        "image": "Weapons/Flamberge.png",
        "primaryColor": "#a1a29f",
        "secondaryColors": [
            "#959595",
            "#949594"
        ]
    },
    {
        "name": "Foot Soldier Sword",
        "image": "Weapons/Foot Soldier Sword.png",
        "primaryColor": "#a6aaa8",
        "secondaryColors": [
            "#a2a6a3",
            "#a1a3a0"
        ]
    },
    {
        "name": "Full Moon Sickle",
        "image": "Weapons/Full Moon Sickle.png",
        "primaryColor": "#9d9f9d",
        "secondaryColors": [
            "#606662",
            "#596062"
        ]
    },
    {
        "name": "Gargoyle Bident",
        "image": "Weapons/Gargoyle Bident.png",
        "primaryColor": "#575f55",
        "secondaryColors": [
            "#4d6058",
            "#49544c"
        ]
    },
    {
        "name": "Giant Stone Axe",
        "image": "Weapons/Giant Stone Axe.png",
        "primaryColor": "#a2a396",
        "secondaryColors": [
            "#606263",
            "#616254"
        ]
    },
    {
        "name": "Giant Warrior Club",
        "image": "Weapons/Giant Warrior Club.png",
        "primaryColor": "#a2a48b",
        "secondaryColors": [
            "#8b8c73",
            "#626355"
        ]
    },
    {
        "name": "Grand Lance",
        "image": "Weapons/Grand Lance.png",
        "primaryColor": "#67645e",
        "secondaryColors": [
            "#66625a",
            "#635b51"
        ]
    },
    {
        "name": "Great Club",
        "image": "Weapons/Great Club.png",
        "primaryColor": "#726962",
        "secondaryColors": [
            "#6a5d47",
            "#554834"
        ]
    },
    {
        "name": "Great Machete",
        "image": "Weapons/Great Machete.png",
        "primaryColor": "#979897",
        "secondaryColors": [
            "#5e6360",
            "#585c59"
        ]
    },
    {
        "name": "Great Scythe",
        "image": "Weapons/Great Scythe.png",
        "primaryColor": "#919393",
        "secondaryColors": [
            "#626462",
            "#68615a"
        ]
    },
    {
        "name": "Greataxe",
        "image": "Weapons/Greataxe.png",
        "primaryColor": "#5a5c58",
        "secondaryColors": [
            "#5c514a",
            "#53453b"
        ]
    },
    {
        "name": "Greatsword",
        "image": "Weapons/Greatsword.png",
        "primaryColor": "#8e918e",
        "secondaryColors": [
            "#646866",
            "#5f6461"
        ]
    },
    {
        "name": "Gyrm Axe",
        "image": "Weapons/Gyrm Axe.png",
        "primaryColor": "#97958b",
        "secondaryColors": [
            "#847971",
            "#6a6668"
        ]
    },
    {
        "name": "Gyrm Great Hammer",
        "image": "Weapons/Gyrm Great Hammer.png",
        "primaryColor": "#9c9b9c",
        "secondaryColors": [
            "#606068",
            "#606060"
        ]
    },
    {
        "name": "Gyrm Greataxe",
        "image": "Weapons/Gyrm Greataxe.png",
        "primaryColor": "#e1ddd8",
        "secondaryColors": [
            "#9d9b91",
            "#888679"
        ]
    },
    {
        "name": "Halberd",
        "image": "Weapons/Halberd.png",
        "primaryColor": "#9fa19c",
        "secondaryColors": [
            "#9b9f9b",
            "#9c9e9b"
        ]
    },
    {
        "name": "Hand Axe",
        "image": "Weapons/Hand Axe.png",
        "primaryColor": "#a5a19b",
        "secondaryColors": [
            "#84776c",
            "#6d5f58"
        ]
    },
    {
        "name": "Handmaid's Ladle",
        "image": "Weapons/Handmaid's Ladle.png",
        "primaryColor": "#8f6d5b",
        "secondaryColors": [
            "#625349",
            "#534638"
        ]
    },
    {
        "name": "Heavy Crossbow",
        "image": "Weapons/Heavy Crossbow.png",
        "primaryColor": "#a88f65",
        "secondaryColors": [
            "#907450",
            "#6a604e"
        ]
    },
    {
        "name": "Heide Greatlance",
        "image": "Weapons/Heide Greatlance.png",
        "primaryColor": "#e7e7df",
        "secondaryColors": [
            "#a8a69d",
            "#a2a39c"
        ]
    },
    {
        "name": "Heide Knight Sword",
        "image": "Weapons/Heide Knight Sword.png",
        "primaryColor": "#d0d0cb",
        "secondaryColors": [
            "#a6a59b",
            "#a1a098"
        ]
    },
    {
        "name": "Heide Lance",
        "image": "Weapons/Heide Lance.png",
        "primaryColor": "#a9a69f",
        "secondaryColors": [
            "#9c9e99",
            "#a29076"
        ]
    },
    {
        "name": "Heide Spear",
        "image": "Weapons/Heide Spear.png",
        "primaryColor": "#aaaba5",
        "secondaryColors": [
            "#a9a79d",
            "#a2a39d"
        ]
    },
    {
        "name": "Helix Halberd",
        "image": "Weapons/Helix Halberd.png",
        "primaryColor": "#5c6866",
        "secondaryColors": [
            "#5d6767",
            "#5c6767"
        ]
    },
    {
        "name": "Homunculus Mace",
        "image": "Weapons/Homunculus Mace.png",
        "primaryColor": "#a38d71",
        "secondaryColors": [
            "#897459",
            "#675c4d"
        ]
    },
    {
        "name": "Hunter's Blackbow",
        "image": "Weapons/Hunter's Blackbow.png",
        "primaryColor": "#b1b0ae",
        "secondaryColors": [
            "#b0b0af",
            "#646363"
        ]
    },
    {
        "name": "Idol's Chime",
        "image": "Weapons/Idol's Chime.png",
        "primaryColor": "#5a5f5f",
        "secondaryColors": [
            "#5a5b58",
            "#39454e"
        ]
    },
    {
        "name": "Infantry Axe",
        "image": "Weapons/Infantry Axe.png",
        "primaryColor": "#e1e0df",
        "secondaryColors": [
            "#9f9e95",
            "#8f8675"
        ]
    },
    {
        "name": "Iron King Hammer",
        "image": "Weapons/Iron King Hammer.png",
        "primaryColor": "#8f9fa5",
        "secondaryColors": [
            "#79898e",
            "#566362"
        ]
    },
    {
        "name": "Key to the Embedded",
        "image": "Weapons/Key to the Embedded.png",
        "primaryColor": "#a8a69f",
        "secondaryColors": [
            "#696759",
            "#636355"
        ]
    },
    {
        "name": "King's Ultra Greatsword",
        "image": "Weapons/King's Ultra Greatsword.png",
        "primaryColor": "#5c5b54",
        "secondaryColors": [
            "#55544c",
            "#45433b"
        ]
    },
    {
        "name": "Large CLub",
        "image": "Weapons/Large CLub.png",
        "primaryColor": "#aba28d",
        "secondaryColors": [
            "#908b75",
            "#6b695a"
        ]
    },
    {
        "name": "Light Crossbow",
        "image": "Weapons/Light Crossbow.png",
        "primaryColor": "#a3a09a",
        "secondaryColors": [
            "#a88c69",
            "#8f7153"
        ]
    },
    {
        "name": "Lion Greataxe",
        "image": "Weapons/Lion Greataxe.png",
        "primaryColor": "#666665",
        "secondaryColors": [
            "#565553",
            "#4a433b"
        ]
    },
    {
        "name": "Lizard Staff",
        "image": "Weapons/Lizard Staff.png",
        "primaryColor": "#8c765e",
        "secondaryColors": [
            "#6c6c5d",
            "#67634f"
        ]
    },
    {
        "name": "Long Bow",
        "image": "Weapons/Long Bow.png",
        "primaryColor": "#a09674",
        "secondaryColors": [
            "#9d8f6d",
            "#a18c62"
        ]
    },
    {
        "name": "Longsword",
        "image": "Weapons/Longsword.png",
        "primaryColor": "#9c9b9a",
        "secondaryColors": [
            "#6e6d65",
            "#6b6d67"
        ]
    },
    {
        "name": "Lost Sinner's Sword",
        "image": "Weapons/Lost Sinner's Sword.png",
        "primaryColor": "#8c898a",
        "secondaryColors": [
            "#685c5a",
            "#645c5b"
        ]
    },
    {
        "name": "Lucerne",
        "image": "Weapons/Lucerne.png",
        "primaryColor": "#a89b92",
        "secondaryColors": [
            "#919491",
            "#65656a"
        ]
    },
    {
        "name": "Mace of the Insolent",
        "image": "Weapons/Mace of the Insolent.png",
        "primaryColor": "#9e9f9d",
        "secondaryColors": [
            "#616860",
            "#62665e"
        ]
    },
    {
        "name": "Mace",
        "image": "Weapons/Mace.png",
        "primaryColor": "#999791",
        "secondaryColors": [
            "#5d5d51",
            "#5b5c56"
        ]
    },
    {
        "name": "Magic Staff of Wisdom",
        "image": "Weapons/Magic Staff of Wisdom.png",
        "primaryColor": "#656565",
        "secondaryColors": [
            "#5a5a57",
            "#5a5a57"
        ]
    },
    {
        "name": "Mail Breaker",
        "image": "Weapons/Mail Breaker.png",
        "primaryColor": "#a39c8e",
        "secondaryColors": [
            "#6e6b5f",
            "#6c675d"
        ]
    },
    {
        "name": "Malformed Claws",
        "image": "Weapons/Malformed Claws.png",
        "primaryColor": "#939296",
        "secondaryColors": [
            "#787083",
            "#5a545f"
        ]
    },
    {
        "name": "Malformed Shell",
        "image": "Weapons/Malformed Shell.png",
        "primaryColor": "#886e64",
        "secondaryColors": [
            "#6b615d",
            "#615252"
        ]
    },
    {
        "name": "Malformed Skull",
        "image": "Weapons/Malformed Skull.png",
        "primaryColor": "#5d5b50",
        "secondaryColors": [
            "#584e46",
            "#4f4338"
        ]
    },
    {
        "name": "Manikin Claws",
        "image": "Weapons/Manikin Claws.png",
        "primaryColor": "#9b9da3",
        "secondaryColors": [
            "#9a9ba0",
            "#999b9c"
        ]
    },
    {
        "name": "Manikin Knife",
        "image": "Weapons/Manikin Knife.png",
        "primaryColor": "#a1a2a4",
        "secondaryColors": [
            "#a1a1a2",
            "#97969c"
        ]
    },
    {
        "name": "Manikin Sabre",
        "image": "Weapons/Manikin Sabre.png",
        "primaryColor": "#d4d0d3",
        "secondaryColors": [
            "#a4999b",
            "#91725c"
        ]
    },
    {
        "name": "Manslayer",
        "image": "Weapons/Manslayer.png",
        "primaryColor": "#aaa8a2",
        "secondaryColors": [
            "#717061",
            "#656353"
        ]
    },
    {
        "name": "Mastodon Greatsword",
        "image": "Weapons/Mastodon Greatsword.png",
        "primaryColor": "#9d9d9c",
        "secondaryColors": [
            "#9b9995",
            "#686865"
        ]
    },
    {
        "name": "Mastodon Halberd",
        "image": "Weapons/Mastodon Halberd.png",
        "primaryColor": "#cbb58b",
        "secondaryColors": [
            "#ad9367",
            "#8d7149"
        ]
    },
    {
        "name": "Melu Scimitar",
        "image": "Weapons/Melu Scimitar.png",
        "primaryColor": "#97998e",
        "secondaryColors": [
            "#938b70",
            "#6a6a60"
        ]
    },
    {
        "name": "Mirrah Greatsword",
        "image": "Weapons/Mirrah Greatsword.png",
        "primaryColor": "#989998",
        "secondaryColors": [
            "#676460",
            "#66605a"
        ]
    },
    {
        "name": "Monastery Scimitar",
        "image": "Weapons/Monastery Scimitar.png",
        "primaryColor": "#9f9f90",
        "secondaryColors": [
            "#8b8975",
            "#60635e"
        ]
    },
    {
        "name": "Moonlight Greatsword",
        "image": "Weapons/Moonlight Greatsword.png",
        "primaryColor": "#59c4b8",
        "secondaryColors": [
            "#4eb1a4",
            "#38998d"
        ]
    },
    {
        "name": "Morning Star",
        "image": "Weapons/Morning Star.png",
        "primaryColor": "#9b9b9c",
        "secondaryColors": [
            "#616161",
            "#625f63"
        ]
    },
    {
        "name": "Murakumo",
        "image": "Weapons/Murakumo.png",
        "primaryColor": "#a9a9a5",
        "secondaryColors": [
            "#9ea39c",
            "#878975"
        ]
    },
    {
        "name": "Mytha's Bent Blade",
        "image": "Weapons/Mytha's Bent Blade.png",
        "primaryColor": "#515b61",
        "secondaryColors": [
            "#525a5e",
            "#53595f"
        ]
    },
    {
        "name": "Notched Whip",
        "image": "Weapons/Notched Whip.png",
        "primaryColor": "#5d615b",
        "secondaryColors": [
            "#545954",
            "#545753"
        ]
    },
    {
        "name": "Old Knight Greatsword",
        "image": "Weapons/Old Knight Greatsword.png",
        "primaryColor": "#505f60",
        "secondaryColors": [
            "#4a5655",
            "#3b4742"
        ]
    },
    {
        "name": "Old Knight Halberd",
        "image": "Weapons/Old Knight Halberd.png",
        "primaryColor": "#5c6561",
        "secondaryColors": [
            "#515c58",
            "#384643"
        ]
    },
    {
        "name": "Old Knight Hammer",
        "image": "Weapons/Old Knight Hammer.png",
        "primaryColor": "#56645d",
        "secondaryColors": [
            "#4a5855",
            "#384745"
        ]
    },
    {
        "name": "Old Knight Pike",
        "image": "Weapons/Old Knight Pike.png",
        "primaryColor": "#4a5c59",
        "secondaryColors": [
            "#4a5955",
            "#485752"
        ]
    },
    {
        "name": "Old Knight Ultra Greatsword",
        "image": "Weapons/Old Knight Ultra Greatsword.png",
        "primaryColor": "#4d605e",
        "secondaryColors": [
            "#4f5f5d",
            "#4f5f5c"
        ]
    },
    {
        "name": "Old Mirrah Greatsword",
        "image": "Weapons/Old Mirrah Greatsword.png",
        "primaryColor": "#989998",
        "secondaryColors": [
            "#676460",
            "#66605a"
        ]
    },
    {
        "name": "Old Whip",
        "image": "Weapons/Old Whip.png",
        "primaryColor": "#5a4531",
        "secondaryColors": [
            "#4a3a27",
            "#483626"
        ]
    },
    {
        "name": "Olenford's Staff",
        "image": "Weapons/Olenford's Staff.png",
        "primaryColor": "#4c8fa3",
        "secondaryColors": [
            "#367387",
            "#256a97"
        ]
    },
    {
        "name": "Parrying Dagger",
        "image": "Weapons/Parrying Dagger.png",
        "primaryColor": "#aca59b",
        "secondaryColors": [
            "#9d8f6c",
            "#6b6b5d"
        ]
    },
    {
        "name": "Partizan",
        "image": "Weapons/Partizan.png",
        "primaryColor": "#969ba0",
        "secondaryColors": [
            "#8a6c5b",
            "#61635d"
        ]
    },
    {
        "name": "Pate's Spear",
        "image": "Weapons/Pate's Spear.png",
        "primaryColor": "#605e5a",
        "secondaryColors": [
            "#595651",
            "#50443c"
        ]
    },
    {
        "name": "Pickaxe",
        "image": "Weapons/Pickaxe.png",
        "primaryColor": "#ab9f93",
        "secondaryColors": [
            "#a28969",
            "#8d755c"
        ]
    },
    {
        "name": "Pike",
        "image": "Weapons/Pike.png",
        "primaryColor": "#9fa0a3",
        "secondaryColors": [
            "#5f656a",
            "#5c5f65"
        ]
    },
    {
        "name": "Priest's Chime",
        "image": "Weapons/Priest's Chime.png",
        "primaryColor": "#a08e68",
        "secondaryColors": [
            "#897552",
            "#756549"
        ]
    },
    {
        "name": "Protective Chime",
        "image": "Weapons/Protective Chime.png",
        "primaryColor": "#60625d",
        "secondaryColors": [
            "#606057",
            "#585c56"
        ]
    },
    {
        "name": "Pursuer's Ultra Greatsword",
        "image": "Weapons/Pursuer's Ultra Greatsword.png",
        "primaryColor": "#cccdcc",
        "secondaryColors": [
            "#9b9e9b",
            "#5d645e"
        ]
    },
    {
        "name": "Pyromancy Flame",
        "image": "Weapons/Pyromancy Flame.png",
        "primaryColor": "#ec5612",
        "secondaryColors": [
            "#d82307",
            "#a42509"
        ]
    },
    {
        "name": "Rapier",
        "image": "Weapons/Rapier.png",
        "primaryColor": "#a6a59c",
        "secondaryColors": [
            "#a6a596",
            "#a3a193"
        ]
    },
    {
        "name": "Red Iron Twinblade",
        "image": "Weapons/Red Iron Twinblade.png",
        "primaryColor": "#e1dcdb",
        "secondaryColors": [
            "#a99c98",
            "#89726c"
        ]
    },
    {
        "name": "Red Rust Scimitar",
        "image": "Weapons/Red Rust Scimitar.png",
        "primaryColor": "#969293",
        "secondaryColors": [
            "#666567",
            "#645c5c"
        ]
    },
    {
        "name": "Red Rust Sword",
        "image": "Weapons/Red Rust Sword.png",
        "primaryColor": "#97999a",
        "secondaryColors": [
            "#908b8b",
            "#6b6565"
        ]
    },
    {
        "name": "Reinforced Club",
        "image": "Weapons/Reinforced Club.png",
        "primaryColor": "#ac9d91",
        "secondaryColors": [
            "#978676",
            "#887767"
        ]
    },
    {
        "name": "Ricard's Rapier",
        "image": "Weapons/Ricard's Rapier.png",
        "primaryColor": "#a7a8a7",
        "secondaryColors": [
            "#a2a5a5",
            "#989a9a"
        ]
    },
    {
        "name": "Roaring Halberd",
        "image": "Weapons/Roaring Halberd.png",
        "primaryColor": "#9a9a95",
        "secondaryColors": [
            "#606261",
            "#615f57"
        ]
    },
    {
        "name": "Royal Dirk",
        "image": "Weapons/Royal Dirk.png",
        "primaryColor": "#a5a8a4",
        "secondaryColors": [
            "#999b95",
            "#979a93"
        ]
    },
    {
        "name": "Royal Greatsword",
        "image": "Weapons/Royal Greatsword.png",
        "primaryColor": "#606564",
        "secondaryColors": [
            "#5d605f",
            "#5a5d5d"
        ]
    },
    {
        "name": "Ruler's Sword",
        "image": "Weapons/Ruler's Sword.png",
        "primaryColor": "#c7cac8",
        "secondaryColors": [
            "#a8aaa9",
            "#a5a7a3"
        ]
    },
    {
        "name": "Sacred Chime Hammer",
        "image": "Weapons/Sacred Chime Hammer.png",
        "primaryColor": "#615f58",
        "secondaryColors": [
            "#5e5b4e",
            "#5b594e"
        ]
    },
    {
        "name": "Santier's Spear (Broken)",
        "image": "Weapons/Santier's Spear (Broken).png",
        "primaryColor": "#626258",
        "secondaryColors": [
            "#5b5c57",
            "#56544c"
        ]
    },
    {
        "name": "Santier's Spear",
        "image": "Weapons/Santier's Spear.png",
        "primaryColor": "#65605b",
        "secondaryColors": [
            "#5c564e",
            "#4b433b"
        ]
    },
    {
        "name": "Scimitar",
        "image": "Weapons/Scimitar.png",
        "primaryColor": "#9d9ca0",
        "secondaryColors": [
            "#9a9e94",
            "#898b7a"
        ]
    },
    {
        "name": "Scythe of Want",
        "image": "Weapons/Scythe of Want.png",
        "primaryColor": "#5f605e",
        "secondaryColors": [
            "#5c5a57",
            "#585855"
        ]
    },
    {
        "name": "Scythe",
        "image": "Weapons/Scythe.png",
        "primaryColor": "#69645b",
        "secondaryColors": [
            "#69635e",
            "#626367"
        ]
    },
    {
        "name": "Scyther of Nahr Alma",
        "image": "Weapons/Scyther of Nahr Alma.png",
        "primaryColor": "#63635e",
        "secondaryColors": [
            "#605e59",
            "#5c5c56"
        ]
    },
    {
        "name": "Sea Bow",
        "image": "Weapons/Sea Bow.png",
        "primaryColor": "#9c9693",
        "secondaryColors": [
            "#6a6462",
            "#605a54"
        ]
    },
    {
        "name": "Shadow Dagger",
        "image": "Weapons/Shadow Dagger.png",
        "primaryColor": "#5d6864",
        "secondaryColors": [
            "#5b615d",
            "#565d58"
        ]
    },
    {
        "name": "Shield Crossbow",
        "image": "Weapons/Shield Crossbow.png",
        "primaryColor": "#9c9f9e",
        "secondaryColors": [
            "#9b9e9f",
            "#5d635f"
        ]
    },
    {
        "name": "Short Bow",
        "image": "Weapons/Short Bow.png",
        "primaryColor": "#929263",
        "secondaryColors": [
            "#696756",
            "#6a6651"
        ]
    },
    {
        "name": "Shortsword",
        "image": "Weapons/Shortsword.png",
        "primaryColor": "#a9a99d",
        "secondaryColors": [
            "#cc9b68",
            "#898b76"
        ]
    },
    {
        "name": "Shotel",
        "image": "Weapons/Shotel.png",
        "primaryColor": "#979b99",
        "secondaryColors": [
            "#6d6f68",
            "#686c63"
        ]
    },
    {
        "name": "Silverblack Sickle",
        "image": "Weapons/Silverblack Sickle.png",
        "primaryColor": "#535e63",
        "secondaryColors": [
            "#4c585a",
            "#344a4f"
        ]
    },
    {
        "name": "Silverblack Spear",
        "image": "Weapons/Silverblack Spear.png",
        "primaryColor": "#626164",
        "secondaryColors": [
            "#5f6262",
            "#575f5e"
        ]
    },
    {
        "name": "Smelter Sword",
        "image": "Weapons/Smelter Sword.png",
        "primaryColor": "#5f5e65",
        "secondaryColors": [
            "#595c63",
            "#575458"
        ]
    },
    {
        "name": "Sorcerer's Staff",
        "image": "Weapons/Sorcerer's Staff.png",
        "primaryColor": "#9c9570",
        "secondaryColors": [
            "#9b956e",
            "#9b9471"
        ]
    },
    {
        "name": "Spear",
        "image": "Weapons/Spear.png",
        "primaryColor": "#9da4a1",
        "secondaryColors": [
            "#6d686d",
            "#705b54"
        ]
    },
    {
        "name": "Spider Fang",
        "image": "Weapons/Spider Fang.png",
        "primaryColor": "#5d5e5e",
        "secondaryColors": [
            "#58595c",
            "#53565a"
        ]
    },
    {
        "name": "Spider's Silk",
        "image": "Weapons/Spider's Silk.png",
        "primaryColor": "#a3a49e",
        "secondaryColors": [
            "#9c9e9a",
            "#5b7488"
        ]
    },
    {
        "name": "Spitfire Spear",
        "image": "Weapons/Spitfire Spear.png",
        "primaryColor": "#966f5a",
        "secondaryColors": [
            "#656158",
            "#5f574e"
        ]
    },
    {
        "name": "Spotted Whip",
        "image": "Weapons/Spotted Whip.png",
        "primaryColor": "#8c6d60",
        "secondaryColors": [
            "#625650",
            "#5f4938"
        ]
    },
    {
        "name": "Staff of Amana",
        "image": "Weapons/Staff of Amana.png",
        "primaryColor": "#dce3e3",
        "secondaryColors": [
            "#a7a8a0",
            "#a6a69b"
        ]
    },
    {
        "name": "Stone Soldier Spear",
        "image": "Weapons/Stone Soldier Spear.png",
        "primaryColor": "#50504f",
        "secondaryColors": [
            "#4d4d49",
            "#484949"
        ]
    },
    {
        "name": "Stone Twinblade",
        "image": "Weapons/Stone Twinblade.png",
        "primaryColor": "#535354",
        "secondaryColors": [
            "#494b4b",
            "#454647"
        ]
    },
    {
        "name": "Sun Sword",
        "image": "Weapons/Sun Sword.png",
        "primaryColor": "#a4a1a0",
        "secondaryColors": [
            "#9ea09c",
            "#a09d9b"
        ]
    },
    {
        "name": "Sunset Staff",
        "image": "Weapons/Sunset Staff.png",
        "primaryColor": "#606161",
        "secondaryColors": [
            "#5a5a59",
            "#585a56"
        ]
    },
    {
        "name": "Syan's Halberd",
        "image": "Weapons/Syan's Halberd.png",
        "primaryColor": "#a0a6a2",
        "secondaryColors": [
            "#9fa19a",
            "#676a5e"
        ]
    },
    {
        "name": "Thief Dagger",
        "image": "Weapons/Thief Dagger.png",
        "primaryColor": "#999b8f",
        "secondaryColors": [
            "#868977",
            "#868876"
        ]
    },
    {
        "name": "Thorned Greatsword",
        "image": "Weapons/Thorned Greatsword.png",
        "primaryColor": "#999ea0",
        "secondaryColors": [
            "#949896",
            "#919694"
        ]
    },
    {
        "name": "Transgressor's Staff",
        "image": "Weapons/Transgressor's Staff.png",
        "primaryColor": "#98916c",
        "secondaryColors": [
            "#63635c",
            "#626258"
        ]
    },
    {
        "name": "Twinblade",
        "image": "Weapons/Twinblade.png",
        "primaryColor": "#dcdddd",
        "secondaryColors": [
            "#9d9fa0",
            "#9b9c9f"
        ]
    },
    {
        "name": "Uchigatana",
        "image": "Weapons/Uchigatana.png",
        "primaryColor": "#9c9f99",
        "secondaryColors": [
            "#9b9d96",
            "#949691"
        ]
    },
    {
        "name": "Varangian Sword",
        "image": "Weapons/Varangian Sword.png",
        "primaryColor": "#a4a09c",
        "secondaryColors": [
            "#6b6a67",
            "#655d57"
        ]
    },
    {
        "name": "Warped Sword",
        "image": "Weapons/Warped Sword.png",
        "primaryColor": "#a5a29c",
        "secondaryColors": [
            "#69655b",
            "#65615a"
        ]
    },
    {
        "name": "Washing Pole",
        "image": "Weapons/Washing Pole.png",
        "primaryColor": "#dcddde",
        "secondaryColors": [
            "#cdcdce",
            "#a9aba6"
        ]
    },
    {
        "name": "Watcher Greatsword",
        "image": "Weapons/Watcher Greatsword.png",
        "primaryColor": "#a6a39f",
        "secondaryColors": [
            "#a19c91",
            "#696862"
        ]
    },
    {
        "name": "Whip",
        "image": "Weapons/Whip.png",
        "primaryColor": "#8a6f5a",
        "secondaryColors": [
            "#6b5851",
            "#604738"
        ]
    },
    {
        "name": "Winged Spear",
        "image": "Weapons/Winged Spear.png",
        "primaryColor": "#a09b94",
        "secondaryColors": [
            "#9c978c",
            "#8a8479"
        ]
    },
    {
        "name": "Witchtree Bellvine",
        "image": "Weapons/Witchtree Bellvine.png",
        "primaryColor": "#e5dccd",
        "secondaryColors": [
            "#8c8379",
            "#69665b"
        ]
    },
    {
        "name": "Withctree Branch",
        "image": "Weapons/Withctree Branch.png",
        "primaryColor": "#a3a4a4",
        "secondaryColors": [
            "#9c9a97",
            "#686967"
        ]
    },
    {
        "name": "Work Hook",
        "image": "Weapons/Work Hook.png",
        "primaryColor": "#dddcdb",
        "secondaryColors": [
            "#9d9a96",
            "#878479"
        ]
    },
    {
        "name": "Yellow Quartz Longsword",
        "image": "Weapons/Yellow Quartz Longsword.png",
        "primaryColor": "#dfcd60",
        "secondaryColors": [
            "#ccb653",
            "#caa927"
        ]
    },
    {
        "name": "Zweihander",
        "image": "Weapons/Zweihander.png",
        "primaryColor": "#aca8a0",
        "secondaryColors": [
            "#a4a29c",
            "#65675f"
        ]
    }
]

def determine_type(image_path):
    image_path = image_path.lower()
    if "head" in image_path:
        return "head"
    elif "chest" in image_path:
        return "chest"
    elif "hands" in image_path:
        return "hands"
    elif "legs" in image_path:
        return "legs"
    elif "weapons" in image_path:
        return "weapons"
    elif "shields" in image_path:
        return "shields"
    return "unknown"  # Return 'unknown' if no match is found

# Add 'type' attribute to each item in the list based on the image path
for item in data:
    item['type'] = determine_type(item['image'])

# Save to a JSON file
with open('typed_items_for_web.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

print("JSON data has been written to typed_items_for_web.json")