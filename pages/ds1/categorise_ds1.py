import json

# Your JSON data as a list of dictionaries
data = [
    {
        "name": "Antiquated Dress",
        "image": "Chest/Antiquated Dress.png",
        "primaryColor": "#d3ccb1",
        "secondaryColors": [
            "#a5a295",
            "#948b73"
        ]
    },
    {
        "name": "Armor of Artorias",
        "image": "Chest/Armor of Artorias.png",
        "primaryColor": "#9a9c9d",
        "secondaryColors": [
            "#59595a",
            "#334967"
        ]
    },
    {
        "name": "Armor of the Glorious",
        "image": "Chest/Armor of the Glorious.png",
        "primaryColor": "#a38c6c",
        "secondaryColors": [
            "#30372e",
            "#6a506c"
        ]
    },
    {
        "name": "Armor of the Sun",
        "image": "Chest/Armor of the Sun.png",
        "primaryColor": "#8c8884",
        "secondaryColors": [
            "#4d5f45",
            "#efc743"
        ]
    },
    {
        "name": "Armor of Thorns",
        "image": "Chest/Armor of Thorns.png",
        "primaryColor": "#6f676a",
        "secondaryColors": [
            "#a39798",
            "#5e5656"
        ]
    },
    {
        "name": "Balder Armor",
        "image": "Chest/Balder Armor.png",
        "primaryColor": "#706e68",
        "secondaryColors": [
            "#5f5c58",
            "#8b4a2a"
        ]
    },
    {
        "name": "Black Cleric Robe",
        "image": "Chest/Black Cleric Robe.png",
        "primaryColor": "#1a1c1a",
        "secondaryColors": [
            "#575656",
            "#403e40"
        ]
    },
    {
        "name": "Black Iron Armor",
        "image": "Chest/Black Iron Armor.png",
        "primaryColor": "#22211a",
        "secondaryColors": [
            "#4d453a",
            "#48382d"
        ]
    },
    {
        "name": "Black Knight Armor",
        "image": "Chest/Black Knight Armor.png",
        "primaryColor": "#8b705c",
        "secondaryColors": [
            "#6c594a",
            "#584738"
        ]
    },
    {
        "name": "Black Leather Armor",
        "image": "Chest/Black Leather Armor.png",
        "primaryColor": "#d1a36a",
        "secondaryColors": [
            "#917457",
            "#65594f"
        ]
    },
    {
        "name": "Black Sorcerer Cloak",
        "image": "Chest/Black Sorcerer Cloak.png",
        "primaryColor": "#222122",
        "secondaryColors": [
            "#968975",
            "#867869"
        ]
    },
    {
        "name": "Brass Armor",
        "image": "Chest/Brass Armor.png",
        "primaryColor": "#d4a566",
        "secondaryColors": [
            "#6c6e6c",
            "#94734c"
        ]
    },
    {
        "name": "Brigand Armor",
        "image": "Chest/Brigand Armor.png",
        "primaryColor": "#15110e",
        "secondaryColors": [
            "#af9b75",
            "#504738"
        ]
    },
    {
        "name": "Catarina Armor",
        "image": "Chest/Catarina Armor.png",
        "primaryColor": "#fff3d3",
        "secondaryColors": [
            "#3f2f2d",
            "#ada08e"
        ]
    },
    {
        "name": "Chain Armor",
        "image": "Chest/Chain Armor.png",
        "primaryColor": "#9e9f98",
        "secondaryColors": [
            "#9a9f96",
            "#85867b"
        ]
    },
    {
        "name": "Chester's Long Coat",
        "image": "Chest/Chester-S Long Coat.png",
        "primaryColor": "#120e0a",
        "secondaryColors": [
            "#67564b",
            "#5a4739"
        ]
    },
    {
        "name": "Crimson Robe",
        "image": "Chest/Crimson Robe.png",
        "primaryColor": "#4c0f0d",
        "secondaryColors": [
            "#71574b",
            "#912a28"
        ]
    },
    {
        "name": "Crystalline Armor",
        "image": "Chest/Crystalline Armor.png",
        "primaryColor": "#aa8d5d",
        "secondaryColors": [
            "#f9f3e8",
            "#6a5f53"
        ]
    },
    {
        "name": "Dark Armor",
        "image": "Chest/Dark Armor.png",
        "primaryColor": "#5f5d5e",
        "secondaryColors": [
            "#9a969b",
            "#59575a"
        ]
    },
    {
        "name": "Dingy Robe",
        "image": "Chest/Dingy Robe.png",
        "primaryColor": "#a5a292",
        "secondaryColors": [
            "#968c74",
            "#635e52"
        ]
    },
    {
        "name": "Eastern Armor",
        "image": "Chest/Eastern Armor.png",
        "primaryColor": "#a99f93",
        "secondaryColors": [
            "#8e725e",
            "#685c50"
        ]
    },
    {
        "name": "Elite Cleric Chest",
        "image": "Chest/Elite Cleric Chest.png",
        "primaryColor": "#9c9895",
        "secondaryColors": [
            "#897360",
            "#5f5b57"
        ]
    },
    {
        "name": "Elite Knight Armor",
        "image": "Chest/Elite Knight Armor.png",
        "primaryColor": "#a39b96",
        "secondaryColors": [
            "#897464",
            "#645953"
        ]
    },
    {
        "name": "Embraced Armor of Favor",
        "image": "Chest/Embraced Armor of Favor.png",
        "primaryColor": "#d3a65e",
        "secondaryColors": [
            "#95662a",
            "#6c4b21"
        ]
    },
    {
        "name": "Giant Armor",
        "image": "Chest/Giant Armor.png",
        "primaryColor": "#baa982",
        "secondaryColors": [
            "#e4e7e9",
            "#685f53"
        ]
    },
    {
        "name": "Goldhemmed Black Cloak",
        "image": "Chest/Goldhemmed Black Cloak.png",
        "primaryColor": "#888f91",
        "secondaryColors": [
            "#53595f",
            "#3b4348"
        ]
    },
    {
        "name": "Golem Armor",
        "image": "Chest/Golem Armor.png",
        "primaryColor": "#736e6b",
        "secondaryColors": [
            "#9e9e98",
            "#5b5a57"
        ]
    },
    {
        "name": "Gough's Chest",
        "image": "Chest/Gough-S Chest.png",
        "primaryColor": "#f2ecdc",
        "secondaryColors": [
            "#a3906f",
            "#675c50"
        ]
    },
    {
        "name": "Guardian Armor",
        "image": "Chest/Guardian Armor.png",
        "primaryColor": "#a48f6c",
        "secondaryColors": [
            "#8b7357",
            "#6e5f4c"
        ]
    },
    {
        "name": "Hard Leather Armor",
        "image": "Chest/Hard Leather Armor.png",
        "primaryColor": "#966e52",
        "secondaryColors": [
            "#8d5838",
            "#625a55"
        ]
    },
    {
        "name": "Havels Armor",
        "image": "Chest/Havels Armor.png",
        "primaryColor": "#736d6a",
        "secondaryColors": [
            "#a09b98",
            "#5f5b58"
        ]
    },
    {
        "name": "Hollow Soldier Armor",
        "image": "Chest/Hollow Soldier Armor.png",
        "primaryColor": "#95908f",
        "secondaryColors": [
            "#a59b94",
            "#8a7469"
        ]
    },
    {
        "name": "Hollow Thiefs Leather Armor",
        "image": "Chest/Hollow Thiefs Leather Armor.png",
        "primaryColor": "#aba38f",
        "secondaryColors": [
            "#8d715d",
            "#695f52"
        ]
    },
    {
        "name": "Hollow Warrior Armor",
        "image": "Chest/Hollow Warrior Armor.png",
        "primaryColor": "#a39891",
        "secondaryColors": [
            "#8b7161",
            "#685c54"
        ]
    },
    {
        "name": "Holy Robe",
        "image": "Chest/Holy Robe.png",
        "primaryColor": "#d69e65",
        "secondaryColors": [
            "#ac8c63",
            "#96714b"
        ]
    },
    {
        "name": "Knight Armor",
        "image": "Chest/Knight Armor.png",
        "primaryColor": "#a39c98",
        "secondaryColors": [
            "#8a7464",
            "#615954"
        ]
    },
    {
        "name": "Leather Armor",
        "image": "Chest/Leather Armor.png",
        "primaryColor": "#aa8d72",
        "secondaryColors": [
            "#8d735c",
            "#6d5b4c"
        ]
    },
    {
        "name": "Lord's Blade Robe",
        "image": "Chest/Lord-S Blade Robe.png",
        "primaryColor": "#a29f96",
        "secondaryColors": [
            "#5f5f59",
            "#2d4d5c"
        ]
    },
    {
        "name": "Maiden Robe",
        "image": "Chest/Maiden Robe.png",
        "primaryColor": "#faf6dd",
        "secondaryColors": [
            "#e9d2ab",
            "#a28c71"
        ]
    },
    {
        "name": "Moonlight Robe",
        "image": "Chest/Moonlight Robe.png",
        "primaryColor": "#dfe1e7",
        "secondaryColors": [
            "#b8b9c5",
            "#8e6e21"
        ]
    },
    {
        "name": "Ornstein's Armor",
        "image": "Chest/Ornstein-S Armor Icon.png",
        "primaryColor": "#dcd3a8",
        "secondaryColors": [
            "#b3aa89",
            "#999070"
        ]
    },
    {
        "name": "Painting Guardian Robe",
        "image": "Chest/Painting Guardian Robe.png",
        "primaryColor": "#c7b7a6",
        "secondaryColors": [
            "#ab9e90",
            "#918679"
        ]
    },
    {
        "name": "Paladin Armor",
        "image": "Chest/Paladin Armor.png",
        "primaryColor": "#e2d5a6",
        "secondaryColors": [
            "#a29362",
            "#6c614b"
        ]
    },
    {
        "name": "Robe of the Channelers",
        "image": "Chest/Robe of the Channelers.png",
        "primaryColor": "#a69063",
        "secondaryColors": [
            "#8b7550",
            "#30303c"
        ]
    },
    {
        "name": "Robe of the Great Lord",
        "image": "Chest/Robe of the Great Lord Icon.png",
        "primaryColor": "#897260",
        "secondaryColors": [
            "#63594f",
            "#55463a"
        ]
    },
    {
        "name": "Sage Robe",
        "image": "Chest/Sage Robe.png",
        "primaryColor": "#916636",
        "secondaryColors": [
            "#675d53",
            "#674b2e"
        ]
    },
    {
        "name": "Shadow Garb",
        "image": "Chest/Shadow Garb.png",
        "primaryColor": "#a59b93",
        "secondaryColors": [
            "#605753",
            "#4e443a"
        ]
    },
    {
        "name": "Silver Knight Armor",
        "image": "Chest/Silver Knight Armor.png",
        "primaryColor": "#f0e8db",
        "secondaryColors": [
            "#aa9e90",
            "#645c53"
        ]
    },
    {
        "name": "Smoughs Armor",
        "image": "Chest/Smoughs Armor.png",
        "primaryColor": "#9d8e71",
        "secondaryColors": [
            "#87765e",
            "#6d604c"
        ]
    },
    {
        "name": "Sorcerer Cloak",
        "image": "Chest/Sorcerer Cloak.png",
        "primaryColor": "#8b724b",
        "secondaryColors": [
            "#6c5f4a",
            "#624f30"
        ]
    },
    {
        "name": "Steel Armor",
        "image": "Chest/Steel Armor.png",
        "primaryColor": "#dfe2d7",
        "secondaryColors": [
            "#a0a296",
            "#5f5e56"
        ]
    },
    {
        "name": "Stone Armor",
        "image": "Chest/Stone Armor.png",
        "primaryColor": "#d9dc9f",
        "secondaryColors": [
            "#afad8e",
            "#979968"
        ]
    },
    {
        "name": "Tattered Cloth Robe",
        "image": "Chest/Tattered Cloth Robe.png",
        "primaryColor": "#a88d65",
        "secondaryColors": [
            "#8d714f",
            "#6d5e4a"
        ]
    },
    {
        "name": "Wanderer Coat",
        "image": "Chest/Wanderer Coat.png",
        "primaryColor": "#968c71",
        "secondaryColors": [
            "#675d4f",
            "#504639"
        ]
    },
    {
        "name": "Witch Cloak",
        "image": "Chest/Witch Cloak.png",
        "primaryColor": "#483b43",
        "secondaryColors": [
            "#534937",
            "#998a66"
        ]
    },
    {
        "name": "Xanthous Overcoat",
        "image": "Chest/Xanthous Overcoat.png",
        "primaryColor": "#d6a613",
        "secondaryColors": [
            "#936c11",
            "#664d17"
        ]
    },
    {
        "name": "Antiquated Gloves",
        "image": "Hands/Antiquated Gloves.png",
        "primaryColor": "#dededd",
        "secondaryColors": [
            "#9c9c9c",
            "#5f605f"
        ]
    },
    {
        "name": "Balder Gauntlets",
        "image": "Hands/Balder Gauntlets.png",
        "primaryColor": "#dbd9d6",
        "secondaryColors": [
            "#a19c98",
            "#87786d"
        ]
    },
    {
        "name": "Black Iron Gauntlets",
        "image": "Hands/Black Iron Gauntlets.png",
        "primaryColor": "#323229",
        "secondaryColors": [
            "#9b9e95",
            "#5c5d54"
        ]
    },
    {
        "name": "Black Knight Gauntlets",
        "image": "Hands/Black Knight Gauntlets.png",
        "primaryColor": "#a38e72",
        "secondaryColors": [
            "#6e5e4c",
            "#554737"
        ]
    },
    {
        "name": "Black Leather Gloves",
        "image": "Hands/Black Leather Gloves.png",
        "primaryColor": "#9b9391",
        "secondaryColors": [
            "#837977",
            "#5c5756"
        ]
    },
    {
        "name": "Black Manchette",
        "image": "Hands/Black Manchette.png",
        "primaryColor": "#1c1b1c",
        "secondaryColors": [
            "#5f5e5c",
            "#565454"
        ]
    },
    {
        "name": "Black Sorcerer Gauntlets",
        "image": "Hands/Black Sorcerer Gauntlets.png",
        "primaryColor": "#282524",
        "secondaryColors": [
            "#625a4f",
            "#4f463a"
        ]
    },
    {
        "name": "Bracelet Of The Great Lord",
        "image": "Hands/Bracelet Of The Great Lord.png",
        "primaryColor": "#af8a70",
        "secondaryColors": [
            "#926e58",
            "#715848"
        ]
    },
    {
        "name": "Brass Gauntlets",
        "image": "Hands/Brass Gauntlets.png",
        "primaryColor": "#f2e19b",
        "secondaryColors": [
            "#ab8e5d",
            "#937248"
        ]
    },
    {
        "name": "Brigand Gauntlets",
        "image": "Hands/Brigand Gauntlets.png",
        "primaryColor": "#ecdaa1",
        "secondaryColors": [
            "#6a5d49",
            "#574b35"
        ]
    },
    {
        "name": "Catarina Gauntlets",
        "image": "Hands/Catarina Gauntlets.png",
        "primaryColor": "#ddd1ae",
        "secondaryColors": [
            "#988c71",
            "#665e4e"
        ]
    },
    {
        "name": "Chester's Gloves",
        "image": "Hands/Chester's Gloves.png",
        "primaryColor": "#996747",
        "secondaryColors": [
            "#88593c",
            "#6d4833"
        ]
    },
    {
        "name": "Crimson Gloves",
        "image": "Hands/Crimson Gloves.png",
        "primaryColor": "#511915",
        "secondaryColors": [
            "#942826",
            "#581918"
        ]
    },
    {
        "name": "Crystalline Gauntlets",
        "image": "Hands/Crystalline Gauntlets.png",
        "primaryColor": "#a86f14",
        "secondaryColors": [
            "#d4d3d0",
            "#624826"
        ]
    },
    {
        "name": "Dark Gauntlets",
        "image": "Hands/Dark Gauntlets.png",
        "primaryColor": "#363536",
        "secondaryColors": [
            "#99979b",
            "#5d5c5e"
        ]
    },
    {
        "name": "Dingy Gloves",
        "image": "Hands/Dingy Gloves.png",
        "primaryColor": "#8d7260",
        "secondaryColors": [
            "#695950",
            "#5f4936"
        ]
    },
    {
        "name": "Eastern Gauntlets",
        "image": "Hands/Eastern Gauntlets.png",
        "primaryColor": "#a2a091",
        "secondaryColors": [
            "#8b8775",
            "#615e51"
        ]
    },
    {
        "name": "Elite Knight Gauntlets",
        "image": "Hands/Elite Knight Gauntlets.png",
        "primaryColor": "#a88974",
        "secondaryColors": [
            "#8f7462",
            "#6c584a"
        ]
    },
    {
        "name": "Gauntlets Of Artorias",
        "image": "Hands/Gauntlets Of Artorias.png",
        "primaryColor": "#9b9891",
        "secondaryColors": [
            "#5c5852",
            "#47423c"
        ]
    },
    {
        "name": "Gauntlets Of Favor",
        "image": "Hands/Gauntlets Of Favor.png",
        "primaryColor": "#d7ac60",
        "secondaryColors": [
            "#966427",
            "#6c4b21"
        ]
    },
    {
        "name": "Gauntlets Of The Channelers",
        "image": "Hands/Gauntlets Of The Channelers.png",
        "primaryColor": "#eedba4",
        "secondaryColors": [
            "#aa9067",
            "#6a5f4d"
        ]
    },
    {
        "name": "Gauntlets Of The Vanquisher",
        "image": "Hands/Gauntlets Of The Vanquisher.png",
        "primaryColor": "#96665b",
        "secondaryColors": [
            "#705049",
            "#69463a"
        ]
    },
    {
        "name": "Gauntlets Of Thorns",
        "image": "Hands/Gauntlets Of Thorns.png",
        "primaryColor": "#a4999a",
        "secondaryColors": [
            "#605758",
            "#443a37"
        ]
    },
    {
        "name": "Giant Gauntlets",
        "image": "Hands/Giant Gauntlets.png",
        "primaryColor": "#b3a488",
        "secondaryColors": [
            "#9e8c71",
            "#877760"
        ]
    },
    {
        "name": "Goldhemmed Black Gloves",
        "image": "Hands/Goldhemmed Black Gloves.png",
        "primaryColor": "#52555f",
        "secondaryColors": [
            "#4e5159",
            "#3d4148"
        ]
    },
    {
        "name": "Golem Gauntlets",
        "image": "Hands/Golem Gauntlets.png",
        "primaryColor": "#9e9b91",
        "secondaryColors": [
            "#585853",
            "#47433c"
        ]
    },
    {
        "name": "Gough's Gloves",
        "image": "Hands/Gough's Gloves.png",
        "primaryColor": "#ede4d8",
        "secondaryColors": [
            "#ab9c92",
            "#645951"
        ]
    },
    {
        "name": "Guardian Gauntlets",
        "image": "Hands/Guardian Gauntlets.png",
        "primaryColor": "#906a56",
        "secondaryColors": [
            "#6c594a",
            "#5b4637"
        ]
    },
    {
        "name": "Hard Leather Gauntlets",
        "image": "Hands/Hard Leather Gauntlets.png",
        "primaryColor": "#ad8b63",
        "secondaryColors": [
            "#966e4d",
            "#624a34"
        ]
    },
    {
        "name": "Havels Gauntlets",
        "image": "Hands/Havels Gauntlets.png",
        "primaryColor": "#e3e0dd",
        "secondaryColors": [
            "#9d9b98",
            "#5c5a58"
        ]
    },
    {
        "name": "Knight Gauntlets",
        "image": "Hands/Knight Gauntlets.png",
        "primaryColor": "#a88a75",
        "secondaryColors": [
            "#8f7466",
            "#6c584e"
        ]
    },
    {
        "name": "Leather Gauntlets",
        "image": "Hands/Leather Gauntlets.png",
        "primaryColor": "#877364",
        "secondaryColors": [
            "#6b5a4d",
            "#55463a"
        ]
    },
    {
        "name": "Leather Gloves",
        "image": "Hands/Leather Gloves.png",
        "primaryColor": "#b18861",
        "secondaryColors": [
            "#94634c",
            "#674835"
        ]
    },
    {
        "name": "Lord's Blade Gloves",
        "image": "Hands/Lord's Blade Gloves.png",
        "primaryColor": "#a7a091",
        "secondaryColors": [
            "#8e8879",
            "#625b53"
        ]
    },
    {
        "name": "Maiden Gloves",
        "image": "Hands/Maiden Gloves.png",
        "primaryColor": "#dfceb0",
        "secondaryColors": [
            "#c8b69a",
            "#b4a68e"
        ]
    },
    {
        "name": "Moonlight Gloves",
        "image": "Hands/Moonlight Gloves.png",
        "primaryColor": "#9b9b9b",
        "secondaryColors": [
            "#6c6c6c",
            "#5e5f5e"
        ]
    },
    {
        "name": "Ornsteins Gauntlets",
        "image": "Hands/Ornsteins Gauntlets.png",
        "primaryColor": "#dcd6aa",
        "secondaryColors": [
            "#b0ac8a",
            "#969171"
        ]
    },
    {
        "name": "Painting Guardian Gloves",
        "image": "Hands/Painting Guardian Gloves.png",
        "primaryColor": "#ad9f8f",
        "secondaryColors": [
            "#958677",
            "#675c51"
        ]
    },
    {
        "name": "Paladin Gauntlets",
        "image": "Hands/Paladin Gauntlets.png",
        "primaryColor": "#eadb5b",
        "secondaryColors": [
            "#6f6348",
            "#5b4e2d"
        ]
    },
    {
        "name": "Shadow Gauntlets",
        "image": "Hands/Shadow Gauntlets.png",
        "primaryColor": "#e9e2dc",
        "secondaryColors": [
            "#9f9b98",
            "#5d5957"
        ]
    },
    {
        "name": "Silver Knight Gauntlets",
        "image": "Hands/Silver Knight Gauntlets.png",
        "primaryColor": "#a69d8f",
        "secondaryColors": [
            "#8f8679",
            "#615b52"
        ]
    },
    {
        "name": "Smoughs Gauntlets",
        "image": "Hands/Smoughs Gauntlets.png",
        "primaryColor": "#e3d3a7",
        "secondaryColors": [
            "#a3906d",
            "#8a7559"
        ]
    },
    {
        "name": "Solaire Brace",
        "image": "Hands/Solaire Brace.png",
        "primaryColor": "#e1dddc",
        "secondaryColors": [
            "#c3bbb7",
            "#a09c9a"
        ]
    },
    {
        "name": "Sorcerer Gauntlets",
        "image": "Hands/Sorcerer Gauntlets.png",
        "primaryColor": "#ab8e63",
        "secondaryColors": [
            "#93744c",
            "#624d31"
        ]
    },
    {
        "name": "Steel Gauntlets",
        "image": "Hands/Steel Gauntlets.png",
        "primaryColor": "#dddfd3",
        "secondaryColors": [
            "#9ea194",
            "#5b5d56"
        ]
    },
    {
        "name": "Stone Gauntlets",
        "image": "Hands/Stone Gauntlets.png",
        "primaryColor": "#d2d3a4",
        "secondaryColors": [
            "#acab8f",
            "#939668"
        ]
    },
    {
        "name": "Tattered Cloth Manchette",
        "image": "Hands/Tattered Cloth Manchette.png",
        "primaryColor": "#897766",
        "secondaryColors": [
            "#63594e",
            "#4f443b"
        ]
    },
    {
        "name": "Traveling Gloves",
        "image": "Hands/Traveling Gloves.png",
        "primaryColor": "#8a7563",
        "secondaryColors": [
            "#6b5c4e",
            "#534538"
        ]
    },
    {
        "name": "Wanderer Manchette",
        "image": "Hands/Wanderer Manchette.png",
        "primaryColor": "#a69b90",
        "secondaryColors": [
            "#8d7263",
            "#675b53"
        ]
    },
    {
        "name": "Witch Gloves",
        "image": "Hands/Witch Gloves.png",
        "primaryColor": "#62605e",
        "secondaryColors": [
            "#585562",
            "#373549"
        ]
    },
    {
        "name": "Xanthous Gloves",
        "image": "Hands/Xanthous Gloves.png",
        "primaryColor": "#f8e927",
        "secondaryColors": [
            "#ad8b28",
            "#916e1d"
        ]
    },
    {
        "name": "Balder Helm",
        "image": "Head/Balder Helm.png",
        "primaryColor": "#9a9693",
        "secondaryColors": [
            "#817c78",
            "#5e5c5a"
        ]
    },
    {
        "name": "Big Hat",
        "image": "Head/Big Hat.png",
        "primaryColor": "#1b1212",
        "secondaryColors": [
            "#5f5853",
            "#4b4236"
        ]
    },
    {
        "name": "Black Iron Helm",
        "image": "Head/Black Iron Helm.png",
        "primaryColor": "#363432",
        "secondaryColors": [
            "#585951",
            "#43433c"
        ]
    },
    {
        "name": "Black Knight Helm",
        "image": "Head/Black Knight Helm.png",
        "primaryColor": "#291f1b",
        "secondaryColors": [
            "#6c584b",
            "#564539"
        ]
    },
    {
        "name": "Bloated Head",
        "image": "Head/Bloated Head.png",
        "primaryColor": "#9a6850",
        "secondaryColors": [
            "#935a36",
            "#674a30"
        ]
    },
    {
        "name": "Bloated Sorcerer Head",
        "image": "Head/Bloated Sorcerer Head.png",
        "primaryColor": "#956d5c",
        "secondaryColors": [
            "#764c6a",
            "#5f4638"
        ]
    },
    {
        "name": "Brass Helm",
        "image": "Head/Brass Helm.png",
        "primaryColor": "#f4e09a",
        "secondaryColors": [
            "#ab8d62",
            "#8e724f"
        ]
    },
    {
        "name": "Brigand Hood",
        "image": "Head/Brigand Hood.png",
        "primaryColor": "#a69365",
        "secondaryColors": [
            "#655b4b",
            "#514837"
        ]
    },
    {
        "name": "Catarina Helm",
        "image": "Head/Catarina Helm.png",
        "primaryColor": "#b0a992",
        "secondaryColors": [
            "#d2caae",
            "#aea78e"
        ]
    },
    {
        "name": "Chain Helm",
        "image": "Head/Chain Helm.png",
        "primaryColor": "#989c95",
        "secondaryColors": [
            "#83847b",
            "#7c817b"
        ]
    },
    {
        "name": "Cleric Helm",
        "image": "Head/Cleric Helm.png",
        "primaryColor": "#666867",
        "secondaryColors": [
            "#9a9999",
            "#827c79"
        ]
    },
    {
        "name": "Crown Of Dusk",
        "image": "Head/Crown Of Dusk.png",
        "primaryColor": "#966e52",
        "secondaryColors": [
            "#68594d",
            "#644a36"
        ]
    },
    {
        "name": "Crown Of The Dark Sun",
        "image": "Head/Crown Of The Dark Sun.png",
        "primaryColor": "#8e7124",
        "secondaryColors": [
            "#545554",
            "#66521b"
        ]
    },
    {
        "name": "Crown Of The Great Lord",
        "image": "Head/Crown Of The Great Lord.png",
        "primaryColor": "#88776c",
        "secondaryColors": [
            "#655950",
            "#4f433b"
        ]
    },
    {
        "name": "Crystalline Helm",
        "image": "Head/Crystalline Helm.png",
        "primaryColor": "#946827",
        "secondaryColors": [
            "#ede1d5",
            "#6a4c23"
        ]
    },
    {
        "name": "Dark Mask",
        "image": "Head/Dark Mask.png",
        "primaryColor": "#9d9996",
        "secondaryColors": [
            "#56575a",
            "#585655"
        ]
    },
    {
        "name": "Dingy Hood",
        "image": "Head/Dingy Hood.png",
        "primaryColor": "#99978d",
        "secondaryColors": [
            "#86847b",
            "#63615b"
        ]
    },
    {
        "name": "Eastern Helm",
        "image": "Head/Eastern Helm.png",
        "primaryColor": "#a28c6e",
        "secondaryColors": [
            "#8a755a",
            "#6d5e4b"
        ]
    },
    {
        "name": "Elite Knight Helm",
        "image": "Head/Elite Knight Helm.png",
        "primaryColor": "#bbb4b2",
        "secondaryColors": [
            "#c2bbb9",
            "#a19d9b"
        ]
    },
    {
        "name": "Fang Boar Helm",
        "image": "Head/Fang Boar Helm.png",
        "primaryColor": "#a7a493",
        "secondaryColors": [
            "#605e54",
            "#46443b"
        ]
    },
    {
        "name": "Gargoyle Helm",
        "image": "Head/Gargoyle Helm.png",
        "primaryColor": "#9ca393",
        "secondaryColors": [
            "#8e8a75",
            "#5d6256"
        ]
    },
    {
        "name": "Giant Helm",
        "image": "Head/Giant Helm Icon.png",
        "primaryColor": "#9a8d70",
        "secondaryColors": [
            "#85785e",
            "#6a604c"
        ]
    },
    {
        "name": "Goldhemmed Black Hood",
        "image": "Head/Goldhemmed Black Hood.png",
        "primaryColor": "#545b5e",
        "secondaryColors": [
            "#4b4738",
            "#3c4345"
        ]
    },
    {
        "name": "Golem Helm",
        "image": "Head/Golem Helm Icon.png",
        "primaryColor": "#353d3e",
        "secondaryColors": [
            "#898578",
            "#5a5a59"
        ]
    },
    {
        "name": "Gough-S Helm",
        "image": "Head/Gough-S Helm.png",
        "primaryColor": "#a09b98",
        "secondaryColors": [
            "#86766f",
            "#625a58"
        ]
    },
    {
        "name": "Guardian Helm",
        "image": "Head/Guardian Helm.png",
        "primaryColor": "#9e8f6e",
        "secondaryColors": [
            "#87775c",
            "#6b614b"
        ]
    },
    {
        "name": "Havels Helm",
        "image": "Head/Havels Helm.png",
        "primaryColor": "#8c8685",
        "secondaryColors": [
            "#a19c97",
            "#5e5b58"
        ]
    },
    {
        "name": "Helm Black Sorcerer Hat",
        "image": "Head/Helm Black Sorcerer Hat.png",
        "primaryColor": "#a48d57",
        "secondaryColors": [
            "#897648",
            "#5e5032"
        ]
    },
    {
        "name": "Helm Of Artorias",
        "image": "Head/Helm Of Artorias.png",
        "primaryColor": "#4f4d48",
        "secondaryColors": [
            "#5b5a59",
            "#22354f"
        ]
    },
    {
        "name": "Helm Of Favor",
        "image": "Head/Helm Of Favor.png",
        "primaryColor": "#e39829",
        "secondaryColors": [
            "#996018",
            "#714713"
        ]
    },
    {
        "name": "Helm Of The Wise",
        "image": "Head/Helm Of The Wise.png",
        "primaryColor": "#f4e397",
        "secondaryColors": [
            "#d4aa60",
            "#614d2c"
        ]
    },
    {
        "name": "Helm Of Thorns",
        "image": "Head/Helm Of Thorns.png",
        "primaryColor": "#d8d8d7",
        "secondaryColors": [
            "#9d9897",
            "#5f5a59"
        ]
    },
    {
        "name": "Helm Sorcerer Hat",
        "image": "Head/Helm Sorcerer Hat.png",
        "primaryColor": "#f0e59d",
        "secondaryColors": [
            "#aa9363",
            "#8b7451"
        ]
    },
    {
        "name": "Hollow Soldier Helm",
        "image": "Head/Hollow Soldier Helm.png",
        "primaryColor": "#e8dfd9",
        "secondaryColors": [
            "#a29893",
            "#877771"
        ]
    },
    {
        "name": "Hollow Thiefs Hood",
        "image": "Head/Hollow Thiefs Hood.png",
        "primaryColor": "#8d6d46",
        "secondaryColors": [
            "#6b5b4a",
            "#654c31"
        ]
    },
    {
        "name": "Hollow Warrior Helm",
        "image": "Head/Hollow Warrior Helm.png",
        "primaryColor": "#99979a",
        "secondaryColors": [
            "#565458",
            "#4a433a"
        ]
    },
    {
        "name": "Knight Helm",
        "image": "Head/Knight Helm.png",
        "primaryColor": "#9f9c9a",
        "secondaryColors": [
            "#83817d",
            "#5d5b5a"
        ]
    },
    {
        "name": "Maiden Hood",
        "image": "Head/Maiden Hood.png",
        "primaryColor": "#e8d2ab",
        "secondaryColors": [
            "#ceb595",
            "#a18d72"
        ]
    },
    {
        "name": "Mask Of The Child",
        "image": "Head/Mask Of The Child.png",
        "primaryColor": "#9e9c99",
        "secondaryColors": [
            "#5f5d59",
            "#46423c"
        ]
    },
    {
        "name": "Mask Of The Father",
        "image": "Head/Mask Of The Father.png",
        "primaryColor": "#8d6c52",
        "secondaryColors": [
            "#755c45",
            "#68492e"
        ]
    },
    {
        "name": "Mask Of The Mother",
        "image": "Head/Mask Of The Mother.png",
        "primaryColor": "#9f9d9d",
        "secondaryColors": [
            "#605a5a",
            "#483834"
        ]
    },
    {
        "name": "Mask Of The Sealer",
        "image": "Head/Mask Of The Sealer.png",
        "primaryColor": "#675a51",
        "secondaryColors": [
            "#544539",
            "#911715"
        ]
    },
    {
        "name": "Mask Of Velka",
        "image": "Head/Mask Of Velka.png",
        "primaryColor": "#a68d6e",
        "secondaryColors": [
            "#2f1b0f",
            "#715e49"
        ]
    },
    {
        "name": "Ornsteins Helm",
        "image": "Head/Ornsteins Helm.png",
        "primaryColor": "#e0d8a9",
        "secondaryColors": [
            "#b3ac88",
            "#9b9370"
        ]
    },
    {
        "name": "Painting Guardian Hood",
        "image": "Head/Painting Guardian Hood.png",
        "primaryColor": "#f8f0de",
        "secondaryColors": [
            "#decbb5",
            "#aa9d90"
        ]
    },
    {
        "name": "Paladin Helm",
        "image": "Head/Paladin Helm.png",
        "primaryColor": "#e5d963",
        "secondaryColors": [
            "#a58f2c",
            "#8d7426"
        ]
    },
    {
        "name": "Phariss Hat",
        "image": "Head/Phariss Hat.png",
        "primaryColor": "#8c6d5f",
        "secondaryColors": [
            "#6b574c",
            "#604438"
        ]
    },
    {
        "name": "Porcelain Mask",
        "image": "Head/Porcelain Mask.png",
        "primaryColor": "#f2f2db",
        "secondaryColors": [
            "#a5a491",
            "#5c6057"
        ]
    },
    {
        "name": "Priests Hat",
        "image": "Head/Priests Hat.png",
        "primaryColor": "#9b8f73",
        "secondaryColors": [
            "#695f4c",
            "#544634"
        ]
    },
    {
        "name": "Royal Helm",
        "image": "Head/Royal Helm.png",
        "primaryColor": "#d3ae58",
        "secondaryColors": [
            "#917130",
            "#665222"
        ]
    },
    {
        "name": "Sack",
        "image": "Head/Sack.png",
        "primaryColor": "#b08a5e",
        "secondaryColors": [
            "#926e4b",
            "#684d34"
        ]
    },
    {
        "name": "Shadow Mask",
        "image": "Head/Shadow Mask.png",
        "primaryColor": "#a09c96",
        "secondaryColors": [
            "#988c6e",
            "#565451"
        ]
    },
    {
        "name": "Silver Knight Helm",
        "image": "Head/Silver Knight Helm.png",
        "primaryColor": "#a79d8f",
        "secondaryColors": [
            "#615951",
            "#4a433c"
        ]
    },
    {
        "name": "Sixeyed Helm Of The Channelers",
        "image": "Head/Sixeyed Helm Of The Channelers.png",
        "primaryColor": "#979794",
        "secondaryColors": [
            "#a58e64",
            "#8a7655"
        ]
    },
    {
        "name": "Smoughs Helm",
        "image": "Head/Smoughs Helm.png",
        "primaryColor": "#e2cfa9",
        "secondaryColors": [
            "#a58e70",
            "#8c735a"
        ]
    },
    {
        "name": "Snickering Top Hat",
        "image": "Head/Snickering Top Hat.png",
        "primaryColor": "#a38b72",
        "secondaryColors": [
            "#69594a",
            "#584637"
        ]
    },
    {
        "name": "Solaire Helm",
        "image": "Head/Solaire Helm.png",
        "primaryColor": "#53504e",
        "secondaryColors": [
            "#5a5656",
            "#413d3b"
        ]
    },
    {
        "name": "Standard Helm",
        "image": "Head/Standard Helm.png",
        "primaryColor": "#a19797",
        "secondaryColors": [
            "#c6b7b0",
            "#a69b94"
        ]
    },
    {
        "name": "Steel Helm",
        "image": "Head/Steel Helm.png",
        "primaryColor": "#9c9f99",
        "secondaryColors": [
            "#565951",
            "#42443c"
        ]
    },
    {
        "name": "Stone Helm",
        "image": "Head/Stone Helm.png",
        "primaryColor": "#cfccad",
        "secondaryColors": [
            "#aab562",
            "#919368"
        ]
    },
    {
        "name": "Sunlight Maggot",
        "image": "Head/Sunlight Maggot.png",
        "primaryColor": "#9c8d73",
        "secondaryColors": [
            "#695b4e",
            "#574838"
        ]
    },
    {
        "name": "Symbol Of Avarice",
        "image": "Head/Symbol Of Avarice.png",
        "primaryColor": "#936f5e",
        "secondaryColors": [
            "#695a4c",
            "#594737"
        ]
    },
    {
        "name": "Tattered Cloth Hood",
        "image": "Head/Tattered Cloth Hood.png",
        "primaryColor": "#a58d70",
        "secondaryColors": [
            "#8a745a",
            "#6d5e4b"
        ]
    },
    {
        "name": "Thief Mask",
        "image": "Head/Thief Mask.png",
        "primaryColor": "#a19490",
        "secondaryColors": [
            "#867872",
            "#615854"
        ]
    },
    {
        "name": "Wanderer Hood",
        "image": "Head/Wanderer Hood.png",
        "primaryColor": "#a69e8f",
        "secondaryColors": [
            "#908777",
            "#635e52"
        ]
    },
    {
        "name": "Witch Hat",
        "image": "Head/Witch Hat.png",
        "primaryColor": "#403237",
        "secondaryColors": [
            "#585a56",
            "#af9c5f"
        ]
    },
    {
        "name": "Xanthous Crown",
        "image": "Head/Xanthous Crown.png",
        "primaryColor": "#f6d919",
        "secondaryColors": [
            "#d7a411",
            "#966e0c"
        ]
    },
    {
        "name": "Anklet Of_The_Great_Lord",
        "image": "Legs/Anklet Of_The_Great_Lord.png",
        "primaryColor": "#8d705e",
        "secondaryColors": [
            "#6b564a",
            "#584539"
        ]
    },
    {
        "name": "Antiquated Skirt",
        "image": "Legs/Antiquated Skirt.png",
        "primaryColor": "#e9e5cf",
        "secondaryColors": [
            "#d6ccab",
            "#ada78f"
        ]
    },
    {
        "name": "Balder Leggings",
        "image": "Legs/Balder Leggings.png",
        "primaryColor": "#9e9d98",
        "secondaryColors": [
            "#635b57",
            "#50433a"
        ]
    },
    {
        "name": "Black Iron_Leggings",
        "image": "Legs/Black Iron_Leggings.png",
        "primaryColor": "#282729",
        "secondaryColors": [
            "#595b53",
            "#42433b"
        ]
    },
    {
        "name": "Black Knight_Leggings",
        "image": "Legs/Black Knight_Leggings.png",
        "primaryColor": "#17110e",
        "secondaryColors": [
            "#b39c86",
            "#5b4738"
        ]
    },
    {
        "name": "Black Leather_Boots",
        "image": "Legs/Black Leather_Boots.png",
        "primaryColor": "#5c544f",
        "secondaryColors": [
            "#5b524c",
            "#4c433b"
        ]
    },
    {
        "name": "Black Tights",
        "image": "Legs/Black Tights.png",
        "primaryColor": "#272627",
        "secondaryColors": [
            "#999897",
            "#606060"
        ]
    },
    {
        "name": "Bloodstained Skirt",
        "image": "Legs/Bloodstained Skirt.png",
        "primaryColor": "#24201e",
        "secondaryColors": [
            "#a28f6c",
            "#ece5c5"
        ]
    },
    {
        "name": "Boots Of_The_Explorer",
        "image": "Legs/Boots Of_The_Explorer.png",
        "primaryColor": "#9a6453",
        "secondaryColors": [
            "#5e624f",
            "#564936"
        ]
    },
    {
        "name": "Brass Leggings",
        "image": "Legs/Brass Leggings.png",
        "primaryColor": "#9a7745",
        "secondaryColors": [
            "#8a6638",
            "#664c2c"
        ]
    },
    {
        "name": "Brigand Trousers",
        "image": "Legs/Brigand Trousers.png",
        "primaryColor": "#9e8c72",
        "secondaryColors": [
            "#6a5e4e",
            "#4f4637"
        ]
    },
    {
        "name": "Catarina Leggings",
        "image": "Legs/Catarina Leggings_Icon.png",
        "primaryColor": "#978a6f",
        "secondaryColors": [
            "#68604e",
            "#4e4638"
        ]
    },
    {
        "name": "Chain Leggings",
        "image": "Legs/Chain Leggings.png",
        "primaryColor": "#dee2dd",
        "secondaryColors": [
            "#9c9d96",
            "#5e5f59"
        ]
    },
    {
        "name": "Chester's Trousers",
        "image": "Legs/Chester's Trousers.png",
        "primaryColor": "#8a735b",
        "secondaryColors": [
            "#64594f",
            "#584737"
        ]
    },
    {
        "name": "Crimson Waistcloth",
        "image": "Legs/Crimson Waistcloth.png",
        "primaryColor": "#d92926",
        "secondaryColors": [
            "#9b1d1b",
            "#5c1110"
        ]
    },
    {
        "name": "Crystalline Leggings",
        "image": "Legs/Crystalline Leggings.png",
        "primaryColor": "#ad8f63",
        "secondaryColors": [
            "#9b6550",
            "#70584a"
        ]
    },
    {
        "name": "Dark Leggings",
        "image": "Legs/Dark Leggings.png",
        "primaryColor": "#98979f",
        "secondaryColors": [
            "#57555a",
            "#56545a"
        ]
    },
    {
        "name": "Eastern Leggings",
        "image": "Legs/Eastern Leggings.png",
        "primaryColor": "#a39d90",
        "secondaryColors": [
            "#8f8878",
            "#635e57"
        ]
    },
    {
        "name": "Elite Knight Leggings",
        "image": "Legs/Elite Knight_Leggings.png",
        "primaryColor": "#888382",
        "secondaryColors": [
            "#a19b96",
            "#605a56"
        ]
    },
    {
        "name": "Giant Leggings",
        "image": "Legs/Giant Leggings.png",
        "primaryColor": "#9d8f6c",
        "secondaryColors": [
            "#645d4e",
            "#554b37"
        ]
    },
    {
        "name": "Goldhemmed Black_Skirt",
        "image": "Legs/Goldhemmed Black_Skirt.png",
        "primaryColor": "#697886",
        "secondaryColors": [
            "#525b64",
            "#3b434b"
        ]
    },
    {
        "name": "Golem Leggings",
        "image": "Legs/Golem Leggings.png",
        "primaryColor": "#292321",
        "secondaryColors": [
            "#595853",
            "#4b4439"
        ]
    },
    {
        "name": "Gough's Legggings",
        "image": "Legs/Gough's Legggings.png",
        "primaryColor": "#aca096",
        "secondaryColors": [
            "#665b51",
            "#5e4b30"
        ]
    },
    {
        "name": "Guardian Leggings",
        "image": "Legs/Guardian Leggings.png",
        "primaryColor": "#887460",
        "secondaryColors": [
            "#66594c",
            "#534837"
        ]
    },
    {
        "name": "Hard Leather_Boots",
        "image": "Legs/Hard Leather_Boots.png",
        "primaryColor": "#966c4f",
        "secondaryColors": [
            "#101110",
            "#644936"
        ]
    },
    {
        "name": "Havels Leggings",
        "image": "Legs/Havels Leggings.png",
        "primaryColor": "#9b9691",
        "secondaryColors": [
            "#5d5a56",
            "#45413c"
        ]
    },
    {
        "name": "Heavy Boots",
        "image": "Legs/Heavy Boots.png",
        "primaryColor": "#221e17",
        "secondaryColors": [
            "#9f8d72",
            "#4e4539"
        ]
    },
    {
        "name": "Hollow Soldier_Waistcloth",
        "image": "Legs/Hollow Soldier_Waistcloth.png",
        "primaryColor": "#9b6d52",
        "secondaryColors": [
            "#695a4e",
            "#634533"
        ]
    },
    {
        "name": "Hollow Thiefs_Tights",
        "image": "Legs/Hollow Thiefs_Tights.png",
        "primaryColor": "#887464",
        "secondaryColors": [
            "#685a4f",
            "#52453a"
        ]
    },
    {
        "name": "Hollow Warrior_Waistcloth",
        "image": "Legs/Hollow Warrior_Waistcloth.png",
        "primaryColor": "#8e7555",
        "secondaryColors": [
            "#6e614e",
            "#5b4d34"
        ]
    },
    {
        "name": "Holy Trousers",
        "image": "Legs/Holy Trousers.png",
        "primaryColor": "#db9e5e",
        "secondaryColors": [
            "#a37347",
            "#8f6138"
        ]
    },
    {
        "name": "Knight Leggings",
        "image": "Legs/Knight Leggings.png",
        "primaryColor": "#a79b93",
        "secondaryColors": [
            "#897565",
            "#65594f"
        ]
    },
    {
        "name": "Leather Boots",
        "image": "Legs/Leather Boots.png",
        "primaryColor": "#955f4a",
        "secondaryColors": [
            "#885639",
            "#704734"
        ]
    },
    {
        "name": "Leggings Of Artorias",
        "image": "Legs/Leggings Of Artorias.png",
        "primaryColor": "#242723",
        "secondaryColors": [
            "#dbd9d6",
            "#5c5957"
        ]
    },
    {
        "name": "Leggings Of Favor",
        "image": "Legs/Leggings Of_Favor.png",
        "primaryColor": "#ab8e66",
        "secondaryColors": [
            "#906e51",
            "#664b2e"
        ]
    },
    {
        "name": "Leggings Of Thorns",
        "image": "Legs/Leggings Of_Thorns.png",
        "primaryColor": "#9e9693",
        "secondaryColors": [
            "#85776f",
            "#605a57"
        ]
    },
    {
        "name": "Lord's Blade Waistcloth",
        "image": "Legs/Lord's Blade Waistcloth.png",
        "primaryColor": "#648fa1",
        "secondaryColors": [
            "#4d5a63",
            "#364a56"
        ]
    },
    {
        "name": "Maiden Skirt",
        "image": "Legs/Maiden Skirt.png",
        "primaryColor": "#f9eca6",
        "secondaryColors": [
            "#a68c6d",
            "#695a48"
        ]
    },
    {
        "name": "Moonlight Waistcloth",
        "image": "Legs/Moonlight Waistcloth.png",
        "primaryColor": "#9798a1",
        "secondaryColors": [
            "#797a83",
            "#5b5b62"
        ]
    },
    {
        "name": "Ornstein's Leggings",
        "image": "Legs/Ornstein's Leggings_Icon.png",
        "primaryColor": "#dbd2aa",
        "secondaryColors": [
            "#b2aa89",
            "#968f6f"
        ]
    },
    {
        "name": "Painting Guardian_Waistcloth",
        "image": "Legs/Painting Guardian_Waistcloth.png",
        "primaryColor": "#f5eddd",
        "secondaryColors": [
            "#ddcab6",
            "#c8b6a3"
        ]
    },
    {
        "name": "Paladin Leggings",
        "image": "Legs/Paladin Leggings.png",
        "primaryColor": "#ecdd69",
        "secondaryColors": [
            "#a69757",
            "#5a4f2e"
        ]
    },
    {
        "name": "Shadow Leggings",
        "image": "Legs/Shadow Leggings.png",
        "primaryColor": "#a69d8f",
        "secondaryColors": [
            "#8b7567",
            "#615a52"
        ]
    },
    {
        "name": "Smoughs Leggings",
        "image": "Legs/Smoughs Leggings.png",
        "primaryColor": "#ded0aa",
        "secondaryColors": [
            "#9e8f72",
            "#877860"
        ]
    },
    {
        "name": "Solaire Legs",
        "image": "Legs/Solaire Legs.png",
        "primaryColor": "#9f9c98",
        "secondaryColors": [
            "#5b5a55",
            "#46433c"
        ]
    },
    {
        "name": "Sorcerer Boots",
        "image": "Legs/Sorcerer Boots.png",
        "primaryColor": "#242221",
        "secondaryColors": [
            "#ac9065",
            "#5d4a34"
        ]
    },
    {
        "name": "Steel Leggings",
        "image": "Legs/Steel Leggings.png",
        "primaryColor": "#9da09a",
        "secondaryColors": [
            "#585955",
            "#4b433a"
        ]
    },
    {
        "name": "Stone Leggings",
        "image": "Legs/Stone Leggings.png",
        "primaryColor": "#d8d8a2",
        "secondaryColors": [
            "#b0ad8b",
            "#98976b"
        ]
    },
    {
        "name": "Traveling Boots",
        "image": "Legs/Traveling Boots.png",
        "primaryColor": "#9f9c97",
        "secondaryColors": [
            "#65625e",
            "#684832"
        ]
    },
    {
        "name": "Waistcloth Of_The_Channelers",
        "image": "Legs/Waistcloth Of_The_Channelers.png",
        "primaryColor": "#a49c8f",
        "secondaryColors": [
            "#9a8b71",
            "#5e5a57"
        ]
    },
    {
        "name": "Wanderer Boots",
        "image": "Legs/Wanderer Boots.png",
        "primaryColor": "#8d715c",
        "secondaryColors": [
            "#67594d",
            "#5a4639"
        ]
    },
    {
        "name": "Witch Skirt",
        "image": "Legs/Witch Skirt.png",
        "primaryColor": "#a88f98",
        "secondaryColors": [
            "#a17885",
            "#8c6a72"
        ]
    },
    {
        "name": "Xanthous Waistcloth",
        "image": "Legs/Xanthous Waistcloth.png",
        "primaryColor": "#f7ea26",
        "secondaryColors": [
            "#d5a51c",
            "#926d14"
        ]
    },
    {
        "name": "Balder Shield",
        "image": "Shields/Balder Shield.png",
        "primaryColor": "#897363",
        "secondaryColors": [
            "#6a5a4f",
            "#54453a"
        ]
    },
    {
        "name": "Black Iron Greatshield",
        "image": "Shields/Black Iron Greatshield.png",
        "primaryColor": "#191919",
        "secondaryColors": [
            "#9d9b9a",
            "#5b5959"
        ]
    },
    {
        "name": "Black Knight Shield",
        "image": "Shields/Black Knight Shield.png",
        "primaryColor": "#0e0d0c",
        "secondaryColors": [
            "#b8a98f",
            "#4d4539"
        ]
    },
    {
        "name": "Bloodshield",
        "image": "Shields/Bloodshield.png",
        "primaryColor": "#575553",
        "secondaryColors": [
            "#9b9899",
            "#9f4e47"
        ]
    },
    {
        "name": "Bonewheel Shield",
        "image": "Shields/Bonewheel Shield.png",
        "primaryColor": "#ebe3da",
        "secondaryColors": [
            "#a49c94",
            "#625b56"
        ]
    },
    {
        "name": "Buckler",
        "image": "Shields/Buckler.png",
        "primaryColor": "#2f3a37",
        "secondaryColors": [
            "#4e5757",
            "#969f9f"
        ]
    },
    {
        "name": "Caduceus Kite Shield",
        "image": "Shields/Caduceus Kite Shield.png",
        "primaryColor": "#454344",
        "secondaryColors": [
            "#989f9f",
            "#585e5d"
        ]
    },
    {
        "name": "Caduceus Round Shield",
        "image": "Shields/Caduceus Round Shield.png",
        "primaryColor": "#999d99",
        "secondaryColors": [
            "#5c655f",
            "#355045"
        ]
    },
    {
        "name": "Cleansing Greatshield",
        "image": "Shields/Cleansing Greatshield.png",
        "primaryColor": "#171417",
        "secondaryColors": [
            "#555656",
            "#3d4042"
        ]
    },
    {
        "name": "Cracked Round Shield",
        "image": "Shields/Cracked Round Shield.png",
        "primaryColor": "#a98973",
        "secondaryColors": [
            "#8e705d",
            "#6d574a"
        ]
    },
    {
        "name": "Crest Shield",
        "image": "Shields/Crest Shield.png",
        "primaryColor": "#2b282d",
        "secondaryColors": [
            "#a39a98",
            "#8a7369"
        ]
    },
    {
        "name": "Crystal Ring Shield",
        "image": "Shields/Crystal Ring Shield.png",
        "primaryColor": "#a8a596",
        "secondaryColors": [
            "#665d51",
            "#4f453a"
        ]
    },
    {
        "name": "Crystal Shield",
        "image": "Shields/Crystal Shield.png",
        "primaryColor": "#6c6655",
        "secondaryColors": [
            "#9c9e9e",
            "#5a5c5c"
        ]
    },
    {
        "name": "Dragon Crest Shield",
        "image": "Shields/Dragon Crest Shield.png",
        "primaryColor": "#313438",
        "secondaryColors": [
            "#cab4a3",
            "#a79a96"
        ]
    },
    {
        "name": "Eagle Shield",
        "image": "Shields/Eagle Shield.png",
        "primaryColor": "#cfb18e",
        "secondaryColors": [
            "#a58e71",
            "#8e7261"
        ]
    },
    {
        "name": "Eastwest Shield",
        "image": "Shields/Eastwest Shield.png",
        "primaryColor": "#a59b91",
        "secondaryColors": [
            "#9b8b74",
            "#877767"
        ]
    },
    {
        "name": "Effigy Shield",
        "image": "Shields/Effigy Shield.png",
        "primaryColor": "#53524d",
        "secondaryColors": [
            "#9b9a97",
            "#5c5a58"
        ]
    },
    {
        "name": "Gargoyles Shield",
        "image": "Shields/Gargoyles Shield.png",
        "primaryColor": "#262a2a",
        "secondaryColors": [
            "#565e5a",
            "#3b4544"
        ]
    },
    {
        "name": "Giant Shield",
        "image": "Shields/Giant Shield.png",
        "primaryColor": "#45443c",
        "secondaryColors": [
            "#aaa191",
            "#958b73"
        ]
    },
    {
        "name": "Grass Crest Shield",
        "image": "Shields/Grass Crest Shield.png",
        "primaryColor": "#eeecd6",
        "secondaryColors": [
            "#d5d2af",
            "#a3a297"
        ]
    },
    {
        "name": "Greatshield Of Artorias",
        "image": "Shields/Greatshield Of Artorias.png",
        "primaryColor": "#211e1d",
        "secondaryColors": [
            "#9b9b9a",
            "#5a5a5a"
        ]
    },
    {
        "name": "Havels Greatshield",
        "image": "Shields/Havels Greatshield.png",
        "primaryColor": "#4b4444",
        "secondaryColors": [
            "#a19c98",
            "#5a5654"
        ]
    },
    {
        "name": "Heater Shield",
        "image": "Shields/Heater Shield.png",
        "primaryColor": "#6e708c",
        "secondaryColors": [
            "#a290a0",
            "#f6e6e7"
        ]
    },
    {
        "name": "Hollow Soldier Shield",
        "image": "Shields/Hollow Soldier Shield.png",
        "primaryColor": "#28221f",
        "secondaryColors": [
            "#897671",
            "#625450"
        ]
    },
    {
        "name": "Iron Round Shield",
        "image": "Shields/Iron Round Shield.png",
        "primaryColor": "#887775",
        "secondaryColors": [
            "#a59a96",
            "#867873"
        ]
    },
    {
        "name": "Knight Shield",
        "image": "Shields/Knight Shield.png",
        "primaryColor": "#cfe8ce",
        "secondaryColors": [
            "#3a6ab5",
            "#96333a"
        ]
    },
    {
        "name": "Large Leather Shield",
        "image": "Shields/Large Leather Shield.png",
        "primaryColor": "#da9355",
        "secondaryColors": [
            "#aa7148",
            "#96552c"
        ]
    },
    {
        "name": "Leather Shield",
        "image": "Shields/Leather Shield.png",
        "primaryColor": "#5d5348",
        "secondaryColors": [
            "#8f8678",
            "#615a50"
        ]
    },
    {
        "name": "Pierce Shield",
        "image": "Shields/Pierce Shield.png",
        "primaryColor": "#474a49",
        "secondaryColors": [
            "#8c8679",
            "#5c5953"
        ]
    },
    {
        "name": "Plank Shield",
        "image": "Shields/Plank Shield.png",
        "primaryColor": "#a38973",
        "secondaryColors": [
            "#8c725f",
            "#6c5b4d"
        ]
    },
    {
        "name": "Red And White Round Shield",
        "image": "Shields/Red And White Round Shield.png",
        "primaryColor": "#cec7ba",
        "secondaryColors": [
            "#5b2d26",
            "#e2c2a9"
        ]
    },
    {
        "name": "Sanctus",
        "image": "Shields/Sanctus.png",
        "primaryColor": "#f0dc62",
        "secondaryColors": [
            "#f1f2dc",
            "#003db9"
        ]
    },
    {
        "name": "Silver Knight Shield",
        "image": "Shields/Silver Knight Shield.png",
        "primaryColor": "#eae3d8",
        "secondaryColors": [
            "#a89f94",
            "#8f8579"
        ]
    },
    {
        "name": "Small Leather Shield",
        "image": "Shields/Small Leather Shield.png",
        "primaryColor": "#9c9b95",
        "secondaryColors": [
            "#8a726a",
            "#605a54"
        ]
    },
    {
        "name": "Spider Shield",
        "image": "Shields/Spider Shield.png",
        "primaryColor": "#e78975",
        "secondaryColors": [
            "#d27463",
            "#9d6258"
        ]
    },
    {
        "name": "Spiked Shield",
        "image": "Shields/Spiked Shield.png",
        "primaryColor": "#231f1a",
        "secondaryColors": [
            "#867573",
            "#5f5452"
        ]
    },
    {
        "name": "Stone Greatshield",
        "image": "Shields/Stone Greatshield.png",
        "primaryColor": "#919564",
        "secondaryColors": [
            "#605d4f",
            "#4e5431"
        ]
    },
    {
        "name": "Sunlight Shield",
        "image": "Shields/Sunlight Shield.png",
        "primaryColor": "#2f2d2d",
        "secondaryColors": [
            "#341719",
            "#7f8965"
        ]
    },
    {
        "name": "Target Shield",
        "image": "Shields/Target Shield.png",
        "primaryColor": "#464643",
        "secondaryColors": [
            "#615d57",
            "#4a443a"
        ]
    },
    {
        "name": "Tower Kite Shield",
        "image": "Shields/Tower Kite Shield.png",
        "primaryColor": "#101110",
        "secondaryColors": [
            "#c6c0b6",
            "#433937"
        ]
    },
    {
        "name": "Tower Shield",
        "image": "Shields/Tower Shield.png",
        "primaryColor": "#3e413e",
        "secondaryColors": [
            "#555853",
            "#42423c"
        ]
    },
    {
        "name": "Warriors Round Shield",
        "image": "Shields/Warriors Round Shield.png",
        "primaryColor": "#dfe1e6",
        "secondaryColors": [
            "#97949c",
            "#857a89"
        ]
    },
    {
        "name": "Wooden Shield",
        "image": "Shields/Wooden Shield.png",
        "primaryColor": "#a49f9c",
        "secondaryColors": [
            "#615c58",
            "#433a35"
        ]
    },
    {
        "name": "Abyss Greatsword",
        "image": "Weapons/Abyss Greatsword.png",
        "primaryColor": "#111110",
        "secondaryColors": [
            "#9e9d9d",
            "#605f5e"
        ]
    },
    {
        "name": "Astoras Straight Sword",
        "image": "Weapons/Astoras Straight Sword.png",
        "primaryColor": "#a19f9e",
        "secondaryColors": [
            "#635c55",
            "#574938"
        ]
    },
    {
        "name": "Avelyn",
        "image": "Weapons/Avelyn.png",
        "primaryColor": "#f8f1d6",
        "secondaryColors": [
            "#efd7a4",
            "#ab8d69"
        ]
    },
    {
        "name": "Balder Side Sword",
        "image": "Weapons/Balder Side Sword.png",
        "primaryColor": "#9ea19a",
        "secondaryColors": [
            "#605c57",
            "#644f30"
        ]
    },
    {
        "name": "Barbed Straight Sword",
        "image": "Weapons/Barbed Straight Sword.png",
        "primaryColor": "#ebe0e5",
        "secondaryColors": [
            "#a0959a",
            "#847578"
        ]
    },
    {
        "name": "Bastard Sword",
        "image": "Weapons/Bastard Sword.png",
        "primaryColor": "#a5a09d",
        "secondaryColors": [
            "#605b59",
            "#5e5b5a"
        ]
    },
    {
        "name": "Battle Axe",
        "image": "Weapons/Battle Axe.png",
        "primaryColor": "#989a97",
        "secondaryColors": [
            "#636463",
            "#616260"
        ]
    },
    {
        "name": "Beatrices Catalyst",
        "image": "Weapons/Beatrices Catalyst.png",
        "primaryColor": "#ada28e",
        "secondaryColors": [
            "#897764",
            "#655c50"
        ]
    },
    {
        "name": "Black Bow Of Pharis",
        "image": "Weapons/Black Bow Of Pharis.png",
        "primaryColor": "#a19e9e",
        "secondaryColors": [
            "#64625f",
            "#62605d"
        ]
    },
    {
        "name": "Black Knight Greataxe",
        "image": "Weapons/Black Knight Greataxe.png",
        "primaryColor": "#897464",
        "secondaryColors": [
            "#69594e",
            "#584539"
        ]
    },
    {
        "name": "Black Knight Greatsword",
        "image": "Weapons/Black Knight Greatsword.png",
        "primaryColor": "#9a8d6f",
        "secondaryColors": [
            "#645c50",
            "#524936"
        ]
    },
    {
        "name": "Black Knight Halberd",
        "image": "Weapons/Black Knight Halberd.png",
        "primaryColor": "#66584b",
        "secondaryColors": [
            "#65574b",
            "#504539"
        ]
    },
    {
        "name": "Black Knight Sword",
        "image": "Weapons/Black Knight Sword.png",
        "primaryColor": "#ada090",
        "secondaryColors": [
            "#675b4f",
            "#50453a"
        ]
    },
    {
        "name": "Blacksmith Giant Hammer",
        "image": "Weapons/Blacksmith Giant Hammer.png",
        "primaryColor": "#9d8f70",
        "secondaryColors": [
            "#85785f",
            "#6b614d"
        ]
    },
    {
        "name": "Blacksmith Hammer",
        "image": "Weapons/Blacksmith Hammer.png",
        "primaryColor": "#a49c94",
        "secondaryColors": [
            "#887461",
            "#645c52"
        ]
    },
    {
        "name": "Broadsword",
        "image": "Weapons/Broadsword.png",
        "primaryColor": "#ebe8dd",
        "secondaryColors": [
            "#ccc6b6",
            "#a8a397"
        ]
    },
    {
        "name": "Broken Straight Sword",
        "image": "Weapons/Broken Straight Sword.png",
        "primaryColor": "#ae9d8f",
        "secondaryColors": [
            "#86766b",
            "#655951"
        ]
    },
    {
        "name": "Butcher Knife",
        "image": "Weapons/Butcher Knife.png",
        "primaryColor": "#9c8873",
        "secondaryColors": [
            "#6b5c4d",
            "#534639"
        ]
    },
    {
        "name": "Caestus",
        "image": "Weapons/Caestus.png",
        "primaryColor": "#af9b8e",
        "secondaryColors": [
            "#8e6f5c",
            "#6a584e"
        ]
    },
    {
        "name": "Canvas Talisman",
        "image": "Weapons/Canvas Talisman.png",
        "primaryColor": "#a88e6c",
        "secondaryColors": [
            "#8c7152",
            "#634c34"
        ]
    },
    {
        "name": "Channelers Trident",
        "image": "Weapons/Channelers Trident.png",
        "primaryColor": "#a48b64",
        "secondaryColors": [
            "#8d7250",
            "#604b33"
        ]
    },
    {
        "name": "Chaos Blade",
        "image": "Weapons/Chaos Blade.png",
        "primaryColor": "#ffffff",
        "secondaryColors": [
            "#9d9e9b",
            "#61605d"
        ]
    },
    {
        "name": "Claw",
        "image": "Weapons/Claw.png",
        "primaryColor": "#ffffff",
        "secondaryColors": [
            "#a09e9d",
            "#605a59"
        ]
    },
    {
        "name": "Claymore",
        "image": "Weapons/Claymore.png",
        "primaryColor": "#a49e98",
        "secondaryColors": [
            "#8c7160",
            "#655e5a"
        ]
    },
    {
        "name": "Club",
        "image": "Weapons/Club.png",
        "primaryColor": "#8f7056",
        "secondaryColors": [
            "#725a47",
            "#604937"
        ]
    },
    {
        "name": "Composite Bow",
        "image": "Weapons/Composite Bow.png",
        "primaryColor": "#a59169",
        "secondaryColors": [
            "#6e6047",
            "#5b4e37"
        ]
    },
    {
        "name": "Crescent Axe",
        "image": "Weapons/Crescent Axe.png",
        "primaryColor": "#aea190",
        "secondaryColors": [
            "#685b4d",
            "#514538"
        ]
    },
    {
        "name": "Crystal Greatsword",
        "image": "Weapons/Crystal Greatsword.png",
        "primaryColor": "#9ea09f",
        "secondaryColors": [
            "#5e5c5d",
            "#5e2915"
        ]
    },
    {
        "name": "Crystal Straight Sword",
        "image": "Weapons/Crystal Straight Sword.png",
        "primaryColor": "#969fa6",
        "secondaryColors": [
            "#535d68",
            "#37485a"
        ]
    },
    {
        "name": "Dark Hand",
        "image": "Weapons/Dark Hand.png",
        "primaryColor": "#cb000a",
        "secondaryColors": [
            "#9d000d",
            "#580007"
        ]
    },
    {
        "name": "Dark Silver Tracer",
        "image": "Weapons/Dark Silver Tracer.png",
        "primaryColor": "#969d9d",
        "secondaryColors": [
            "#5b5f5f",
            "#5b5d5c"
        ]
    },
    {
        "name": "Darkmoon Bow",
        "image": "Weapons/Darkmoon Bow.png",
        "primaryColor": "#eddca2",
        "secondaryColors": [
            "#a89569",
            "#62605d"
        ]
    },
    {
        "name": "Darkmoon Talisman",
        "image": "Weapons/Darkmoon Talisman.png",
        "primaryColor": "#d6d5da",
        "secondaryColors": [
            "#9c9ca5",
            "#787885"
        ]
    },
    {
        "name": "Darksword",
        "image": "Weapons/Darksword.png",
        "primaryColor": "#a59f94",
        "secondaryColors": [
            "#9b8c73",
            "#625b52"
        ]
    },
    {
        "name": "Demon Great Machete",
        "image": "Weapons/Demon Great Machete.png",
        "primaryColor": "#8b7152",
        "secondaryColors": [
            "#735f48",
            "#5e4a36"
        ]
    },
    {
        "name": "Demons Catalyst",
        "image": "Weapons/Demons Catalyst.png",
        "primaryColor": "#eae5dd",
        "secondaryColors": [
            "#a29d97",
            "#958878"
        ]
    },
    {
        "name": "Demons Great Hammer",
        "image": "Weapons/Demons Great Hammer.png",
        "primaryColor": "#877765",
        "secondaryColors": [
            "#685d4e",
            "#504739"
        ]
    },
    {
        "name": "Demons Greataxe",
        "image": "Weapons/Demons Greataxe.png",
        "primaryColor": "#a59169",
        "secondaryColors": [
            "#8b7253",
            "#726249"
        ]
    },
    {
        "name": "Demons Spear",
        "image": "Weapons/Demons Spear.png",
        "primaryColor": "#a29c9e",
        "secondaryColors": [
            "#a29c9d",
            "#605a5c"
        ]
    },
    {
        "name": "Dragon Bone Fist",
        "image": "Weapons/Dragon Bone Fist.png",
        "primaryColor": "#a39060",
        "secondaryColors": [
            "#8c774c",
            "#716445"
        ]
    },
    {
        "name": "Dragon Greatsword",
        "image": "Weapons/Dragon Greatsword.png",
        "primaryColor": "#a38f6e",
        "secondaryColors": [
            "#685e4e",
            "#594a35"
        ]
    },
    {
        "name": "Dragon King Greataxe",
        "image": "Weapons/Dragon King Greataxe.png",
        "primaryColor": "#a39e94",
        "secondaryColors": [
            "#605b53",
            "#52453a"
        ]
    },
    {
        "name": "Dragon Tooth",
        "image": "Weapons/Dragon Tooth.png",
        "primaryColor": "#99948f",
        "secondaryColors": [
            "#5b5755",
            "#45413d"
        ]
    },
    {
        "name": "Dragonslayer Greatbow",
        "image": "Weapons/Dragonslayer Greatbow.png",
        "primaryColor": "#cdb094",
        "secondaryColors": [
            "#65574c",
            "#54453a"
        ]
    },
    {
        "name": "Dragonslayer Spear",
        "image": "Weapons/Dragonslayer Spear.png",
        "primaryColor": "#e0d2a8",
        "secondaryColors": [
            "#aca694",
            "#9d916c"
        ]
    },
    {
        "name": "Drake Sword",
        "image": "Weapons/Drake Sword.png",
        "primaryColor": "#a7a092",
        "secondaryColors": [
            "#655d52",
            "#4c4439"
        ]
    },
    {
        "name": "Estoc",
        "image": "Weapons/Estoc.png",
        "primaryColor": "#e2dedb",
        "secondaryColors": [
            "#9d9896",
            "#5c5a58"
        ]
    },
    {
        "name": "Falchion",
        "image": "Weapons/Falchion.png",
        "primaryColor": "#dedddb",
        "secondaryColors": [
            "#9e9c9a",
            "#9f9073"
        ]
    },
    {
        "name": "Flamberge",
        "image": "Weapons/Flamberge.png",
        "primaryColor": "#e7e2e0",
        "secondaryColors": [
            "#a39b9a",
            "#8b736e"
        ]
    },
    {
        "name": "Four-Pronged Plow",
        "image": "Weapons/Four-Pronged Plow.png",
        "primaryColor": "#a49e94",
        "secondaryColors": [
            "#675d54",
            "#5d4638"
        ]
    },
    {
        "name": "Gargoyle Tail Axe",
        "image": "Weapons/Gargoyle Tail Axe.png",
        "primaryColor": "#d9ebe8",
        "secondaryColors": [
            "#92a7a1",
            "#52625d"
        ]
    },
    {
        "name": "Gargoyles Halberd",
        "image": "Weapons/Gargoyles Halberd.png",
        "primaryColor": "#8c9a92",
        "secondaryColors": [
            "#565f5a",
            "#555c56"
        ]
    },
    {
        "name": "Giants Halberd",
        "image": "Weapons/Giants Halberd.png",
        "primaryColor": "#aba38e",
        "secondaryColors": [
            "#9b8e6f",
            "#6c624f"
        ]
    },
    {
        "name": "Gold Tracer",
        "image": "Weapons/Gold Tracer.png",
        "primaryColor": "#f49850",
        "secondaryColors": [
            "#e96d38",
            "#9c592d"
        ]
    },
    {
        "name": "Golem Axe",
        "image": "Weapons/Golem Axe.png",
        "primaryColor": "#d8d7db",
        "secondaryColors": [
            "#99999c",
            "#56585b"
        ]
    },
    {
        "name": "Gough-S Greatbow",
        "image": "Weapons/Gough-S Greatbow.png",
        "primaryColor": "#ebd7a0",
        "secondaryColors": [
            "#a68d64",
            "#91734e"
        ]
    },
    {
        "name": "Grant",
        "image": "Weapons/Grant.png",
        "primaryColor": "#a19c9c",
        "secondaryColors": [
            "#837a77",
            "#605b5b"
        ]
    },
    {
        "name": "Gravelord Sword",
        "image": "Weapons/Gravelord Sword.png",
        "primaryColor": "#9b8e6f",
        "secondaryColors": [
            "#69604d",
            "#534937"
        ]
    },
    {
        "name": "Great Club",
        "image": "Weapons/Great Club.png",
        "primaryColor": "#877557",
        "secondaryColors": [
            "#6d5e49",
            "#584933"
        ]
    },
    {
        "name": "Great Lord Greatsword",
        "image": "Weapons/Great Lord Greatsword.png",
        "primaryColor": "#988b6e",
        "secondaryColors": [
            "#86785c",
            "#6d644f"
        ]
    },
    {
        "name": "Great Scythe",
        "image": "Weapons/Great Scythe.png",
        "primaryColor": "#969ca6",
        "secondaryColors": [
            "#91715a",
            "#645953"
        ]
    },
    {
        "name": "Greataxe",
        "image": "Weapons/Greataxe.png",
        "primaryColor": "#aa9d8f",
        "secondaryColors": [
            "#887566",
            "#65574d"
        ]
    },
    {
        "name": "Greatsword Of Artorias (2)",
        "image": "Weapons/Greatsword Of Artorias (2).png",
        "primaryColor": "#989796",
        "secondaryColors": [
            "#5c5959",
            "#565555"
        ]
    },
    {
        "name": "Greatsword Of Artorias",
        "image": "Weapons/Greatsword Of Artorias.png",
        "primaryColor": "#e0e3e4",
        "secondaryColors": [
            "#9d9da0",
            "#6c778a"
        ]
    },
    {
        "name": "Greatsword",
        "image": "Weapons/Greatsword.png",
        "primaryColor": "#d6dcd4",
        "secondaryColors": [
            "#989d95",
            "#5d605b"
        ]
    },
    {
        "name": "Guardian Tail",
        "image": "Weapons/Guardian Tail.png",
        "primaryColor": "#a69d99",
        "secondaryColors": [
            "#625553",
            "#4d312c"
        ]
    },
    {
        "name": "Halberd",
        "image": "Weapons/Halberd.png",
        "primaryColor": "#929397",
        "secondaryColors": [
            "#696768",
            "#656564"
        ]
    },
    {
        "name": "Hammer Of Vamos",
        "image": "Weapons/Hammer Of Vamos.png",
        "primaryColor": "#a19d98",
        "secondaryColors": [
            "#998e74",
            "#5d5b58"
        ]
    },
    {
        "name": "Hand Axe",
        "image": "Weapons/Hand Axe.png",
        "primaryColor": "#9d9793",
        "secondaryColors": [
            "#8c7163",
            "#55331c"
        ]
    },
    {
        "name": "Heavy Crossbow",
        "image": "Weapons/Heavy Crossbow.png",
        "primaryColor": "#897257",
        "secondaryColors": [
            "#6b5d4c",
            "#5a4a36"
        ]
    },
    {
        "name": "Iaito",
        "image": "Weapons/Iaito.png",
        "primaryColor": "#a2a09c",
        "secondaryColors": [
            "#615e58",
            "#5e5d5d"
        ]
    },
    {
        "name": "Ivory Talisman",
        "image": "Weapons/Ivory Talisman.png",
        "primaryColor": "#ebe2d8",
        "secondaryColors": [
            "#dccab4",
            "#cfb89e"
        ]
    },
    {
        "name": "Izalith Catalyst",
        "image": "Weapons/Izalith Catalyst.png",
        "primaryColor": "#eae1d1",
        "secondaryColors": [
            "#d5c9b5",
            "#a9a093"
        ]
    },
    {
        "name": "Jagged Ghost Blade",
        "image": "Weapons/Jagged Ghost Blade.png",
        "primaryColor": "#dee6e8",
        "secondaryColors": [
            "#95a0a4",
            "#586165"
        ]
    },
    {
        "name": "Large Club",
        "image": "Weapons/Large Club.png",
        "primaryColor": "#968a73",
        "secondaryColors": [
            "#645c4d",
            "#4b4639"
        ]
    },
    {
        "name": "Lifehunt Scythe",
        "image": "Weapons/Lifehunt Scythe.png",
        "primaryColor": "#9d9e9e",
        "secondaryColors": [
            "#5e5d5e",
            "#5a5a59"
        ]
    },
    {
        "name": "Light Crossbow",
        "image": "Weapons/Light Crossbow.png",
        "primaryColor": "#8c7251",
        "secondaryColors": [
            "#73614a",
            "#614d34"
        ]
    },
    {
        "name": "Logans Catalyst",
        "image": "Weapons/Logans Catalyst.png",
        "primaryColor": "#8a7654",
        "secondaryColors": [
            "#716145",
            "#554a33"
        ]
    },
    {
        "name": "Longbow",
        "image": "Weapons/Longbow.png",
        "primaryColor": "#ceaf76",
        "secondaryColors": [
            "#a99161",
            "#89744e"
        ]
    },
    {
        "name": "Longsword",
        "image": "Weapons/Longsword.png",
        "primaryColor": "#ebe1e0",
        "secondaryColors": [
            "#a69897",
            "#8d7470"
        ]
    },
    {
        "name": "Lucerne",
        "image": "Weapons/Lucerne.png",
        "primaryColor": "#d5d5d5",
        "secondaryColors": [
            "#9d9c9a",
            "#5d5a56"
        ]
    },
    {
        "name": "Mace",
        "image": "Weapons/Mace.png",
        "primaryColor": "#a89e96",
        "secondaryColors": [
            "#90785f",
            "#5f5853"
        ]
    },
    {
        "name": "Mail Breaker",
        "image": "Weapons/Mail Breaker.png",
        "primaryColor": "#e6e3e0",
        "secondaryColors": [
            "#a8a39a",
            "#a69f97"
        ]
    },
    {
        "name": "Manserpent Greatsword",
        "image": "Weapons/Manserpent Greatsword.png",
        "primaryColor": "#a8a596",
        "secondaryColors": [
            "#625e51",
            "#4b4539"
        ]
    },
    {
        "name": "Manus Catalyst",
        "image": "Weapons/Manus Catalyst.png",
        "primaryColor": "#a09362",
        "secondaryColors": [
            "#6e6249",
            "#594c35"
        ]
    },
    {
        "name": "Moonlight Butterfly Horn",
        "image": "Weapons/Moonlight Butterfly Horn.png",
        "primaryColor": "#ffffff",
        "secondaryColors": [
            "#a29e95",
            "#5e5c56"
        ]
    },
    {
        "name": "Moonlight Greatsword",
        "image": "Weapons/Moonlight Greatsword.png",
        "primaryColor": "#dfe7dc",
        "secondaryColors": [
            "#a0a699",
            "#a1916f"
        ]
    },
    {
        "name": "Morning Star",
        "image": "Weapons/Morning Star.png",
        "primaryColor": "#a09898",
        "secondaryColors": [
            "#625a5a",
            "#5c5a5b"
        ]
    },
    {
        "name": "Murakumo",
        "image": "Weapons/Murakumo.png",
        "primaryColor": "#939293",
        "secondaryColors": [
            "#605f5b",
            "#5d5c5c"
        ]
    },
    {
        "name": "Notched Whip",
        "image": "Weapons/Notched Whip.png",
        "primaryColor": "#a09a9b",
        "secondaryColors": [
            "#5e5957",
            "#5e5858"
        ]
    },
    {
        "name": "Obsidian Greatsword",
        "image": "Weapons/Obsidian Greatsword.png",
        "primaryColor": "#a09d9d",
        "secondaryColors": [
            "#948778",
            "#5d5a5c"
        ]
    },
    {
        "name": "Oolacile Catalyst",
        "image": "Weapons/Oolacile Catalyst.png",
        "primaryColor": "#dddad6",
        "secondaryColors": [
            "#9f9c9a",
            "#5d5b5a"
        ]
    },
    {
        "name": "Oolacile Ivory Catalyst",
        "image": "Weapons/Oolacile Ivory Catalyst.png",
        "primaryColor": "#a2a1a0",
        "secondaryColors": [
            "#999898",
            "#626161"
        ]
    },
    {
        "name": "Painting Guardian Sword",
        "image": "Weapons/Painting Guardian Sword.png",
        "primaryColor": "#a5a3a1",
        "secondaryColors": [
            "#a19c97",
            "#5f5b57"
        ]
    },
    {
        "name": "Partizan",
        "image": "Weapons/Partizan.png",
        "primaryColor": "#9f9c9c",
        "secondaryColors": [
            "#8e756b",
            "#5c5a5a"
        ]
    },
    {
        "name": "Pickaxe",
        "image": "Weapons/Pickaxe.png",
        "primaryColor": "#ad8c5d",
        "secondaryColors": [
            "#8e6236",
            "#674c2e"
        ]
    },
    {
        "name": "Pike",
        "image": "Weapons/Pike.png",
        "primaryColor": "#ab9c9a",
        "secondaryColors": [
            "#955d5b",
            "#5c312f"
        ]
    },
    {
        "name": "Pyromancy Flame (2)",
        "image": "Weapons/Pyromancy Flame (2).png",
        "primaryColor": "#ef5508",
        "secondaryColors": [
            "#e11c03",
            "#a11c07"
        ]
    },
    {
        "name": "Pyromancy Flame",
        "image": "Weapons/Pyromancy Flame.png",
        "primaryColor": "#eb540d",
        "secondaryColors": [
            "#d72206",
            "#9f2107"
        ]
    },
    {
        "name": "Quelaags Furysword",
        "image": "Weapons/Quelaags Furysword.png",
        "primaryColor": "#efe5db",
        "secondaryColors": [
            "#a79a91",
            "#625954"
        ]
    },
    {
        "name": "Rapier",
        "image": "Weapons/Rapier.png",
        "primaryColor": "#e2e0dd",
        "secondaryColors": [
            "#a19f9b",
            "#9f9d9b"
        ]
    },
    {
        "name": "Reinforced Club",
        "image": "Weapons/Reinforced Club.png",
        "primaryColor": "#b09c8d",
        "secondaryColors": [
            "#8a7667",
            "#66584e"
        ]
    },
    {
        "name": "Ricards Rapier",
        "image": "Weapons/Ricards Rapier.png",
        "primaryColor": "#f1efdf",
        "secondaryColors": [
            "#eadba3",
            "#a19f9b"
        ]
    },
    {
        "name": "Scimitar",
        "image": "Weapons/Scimitar.png",
        "primaryColor": "#dbd9d5",
        "secondaryColors": [
            "#9e9d9c",
            "#68625b"
        ]
    },
    {
        "name": "Scythe",
        "image": "Weapons/Scythe.png",
        "primaryColor": "#9e92a1",
        "secondaryColors": [
            "#594d52",
            "#4f443b"
        ]
    },
    {
        "name": "Server",
        "image": "Weapons/Server.png",
        "primaryColor": "#9da09d",
        "secondaryColors": [
            "#625d55",
            "#552d23"
        ]
    },
    {
        "name": "Short Bow",
        "image": "Weapons/Short Bow.png",
        "primaryColor": "#9c8d6e",
        "secondaryColors": [
            "#6a6355",
            "#645d4f"
        ]
    },
    {
        "name": "Shortsword",
        "image": "Weapons/Shortsword.png",
        "primaryColor": "#edf2d8",
        "secondaryColors": [
            "#d5d9b3",
            "#a9ad96"
        ]
    },
    {
        "name": "Shotel",
        "image": "Weapons/Shotel.png",
        "primaryColor": "#d8d8d8",
        "secondaryColors": [
            "#9d9c9c",
            "#666363"
        ]
    },
    {
        "name": "Silv Knight Str Sword",
        "image": "Weapons/Silv Knight Str Sword.png",
        "primaryColor": "#ffffff",
        "secondaryColors": [
            "#a49d95",
            "#615b54"
        ]
    },
    {
        "name": "Silver Knight Spear",
        "image": "Weapons/Silver Knight Spear.png",
        "primaryColor": "#ebe6e0",
        "secondaryColors": [
            "#a59d96",
            "#665e58"
        ]
    },
    {
        "name": "Smoughs Hammer",
        "image": "Weapons/Smoughs Hammer.png",
        "primaryColor": "#ada690",
        "secondaryColors": [
            "#948c74",
            "#666050"
        ]
    },
    {
        "name": "Sniper Crossbow",
        "image": "Weapons/Sniper Crossbow.png",
        "primaryColor": "#9c885d",
        "secondaryColors": [
            "#5d5851",
            "#5b4d2f"
        ]
    },
    {
        "name": "Sorcerers Catalyst",
        "image": "Weapons/Sorcerers Catalyst.png",
        "primaryColor": "#e2d197",
        "secondaryColors": [
            "#a3956b",
            "#564c36"
        ]
    },
    {
        "name": "Spear",
        "image": "Weapons/Spear.png",
        "primaryColor": "#90635c",
        "secondaryColors": [
            "#615454",
            "#4f3532"
        ]
    },
    {
        "name": "Stone Greataxe",
        "image": "Weapons/Stone Greataxe.png",
        "primaryColor": "#e1e0e1",
        "secondaryColors": [
            "#a09d9c",
            "#615a54"
        ]
    },
    {
        "name": "Stone Greatsword",
        "image": "Weapons/Stone Greatsword.png",
        "primaryColor": "#8c9565",
        "secondaryColors": [
            "#5e6350",
            "#4e5634"
        ]
    },
    {
        "name": "Straight Sword Hilt",
        "image": "Weapons/Straight Sword Hilt.png",
        "primaryColor": "#a99c92",
        "secondaryColors": [
            "#685c52",
            "#463931"
        ]
    },
    {
        "name": "Sunlight Straight Sword",
        "image": "Weapons/Sunlight Straight Sword.png",
        "primaryColor": "#ddd9d5",
        "secondaryColors": [
            "#a2a29f",
            "#5c5a58"
        ]
    },
    {
        "name": "Sunlight Talisman",
        "image": "Weapons/Sunlight Talisman.png",
        "primaryColor": "#e5ded3",
        "secondaryColors": [
            "#aba192",
            "#978b70"
        ]
    },
    {
        "name": "Talisman",
        "image": "Weapons/Talisman.png",
        "primaryColor": "#9f9795",
        "secondaryColors": [
            "#625951",
            "#554837"
        ]
    },
    {
        "name": "Thorolund Talisman",
        "image": "Weapons/Thorolund Talisman.png",
        "primaryColor": "#99581f",
        "secondaryColors": [
            "#6e4821",
            "#5c2c1d"
        ]
    },
    {
        "name": "Tin Banishment Catalyst",
        "image": "Weapons/Tin Banishment Catalyst.png",
        "primaryColor": "#a69591",
        "secondaryColors": [
            "#89736e",
            "#645755"
        ]
    },
    {
        "name": "Tin Crystallization Ctlyst",
        "image": "Weapons/Tin Crystallization Ctlyst.png",
        "primaryColor": "#a6a499",
        "secondaryColors": [
            "#978f6e",
            "#635f54"
        ]
    },
    {
        "name": "Tin Darkmoon Catalyst",
        "image": "Weapons/Tin Darkmoon Catalyst.png",
        "primaryColor": "#a4a197",
        "secondaryColors": [
            "#a0905d",
            "#65635a"
        ]
    },
    {
        "name": "Titanite Catch Pole",
        "image": "Weapons/Titanite Catch Pole.png",
        "primaryColor": "#e0e0e1",
        "secondaryColors": [
            "#9c9c9f",
            "#626264"
        ]
    },
    {
        "name": "Uchigatana",
        "image": "Weapons/Uchigatana.png",
        "primaryColor": "#ffffff",
        "secondaryColors": [
            "#9e9e9d",
            "#5d5d5a"
        ]
    },
    {
        "name": "Velkas Rapier",
        "image": "Weapons/Velkas Rapier.png",
        "primaryColor": "#e0dfdf",
        "secondaryColors": [
            "#9c9b9b",
            "#616060"
        ]
    },
    {
        "name": "Velkas Talisman",
        "image": "Weapons/Velkas Talisman.png",
        "primaryColor": "#5e5e5e",
        "secondaryColors": [
            "#585858",
            "#565656"
        ]
    },
    {
        "name": "Warpick",
        "image": "Weapons/Warpick.png",
        "primaryColor": "#a69b99",
        "secondaryColors": [
            "#635955",
            "#463a35"
        ]
    },
    {
        "name": "Washing Pole",
        "image": "Weapons/Washing Pole.png",
        "primaryColor": "#e1dedc",
        "secondaryColors": [
            "#a8a095",
            "#655e56"
        ]
    },
    {
        "name": "Whip",
        "image": "Weapons/Whip.png",
        "primaryColor": "#e1d8d7",
        "secondaryColors": [
            "#a2989a",
            "#61595b"
        ]
    },
    {
        "name": "Winged Spear",
        "image": "Weapons/Winged Spear.png",
        "primaryColor": "#a79b91",
        "secondaryColors": [
            "#8f8579",
            "#655d55"
        ]
    },
    {
        "name": "Wpn Bandit-S Knife",
        "image": "Weapons/Wpn Bandit-S Knife.png",
        "primaryColor": "#8b725a",
        "secondaryColors": [
            "#69594a",
            "#594838"
        ]
    },
    {
        "name": "Wpn Dagger",
        "image": "Weapons/Wpn Dagger.png",
        "primaryColor": "#ede4db",
        "secondaryColors": [
            "#aa9e95",
            "#695b51"
        ]
    },
    {
        "name": "Wpn Ghost Blade",
        "image": "Weapons/Wpn Ghost Blade.png",
        "primaryColor": "#d4dadb",
        "secondaryColors": [
            "#969d9d",
            "#5a5f60"
        ]
    },
    {
        "name": "Wpn Parrying Dagger",
        "image": "Weapons/Wpn Parrying Dagger.png",
        "primaryColor": "#a29e97",
        "secondaryColors": [
            "#615a51",
            "#5b4935"
        ]
    },
    {
        "name": "Wpn Priscilla-S Dagger",
        "image": "Weapons/Wpn Priscilla-S Dagger.png",
        "primaryColor": "#dadada",
        "secondaryColors": [
            "#9f9f9f",
            "#5f5f5f"
        ]
    },
    {
        "name": "Zweihander",
        "image": "Weapons/Zweihander.png",
        "primaryColor": "#ebe4d9",
        "secondaryColors": [
            "#a49d95",
            "#928579"
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
