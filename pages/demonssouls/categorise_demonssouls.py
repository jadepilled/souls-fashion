import json

# Your JSON data as a list of dictionaries
data = [
    {
        "name": "Ancient King'S Breastplate",
        "image": "Chest/Ancient King's Breastplate.png",
        "primaryColor": "#d8efe5",
        "secondaryColors": [
            "#95a59a",
            "#77938a"
        ]
    },
    {
        "name": "Binded Cross",
        "image": "Chest/Binded Cross.png",
        "primaryColor": "#ece4dd",
        "secondaryColors": [
            "#a88b6f",
            "#8d725a"
        ]
    },
    {
        "name": "Black Leather",
        "image": "Chest/Black Leather.png",
        "primaryColor": "#a49b8e",
        "secondaryColors": [
            "#8f8778",
            "#847a6d"
        ]
    },
    {
        "name": "Brushwood Armor",
        "image": "Chest/Brushwood Armor.png",
        "primaryColor": "#ad9e8c",
        "secondaryColors": [
            "#9c8973",
            "#877562"
        ]
    },
    {
        "name": "Chain Mail",
        "image": "Chest/Chain Mail.png",
        "primaryColor": "#a99a90",
        "secondaryColors": [
            "#877367",
            "#67584f"
        ]
    },
    {
        "name": "Coat Of Plate",
        "image": "Chest/Coat of Plate.png",
        "primaryColor": "#e7e4e0",
        "secondaryColors": [
            "#a39d96",
            "#84786f"
        ]
    },
    {
        "name": "Dark Silver Armor",
        "image": "Chest/Dark Silver Armor.png",
        "primaryColor": "#a19e9b",
        "secondaryColors": [
            "#5d5b58",
            "#44423d"
        ]
    },
    {
        "name": "Dull Gold Armor",
        "image": "Chest/Dull Gold Armor.png",
        "primaryColor": "#ecd9a3",
        "secondaryColors": [
            "#a68c62",
            "#8b7451"
        ]
    },
    {
        "name": "Fluted Armor",
        "image": "Chest/Fluted Armor.png",
        "primaryColor": "#e5e1dc",
        "secondaryColors": [
            "#a29c96",
            "#837a74"
        ]
    },
    {
        "name": "Gloom Armor",
        "image": "Chest/Gloom Armor.png",
        "primaryColor": "#f5efdf",
        "secondaryColors": [
            "#9f8a6f",
            "#89745a"
        ]
    },
    {
        "name": "Leather Armor",
        "image": "Chest/Leather Armor.png",
        "primaryColor": "#b09f8a",
        "secondaryColors": [
            "#9f8975",
            "#8a7361"
        ]
    },
    {
        "name": "Mirdan Scale Mail",
        "image": "Chest/Mirdan Scale Mail.png",
        "primaryColor": "#f1ebe0",
        "secondaryColors": [
            "#a9a093",
            "#8f867a"
        ]
    },
    {
        "name": "Old Raggedy Robes",
        "image": "Chest/Old Raggedy Robes.png",
        "primaryColor": "#9d9992",
        "secondaryColors": [
            "#86837b",
            "#635e59"
        ]
    },
    {
        "name": "Rogue'S Clothes",
        "image": "Chest/Rogue's Clothes.png",
        "primaryColor": "#e7d6a1",
        "secondaryColors": [
            "#a4906a",
            "#8a7655"
        ]
    },
    {
        "name": "Saint'S Robes",
        "image": "Chest/Saint's Robes.png",
        "primaryColor": "#ddd9d1",
        "secondaryColors": [
            "#c7c4ba",
            "#a3a199"
        ]
    },
    {
        "name": "Shaman'S Clothes",
        "image": "Chest/Shaman's Clothes.png",
        "primaryColor": "#a89f92",
        "secondaryColors": [
            "#928778",
            "#86786c"
        ]
    },
    {
        "name": "Venerable Sage'S Robe",
        "image": "Chest/Venerable Sage's Robe.png",
        "primaryColor": "#ae9d8c",
        "secondaryColors": [
            "#9d8875",
            "#897463"
        ]
    },
    {
        "name": "Wizard'S Clothes",
        "image": "Chest/Wizard's Clothes.png",
        "primaryColor": "#e7e3d9",
        "secondaryColors": [
            "#a2a093",
            "#898678"
        ]
    },
    {
        "name": "Ancient King'S Gauntlet",
        "image": "Hands/Ancient King's Gauntlet.png",
        "primaryColor": "#addece",
        "secondaryColors": [
            "#8ab1a2",
            "#6f9c8f"
        ]
    },
    {
        "name": "Binded Gloves",
        "image": "Hands/Binded Gloves.png",
        "primaryColor": "#ac8966",
        "secondaryColors": [
            "#907154",
            "#8d6235"
        ]
    },
    {
        "name": "Black Gloves",
        "image": "Hands/Black Gloves.png",
        "primaryColor": "#a79a8c",
        "secondaryColors": [
            "#948677",
            "#85786c"
        ]
    },
    {
        "name": "Brushwood Gauntlets",
        "image": "Hands/Brushwood Gauntlets.png",
        "primaryColor": "#b29f8a",
        "secondaryColors": [
            "#a28a72",
            "#8a7460"
        ]
    },
    {
        "name": "Chain Gloves",
        "image": "Hands/Chain Gloves.png",
        "primaryColor": "#c5b7b0",
        "secondaryColors": [
            "#a49791",
            "#857973"
        ]
    },
    {
        "name": "Dark Silver Manifer",
        "image": "Hands/Dark Silver Manifer.png",
        "primaryColor": "#e2dfdc",
        "secondaryColors": [
            "#a19e9a",
            "#84817d"
        ]
    },
    {
        "name": "Dull Gold Manifer",
        "image": "Hands/Dull Gold Manifer.png",
        "primaryColor": "#f3d95e",
        "secondaryColors": [
            "#aca693",
            "#635e52"
        ]
    },
    {
        "name": "Fluted Gauntlet",
        "image": "Hands/Fluted Gauntlet.png",
        "primaryColor": "#e4e0da",
        "secondaryColors": [
            "#a39d98",
            "#837b73"
        ]
    },
    {
        "name": "Gloom Gauntlet",
        "image": "Hands/Gloom Gauntlet.png",
        "primaryColor": "#f6f2e0",
        "secondaryColors": [
            "#ab8e67",
            "#8d7353"
        ]
    },
    {
        "name": "Leather Gloves",
        "image": "Hands/Leather Gloves.png",
        "primaryColor": "#cfac8e",
        "secondaryColors": [
            "#aa8c71",
            "#8d745e"
        ]
    },
    {
        "name": "Mirdan Manifer",
        "image": "Hands/Mirdan Manifer.png",
        "primaryColor": "#efe9dd",
        "secondaryColors": [
            "#cfc6b8",
            "#a79c90"
        ]
    },
    {
        "name": "Old Raggedy Gloves",
        "image": "Hands/Old Raggedy Gloves.png",
        "primaryColor": "#aa9989",
        "secondaryColors": [
            "#a08875",
            "#8c7666"
        ]
    },
    {
        "name": "Plate Gauntlet",
        "image": "Hands/Plate Gauntlet.png",
        "primaryColor": "#f0e7de",
        "secondaryColors": [
            "#dec8b3",
            "#ccb39e"
        ]
    },
    {
        "name": "Rogue'S Gloves",
        "image": "Hands/Rogue's Gloves.png",
        "primaryColor": "#edead3",
        "secondaryColors": [
            "#9f9b94",
            "#575452"
        ]
    },
    {
        "name": "Saint'S Gloves",
        "image": "Hands/Saint's Gloves.png",
        "primaryColor": "#eae5df",
        "secondaryColors": [
            "#a89c92",
            "#958578"
        ]
    },
    {
        "name": "Shaman'S Armband",
        "image": "Hands/Shaman's Armband.png",
        "primaryColor": "#a79f95",
        "secondaryColors": [
            "#8b847a",
            "#837a70"
        ]
    },
    {
        "name": "Silver Bracelet",
        "image": "Hands/Silver Bracelet.png",
        "primaryColor": "#e0dbd8",
        "secondaryColors": [
            "#c7c2bc",
            "#c2bcb7"
        ]
    },
    {
        "name": "Venerable Sage'S Gloves",
        "image": "Hands/Venerable Sage's Gloves.png",
        "primaryColor": "#ae998b",
        "secondaryColors": [
            "#9e8776",
            "#897466"
        ]
    },
    {
        "name": "Wizard'S Gloves",
        "image": "Hands/Wizard's Gloves.png",
        "primaryColor": "#d4c6b8",
        "secondaryColors": [
            "#c5b8aa",
            "#a89d92"
        ]
    },
    {
        "name": "Ancient King'S Mask",
        "image": "Head/Ancient King's Mask.png",
        "primaryColor": "#dbeae3",
        "secondaryColors": [
            "#92a99e",
            "#789187"
        ]
    },
    {
        "name": "Assassin'S Mask",
        "image": "Head/Assassin's Mask.png",
        "primaryColor": "#d0c8b6",
        "secondaryColors": [
            "#a39c90",
            "#8b8479"
        ]
    },
    {
        "name": "Binded Hood",
        "image": "Head/Binded Hood.png",
        "primaryColor": "#d0ae8d",
        "secondaryColors": [
            "#ab8b6b",
            "#8f7052"
        ]
    },
    {
        "name": "Brushwood Helmet",
        "image": "Head/Brushwood Helmet.png",
        "primaryColor": "#f5eddd",
        "secondaryColors": [
            "#c9b59f",
            "#b2a18d"
        ]
    },
    {
        "name": "Chain Helmet",
        "image": "Head/Chain Helmet.png",
        "primaryColor": "#a49891",
        "secondaryColors": [
            "#8f837b",
            "#857a73"
        ]
    },
    {
        "name": "Dark Silver Helmet",
        "image": "Head/Dark Silver Helmet.png",
        "primaryColor": "#d9d7d5",
        "secondaryColors": [
            "#a4a19e",
            "#a3a09c"
        ]
    },
    {
        "name": "Dull Gold Helmet",
        "image": "Head/Dull Gold Helmet.png",
        "primaryColor": "#f3e89b",
        "secondaryColors": [
            "#cfa95a",
            "#ab8f51"
        ]
    },
    {
        "name": "Fluted Helmet",
        "image": "Head/Fluted Helmet.png",
        "primaryColor": "#a39e9a",
        "secondaryColors": [
            "#837d7a",
            "#5d5955"
        ]
    },
    {
        "name": "Gloom Helmet",
        "image": "Head/Gloom Helmet.png",
        "primaryColor": "#eae5db",
        "secondaryColors": [
            "#aba295",
            "#87755f"
        ]
    },
    {
        "name": "Gold Mask",
        "image": "Head/Gold Mask.png",
        "primaryColor": "#f3e29d",
        "secondaryColors": [
            "#d0ab64",
            "#ad8f58"
        ]
    },
    {
        "name": "Leather Cap",
        "image": "Head/Leather Cap.png",
        "primaryColor": "#aa9488",
        "secondaryColors": [
            "#9a8578",
            "#89756a"
        ]
    },
    {
        "name": "Mirdan Helmet",
        "image": "Head/Mirdan Helmet.png",
        "primaryColor": "#ece8e0",
        "secondaryColors": [
            "#a49d93",
            "#8a837a"
        ]
    },
    {
        "name": "Monk'S Head Collar",
        "image": "Head/Monk's Head Collar.png",
        "primaryColor": "#f9d550",
        "secondaryColors": [
            "#e4ac48",
            "#e19b2c"
        ]
    },
    {
        "name": "Official'S Cap",
        "image": "Head/Official's Cap.png",
        "primaryColor": "#897266",
        "secondaryColors": [
            "#655249",
            "#57433a"
        ]
    },
    {
        "name": "Plate Helmet",
        "image": "Head/Plate Helmet.png",
        "primaryColor": "#e7e3df",
        "secondaryColors": [
            "#a39e9a",
            "#8b827c"
        ]
    },
    {
        "name": "Silver Coronet",
        "image": "Head/Silver Coronet.png",
        "primaryColor": "#a3a09e",
        "secondaryColors": [
            "#a09b99",
            "#656160"
        ]
    },
    {
        "name": "Three-Cornered Hat",
        "image": "Head/Three-cornered Hat.png",
        "primaryColor": "#a0988d",
        "secondaryColors": [
            "#5c5952",
            "#45433b"
        ]
    },
    {
        "name": "Venerable Sage'S Hood",
        "image": "Head/Venerable Sage's Hood.png",
        "primaryColor": "#ad9f8d",
        "secondaryColors": [
            "#948775",
            "#867868"
        ]
    },
    {
        "name": "Ancient King'S Leggings",
        "image": "Legs/Ancient King's Leggings.png",
        "primaryColor": "#99a49b",
        "secondaryColors": [
            "#58625a",
            "#38423a"
        ]
    },
    {
        "name": "Binded Boots",
        "image": "Legs/Binded Boots.png",
        "primaryColor": "#8c735c",
        "secondaryColors": [
            "#6d5c4c",
            "#5b4836"
        ]
    },
    {
        "name": "Black Boots",
        "image": "Legs/Black Boots.png",
        "primaryColor": "#a2988f",
        "secondaryColors": [
            "#8d857a",
            "#635c55"
        ]
    },
    {
        "name": "Brushwood Leggings",
        "image": "Legs/Brushwood Leggings.png",
        "primaryColor": "#b09e8c",
        "secondaryColors": [
            "#887563",
            "#6b5c4d"
        ]
    },
    {
        "name": "Dark Silver Leggings",
        "image": "Legs/Dark Silver Leggings.png",
        "primaryColor": "#a3a09a",
        "secondaryColors": [
            "#5b5a58",
            "#5a5854"
        ]
    },
    {
        "name": "Dull Gold Leggings",
        "image": "Legs/Dull Gold Leggings.png",
        "primaryColor": "#a48e6f",
        "secondaryColors": [
            "#8b7558",
            "#6e604a"
        ]
    },
    {
        "name": "Fluted Leggings",
        "image": "Legs/Fluted Leggings.png",
        "primaryColor": "#c9b6a9",
        "secondaryColors": [
            "#a69d96",
            "#85766c"
        ]
    },
    {
        "name": "Gloom Leggings",
        "image": "Legs/Gloom Leggings.png",
        "primaryColor": "#f2ede0",
        "secondaryColors": [
            "#9a8973",
            "#6a5c4c"
        ]
    },
    {
        "name": "Hard Leather Boots",
        "image": "Legs/Hard Leather Boots.png",
        "primaryColor": "#ceb6ac",
        "secondaryColors": [
            "#a8978e",
            "#867870"
        ]
    },
    {
        "name": "Leather Boots",
        "image": "Legs/Leather Boots.png",
        "primaryColor": "#cab3a3",
        "secondaryColors": [
            "#af9b8e",
            "#998778"
        ]
    },
    {
        "name": "Old Raggedy Boots",
        "image": "Legs/Old Raggedy Boots.png",
        "primaryColor": "#9b958c",
        "secondaryColors": [
            "#5e5b52",
            "#47433b"
        ]
    },
    {
        "name": "Plate Leggings",
        "image": "Legs/Plate Leggings.png",
        "primaryColor": "#ebe6df",
        "secondaryColors": [
            "#d0c8b4",
            "#a8a195"
        ]
    },
    {
        "name": "Rogue'S Boots",
        "image": "Legs/Rogue's Boots.png",
        "primaryColor": "#54504b",
        "secondaryColors": [
            "#4f4b47",
            "#47433c"
        ]
    },
    {
        "name": "Saint'S Boots",
        "image": "Legs/Saint's Boots.png",
        "primaryColor": "#a6a199",
        "secondaryColors": [
            "#948679",
            "#605a54"
        ]
    },
    {
        "name": "Shaman'S Tabi Socks",
        "image": "Legs/Shaman's Tabi Socks.png",
        "primaryColor": "#a99a8e",
        "secondaryColors": [
            "#85796f",
            "#635c55"
        ]
    },
    {
        "name": "Venerable Sage'S Boots",
        "image": "Legs/Venerable Sage's Boots.png",
        "primaryColor": "#ab998b",
        "secondaryColors": [
            "#9f8a76",
            "#88776a"
        ]
    },
    {
        "name": "Wizard'S Shoes",
        "image": "Legs/Wizard's Shoes.png",
        "primaryColor": "#e5dfdb",
        "secondaryColors": [
            "#9d9690",
            "#615e5b"
        ]
    },
    {
        "name": "Adjudicators Shield ",
        "image": "Shields/Adjudicators Shield .png",
        "primaryColor": "#a08c5e",
        "secondaryColors": [
            "#8d7250",
            "#8f6632"
        ]
    },
    {
        "name": "Buckler",
        "image": "Shields/Buckler.png",
        "primaryColor": "#a99c92",
        "secondaryColors": [
            "#92847a",
            "#867970"
        ]
    },
    {
        "name": "Dark Silver Shield",
        "image": "Shields/Dark Silver Shield.png",
        "primaryColor": "#9f9991",
        "secondaryColors": [
            "#5a5652",
            "#44403e"
        ]
    },
    {
        "name": "Dregling Shield Small",
        "image": "Shields/Dregling Shield Small.png",
        "primaryColor": "#5e5147",
        "secondaryColors": [
            "#584434",
            "#493625"
        ]
    },
    {
        "name": "Heater Shield",
        "image": "Shields/Heater Shield.png",
        "primaryColor": "#8f8485",
        "secondaryColors": [
            "#847879",
            "#605757"
        ]
    },
    {
        "name": "Hoplite Shield",
        "image": "Shields/Hoplite Shield.png",
        "primaryColor": "#a88b63",
        "secondaryColors": [
            "#8d724f",
            "#6b5e49"
        ]
    },
    {
        "name": "Kite Shield",
        "image": "Shields/Kite Shield.png",
        "primaryColor": "#846631",
        "secondaryColors": [
            "#6a4e1d",
            "#544f4c"
        ]
    },
    {
        "name": "Knights Shield Standar Shield ",
        "image": "Shields/Knights Shield Standar Shield .png",
        "primaryColor": "#a88a61",
        "secondaryColors": [
            "#8e714d",
            "#5a534d"
        ]
    },
    {
        "name": "Large Brushwood Shield",
        "image": "Shields/Large Brushwood Shield.png",
        "primaryColor": "#906f4f",
        "secondaryColors": [
            "#61584f",
            "#5f4935"
        ]
    },
    {
        "name": "Leather Shield ",
        "image": "Shields/Leather Shield .png",
        "primaryColor": "#897152",
        "secondaryColors": [
            "#6c5f58",
            "#6c5d54"
        ]
    },
    {
        "name": "Purple Flame Shield",
        "image": "Shields/Purple Flame Shield.png",
        "primaryColor": "#cdac93",
        "secondaryColors": [
            "#b18d89",
            "#b08a71"
        ]
    },
    {
        "name": "Rune Shield ",
        "image": "Shields/Rune Shield .png",
        "primaryColor": "#8c6530",
        "secondaryColors": [
            "#6b4e25",
            "#684e27"
        ]
    },
    {
        "name": "Soldier'S Shield",
        "image": "Shields/Soldier's Shield.png",
        "primaryColor": "#9e988f",
        "secondaryColors": [
            "#5c5751",
            "#47423b"
        ]
    },
    {
        "name": "Spiked Shield",
        "image": "Shields/Spiked Shield.png",
        "primaryColor": "#a8a397",
        "secondaryColors": [
            "#585650",
            "#47423a"
        ]
    },
    {
        "name": "Steel Shield",
        "image": "Shields/Steel Shield.png",
        "primaryColor": "#a39a90",
        "secondaryColors": [
            "#5f574f",
            "#4c423b"
        ]
    },
    {
        "name": "Tower Shield",
        "image": "Shields/Tower Shield.png",
        "primaryColor": "#a29a91",
        "secondaryColors": [
            "#877658",
            "#5a554e"
        ]
    },
    {
        "name": "Wooden Shield Small",
        "image": "Shields/Wooden Shield Small.png",
        "primaryColor": "#867164",
        "secondaryColors": [
            "#615750",
            "#534338"
        ]
    },
    {
        "name": "Babys Nail",
        "image": "Weapons/Babys Nail.png",
        "primaryColor": "#655041",
        "secondaryColors": [
            "#624634",
            "#4c3222"
        ]
    },
    {
        "name": "Bastard Sword",
        "image": "Weapons/Bastard Sword.png",
        "primaryColor": "#91888c",
        "secondaryColors": [
            "#564f51",
            "#433e40"
        ]
    },
    {
        "name": "Battle Axe",
        "image": "Weapons/Battle Axe.png",
        "primaryColor": "#645e5c",
        "secondaryColors": [
            "#615a57",
            "#674633"
        ]
    },
    {
        "name": "Blind",
        "image": "Weapons/Blind.png",
        "primaryColor": "#4e524f",
        "secondaryColors": [
            "#42423d",
            "#3e4241"
        ]
    },
    {
        "name": "Blueblood Sword",
        "image": "Weapons/Blueblood Sword.png",
        "primaryColor": "#504b46",
        "secondaryColors": [
            "#4c4a47",
            "#47423d"
        ]
    },
    {
        "name": "Bramd",
        "image": "Weapons/Bramd.png",
        "primaryColor": "#625d52",
        "secondaryColors": [
            "#615747",
            "#5a4b35"
        ]
    },
    {
        "name": "Broadsword",
        "image": "Weapons/Broadsword.png",
        "primaryColor": "#575455",
        "secondaryColors": [
            "#504e4c",
            "#3c3c41"
        ]
    },
    {
        "name": "Broken Sword",
        "image": "Weapons/Broken Sword.png",
        "primaryColor": "#5c5048",
        "secondaryColors": [
            "#52443b",
            "#463730"
        ]
    },
    {
        "name": "Claws",
        "image": "Weapons/Claws.png",
        "primaryColor": "#a39b8f",
        "secondaryColors": [
            "#5f5850",
            "#49433b"
        ]
    },
    {
        "name": "Claymore",
        "image": "Weapons/Claymore.png",
        "primaryColor": "#a39e9b",
        "secondaryColors": [
            "#565454",
            "#5f4b2f"
        ]
    },
    {
        "name": "Club",
        "image": "Weapons/Club.png",
        "primaryColor": "#5e482d",
        "secondaryColors": [
            "#483621",
            "#312616"
        ]
    },
    {
        "name": "Compound Long Bow",
        "image": "Weapons/Compound Long Bow.png",
        "primaryColor": "#694324",
        "secondaryColors": [
            "#503018",
            "#4d3019"
        ]
    },
    {
        "name": "Compound Short Bow",
        "image": "Weapons/Compound Short Bow.png",
        "primaryColor": "#63472e",
        "secondaryColors": [
            "#4a321d",
            "#433024"
        ]
    },
    {
        "name": "Crescent Axe",
        "image": "Weapons/Crescent Axe.png",
        "primaryColor": "#98928a",
        "secondaryColors": [
            "#65625d",
            "#635b54"
        ]
    },
    {
        "name": "Dagger",
        "image": "Weapons/Dagger.png",
        "primaryColor": "#9b9693",
        "secondaryColors": [
            "#595351",
            "#684632"
        ]
    },
    {
        "name": "Demonbrandt",
        "image": "Weapons/Demonbrandt.png",
        "primaryColor": "#c4b7a7",
        "secondaryColors": [
            "#b1a28f",
            "#988771"
        ]
    },
    {
        "name": "Dozer Axe",
        "image": "Weapons/Dozer Axe.png",
        "primaryColor": "#4f4948",
        "secondaryColors": [
            "#49403e",
            "#413f40"
        ]
    },
    {
        "name": "Epee Rapier",
        "image": "Weapons/Epee Rapier.png",
        "primaryColor": "#927749",
        "secondaryColors": [
            "#634b2a",
            "#49331c"
        ]
    },
    {
        "name": "Estoc",
        "image": "Weapons/Estoc.png",
        "primaryColor": "#60605c",
        "secondaryColors": [
            "#5e5e5a",
            "#5c5c58"
        ]
    },
    {
        "name": "Flamberge",
        "image": "Weapons/Flamberge.png",
        "primaryColor": "#555351",
        "secondaryColors": [
            "#504e4c",
            "#4d4137"
        ]
    },
    {
        "name": "Gargoyle Crossbow",
        "image": "Weapons/Gargoyle Crossbow.png",
        "primaryColor": "#59524c",
        "secondaryColors": [
            "#57524e",
            "#584336"
        ]
    },
    {
        "name": "Great Axe",
        "image": "Weapons/Great Axe.png",
        "primaryColor": "#625e59",
        "secondaryColors": [
            "#5d5850",
            "#4d4338"
        ]
    },
    {
        "name": "Great Club",
        "image": "Weapons/Great Club.png",
        "primaryColor": "#8f6449",
        "secondaryColors": [
            "#635043",
            "#684935"
        ]
    },
    {
        "name": "Guillotine Axe",
        "image": "Weapons/Guillotine Axe.png",
        "primaryColor": "#5b5650",
        "secondaryColors": [
            "#585652",
            "#49423b"
        ]
    },
    {
        "name": "Heavy Crossbow",
        "image": "Weapons/Heavy Crossbow.png",
        "primaryColor": "#625a4f",
        "secondaryColors": [
            "#554735",
            "#463729"
        ]
    },
    {
        "name": "Hiltless",
        "image": "Weapons/Hiltless.png",
        "primaryColor": "#655e5c",
        "secondaryColors": [
            "#5c5956",
            "#644a37"
        ]
    },
    {
        "name": "Insanity Catalyst",
        "image": "Weapons/Insanity Catalyst.png",
        "primaryColor": "#94642b",
        "secondaryColors": [
            "#6c614e",
            "#644a29"
        ]
    },
    {
        "name": "Iron Knuckles",
        "image": "Weapons/Iron Knuckles.png",
        "primaryColor": "#58524f",
        "secondaryColors": [
            "#554337",
            "#48352a"
        ]
    },
    {
        "name": "Istarelle",
        "image": "Weapons/Istarelle.png",
        "primaryColor": "#e8e5dd",
        "secondaryColors": [
            "#5f5b55",
            "#504231"
        ]
    },
    {
        "name": "Kilij",
        "image": "Weapons/Kilij.png",
        "primaryColor": "#73634c",
        "secondaryColors": [
            "#6a5b46",
            "#564738"
        ]
    },
    {
        "name": "Kris Blade",
        "image": "Weapons/Kris Blade.png",
        "primaryColor": "#585957",
        "secondaryColors": [
            "#494a49",
            "#534137"
        ]
    },
    {
        "name": "Lava Bow",
        "image": "Weapons/Lava Bow.png",
        "primaryColor": "#585049",
        "secondaryColors": [
            "#413831",
            "#0000ff"
        ]
    },
    {
        "name": "Light Crossbow",
        "image": "Weapons/Light Crossbow.png",
        "primaryColor": "#886d4f",
        "secondaryColors": [
            "#6c5c4a",
            "#5d4933"
        ]
    },
    {
        "name": "Long Bow",
        "image": "Weapons/Long Bow.png",
        "primaryColor": "#86532f",
        "secondaryColors": [
            "#744c2f",
            "#744829"
        ]
    },
    {
        "name": "Long Sword",
        "image": "Weapons/Long Sword.png",
        "primaryColor": "#979695",
        "secondaryColors": [
            "#5b5753",
            "#4c4339"
        ]
    },
    {
        "name": "Mace",
        "image": "Weapons/Mace.png",
        "primaryColor": "#5b504b",
        "secondaryColors": [
            "#4d413c",
            "#49413d"
        ]
    },
    {
        "name": "Magic Sword Makoto",
        "image": "Weapons/Magic Sword Makoto.png",
        "primaryColor": "#8a7865",
        "secondaryColors": [
            "#61574d",
            "#5d544b"
        ]
    },
    {
        "name": "Mail Breaker",
        "image": "Weapons/Mail Breaker.png",
        "primaryColor": "#9b9494",
        "secondaryColors": [
            "#5d5657",
            "#5a5556"
        ]
    },
    {
        "name": "Meat Cleaver",
        "image": "Weapons/Meat Cleaver.png",
        "primaryColor": "#514b47",
        "secondaryColors": [
            "#49413d",
            "#433732"
        ]
    },
    {
        "name": "Mirdan Hammer3",
        "image": "Weapons/Mirdan Hammer3.png",
        "primaryColor": "#55524e",
        "secondaryColors": [
            "#52504c",
            "#42413b"
        ]
    },
    {
        "name": "Morning Star",
        "image": "Weapons/Morning Star.png",
        "primaryColor": "#55524e",
        "secondaryColors": [
            "#55514c",
            "#4d423b"
        ]
    },
    {
        "name": "Northern Regalia",
        "image": "Weapons/Northern Regalia.png",
        "primaryColor": "#c8b299",
        "secondaryColors": [
            "#b09d88",
            "#9c8b77"
        ]
    },
    {
        "name": "Penetrating Word",
        "image": "Weapons/Penetrating Word.png",
        "primaryColor": "#989696",
        "secondaryColors": [
            "#535050",
            "#515050"
        ]
    },
    {
        "name": "Phosporescent Pole",
        "image": "Weapons/Phosporescent Pole.png",
        "primaryColor": "#5a5b4f",
        "secondaryColors": [
            "#584a33",
            "#45392a"
        ]
    },
    {
        "name": "Pickaxe",
        "image": "Weapons/Pickaxe.png",
        "primaryColor": "#006a6a",
        "secondaryColors": [
            "#4c4643",
            "#4e4239"
        ]
    },
    {
        "name": "Rapier",
        "image": "Weapons/Rapier.png",
        "primaryColor": "#625a54",
        "secondaryColors": [
            "#615a55",
            "#514439"
        ]
    },
    {
        "name": "Reaper'S Scythe",
        "image": "Weapons/Reaper's Scythe.png",
        "primaryColor": "#a3895e",
        "secondaryColors": [
            "#8d744d",
            "#6b4e31"
        ]
    },
    {
        "name": "Ritual Blade",
        "image": "Weapons/Ritual Blade.png",
        "primaryColor": "#5f5b52",
        "secondaryColors": [
            "#58554c",
            "#59482f"
        ]
    },
    {
        "name": "Rune Sword",
        "image": "Weapons/Rune Sword.png",
        "primaryColor": "#684a1e",
        "secondaryColors": [
            "#4a3314",
            "#4d3211"
        ]
    },
    {
        "name": "Scimitar 1",
        "image": "Weapons/Scimitar 1.png",
        "primaryColor": "#938d8e",
        "secondaryColors": [
            "#635f61",
            "#645d5f"
        ]
    },
    {
        "name": "Scrapping Spear",
        "image": "Weapons/Scrapping Spear.png",
        "primaryColor": "#565655",
        "secondaryColors": [
            "#5c544e",
            "#514438"
        ]
    },
    {
        "name": "Short Bow",
        "image": "Weapons/Short Bow.png",
        "primaryColor": "#684b30",
        "secondaryColors": [
            "#493723",
            "#4e341e"
        ]
    },
    {
        "name": "Short Spear",
        "image": "Weapons/Short Spear.png",
        "primaryColor": "#58574e",
        "secondaryColors": [
            "#53524b",
            "#44433c"
        ]
    },
    {
        "name": "Short Sword",
        "image": "Weapons/Short Sword.png",
        "primaryColor": "#565554",
        "secondaryColors": [
            "#524e4d",
            "#5e443b"
        ]
    },
    {
        "name": "Shotel",
        "image": "Weapons/Shotel.png",
        "primaryColor": "#615955",
        "secondaryColors": [
            "#5d5956",
            "#564436"
        ]
    },
    {
        "name": "Silver Catalyst",
        "image": "Weapons/Silver Catalyst.png",
        "primaryColor": "#86786d",
        "secondaryColors": [
            "#62564f",
            "#4e433d"
        ]
    },
    {
        "name": "Spiral Rapier",
        "image": "Weapons/Spiral Rapier.png",
        "primaryColor": "#504f4d",
        "secondaryColors": [
            "#4c4b4b",
            "#45413b"
        ]
    },
    {
        "name": "Storm Ruler",
        "image": "Weapons/Storm Ruler.png",
        "primaryColor": "#867261",
        "secondaryColors": [
            "#59534b",
            "#4d443a"
        ]
    },
    {
        "name": "Uchigatana",
        "image": "Weapons/Uchigatana.png",
        "primaryColor": "#d1cfcf",
        "secondaryColors": [
            "#9b9998",
            "#5a5754"
        ]
    },
    {
        "name": "War Pick",
        "image": "Weapons/War Pick.png",
        "primaryColor": "#5a5753",
        "secondaryColors": [
            "#504c49",
            "#46413e"
        ]
    },
    {
        "name": "War Scythe",
        "image": "Weapons/War Scythe.png",
        "primaryColor": "#494646",
        "secondaryColors": [
            "#474744",
            "#464544"
        ]
    },
    {
        "name": "Winged Spear",
        "image": "Weapons/Winged Spear.png",
        "primaryColor": "#5b5652",
        "secondaryColors": [
            "#56442c",
            "#46321b"
        ]
    },
    {
        "name": "Wooden Catalyst",
        "image": "Weapons/Wooden Catalyst.png",
        "primaryColor": "#69442b",
        "secondaryColors": [
            "#51311b",
            "#4f301b"
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