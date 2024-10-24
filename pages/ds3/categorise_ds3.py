import json

# Your JSON data as a list of dictionaries
data = [
    {
        "name": "Alva Armor",
        "image": "Chest/Alva Armor.png",
        "primaryColor": "#949697",
        "secondaryColors": [
            "#615552",
            "#52453a"
        ]
    },
    {
        "name": "Antiquated Dress",
        "image": "Chest/Antiquated Dress.png",
        "primaryColor": "#e8e7de",
        "secondaryColors": [
            "#d0cab5",
            "#aca99c"
        ]
    },
    {
        "name": "Antiquated Plain Garb",
        "image": "Chest/Antiquated Plain Garb.png",
        "primaryColor": "#a7a29d",
        "secondaryColors": [
            "#605c5b",
            "#4b463a"
        ]
    },
    {
        "name": "Archdeacon Holy Garb",
        "image": "Chest/Archdeacon Holy Garb.png",
        "primaryColor": "#a98f62",
        "secondaryColors": [
            "#8e7350",
            "#735f48"
        ]
    },
    {
        "name": "Armor Of The Sun",
        "image": "Chest/Armor Of The Sun.png",
        "primaryColor": "#b19f8a",
        "secondaryColors": [
            "#9c8a74",
            "#8c7361"
        ]
    },
    {
        "name": "Armor Of Thorns",
        "image": "Chest/Armor Of Thorns.png",
        "primaryColor": "#98959a",
        "secondaryColors": [
            "#585356",
            "#4e423a"
        ]
    },
    {
        "name": "Assassin Armor",
        "image": "Chest/Assassin Armor.png",
        "primaryColor": "#5b5651",
        "secondaryColors": [
            "#5c554d",
            "#4b443b"
        ]
    },
    {
        "name": "Black Dress",
        "image": "Chest/Black Dress.png",
        "primaryColor": "#5c5b5d",
        "secondaryColors": [
            "#4c4d4d",
            "#40413e"
        ]
    },
    {
        "name": "Black Hand Armor",
        "image": "Chest/Black Hand Armor.png",
        "primaryColor": "#5a534a",
        "secondaryColors": [
            "#524e48",
            "#4b443b"
        ]
    },
    {
        "name": "Black Iron Armor",
        "image": "Chest/Black Iron Armor.png",
        "primaryColor": "#95979a",
        "secondaryColors": [
            "#595450",
            "#4d433c"
        ]
    },
    {
        "name": "Black Knight Armor",
        "image": "Chest/Black Knight Armor.png",
        "primaryColor": "#94908e",
        "secondaryColors": [
            "#595654",
            "#44413d"
        ]
    },
    {
        "name": "Black Leather Armor",
        "image": "Chest/Black Leather Armor.png",
        "primaryColor": "#8d7053",
        "secondaryColors": [
            "#5c534c",
            "#52463a"
        ]
    },
    {
        "name": "Black Witch Garb",
        "image": "Chest/Black Witch Garb.png",
        "primaryColor": "#6d7389",
        "secondaryColors": [
            "#4c4a5c",
            "#433c4c"
        ]
    },
    {
        "name": "Brass Armor",
        "image": "Chest/Brass Armor.png",
        "primaryColor": "#8c704c",
        "secondaryColors": [
            "#58544e",
            "#5d4a33"
        ]
    },
    {
        "name": "Brigand Armor",
        "image": "Chest/Brigand Armor.png",
        "primaryColor": "#a69871",
        "secondaryColors": [
            "#625348",
            "#554639"
        ]
    },
    {
        "name": "Catarina Armor",
        "image": "Chest/Catarina Armor.png",
        "primaryColor": "#cfc7b3",
        "secondaryColors": [
            "#aba390",
            "#948975"
        ]
    },
    {
        "name": "Cathedral Knight Armor",
        "image": "Chest/Cathedral Knight Armor.png",
        "primaryColor": "#9f9c97",
        "secondaryColors": [
            "#8a6b5e",
            "#655751"
        ]
    },
    {
        "name": "Chain Armor",
        "image": "Chest/Chain Armor.png",
        "primaryColor": "#55534f",
        "secondaryColors": [
            "#514f4b",
            "#45413d"
        ]
    },
    {
        "name": "Clandestine Coat",
        "image": "Chest/Clandestine Coat.png",
        "primaryColor": "#8f8c8c",
        "secondaryColors": [
            "#5d5851",
            "#49443b"
        ]
    },
    {
        "name": "Cleric Blue Robe",
        "image": "Chest/Cleric Blue Robe.png",
        "primaryColor": "#9a9c9e",
        "secondaryColors": [
            "#5d6b8e",
            "#52586a"
        ]
    },
    {
        "name": "Conjurator Robe",
        "image": "Chest/Conjurator Robe.png",
        "primaryColor": "#a78a65",
        "secondaryColors": [
            "#907251",
            "#705f4c"
        ]
    },
    {
        "name": "Cornyx's Garb",
        "image": "Chest/Cornyx's Garb.png",
        "primaryColor": "#505255",
        "secondaryColors": [
            "#4d4e4f",
            "#3e4146"
        ]
    },
    {
        "name": "Court Sorcerer Robe",
        "image": "Chest/Court Sorcerer Robe.png",
        "primaryColor": "#c3bab0",
        "secondaryColors": [
            "#a89f96",
            "#8e847b"
        ]
    },
    {
        "name": "Dancer's Armor",
        "image": "Chest/Dancer's Armor.png",
        "primaryColor": "#96989a",
        "secondaryColors": [
            "#595959",
            "#44423b"
        ]
    },
    {
        "name": "Dark Armor",
        "image": "Chest/Dark Armor.png",
        "primaryColor": "#909394",
        "secondaryColors": [
            "#555555",
            "#545555"
        ]
    },
    {
        "name": "Deacon Robe",
        "image": "Chest/Deacon Robe.png",
        "primaryColor": "#aa8b6e",
        "secondaryColors": [
            "#946a58",
            "#745548"
        ]
    },
    {
        "name": "Desert Pyromancer Garb",
        "image": "Chest/Desert Pyromancer Garb.png",
        "primaryColor": "#916f65",
        "secondaryColors": [
            "#65554f",
            "#54433c"
        ]
    },
    {
        "name": "Deserter Armor",
        "image": "Chest/Deserter Armor.png",
        "primaryColor": "#877464",
        "secondaryColors": [
            "#5c5653",
            "#50443b"
        ]
    },
    {
        "name": "Dragonscale Armor",
        "image": "Chest/Dragonscale Armor.png",
        "primaryColor": "#877663",
        "secondaryColors": [
            "#61594f",
            "#4f453a"
        ]
    },
    {
        "name": "Dragonslayer Armor",
        "image": "Chest/Dragonslayer Armor.png",
        "primaryColor": "#a09c8f",
        "secondaryColors": [
            "#5f5a51",
            "#4a443a"
        ]
    },
    {
        "name": "Drakeblood Armor",
        "image": "Chest/Drakeblood Armor.png",
        "primaryColor": "#8e8d90",
        "secondaryColors": [
            "#555253",
            "#4a413d"
        ]
    },
    {
        "name": "Drang Armor",
        "image": "Chest/Drang Armor.png",
        "primaryColor": "#a9a6a0",
        "secondaryColors": [
            "#575756",
            "#42403e"
        ]
    },
    {
        "name": "Eastern Armor",
        "image": "Chest/Eastern Armor.png",
        "primaryColor": "#a28a71",
        "secondaryColors": [
            "#936a59",
            "#6a594c"
        ]
    },
    {
        "name": "Elite Knight Armor",
        "image": "Chest/Elite Knight Armor.png",
        "primaryColor": "#88756a",
        "secondaryColors": [
            "#5d5653",
            "#4c4439"
        ]
    },
    {
        "name": "Embraced Armor Of Favor",
        "image": "Chest/Embraced Armor Of Favor.png",
        "primaryColor": "#8b6f51",
        "secondaryColors": [
            "#725d45",
            "#5f4936"
        ]
    },
    {
        "name": "Evangelist Robe",
        "image": "Chest/Evangelist Robe.png",
        "primaryColor": "#a88e6f",
        "secondaryColors": [
            "#8c6f59",
            "#67564c"
        ]
    },
    {
        "name": "Executioner Armor",
        "image": "Chest/Executioner Armor.png",
        "primaryColor": "#9c9b9f",
        "secondaryColors": [
            "#555355",
            "#524538"
        ]
    },
    {
        "name": "Exile Armor",
        "image": "Chest/Exile Armor.png",
        "primaryColor": "#9c9592",
        "secondaryColors": [
            "#5a5450",
            "#49433b"
        ]
    },
    {
        "name": "Fallen Knight Armor",
        "image": "Chest/Fallen Knight Armor.png",
        "primaryColor": "#56524a",
        "secondaryColors": [
            "#545048",
            "#47433b"
        ]
    },
    {
        "name": "Faraam Armor",
        "image": "Chest/Faraam Armor.png",
        "primaryColor": "#91929c",
        "secondaryColors": [
            "#555655",
            "#37484c"
        ]
    },
    {
        "name": "Fire Keeper Robe",
        "image": "Chest/Fire Keeper Robe.png",
        "primaryColor": "#908779",
        "secondaryColors": [
            "#534f4c",
            "#47413c"
        ]
    },
    {
        "name": "Fire Witch Armor",
        "image": "Chest/Fire Witch Armor.png",
        "primaryColor": "#d0d1d3",
        "secondaryColors": [
            "#9e9d9e",
            "#5c5b5b"
        ]
    },
    {
        "name": "Firelink Armor",
        "image": "Chest/Firelink Armor.png",
        "primaryColor": "#929394",
        "secondaryColors": [
            "#565250",
            "#4d423c"
        ]
    },
    {
        "name": "Follower Armor",
        "image": "Chest/Follower Armor.png",
        "primaryColor": "#9c9d9b",
        "secondaryColors": [
            "#5d5b56",
            "#4f453a"
        ]
    },
    {
        "name": "Grave Warden Robe",
        "image": "Chest/Grave Warden Robe.png",
        "primaryColor": "#9a928c",
        "secondaryColors": [
            "#857874",
            "#675e5b"
        ]
    },
    {
        "name": "Gundyr's Armor",
        "image": "Chest/Gundyr's Armor.png",
        "primaryColor": "#929193",
        "secondaryColors": [
            "#5b5858",
            "#49433a"
        ]
    },
    {
        "name": "Harald Legion Armor",
        "image": "Chest/Harald Legion Armor.png",
        "primaryColor": "#4d4c49",
        "secondaryColors": [
            "#45423d",
            "#3e403d"
        ]
    },
    {
        "name": "Hard Leather Armor",
        "image": "Chest/Hard Leather Armor.png",
        "primaryColor": "#ab8a6b",
        "secondaryColors": [
            "#996e52",
            "#605751"
        ]
    },
    {
        "name": "Havel's Armor",
        "image": "Chest/Havel's Armor.png",
        "primaryColor": "#9b9794",
        "secondaryColors": [
            "#86817d",
            "#827c78"
        ]
    },
    {
        "name": "Herald Armor",
        "image": "Chest/Herald Armor.png",
        "primaryColor": "#979696",
        "secondaryColors": [
            "#5b5858",
            "#595859"
        ]
    },
    {
        "name": "Iron Dragonslayer Armor",
        "image": "Chest/Iron Dragonslayer Armor.png",
        "primaryColor": "#8c8e8f",
        "secondaryColors": [
            "#5e5f5e",
            "#535553"
        ]
    },
    {
        "name": "Jailer Robe",
        "image": "Chest/Jailer Robe.png",
        "primaryColor": "#83796f",
        "secondaryColors": [
            "#58524d",
            "#49443c"
        ]
    },
    {
        "name": "Karla's Coat",
        "image": "Chest/Karla's Coat.png",
        "primaryColor": "#5e5b55",
        "secondaryColors": [
            "#56514d",
            "#47423d"
        ]
    },
    {
        "name": "Knight Armor",
        "image": "Chest/Knight Armor.png",
        "primaryColor": "#97989b",
        "secondaryColors": [
            "#545250",
            "#49423b"
        ]
    },
    {
        "name": "Lapp's Armor",
        "image": "Chest/Lapp's Armor.png",
        "primaryColor": "#86786a",
        "secondaryColors": [
            "#60554e",
            "#4f433a"
        ]
    },
    {
        "name": "Leather Armor",
        "image": "Chest/Leather Armor.png",
        "primaryColor": "#9f8c73",
        "secondaryColors": [
            "#877662",
            "#665a4f"
        ]
    },
    {
        "name": "Leonhard's Garb",
        "image": "Chest/Leonhard's Garb.png",
        "primaryColor": "#979595",
        "secondaryColors": [
            "#5e5750",
            "#4d433b"
        ]
    },
    {
        "name": "Lorian's Armor",
        "image": "Chest/Lorian's Armor.png",
        "primaryColor": "#a19c90",
        "secondaryColors": [
            "#58544f",
            "#48423c"
        ]
    },
    {
        "name": "Lothric Knight Armor",
        "image": "Chest/Lothric Knight Armor.png",
        "primaryColor": "#8a6a63",
        "secondaryColors": [
            "#615250",
            "#59423c"
        ]
    },
    {
        "name": "Maiden Robe",
        "image": "Chest/Maiden Robe.png",
        "primaryColor": "#f7efda",
        "secondaryColors": [
            "#e2d2af",
            "#ccb393"
        ]
    },
    {
        "name": "Master's Attire",
        "image": "Chest/Master's Attire.png",
        "primaryColor": "#62594a",
        "secondaryColors": [
            "#514837",
            "#514737"
        ]
    },
    {
        "name": "Millwood Knight Armor",
        "image": "Chest/Millwood Knight Armor.png",
        "primaryColor": "#56534d",
        "secondaryColors": [
            "#48433c",
            "#3e403d"
        ]
    },
    {
        "name": "Mirrah Chain Mail",
        "image": "Chest/Mirrah Chain Mail.png",
        "primaryColor": "#51514e",
        "secondaryColors": [
            "#46423c",
            "#413d38"
        ]
    },
    {
        "name": "Mirrah Vest",
        "image": "Chest/Mirrah Vest.png",
        "primaryColor": "#e6e0d8",
        "secondaryColors": [
            "#a8a096",
            "#555352"
        ]
    },
    {
        "name": "Morne's Armor",
        "image": "Chest/Morne's Armor.png",
        "primaryColor": "#555250",
        "secondaryColors": [
            "#514539",
            "#453a31"
        ]
    },
    {
        "name": "Nameless Knight Armor",
        "image": "Chest/Nameless Knight Armor.png",
        "primaryColor": "#979393",
        "secondaryColors": [
            "#8a7264",
            "#5c5653"
        ]
    },
    {
        "name": "Northern Armor",
        "image": "Chest/Northern Armor.png",
        "primaryColor": "#857169",
        "secondaryColors": [
            "#595451",
            "#4c423c"
        ]
    },
    {
        "name": "Old Sorcerer Coat",
        "image": "Chest/Old Sorcerer Coat.png",
        "primaryColor": "#89684f",
        "secondaryColors": [
            "#675547",
            "#594737"
        ]
    },
    {
        "name": "Ordained Dress",
        "image": "Chest/Ordained Dress.png",
        "primaryColor": "#9b9b90",
        "secondaryColors": [
            "#85867a",
            "#64645b"
        ]
    },
    {
        "name": "Outrider Knight Armor",
        "image": "Chest/Outrider Knight Armor.png",
        "primaryColor": "#8f9aad",
        "secondaryColors": [
            "#687389",
            "#505664"
        ]
    },
    {
        "name": "Painting Guardian Gown",
        "image": "Chest/Painting Guardian Gown.png",
        "primaryColor": "#e3dcd2",
        "secondaryColors": [
            "#cfc6b9",
            "#c5bbae"
        ]
    },
    {
        "name": "Pale Shade Robe",
        "image": "Chest/Pale Shade Robe.png",
        "primaryColor": "#cecdcc",
        "secondaryColors": [
            "#c4c1bc",
            "#c1bdb9"
        ]
    },
    {
        "name": "Pontiff Knight Armor",
        "image": "Chest/Pontiff Knight Armor.png",
        "primaryColor": "#929a9b",
        "secondaryColors": [
            "#79868d",
            "#5c5e5e"
        ]
    },
    {
        "name": "Pyromancer Garb",
        "image": "Chest/Pyromancer Garb.png",
        "primaryColor": "#a29f92",
        "secondaryColors": [
            "#8e8778",
            "#86756a"
        ]
    },
    {
        "name": "Ringed Knight Armor",
        "image": "Chest/Ringed Knight Armor.png",
        "primaryColor": "#504e4e",
        "secondaryColors": [
            "#594639",
            "#3d4143"
        ]
    },
    {
        "name": "Robe Of Prayer",
        "image": "Chest/Robe Of Prayer.png",
        "primaryColor": "#554f4d",
        "secondaryColors": [
            "#4b443b",
            "#423d42"
        ]
    },
    {
        "name": "Ruin Armor",
        "image": "Chest/Ruin Armor.png",
        "primaryColor": "#857863",
        "secondaryColors": [
            "#61584b",
            "#4d4439"
        ]
    },
    {
        "name": "Scholar's Robe",
        "image": "Chest/Scholar's Robe.png",
        "primaryColor": "#f3e9d9",
        "secondaryColors": [
            "#a48973",
            "#946a60"
        ]
    },
    {
        "name": "Sellsword Armor",
        "image": "Chest/Sellsword Armor.png",
        "primaryColor": "#88755e",
        "secondaryColors": [
            "#60554d",
            "#55443a"
        ]
    },
    {
        "name": "Shadow Garb",
        "image": "Chest/Shadow Garb.png",
        "primaryColor": "#887064",
        "secondaryColors": [
            "#57514f",
            "#49433a"
        ]
    },
    {
        "name": "Shira's Armor",
        "image": "Chest/Shira's Armor.png",
        "primaryColor": "#a59c91",
        "secondaryColors": [
            "#918970",
            "#656051"
        ]
    },
    {
        "name": "Silver Knight Armor",
        "image": "Chest/Silver Knight Armor.png",
        "primaryColor": "#9c9b97",
        "secondaryColors": [
            "#5b5956",
            "#48423b"
        ]
    },
    {
        "name": "Slave Knight Armor",
        "image": "Chest/Slave Knight Armor.png",
        "primaryColor": "#865450",
        "secondaryColors": [
            "#645048",
            "#50443b"
        ]
    },
    {
        "name": "Smough's Armor",
        "image": "Chest/Smough's Armor.png",
        "primaryColor": "#9f9d8f",
        "secondaryColors": [
            "#615a50",
            "#4c443a"
        ]
    },
    {
        "name": "Sorcerer Robe",
        "image": "Chest/Sorcerer Robe.png",
        "primaryColor": "#8f928f",
        "secondaryColors": [
            "#83837b",
            "#646462"
        ]
    },
    {
        "name": "Sunless Armor",
        "image": "Chest/Sunless Armor.png",
        "primaryColor": "#c8c6c6",
        "secondaryColors": [
            "#9a999a",
            "#5b5b5e"
        ]
    },
    {
        "name": "Sunset Armor",
        "image": "Chest/Sunset Armor.png",
        "primaryColor": "#5d564e",
        "secondaryColors": [
            "#5c534a",
            "#4e4539"
        ]
    },
    {
        "name": "Undead Legion Armor",
        "image": "Chest/Undead Legion Armor.png",
        "primaryColor": "#595253",
        "secondaryColors": [
            "#48423c",
            "#473d41"
        ]
    },
    {
        "name": "Vilhelm's Armor",
        "image": "Chest/Vilhelm's Armor.png",
        "primaryColor": "#50524c",
        "secondaryColors": [
            "#464438",
            "#3e413a"
        ]
    },
    {
        "name": "Winged Knight Armor",
        "image": "Chest/Winged Knight Armor.png",
        "primaryColor": "#9b9999",
        "secondaryColors": [
            "#56555d",
            "#423c36"
        ]
    },
    {
        "name": "Wolf Knight Armor",
        "image": "Chest/Wolf Knight Armor.png",
        "primaryColor": "#95979c",
        "secondaryColors": [
            "#64748a",
            "#55565a"
        ]
    },
    {
        "name": "Worker Garb",
        "image": "Chest/Worker Garb.png",
        "primaryColor": "#938974",
        "secondaryColors": [
            "#53504b",
            "#48433a"
        ]
    },
    {
        "name": "Xanthous Overcoat",
        "image": "Chest/Xanthous Overcoat.png",
        "primaryColor": "#a89268",
        "secondaryColors": [
            "#8b7453",
            "#6d5d49"
        ]
    },
    {
        "name": "Alva Gauntlets",
        "image": "Hands/Alva Gauntlets.png",
        "primaryColor": "#989da0",
        "secondaryColors": [
            "#5f5957",
            "#4b443a"
        ]
    },
    {
        "name": "Antiquated Gloves",
        "image": "Hands/Antiquated Gloves.png",
        "primaryColor": "#d4d4d4",
        "secondaryColors": [
            "#a6a6a6",
            "#a1a1a2"
        ]
    },
    {
        "name": "Assassin Gloves",
        "image": "Hands/Assassin Gloves.png",
        "primaryColor": "#867465",
        "secondaryColors": [
            "#62564e",
            "#4d443b"
        ]
    },
    {
        "name": "Black Gauntlets",
        "image": "Hands/Black Gauntlets.png",
        "primaryColor": "#999c9b",
        "secondaryColors": [
            "#545657",
            "#3e4042"
        ]
    },
    {
        "name": "Black Iron Gauntlets",
        "image": "Hands/Black Iron Gauntlets.png",
        "primaryColor": "#dbddde",
        "secondaryColors": [
            "#9b9ea1",
            "#585a59"
        ]
    },
    {
        "name": "Black Knight Gauntlets",
        "image": "Hands/Black Knight Gauntlets.png",
        "primaryColor": "#999593",
        "secondaryColors": [
            "#585452",
            "#47423c"
        ]
    },
    {
        "name": "Black Leather Gloves",
        "image": "Hands/Black Leather Gloves.png",
        "primaryColor": "#959293",
        "secondaryColors": [
            "#656464",
            "#605d5d"
        ]
    },
    {
        "name": "Black Witch Wrappings",
        "image": "Hands/Black Witch Wrappings.png",
        "primaryColor": "#504a58",
        "secondaryColors": [
            "#433c4c",
            "#423b3d"
        ]
    },
    {
        "name": "Brass Gauntlets",
        "image": "Hands/Brass Gauntlets.png",
        "primaryColor": "#ab8f65",
        "secondaryColors": [
            "#8e704c",
            "#6f5b45"
        ]
    },
    {
        "name": "Brigand Gauntlets",
        "image": "Hands/Brigand Gauntlets.png",
        "primaryColor": "#a18a6b",
        "secondaryColors": [
            "#8c7358",
            "#675b4d"
        ]
    },
    {
        "name": "Catarina Gauntlets",
        "image": "Hands/Catarina Gauntlets.png",
        "primaryColor": "#dedbd5",
        "secondaryColors": [
            "#cec6b4",
            "#a9a294"
        ]
    },
    {
        "name": "Cathedral Knight Gauntlets",
        "image": "Hands/Cathedral Knight Gauntlets.png",
        "primaryColor": "#dbdadb",
        "secondaryColors": [
            "#a09b9c",
            "#655d5a"
        ]
    },
    {
        "name": "Cleric Gloves",
        "image": "Hands/Cleric Gloves.png",
        "primaryColor": "#a29795",
        "secondaryColors": [
            "#978571",
            "#87796a"
        ]
    },
    {
        "name": "Conjurator Manchettes",
        "image": "Hands/Conjurator Manchettes.png",
        "primaryColor": "#a28a71",
        "secondaryColors": [
            "#8f745d",
            "#9d522e"
        ]
    },
    {
        "name": "Cornyx's Wrap",
        "image": "Hands/Cornyx's Wrap.png",
        "primaryColor": "#8a8784",
        "secondaryColors": [
            "#676663",
            "#63615f"
        ]
    },
    {
        "name": "Court Sorcerer Gloves",
        "image": "Hands/Court Sorcerer Gloves.png",
        "primaryColor": "#dad3cb",
        "secondaryColors": [
            "#ccc4ba",
            "#c4bab0"
        ]
    },
    {
        "name": "Dancer's Gauntlets",
        "image": "Hands/Dancer's Gauntlets.png",
        "primaryColor": "#d3d5d7",
        "secondaryColors": [
            "#9a9ca0",
            "#5a5b5d"
        ]
    },
    {
        "name": "Dark Gauntlets",
        "image": "Hands/Dark Gauntlets.png",
        "primaryColor": "#93979a",
        "secondaryColors": [
            "#7d8185",
            "#5d5f61"
        ]
    },
    {
        "name": "Desert Pyromancer Gloves",
        "image": "Hands/Desert Pyromancer Gloves.png",
        "primaryColor": "#8f938f",
        "secondaryColors": [
            "#5a5956",
            "#43413e"
        ]
    },
    {
        "name": "Dragonslayer Gauntlets",
        "image": "Hands/Dragonslayer Gauntlets.png",
        "primaryColor": "#a7a495",
        "secondaryColors": [
            "#5c5a52",
            "#494439"
        ]
    },
    {
        "name": "Drakeblood Gauntlets",
        "image": "Hands/Drakeblood Gauntlets.png",
        "primaryColor": "#d6d6d7",
        "secondaryColors": [
            "#9c9c9e",
            "#5a5759"
        ]
    },
    {
        "name": "Drang Gauntlets",
        "image": "Hands/Drang Gauntlets.png",
        "primaryColor": "#51504f",
        "secondaryColors": [
            "#4d4c49",
            "#41403d"
        ]
    },
    {
        "name": "Eastern Gauntlets",
        "image": "Hands/Eastern Gauntlets.png",
        "primaryColor": "#a2a095",
        "secondaryColors": [
            "#5e5b52",
            "#46443b"
        ]
    },
    {
        "name": "Elite Knight Gauntlets",
        "image": "Hands/Elite Knight Gauntlets.png",
        "primaryColor": "#a38875",
        "secondaryColors": [
            "#8b7366",
            "#6c5a55"
        ]
    },
    {
        "name": "Evangelist Gloves",
        "image": "Hands/Evangelist Gloves.png",
        "primaryColor": "#d08d61",
        "secondaryColors": [
            "#aa6e4e",
            "#975936"
        ]
    },
    {
        "name": "Executioner Gauntlets",
        "image": "Hands/Executioner Gauntlets.png",
        "primaryColor": "#dbdadc",
        "secondaryColors": [
            "#9b9b9e",
            "#59585b"
        ]
    },
    {
        "name": "Exile Gauntlets",
        "image": "Hands/Exile Gauntlets.png",
        "primaryColor": "#cfd0cd",
        "secondaryColors": [
            "#999a97",
            "#5d5e5c"
        ]
    },
    {
        "name": "Fallen Knight Gauntlets",
        "image": "Hands/Fallen Knight Gauntlets.png",
        "primaryColor": "#969688",
        "secondaryColors": [
            "#5d5851",
            "#4c433b"
        ]
    },
    {
        "name": "Faraam Gauntlets",
        "image": "Hands/Faraam Gauntlets.png",
        "primaryColor": "#dcdee0",
        "secondaryColors": [
            "#9a9da1",
            "#57575a"
        ]
    },
    {
        "name": "Fire Keeper Gloves",
        "image": "Hands/Fire Keeper Gloves.png",
        "primaryColor": "#695146",
        "secondaryColors": [
            "#584438",
            "#4d372e"
        ]
    },
    {
        "name": "Fire Witch Gauntlets",
        "image": "Hands/Fire Witch Gauntlets.png",
        "primaryColor": "#9ea1a4",
        "secondaryColors": [
            "#5c5c5b",
            "#4b4537"
        ]
    },
    {
        "name": "Firelink Gauntlets",
        "image": "Hands/Firelink Gauntlets.png",
        "primaryColor": "#95979a",
        "secondaryColors": [
            "#605b5a",
            "#4f433b"
        ]
    },
    {
        "name": "Follower Gloves",
        "image": "Hands/Follower Gloves.png",
        "primaryColor": "#5e5149",
        "secondaryColors": [
            "#58453a",
            "#583028"
        ]
    },
    {
        "name": "Gauntlets of Favor",
        "image": "Hands/Gauntlets of Favor.png",
        "primaryColor": "#a2906a",
        "secondaryColors": [
            "#8a7054",
            "#715f48"
        ]
    },
    {
        "name": "Gauntlets of Thorns",
        "image": "Hands/Gauntlets of Thorns.png",
        "primaryColor": "#9f989b",
        "secondaryColors": [
            "#5f5859",
            "#443a33"
        ]
    },
    {
        "name": "Golden Bracelets",
        "image": "Hands/Golden Bracelets.png",
        "primaryColor": "#a89c8d",
        "secondaryColors": [
            "#978776",
            "#857768"
        ]
    },
    {
        "name": "Grave Warden Wrap",
        "image": "Hands/Grave Warden Wrap.png",
        "primaryColor": "#9a958e",
        "secondaryColors": [
            "#847973",
            "#665c57"
        ]
    },
    {
        "name": "Gundyr's Gauntlets",
        "image": "Hands/Gundyr's Gauntlets.png",
        "primaryColor": "#ceced0",
        "secondaryColors": [
            "#989698",
            "#605a5a"
        ]
    },
    {
        "name": "Harald Legion Gauntlets",
        "image": "Hands/Harald Legion Gauntlets.png",
        "primaryColor": "#88746a",
        "secondaryColors": [
            "#6b5950",
            "#54433b"
        ]
    },
    {
        "name": "Hard Leather Gauntlets",
        "image": "Hands/Hard Leather Gauntlets.png",
        "primaryColor": "#d3ac94",
        "secondaryColors": [
            "#ca9673",
            "#996c54"
        ]
    },
    {
        "name": "Havel's Gauntlets",
        "image": "Hands/Havel's Gauntlets.png",
        "primaryColor": "#d9d7d6",
        "secondaryColors": [
            "#9f9b99",
            "#5d5857"
        ]
    },
    {
        "name": "Herald Gloves",
        "image": "Hands/Herald Gloves.png",
        "primaryColor": "#9f8872",
        "secondaryColors": [
            "#88725e",
            "#6f5d4e"
        ]
    },
    {
        "name": "Iron Bracelets",
        "image": "Hands/Iron Bracelets.png",
        "primaryColor": "#dcd8d1",
        "secondaryColors": [
            "#cac3b9",
            "#aaa396"
        ]
    },
    {
        "name": "Iron Dragonslayer Gauntlets",
        "image": "Hands/Iron Dragonslayer Gauntlets.png",
        "primaryColor": "#949899",
        "secondaryColors": [
            "#595b58",
            "#45443b"
        ]
    },
    {
        "name": "Jailer Gloves",
        "image": "Hands/Jailer Gloves.png",
        "primaryColor": "#86756d",
        "secondaryColors": [
            "#6b5951",
            "#54443b"
        ]
    },
    {
        "name": "Karla's Gloves",
        "image": "Hands/Karla's Gloves.png",
        "primaryColor": "#876b5c",
        "secondaryColors": [
            "#5b544c",
            "#4a433c"
        ]
    },
    {
        "name": "Knight Gauntlets",
        "image": "Hands/Knight Gauntlets.png",
        "primaryColor": "#dedfe1",
        "secondaryColors": [
            "#9a9c9f",
            "#58595c"
        ]
    },
    {
        "name": "Lapp's Gauntlets",
        "image": "Hands/Lapp's Gauntlets.png",
        "primaryColor": "#a99c8f",
        "secondaryColors": [
            "#675c53",
            "#4d433a"
        ]
    },
    {
        "name": "Leather Gauntlets",
        "image": "Hands/Leather Gauntlets.png",
        "primaryColor": "#847871",
        "secondaryColors": [
            "#695d55",
            "#52453b"
        ]
    },
    {
        "name": "Leather Gloves",
        "image": "Hands/Leather Gloves.png",
        "primaryColor": "#97908f",
        "secondaryColors": [
            "#635956",
            "#4c413d"
        ]
    },
    {
        "name": "Leonhard's Gauntlets",
        "image": "Hands/Leonhard's Gauntlets.png",
        "primaryColor": "#ced1d3",
        "secondaryColors": [
            "#9c9da0",
            "#5b595b"
        ]
    },
    {
        "name": "Lorian's Gauntlets",
        "image": "Hands/Lorian's Gauntlets.png",
        "primaryColor": "#8c8478",
        "secondaryColors": [
            "#625d55",
            "#47423c"
        ]
    },
    {
        "name": "Lothric Knight Gauntlets",
        "image": "Hands/Lothric Knight Gauntlets.png",
        "primaryColor": "#9c9ca1",
        "secondaryColors": [
            "#5a575a",
            "#433b38"
        ]
    },
    {
        "name": "Maiden Gloves",
        "image": "Hands/Maiden Gloves.png",
        "primaryColor": "#f4eede",
        "secondaryColors": [
            "#dcceb3",
            "#aea18b"
        ]
    },
    {
        "name": "Master's Gloves",
        "image": "Hands/Master's Gloves.png",
        "primaryColor": "#897165",
        "secondaryColors": [
            "#6c5c54",
            "#53443b"
        ]
    },
    {
        "name": "Millwood Knight Gauntlets",
        "image": "Hands/Millwood Knight Gauntlets.png",
        "primaryColor": "#8f8872",
        "secondaryColors": [
            "#5c584f",
            "#4e4538"
        ]
    },
    {
        "name": "Mirrah Chain Gloves",
        "image": "Hands/Mirrah Chain Gloves.png",
        "primaryColor": "#8d8c8e",
        "secondaryColors": [
            "#88786d",
            "#5d5b5b"
        ]
    },
    {
        "name": "Mirrah Gloves",
        "image": "Hands/Mirrah Gloves.png",
        "primaryColor": "#846e5e",
        "secondaryColors": [
            "#6b594c",
            "#58463a"
        ]
    },
    {
        "name": "Morne's Gauntlets",
        "image": "Hands/Morne's Gauntlets.png",
        "primaryColor": "#949495",
        "secondaryColors": [
            "#575657",
            "#45413c"
        ]
    },
    {
        "name": "Nameless Knight Gauntlets",
        "image": "Hands/Nameless Knight Gauntlets.png",
        "primaryColor": "#897264",
        "secondaryColors": [
            "#635551",
            "#50433c"
        ]
    },
    {
        "name": "Northern Gloves",
        "image": "Hands/Northern Gloves.png",
        "primaryColor": "#877166",
        "secondaryColors": [
            "#6a5b53",
            "#52443b"
        ]
    },
    {
        "name": "Old Sorcerer Gauntlets",
        "image": "Hands/Old Sorcerer Gauntlets.png",
        "primaryColor": "#ae8c69",
        "secondaryColors": [
            "#926d52",
            "#725a4b"
        ]
    },
    {
        "name": "Outrider Knight Gauntlets",
        "image": "Hands/Outrider Knight Gauntlets.png",
        "primaryColor": "#d1d6dd",
        "secondaryColors": [
            "#b2b8c6",
            "#9b9fa7"
        ]
    },
    {
        "name": "Painting Guardian Gloves",
        "image": "Hands/Painting Guardian Gloves.png",
        "primaryColor": "#c7b29d",
        "secondaryColors": [
            "#b59f89",
            "#a18b76"
        ]
    },
    {
        "name": "Pale Shade Gloves",
        "image": "Hands/Pale Shade Gloves.png",
        "primaryColor": "#d0cfca",
        "secondaryColors": [
            "#c4c2bc",
            "#aaa8a2"
        ]
    },
    {
        "name": "Pontiff Knight Gauntlets",
        "image": "Hands/Pontiff Knight Gauntlets.png",
        "primaryColor": "#b6c7d0",
        "secondaryColors": [
            "#939fa6",
            "#7a858c"
        ]
    },
    {
        "name": "Pyromancer Wrap",
        "image": "Hands/Pyromancer Wrap.png",
        "primaryColor": "#6a5c4d",
        "secondaryColors": [
            "#605b50",
            "#5c4738"
        ]
    },
    {
        "name": "Ringed Knight Gauntlets",
        "image": "Hands/Ringed Knight Gauntlets.png",
        "primaryColor": "#575a5b",
        "secondaryColors": [
            "#545757",
            "#525554"
        ]
    },
    {
        "name": "Ruin Gauntlets",
        "image": "Hands/Ruin Gauntlets.png",
        "primaryColor": "#9c8d71",
        "secondaryColors": [
            "#655d4c",
            "#4d4639"
        ]
    },
    {
        "name": "Sellsword Gauntlets",
        "image": "Hands/Sellsword Gauntlets.png",
        "primaryColor": "#847772",
        "secondaryColors": [
            "#615953",
            "#4b433c"
        ]
    },
    {
        "name": "Shadow Gauntlets",
        "image": "Hands/Shadow Gauntlets.png",
        "primaryColor": "#979799",
        "secondaryColors": [
            "#585555",
            "#4e433c"
        ]
    },
    {
        "name": "Shira's Gloves",
        "image": "Hands/Shira's Gloves.png",
        "primaryColor": "#87746a",
        "secondaryColors": [
            "#6a594f",
            "#53453a"
        ]
    },
    {
        "name": "Silver Knight Gauntlets",
        "image": "Hands/Silver Knight Gauntlets.png",
        "primaryColor": "#9e9d9a",
        "secondaryColors": [
            "#585754",
            "#45423c"
        ]
    },
    {
        "name": "Slave Knight Gauntlets",
        "image": "Hands/Slave Knight Gauntlets.png",
        "primaryColor": "#51524e",
        "secondaryColors": [
            "#47443c",
            "#3e4141"
        ]
    },
    {
        "name": "Smough's Gauntlets",
        "image": "Hands/Smough's Gauntlets.png",
        "primaryColor": "#958b6e",
        "secondaryColors": [
            "#5e594e",
            "#4f463a"
        ]
    },
    {
        "name": "Sorcerer Gloves",
        "image": "Hands/Sorcerer Gloves.png",
        "primaryColor": "#9e9c9c",
        "secondaryColors": [
            "#856b6a",
            "#625254"
        ]
    },
    {
        "name": "Sunless Guantlets",
        "image": "Hands/Sunless Guantlets.png",
        "primaryColor": "#cfd1d3",
        "secondaryColors": [
            "#98999b",
            "#615f5f"
        ]
    },
    {
        "name": "Sunset Gauntlets",
        "image": "Hands/Sunset Gauntlets.png",
        "primaryColor": "#af9a8b",
        "secondaryColors": [
            "#9d8776",
            "#8b7163"
        ]
    },
    {
        "name": "Undead Legion Gauntlets",
        "image": "Hands/Undead Legion Gauntlets.png",
        "primaryColor": "#8f8d8b",
        "secondaryColors": [
            "#5d544f",
            "#4c423c"
        ]
    },
    {
        "name": "Vilhelm's Gauntlets",
        "image": "Hands/Vilhelm's Gauntlets.png",
        "primaryColor": "#827c6a",
        "secondaryColors": [
            "#5d5a50",
            "#46433b"
        ]
    },
    {
        "name": "Violet Wrappings",
        "image": "Hands/Violet Wrappings.png",
        "primaryColor": "#6d558f",
        "secondaryColors": [
            "#5d4b6c",
            "#47385a"
        ]
    },
    {
        "name": "Winged Knight Gauntlets",
        "image": "Hands/Winged Knight Gauntlets.png",
        "primaryColor": "#dbdddf",
        "secondaryColors": [
            "#9a9ca0",
            "#5a5a5c"
        ]
    },
    {
        "name": "Wolf Knight Gauntlets",
        "image": "Hands/Wolf Knight Gauntlets.png",
        "primaryColor": "#95979a",
        "secondaryColors": [
            "#555658",
            "#423c3a"
        ]
    },
    {
        "name": "Worker Gloves",
        "image": "Hands/Worker Gloves.png",
        "primaryColor": "#aa9d8b",
        "secondaryColors": [
            "#978976",
            "#887665"
        ]
    },
    {
        "name": "Xanthous Gloves",
        "image": "Hands/Xanthous Gloves.png",
        "primaryColor": "#90837a",
        "secondaryColors": [
            "#85776e",
            "#6a5b54"
        ]
    },
    {
        "name": "Alva Helm",
        "image": "Head/Alva Helm.PNG",
        "primaryColor": "#d8dbdd",
        "secondaryColors": [
            "#9a9795",
            "#5c5957"
        ]
    },
    {
        "name": "Archdeacon White Crown",
        "image": "Head/Archdeacon White Crown.PNG",
        "primaryColor": "#decfa1",
        "secondaryColors": [
            "#c9b68a",
            "#a6926b"
        ]
    },
    {
        "name": "Aristocrat's Mask",
        "image": "Head/Aristocrat's Mask.PNG",
        "primaryColor": "#574f4c",
        "secondaryColors": [
            "#4f423b",
            "#413e40"
        ]
    },
    {
        "name": "Assassin Hood",
        "image": "Head/Assassin Hood.PNG",
        "primaryColor": "#827b76",
        "secondaryColors": [
            "#605c57",
            "#47423d"
        ]
    },
    {
        "name": "Billed Mask",
        "image": "Head/Billed Mask.PNG",
        "primaryColor": "#525251",
        "secondaryColors": [
            "#43413d",
            "#403e3b"
        ]
    },
    {
        "name": "Black Hand Hat",
        "image": "Head/Black Hand Hat.PNG",
        "primaryColor": "#625c57",
        "secondaryColors": [
            "#4d433b",
            "#463c33"
        ]
    },
    {
        "name": "Black Iron Helm",
        "image": "Head/Black Iron Helm.PNG",
        "primaryColor": "#d2d5d7",
        "secondaryColors": [
            "#9a9ea1",
            "#545657"
        ]
    },
    {
        "name": "Black Knight Helm",
        "image": "Head/Black Knight Helm.PNG",
        "primaryColor": "#9e9a98",
        "secondaryColors": [
            "#565351",
            "#46413d"
        ]
    },
    {
        "name": "Black Witch Hat",
        "image": "Head/Black Witch Hat.png",
        "primaryColor": "#504a59",
        "secondaryColors": [
            "#46443c",
            "#423b4d"
        ]
    },
    {
        "name": "Black Witch Veil",
        "image": "Head/Black Witch Veil.png",
        "primaryColor": "#4c4858",
        "secondaryColors": [
            "#46433b",
            "#423c4d"
        ]
    },
    {
        "name": "Blindfold Mask",
        "image": "Head/Blindfold Mask.png",
        "primaryColor": "#8c93b1",
        "secondaryColors": [
            "#6a6e8f",
            "#53566d"
        ]
    },
    {
        "name": "Brass Helm",
        "image": "Head/Brass Helm.PNG",
        "primaryColor": "#937248",
        "secondaryColors": [
            "#60574c",
            "#5b4933"
        ]
    },
    {
        "name": "Brigand Hood",
        "image": "Head/Brigand Hood.PNG",
        "primaryColor": "#89674f",
        "secondaryColors": [
            "#745846",
            "#5f4838"
        ]
    },
    {
        "name": "Catarina Helm",
        "image": "Head/Catarina Helm.PNG",
        "primaryColor": "#dcdbd5",
        "secondaryColors": [
            "#cbc5b5",
            "#aaa496"
        ]
    },
    {
        "name": "Cathedral Knight Helm",
        "image": "Head/Cathedral Knight Helm.PNG",
        "primaryColor": "#999799",
        "secondaryColors": [
            "#5e5756",
            "#50443b"
        ]
    },
    {
        "name": "Chain Helm (Female)",
        "image": "Head/Chain Helm (Female).PNG",
        "primaryColor": "#4e4c48",
        "secondaryColors": [
            "#4d4a45",
            "#47433b"
        ]
    },
    {
        "name": "Chain Helm",
        "image": "Head/Chain Helm.PNG",
        "primaryColor": "#4d4c47",
        "secondaryColors": [
            "#484744",
            "#43413d"
        ]
    },
    {
        "name": "Cleric Hat (Female)",
        "image": "Head/Cleric Hat (Female).PNG",
        "primaryColor": "#c9cbc9",
        "secondaryColors": [
            "#a4a29a",
            "#9f9d95"
        ]
    },
    {
        "name": "Cleric Hat",
        "image": "Head/Cleric Hat.PNG",
        "primaryColor": "#d3d1c7",
        "secondaryColors": [
            "#c7c5ba",
            "#c1bdb3"
        ]
    },
    {
        "name": "Conjurator Hood",
        "image": "Head/Conjurator Hood.PNG",
        "primaryColor": "#a99064",
        "secondaryColors": [
            "#8b724c",
            "#746145"
        ]
    },
    {
        "name": "Court Sorceror Hood",
        "image": "Head/Court Sorceror Hood.PNG",
        "primaryColor": "#55504c",
        "secondaryColors": [
            "#4d4846",
            "#46413e"
        ]
    },
    {
        "name": "Creighton's Steel Mask",
        "image": "Head/Creighton's Steel Mask.PNG",
        "primaryColor": "#888a88",
        "secondaryColors": [
            "#50514e",
            "#42413d"
        ]
    },
    {
        "name": "Crown of Dusk",
        "image": "Head/Crown of Dusk.PNG",
        "primaryColor": "#a98a70",
        "secondaryColors": [
            "#8c6d57",
            "#656357"
        ]
    },
    {
        "name": "Dancer's Crown",
        "image": "Head/Dancer's Crown.PNG",
        "primaryColor": "#6c7488",
        "secondaryColors": [
            "#575557",
            "#4b4d51"
        ]
    },
    {
        "name": "Dark Mask",
        "image": "Head/Dark Mask.PNG",
        "primaryColor": "#524f4e",
        "secondaryColors": [
            "#45413c",
            "#3e3e40"
        ]
    },
    {
        "name": "Desert Pyromancer Hood",
        "image": "Head/Desert Pyromancer Hood.png",
        "primaryColor": "#8a5149",
        "secondaryColors": [
            "#7a4f44",
            "#70443a"
        ]
    },
    {
        "name": "Dragonslayer Helm",
        "image": "Head/Dragonslayer Helm.PNG",
        "primaryColor": "#a8a494",
        "secondaryColors": [
            "#5c5a51",
            "#49433a"
        ]
    },
    {
        "name": "Drakeblood Helm",
        "image": "Head/Drakeblood Helm.PNG",
        "primaryColor": "#514e4f",
        "secondaryColors": [
            "#46413d",
            "#423c3a"
        ]
    },
    {
        "name": "Eastern Helm",
        "image": "Head/Eastern Helm.PNG",
        "primaryColor": "#968771",
        "secondaryColors": [
            "#87755e",
            "#675b4d"
        ]
    },
    {
        "name": "Elite Knight Helm",
        "image": "Head/Elite Knight Helm.PNG",
        "primaryColor": "#959aa2",
        "secondaryColors": [
            "#515155",
            "#48433b"
        ]
    },
    {
        "name": "Evangelist Hat",
        "image": "Head/Evangelist Hat.PNG",
        "primaryColor": "#4f4d4c",
        "secondaryColors": [
            "#464545",
            "#46413d"
        ]
    },
    {
        "name": "Executioner Helm",
        "image": "Head/Executioner Helm.PNG",
        "primaryColor": "#9b999b",
        "secondaryColors": [
            "#5a5759",
            "#473a36"
        ]
    },
    {
        "name": "Exile Mask",
        "image": "Head/Exile Mask.PNG",
        "primaryColor": "#949594",
        "secondaryColors": [
            "#555654",
            "#43413d"
        ]
    },
    {
        "name": "Fallen Knight Helm",
        "image": "Head/Fallen Knight Helm.PNG",
        "primaryColor": "#5e5a51",
        "secondaryColors": [
            "#5e5950",
            "#46433c"
        ]
    },
    {
        "name": "Faraam Helm",
        "image": "Head/Faraam Helm.PNG",
        "primaryColor": "#939598",
        "secondaryColors": [
            "#545456",
            "#44413d"
        ]
    },
    {
        "name": "Fire Witch Helm",
        "image": "Head/Fire Witch Helm.PNG",
        "primaryColor": "#555454",
        "secondaryColors": [
            "#484338",
            "#3d424d"
        ]
    },
    {
        "name": "Firelink Helm",
        "image": "Head/Firelink Helm.PNG",
        "primaryColor": "#895e5a",
        "secondaryColors": [
            "#5c5050",
            "#51403e"
        ]
    },
    {
        "name": "Golden Crown",
        "image": "Head/Golden Crown.PNG",
        "primaryColor": "#cbcccd",
        "secondaryColors": [
            "#a2a3a4",
            "#a1a2a3"
        ]
    },
    {
        "name": "Grave Warden Hood",
        "image": "Head/Grave Warden Hood.PNG",
        "primaryColor": "#98928c",
        "secondaryColors": [
            "#8a837b",
            "#857972"
        ]
    },
    {
        "name": "Gundyr's Helm",
        "image": "Head/Gundyr's Helm.PNG",
        "primaryColor": "#959596",
        "secondaryColors": [
            "#595454",
            "#44413e"
        ]
    },
    {
        "name": "Havel's Helm",
        "image": "Head/Havel's Helm.PNG",
        "primaryColor": "#d2cfcd",
        "secondaryColors": [
            "#a09b98",
            "#89827c"
        ]
    },
    {
        "name": "Helm of Favor",
        "image": "Head/Helm of Favor.PNG",
        "primaryColor": "#8b6f4d",
        "secondaryColors": [
            "#6a5c45",
            "#5c4934"
        ]
    },
    {
        "name": "Helm of Thorns",
        "image": "Head/Helm of Thorns.PNG",
        "primaryColor": "#564f51",
        "secondaryColors": [
            "#443d41",
            "#423a38"
        ]
    },
    {
        "name": "Herald Helm",
        "image": "Head/Herald Helm.PNG",
        "primaryColor": "#504c4a",
        "secondaryColors": [
            "#4d443a",
            "#3b3d43"
        ]
    },
    {
        "name": "Hood of Prayer",
        "image": "Head/Hood of Prayer.PNG",
        "primaryColor": "#4c484c",
        "secondaryColors": [
            "#423d42",
            "#413b37"
        ]
    },
    {
        "name": "Iron Dragonslayer Helm",
        "image": "Head/Iron Dragonslayer Helm.png",
        "primaryColor": "#969999",
        "secondaryColors": [
            "#585958",
            "#503335"
        ]
    },
    {
        "name": "Iron Helm",
        "image": "Head/Iron Helm.PNG",
        "primaryColor": "#969799",
        "secondaryColors": [
            "#5b5855",
            "#49433c"
        ]
    },
    {
        "name": "Karla's Pointed Hat",
        "image": "Head/Karla's Pointed Hat.PNG",
        "primaryColor": "#565452",
        "secondaryColors": [
            "#494946",
            "#3e4040"
        ]
    },
    {
        "name": "Knight Helm",
        "image": "Head/Knight Helm.PNG",
        "primaryColor": "#999ca0",
        "secondaryColors": [
            "#505354",
            "#46423b"
        ]
    },
    {
        "name": "Lapp's Helm",
        "image": "Head/Lapp's Helm.png",
        "primaryColor": "#efe7d7",
        "secondaryColors": [
            "#ac9d8d",
            "#87786b"
        ]
    },
    {
        "name": "Lorian's Helm",
        "image": "Head/Lorian's Helm.PNG",
        "primaryColor": "#a4a19b",
        "secondaryColors": [
            "#5a5652",
            "#45413c"
        ]
    },
    {
        "name": "Lothric Knight Helm",
        "image": "Head/Lothric Knight Helm.PNG",
        "primaryColor": "#999ba0",
        "secondaryColors": [
            "#525257",
            "#47423b"
        ]
    },
    {
        "name": "Lucatiel Mask",
        "image": "Head/Lucatiel Mask.PNG",
        "primaryColor": "#a29e9b",
        "secondaryColors": [
            "#5d5b5e",
            "#364361"
        ]
    },
    {
        "name": "Maiden Hood",
        "image": "Head/Maiden Hood.PNG",
        "primaryColor": "#e5d2ae",
        "secondaryColors": [
            "#9e8b71",
            "#8e745c"
        ]
    },
    {
        "name": "Morne's Helm",
        "image": "Head/Morne's Helm.PNG",
        "primaryColor": "#504f4e",
        "secondaryColors": [
            "#4d4d4b",
            "#43403e"
        ]
    },
    {
        "name": "Nameless Knight Helm",
        "image": "Head/Nameless Knight Helm.PNG",
        "primaryColor": "#4f4f50",
        "secondaryColors": [
            "#4e4e4e",
            "#44413d"
        ]
    },
    {
        "name": "Northern Helm",
        "image": "Head/Northern Helm.PNG",
        "primaryColor": "#96948d",
        "secondaryColors": [
            "#84837b",
            "#5b5a55"
        ]
    },
    {
        "name": "Old Sage's Blindfold",
        "image": "Head/Old Sage's Blindfold.PNG",
        "primaryColor": "#918579",
        "secondaryColors": [
            "#85796f",
            "#655d56"
        ]
    },
    {
        "name": "Old Sorceror Hat",
        "image": "Head/Old Sorceror Hat.PNG",
        "primaryColor": "#938d77",
        "secondaryColors": [
            "#625b4c",
            "#4f4639"
        ]
    },
    {
        "name": "Outrider Knight Helm",
        "image": "Head/Outrider Knight Helm.PNG",
        "primaryColor": "#8e96a7",
        "secondaryColors": [
            "#6f7587",
            "#53545b"
        ]
    },
    {
        "name": "Painting Guardian Hood",
        "image": "Head/Painting Guardian Hood.PNG",
        "primaryColor": "#e4dcd2",
        "secondaryColors": [
            "#d0c6b8",
            "#c5baab"
        ]
    },
    {
        "name": "Pharis's Hat",
        "image": "Head/Pharis's Hat.PNG",
        "primaryColor": "#a49b8d",
        "secondaryColors": [
            "#5a4f4a",
            "#4b413d"
        ]
    },
    {
        "name": "Pontiff Knight Crown",
        "image": "Head/Pontiff Knight Crown.PNG",
        "primaryColor": "#e5d194",
        "secondaryColors": [
            "#ab9362",
            "#726245"
        ]
    },
    {
        "name": "Pyromancer Crown",
        "image": "Head/Pyromancer Crown.PNG",
        "primaryColor": "#69665b",
        "secondaryColors": [
            "#60574f",
            "#4e443b"
        ]
    },
    {
        "name": "Ragged Mask",
        "image": "Head/Ragged Mask.png",
        "primaryColor": "#87725f",
        "secondaryColors": [
            "#6b5a4a",
            "#564737"
        ]
    },
    {
        "name": "Ringed Knight Hood",
        "image": "Head/Ringed Knight Hood.png",
        "primaryColor": "#4c4b4d",
        "secondaryColors": [
            "#4f413c",
            "#3b4246"
        ]
    },
    {
        "name": "Ruin Helm",
        "image": "Head/Ruin Helm.png",
        "primaryColor": "#84775a",
        "secondaryColors": [
            "#6a5f4b",
            "#504736"
        ]
    },
    {
        "name": "Sage's Big Hat",
        "image": "Head/Sage's Big Hat.PNG",
        "primaryColor": "#8c8b8b",
        "secondaryColors": [
            "#696869",
            "#646363"
        ]
    },
    {
        "name": "Sellsword Helm",
        "image": "Head/Sellsword Helm.PNG",
        "primaryColor": "#938772",
        "secondaryColors": [
            "#857662",
            "#665b4e"
        ]
    },
    {
        "name": "Shadow Mask",
        "image": "Head/Shadow Mask.PNG",
        "primaryColor": "#594835",
        "secondaryColors": [
            "#454443",
            "#3e4041"
        ]
    },
    {
        "name": "Shira's_Crown",
        "image": "Head/Shira's_Crown.png",
        "primaryColor": "#5d5c56",
        "secondaryColors": [
            "#595a58",
            "#5a5a55"
        ]
    },
    {
        "name": "Silver Knight Helm",
        "image": "Head/Silver Knight Helm.PNG",
        "primaryColor": "#999999",
        "secondaryColors": [
            "#585755",
            "#46423a"
        ]
    },
    {
        "name": "Silver Mask",
        "image": "Head/Silver Mask.PNG",
        "primaryColor": "#60554f",
        "secondaryColors": [
            "#574f4c",
            "#48413c"
        ]
    },
    {
        "name": "Smough's Helm",
        "image": "Head/Smough's Helm.PNG",
        "primaryColor": "#f3eddb",
        "secondaryColors": [
            "#ada490",
            "#5d564d"
        ]
    },
    {
        "name": "Sneering Mask",
        "image": "Head/Sneering Mask.PNG",
        "primaryColor": "#d6d2cc",
        "secondaryColors": [
            "#c8c3ba",
            "#c2bcb2"
        ]
    },
    {
        "name": "Sorceror Hood",
        "image": "Head/Sorceror Hood.PNG",
        "primaryColor": "#5e4949",
        "secondaryColors": [
            "#54413e",
            "#513e40"
        ]
    },
    {
        "name": "Standard Helm",
        "image": "Head/Standard Helm.PNG",
        "primaryColor": "#d9d8da",
        "secondaryColors": [
            "#9c9999",
            "#5b5655"
        ]
    },
    {
        "name": "Steel Soldier Helm",
        "image": "Head/Steel Soldier Helm.PNG",
        "primaryColor": "#9e9899",
        "secondaryColors": [
            "#585153",
            "#4c423c"
        ]
    },
    {
        "name": "Sunless Veil",
        "image": "Head/Sunless Veil.PNG",
        "primaryColor": "#cac9ca",
        "secondaryColors": [
            "#a3a1a1",
            "#605f5e"
        ]
    },
    {
        "name": "Sunset Helm",
        "image": "Head/Sunset Helm.PNG",
        "primaryColor": "#9b968f",
        "secondaryColors": [
            "#5f5a55",
            "#524539"
        ]
    },
    {
        "name": "Symbol of Avarice",
        "image": "Head/Symbol of Avarice.PNG",
        "primaryColor": "#a78574",
        "secondaryColors": [
            "#9a6c5b",
            "#67594d"
        ]
    },
    {
        "name": "Thief Mask",
        "image": "Head/Thief Mask.PNG",
        "primaryColor": "#898479",
        "secondaryColors": [
            "#5e5a53",
            "#47433c"
        ]
    },
    {
        "name": "Thrall Hood",
        "image": "Head/Thrall Hood.PNG",
        "primaryColor": "#94969c",
        "secondaryColors": [
            "#7a838b",
            "#757a82"
        ]
    },
    {
        "name": "Undead Legion Helm",
        "image": "Head/Undead Legion Helm.PNG",
        "primaryColor": "#909aa9",
        "secondaryColors": [
            "#6c7787",
            "#4e5156"
        ]
    },
    {
        "name": "Varangian Helm",
        "image": "Head/Varangian Helm.PNG",
        "primaryColor": "#545256",
        "secondaryColors": [
            "#443734",
            "#313949"
        ]
    },
    {
        "name": "Vilhelm's Helm",
        "image": "Head/Vilhelm's Helm.png",
        "primaryColor": "#90714d",
        "secondaryColors": [
            "#524d4a",
            "#554637"
        ]
    },
    {
        "name": "White_Preacher_Head",
        "image": "Head/White_Preacher_Head.png",
        "primaryColor": "#ced4d4",
        "secondaryColors": [
            "#99a09f",
            "#5f605d"
        ]
    },
    {
        "name": "Winged Knight Helm",
        "image": "Head/Winged Knight Helm.PNG",
        "primaryColor": "#d3d5d8",
        "secondaryColors": [
            "#9d9fa4",
            "#535459"
        ]
    },
    {
        "name": "Wolf Knight Helm",
        "image": "Head/Wolf Knight Helm.PNG",
        "primaryColor": "#627086",
        "secondaryColors": [
            "#4f545d",
            "#3a4658"
        ]
    },
    {
        "name": "Wolnir's Crown",
        "image": "Head/Wolnir's Crown.PNG",
        "primaryColor": "#948971",
        "secondaryColors": [
            "#63594d",
            "#504539"
        ]
    },
    {
        "name": "Worker Hat",
        "image": "Head/Worker Hat.PNG",
        "primaryColor": "#4f4b4d",
        "secondaryColors": [
            "#49403e",
            "#423e40"
        ]
    },
    {
        "name": "Xanthous Crown",
        "image": "Head/Xanthous Crown.PNG",
        "primaryColor": "#dccfa1",
        "secondaryColors": [
            "#c9b789",
            "#a99469"
        ]
    },
    {
        "name": "Alva Leggings",
        "image": "Legs/Alva Leggings.png",
        "primaryColor": "#5b5451",
        "secondaryColors": [
            "#564c48",
            "#49423b"
        ]
    },
    {
        "name": "Antiquated Skirt",
        "image": "Legs/Antiquated Skirt.png",
        "primaryColor": "#efebdc",
        "secondaryColors": [
            "#dfd6b1",
            "#c6ba95"
        ]
    },
    {
        "name": "Archdeacon Skirt",
        "image": "Legs/Archdeacon Skirt.png",
        "primaryColor": "#d9c8ac",
        "secondaryColors": [
            "#c9b597",
            "#b6a389"
        ]
    },
    {
        "name": "Assassin Trousers",
        "image": "Legs/Assassin Trousers.png",
        "primaryColor": "#5c544c",
        "secondaryColors": [
            "#57504b",
            "#4c433c"
        ]
    },
    {
        "name": "Black Iron Leggings",
        "image": "Legs/Black Iron Leggings.png",
        "primaryColor": "#4d4f4b",
        "secondaryColors": [
            "#46433a",
            "#3e403d"
        ]
    },
    {
        "name": "Black Knight Leggings",
        "image": "Legs/Black Knight Leggings.png",
        "primaryColor": "#8f8d8c",
        "secondaryColors": [
            "#565352",
            "#44413d"
        ]
    },
    {
        "name": "Black Leather Boots",
        "image": "Legs/Black Leather Boots.png",
        "primaryColor": "#55514d",
        "secondaryColors": [
            "#55514d",
            "#54443a"
        ]
    },
    {
        "name": "Black Leggings",
        "image": "Legs/Black Leggings.png",
        "primaryColor": "#515150",
        "secondaryColors": [
            "#4c4c49",
            "#41413e"
        ]
    },
    {
        "name": "Black Witch Trousers",
        "image": "Legs/Black Witch Trousers.png",
        "primaryColor": "#4f4f4f",
        "secondaryColors": [
            "#48454d",
            "#433b49"
        ]
    },
    {
        "name": "Brass Leggings",
        "image": "Legs/Brass Leggings.png",
        "primaryColor": "#5f524d",
        "secondaryColors": [
            "#5d4a30",
            "#473825"
        ]
    },
    {
        "name": "Brigand Trousers",
        "image": "Legs/Brigand Trousers.png",
        "primaryColor": "#87755a",
        "secondaryColors": [
            "#60554a",
            "#50463a"
        ]
    },
    {
        "name": "Catarina Leggings",
        "image": "Legs/Catarina Leggings.png",
        "primaryColor": "#a7a192",
        "secondaryColors": [
            "#908976",
            "#665c52"
        ]
    },
    {
        "name": "Cathedral Knight Leggings",
        "image": "Legs/Cathedral Knight Leggings.png",
        "primaryColor": "#9e9896",
        "secondaryColors": [
            "#625d52",
            "#494539"
        ]
    },
    {
        "name": "Chain Leggings",
        "image": "Legs/Chain Leggings.png",
        "primaryColor": "#84837a",
        "secondaryColors": [
            "#575652",
            "#44413d"
        ]
    },
    {
        "name": "Cleric Trousers",
        "image": "Legs/Cleric Trousers.png",
        "primaryColor": "#867053",
        "secondaryColors": [
            "#605750",
            "#544639"
        ]
    },
    {
        "name": "Conjurator Boots",
        "image": "Legs/Conjurator Boots.png",
        "primaryColor": "#897562",
        "secondaryColors": [
            "#554e48",
            "#48423c"
        ]
    },
    {
        "name": "Cornyx's Skirt",
        "image": "Legs/Cornyx's Skirt.png",
        "primaryColor": "#4e5250",
        "secondaryColors": [
            "#4a483a",
            "#3d4142"
        ]
    },
    {
        "name": "Court Sorcerer Trousers",
        "image": "Legs/Court Sorcerer Trousers.png",
        "primaryColor": "#a29b90",
        "secondaryColors": [
            "#8c847a",
            "#837b73"
        ]
    },
    {
        "name": "Dancer's Leggings",
        "image": "Legs/Dancer's Leggings.png",
        "primaryColor": "#5d6063",
        "secondaryColors": [
            "#555454",
            "#44413c"
        ]
    },
    {
        "name": "Dark Leggings",
        "image": "Legs/Dark Leggings.png",
        "primaryColor": "#525454",
        "secondaryColors": [
            "#535253",
            "#444238"
        ]
    },
    {
        "name": "Deacon Skirt",
        "image": "Legs/Deacon Skirt.png",
        "primaryColor": "#d5c6af",
        "secondaryColors": [
            "#c8b79d",
            "#b4a48c"
        ]
    },
    {
        "name": "Desert Pyromancer Skirt",
        "image": "Legs/Desert Pyromancer Skirt.png",
        "primaryColor": "#84514e",
        "secondaryColors": [
            "#6d4a47",
            "#5e433c"
        ]
    },
    {
        "name": "Deserter Trousers",
        "image": "Legs/Deserter Trousers.png",
        "primaryColor": "#89755f",
        "secondaryColors": [
            "#58514c",
            "#51463a"
        ]
    },
    {
        "name": "Dragonscale Waistcloth",
        "image": "Legs/Dragonscale Waistcloth.png",
        "primaryColor": "#56524f",
        "secondaryColors": [
            "#48433c",
            "#423c36"
        ]
    },
    {
        "name": "Dragonslayer Leggings",
        "image": "Legs/Dragonslayer Leggings.png",
        "primaryColor": "#5c574d",
        "secondaryColors": [
            "#4b4437",
            "#433c31"
        ]
    },
    {
        "name": "Drakeblood Leggings",
        "image": "Legs/Drakeblood Leggings.png",
        "primaryColor": "#929496",
        "secondaryColors": [
            "#514f4e",
            "#43413d"
        ]
    },
    {
        "name": "Drang Shoes",
        "image": "Legs/Drang Shoes.png",
        "primaryColor": "#484848",
        "secondaryColors": [
            "#42403e",
            "#3e3e40"
        ]
    },
    {
        "name": "Eastern Leggings",
        "image": "Legs/Eastern Leggings.png",
        "primaryColor": "#988d72",
        "secondaryColors": [
            "#5a554e",
            "#47433a"
        ]
    },
    {
        "name": "Elite Knight Leggings",
        "image": "Legs/Elite Knight Leggings.png",
        "primaryColor": "#9e9d9e",
        "secondaryColors": [
            "#5e5855",
            "#47423c"
        ]
    },
    {
        "name": "Evangelist Trousers",
        "image": "Legs/Evangelist Trousers.png",
        "primaryColor": "#9f9c93",
        "secondaryColors": [
            "#8d867a",
            "#615e57"
        ]
    },
    {
        "name": "Executioner Leggings",
        "image": "Legs/Executioner Leggings.png",
        "primaryColor": "#979597",
        "secondaryColors": [
            "#595451",
            "#50453a"
        ]
    },
    {
        "name": "Exile Leggings",
        "image": "Legs/Exile Leggings.png",
        "primaryColor": "#989693",
        "secondaryColors": [
            "#55514d",
            "#46423d"
        ]
    },
    {
        "name": "Fallen Knight Trousers",
        "image": "Legs/Fallen Knight Trousers.png",
        "primaryColor": "#534c49",
        "secondaryColors": [
            "#4a433a",
            "#423e41"
        ]
    },
    {
        "name": "Faraam Boots",
        "image": "Legs/Faraam Boots.png",
        "primaryColor": "#4f4b49",
        "secondaryColors": [
            "#55443a",
            "#3e4040"
        ]
    },
    {
        "name": "Fire Keeper Skirt",
        "image": "Legs/Fire Keeper Skirt.png",
        "primaryColor": "#4e4e4f",
        "secondaryColors": [
            "#4a443b",
            "#3e3d40"
        ]
    },
    {
        "name": "Fire Witch Leggings",
        "image": "Legs/Fire Witch Leggings.png",
        "primaryColor": "#55585d",
        "secondaryColors": [
            "#53565c",
            "#3d4147"
        ]
    },
    {
        "name": "Firelink Leggings",
        "image": "Legs/Firelink Leggings.png",
        "primaryColor": "#837a74",
        "secondaryColors": [
            "#5e5954",
            "#46423c"
        ]
    },
    {
        "name": "Follower Boots",
        "image": "Legs/Follower Boots.png",
        "primaryColor": "#555048",
        "secondaryColors": [
            "#4e453a",
            "#3d403c"
        ]
    },
    {
        "name": "Grave Warden Skirt",
        "image": "Legs/Grave Warden Skirt.png",
        "primaryColor": "#887369",
        "secondaryColors": [
            "#685651",
            "#52423c"
        ]
    },
    {
        "name": "Gundyr's Leggings",
        "image": "Legs/Gundyr's Leggings.png",
        "primaryColor": "#909092",
        "secondaryColors": [
            "#585657",
            "#48413e"
        ]
    },
    {
        "name": "Harald Legion Leggings",
        "image": "Legs/Harald Legion Leggings.png",
        "primaryColor": "#817a6d",
        "secondaryColors": [
            "#5a554d",
            "#48433b"
        ]
    },
    {
        "name": "Hard Leather Boots",
        "image": "Legs/Hard Leather Boots.png",
        "primaryColor": "#946d54",
        "secondaryColors": [
            "#585655",
            "#604737"
        ]
    },
    {
        "name": "Havel's Leggings",
        "image": "Legs/Havel's Leggings.png",
        "primaryColor": "#9c9794",
        "secondaryColors": [
            "#8a837b",
            "#837b74"
        ]
    },
    {
        "name": "Herald Leggings",
        "image": "Legs/Herald Leggings.png",
        "primaryColor": "#8a8c8d",
        "secondaryColors": [
            "#867464",
            "#666360"
        ]
    },
    {
        "name": "Iron Dragonslayer Leggings",
        "image": "Legs/Iron Dragonslayer Leggings.png",
        "primaryColor": "#939697",
        "secondaryColors": [
            "#555755",
            "#43423c"
        ]
    },
    {
        "name": "Iron Leggings",
        "image": "Legs/Iron Leggings.png",
        "primaryColor": "#9b9690",
        "secondaryColors": [
            "#857a6d",
            "#5b5751"
        ]
    },
    {
        "name": "Jailer Trousers",
        "image": "Legs/Jailer Trousers.png",
        "primaryColor": "#ada596",
        "secondaryColors": [
            "#867665",
            "#645951"
        ]
    },
    {
        "name": "Karla's Trousers",
        "image": "Legs/Karla's Trousers.png",
        "primaryColor": "#5a5653",
        "secondaryColors": [
            "#4d4c4b",
            "#4a423c"
        ]
    },
    {
        "name": "Knight Leggings",
        "image": "Legs/Knight Leggings.png",
        "primaryColor": "#a2a3a6",
        "secondaryColors": [
            "#525050",
            "#47413c"
        ]
    },
    {
        "name": "Lapp's Leggings",
        "image": "Legs/Lapp's Leggings.png",
        "primaryColor": "#ab9e8f",
        "secondaryColors": [
            "#5d5148",
            "#534439"
        ]
    },
    {
        "name": "Leather Boots",
        "image": "Legs/Leather Boots.png",
        "primaryColor": "#86786a",
        "secondaryColors": [
            "#5a5450",
            "#4f423b"
        ]
    },
    {
        "name": "Leggings Of Favor",
        "image": "Legs/Leggings Of Favor.png",
        "primaryColor": "#a59268",
        "secondaryColors": [
            "#8a7150",
            "#6f5c45"
        ]
    },
    {
        "name": "Leggings Of Thorns",
        "image": "Legs/Leggings Of Thorns.png",
        "primaryColor": "#514e4e",
        "secondaryColors": [
            "#443e41",
            "#3e3e40"
        ]
    },
    {
        "name": "Leonhard's Trousers",
        "image": "Legs/Leonhard's Trousers.png",
        "primaryColor": "#5d5653",
        "secondaryColors": [
            "#5b544f",
            "#47423c"
        ]
    },
    {
        "name": "Loincloth (Trc)",
        "image": "Legs/Loincloth (Trc).png",
        "primaryColor": "#a6a194",
        "secondaryColors": [
            "#8b857a",
            "#645b50"
        ]
    },
    {
        "name": "Loincloth",
        "image": "Legs/Loincloth.png",
        "primaryColor": "#5b5148",
        "secondaryColors": [
            "#4e443b",
            "#4e443a"
        ]
    },
    {
        "name": "Lorian's Leggings",
        "image": "Legs/Lorian's Leggings.png",
        "primaryColor": "#4e4b4d",
        "secondaryColors": [
            "#48423a",
            "#443935"
        ]
    },
    {
        "name": "Lothric Knight Leggings",
        "image": "Legs/Lothric Knight Leggings.png",
        "primaryColor": "#9a999c",
        "secondaryColors": [
            "#5b5655",
            "#4a433c"
        ]
    },
    {
        "name": "Maiden Skirt",
        "image": "Legs/Maiden Skirt.png",
        "primaryColor": "#f9f0da",
        "secondaryColors": [
            "#e6cfa9",
            "#d2b58e"
        ]
    },
    {
        "name": "Millwood Knight Leggings",
        "image": "Legs/Millwood Knight Leggings.png",
        "primaryColor": "#9e8871",
        "secondaryColors": [
            "#5c5c54",
            "#4f4639"
        ]
    },
    {
        "name": "Mirrah Chain Leggings",
        "image": "Legs/Mirrah Chain Leggings.png",
        "primaryColor": "#8f969b",
        "secondaryColors": [
            "#5e5a58",
            "#49423c"
        ]
    },
    {
        "name": "Mirrah Trousers",
        "image": "Legs/Mirrah Trousers.png",
        "primaryColor": "#83736c",
        "secondaryColors": [
            "#65554e",
            "#56433a"
        ]
    },
    {
        "name": "Morne's Leggings",
        "image": "Legs/Morne's Leggings.png",
        "primaryColor": "#4d4b4a",
        "secondaryColors": [
            "#48413d",
            "#3d3e40"
        ]
    },
    {
        "name": "Nameless Knight Leggings",
        "image": "Legs/Nameless Knight Leggings.png",
        "primaryColor": "#897769",
        "secondaryColors": [
            "#605650",
            "#4c433b"
        ]
    },
    {
        "name": "Northern Trousers",
        "image": "Legs/Northern Trousers.png",
        "primaryColor": "#a2968b",
        "secondaryColors": [
            "#86786f",
            "#59544f"
        ]
    },
    {
        "name": "Old Sorcerer Boots",
        "image": "Legs/Old Sorcerer Boots.png",
        "primaryColor": "#8b6f56",
        "secondaryColors": [
            "#524e4c",
            "#514539"
        ]
    },
    {
        "name": "Ordained Trousers",
        "image": "Legs/Ordained Trousers.png",
        "primaryColor": "#484844",
        "secondaryColors": [
            "#48433c",
            "#3d413d"
        ]
    },
    {
        "name": "Outrider Knight Leggings",
        "image": "Legs/Outrider Knight Leggings.png",
        "primaryColor": "#95979d",
        "secondaryColors": [
            "#5e5d5e",
            "#595959"
        ]
    },
    {
        "name": "Painting Guardian Waistcloth",
        "image": "Legs/Painting Guardian Waistcloth.png",
        "primaryColor": "#e8e2db",
        "secondaryColors": [
            "#d2c6b8",
            "#a39c94"
        ]
    },
    {
        "name": "Pale Shade Trousers",
        "image": "Legs/Pale Shade Trousers.png",
        "primaryColor": "#9e9b95",
        "secondaryColors": [
            "#85827b",
            "#504f52"
        ]
    },
    {
        "name": "Pontiff Knight Leggings",
        "image": "Legs/Pontiff Knight Leggings.png",
        "primaryColor": "#9d999a",
        "secondaryColors": [
            "#575959",
            "#3d4143"
        ]
    },
    {
        "name": "Pyromancer Trousers",
        "image": "Legs/Pyromancer Trousers.png",
        "primaryColor": "#896a5a",
        "secondaryColors": [
            "#665149",
            "#594539"
        ]
    },
    {
        "name": "Ringed Knight Leggings",
        "image": "Legs/Ringed Knight Leggings.png",
        "primaryColor": "#545656",
        "secondaryColors": [
            "#525253",
            "#4d4f4f"
        ]
    },
    {
        "name": "Ruin Leggings",
        "image": "Legs/Ruin Leggings.png",
        "primaryColor": "#847960",
        "secondaryColors": [
            "#665d4b",
            "#4e4637"
        ]
    },
    {
        "name": "Sellsword Trousers",
        "image": "Legs/Sellsword Trousers.png",
        "primaryColor": "#5e4f46",
        "secondaryColors": [
            "#50433b",
            "#453a34"
        ]
    },
    {
        "name": "Shadow Leggings",
        "image": "Legs/Shadow Leggings.png",
        "primaryColor": "#916e66",
        "secondaryColors": [
            "#544e4a",
            "#45423d"
        ]
    },
    {
        "name": "Shira's Trousers",
        "image": "Legs/Shira's Trousers.png",
        "primaryColor": "#d8d7cc",
        "secondaryColors": [
            "#c6c5b8",
            "#a9a79a"
        ]
    },
    {
        "name": "Silver Knight Leggings",
        "image": "Legs/Silver Knight Leggings.png",
        "primaryColor": "#9d9e9c",
        "secondaryColors": [
            "#524f4c",
            "#46423b"
        ]
    },
    {
        "name": "Skirt Of Prayer",
        "image": "Legs/Skirt Of Prayer.png",
        "primaryColor": "#c8b7a4",
        "secondaryColors": [
            "#ac9b8d",
            "#86766b"
        ]
    },
    {
        "name": "Slave Knight Leggings",
        "image": "Legs/Slave Knight Leggings.png",
        "primaryColor": "#8f8679",
        "secondaryColors": [
            "#60594f",
            "#4b453a"
        ]
    },
    {
        "name": "Smough's Leggings",
        "image": "Legs/Smough's Leggings.png",
        "primaryColor": "#55524b",
        "secondaryColors": [
            "#4a443a",
            "#3e3e40"
        ]
    },
    {
        "name": "Sorcerer Trousers",
        "image": "Legs/Sorcerer Trousers.png",
        "primaryColor": "#84786f",
        "secondaryColors": [
            "#5e544d",
            "#53453a"
        ]
    },
    {
        "name": "Sunless Leggings",
        "image": "Legs/Sunless Leggings.png",
        "primaryColor": "#949494",
        "secondaryColors": [
            "#595553",
            "#49423a"
        ]
    },
    {
        "name": "Sunset Leggings",
        "image": "Legs/Sunset Leggings.png",
        "primaryColor": "#86766a",
        "secondaryColors": [
            "#655950",
            "#4f4439"
        ]
    },
    {
        "name": "Undead Legion Leggings",
        "image": "Legs/Undead Legion Leggings.png",
        "primaryColor": "#8b8c8e",
        "secondaryColors": [
            "#5d5554",
            "#4e423c"
        ]
    },
    {
        "name": "Vilhelm's Leggings",
        "image": "Legs/Vilhelm's Leggings.png",
        "primaryColor": "#4b4e4f",
        "secondaryColors": [
            "#43413d",
            "#3d4243"
        ]
    },
    {
        "name": "Winged Knight Leggings",
        "image": "Legs/Winged Knight Leggings.png",
        "primaryColor": "#96979a",
        "secondaryColors": [
            "#595554",
            "#46423b"
        ]
    },
    {
        "name": "Wolf Knight Leggings",
        "image": "Legs/Wolf Knight Leggings.png",
        "primaryColor": "#9b928a",
        "secondaryColors": [
            "#857a72",
            "#5b5856"
        ]
    },
    {
        "name": "Worker Trousers",
        "image": "Legs/Worker Trousers.png",
        "primaryColor": "#574f4f",
        "secondaryColors": [
            "#4d423b",
            "#453835"
        ]
    },
    {
        "name": "Xanthous Trousers",
        "image": "Legs/Xanthous Trousers.png",
        "primaryColor": "#9e8b61",
        "secondaryColors": [
            "#897352",
            "#655a4f"
        ]
    },
    {
        "name": "Ancient Dragon Greatshield",
        "image": "Shields/Ancient Dragon Greatshield.png",
        "primaryColor": "#afa58f",
        "secondaryColors": [
            "#9f8e6f",
            "#8a745e"
        ]
    },
    {
        "name": "Black Iron Greatshield",
        "image": "Shields/Black Iron Greatshield.png",
        "primaryColor": "#dfdfe0",
        "secondaryColors": [
            "#9c9a9d",
            "#595558"
        ]
    },
    {
        "name": "Black Knight Shield",
        "image": "Shields/Black Knight Shield.png",
        "primaryColor": "#939190",
        "secondaryColors": [
            "#595655",
            "#44413e"
        ]
    },
    {
        "name": "Blue Wooden Shield",
        "image": "Shields/Blue Wooden Shield.png",
        "primaryColor": "#949fa7",
        "secondaryColors": [
            "#718ea0",
            "#5f7789"
        ]
    },
    {
        "name": "Bonewheel Shield",
        "image": "Shields/Bonewheel Shield.png",
        "primaryColor": "#c6b7ac",
        "secondaryColors": [
            "#a99d95",
            "#8a756c"
        ]
    },
    {
        "name": "Buckler",
        "image": "Shields/Buckler.png",
        "primaryColor": "#929395",
        "secondaryColors": [
            "#545456",
            "#413d3d"
        ]
    },
    {
        "name": "Caduceus Round Shield",
        "image": "Shields/Caduceus Round Shield.png",
        "primaryColor": "#95a291",
        "secondaryColors": [
            "#7a9884",
            "#8b9177"
        ]
    },
    {
        "name": "Carthus Shield",
        "image": "Shields/Carthus Shield.png",
        "primaryColor": "#a2886a",
        "secondaryColors": [
            "#8b705a",
            "#64564d"
        ]
    },
    {
        "name": "Cathedral Knight Greatshield",
        "image": "Shields/Cathedral Knight Greatshield.png",
        "primaryColor": "#989589",
        "secondaryColors": [
            "#968d71",
            "#837a65"
        ]
    },
    {
        "name": "Crest Shield",
        "image": "Shields/Crest Shield.png",
        "primaryColor": "#dedbd1",
        "secondaryColors": [
            "#9c9c9e",
            "#998d73"
        ]
    },
    {
        "name": "Crimson Parma",
        "image": "Shields/Crimson Parma.png",
        "primaryColor": "#cacbca",
        "secondaryColors": [
            "#c49d9c",
            "#aaa4a4"
        ]
    },
    {
        "name": "Curse Ward Greatshield",
        "image": "Shields/Curse Ward Greatshield.png",
        "primaryColor": "#929497",
        "secondaryColors": [
            "#5a585a",
            "#46413d"
        ]
    },
    {
        "name": "Dragon Crest Shield",
        "image": "Shields/Dragon Crest Shield.png",
        "primaryColor": "#9b9c9c",
        "secondaryColors": [
            "#79869b",
            "#667389"
        ]
    },
    {
        "name": "Dragonhead Greatshield",
        "image": "Shields/Dragonhead Greatshield.png",
        "primaryColor": "#8f8f8e",
        "secondaryColors": [
            "#646463",
            "#605f5e"
        ]
    },
    {
        "name": "Dragonhead Shield",
        "image": "Shields/Dragonhead Shield.png",
        "primaryColor": "#939595",
        "secondaryColors": [
            "#5e5f5e",
            "#5d5f5f"
        ]
    },
    {
        "name": "Dragonslayer Greatshield",
        "image": "Shields/Dragonslayer Greatshield.png",
        "primaryColor": "#8f9494",
        "secondaryColors": [
            "#5e605f",
            "#565857"
        ]
    },
    {
        "name": "East-West Shield",
        "image": "Shields/East-West Shield.png",
        "primaryColor": "#d9c9ac",
        "secondaryColors": [
            "#c9b49b",
            "#a99e96"
        ]
    },
    {
        "name": "Eastern Iron Shield",
        "image": "Shields/Eastern Iron Shield.png",
        "primaryColor": "#cccbcb",
        "secondaryColors": [
            "#979796",
            "#5b5a5a"
        ]
    },
    {
        "name": "Elkhorn Round Shield",
        "image": "Shields/Elkhorn Round Shield.png",
        "primaryColor": "#9a9d98",
        "secondaryColors": [
            "#8b8576",
            "#827a6b"
        ]
    },
    {
        "name": "Ethereal Oak Shield",
        "image": "Shields/Ethereal Oak Shield.png",
        "primaryColor": "#94999a",
        "secondaryColors": [
            "#565957",
            "#3d4141"
        ]
    },
    {
        "name": "Follower Shield",
        "image": "Shields/Follower Shield.png",
        "primaryColor": "#d9dcdd",
        "secondaryColors": [
            "#979a9d",
            "#7c8285"
        ]
    },
    {
        "name": "Ghru Rotshield",
        "image": "Shields/Ghru Rotshield.png",
        "primaryColor": "#c6b5a5",
        "secondaryColors": [
            "#a69a91",
            "#998778"
        ]
    },
    {
        "name": "Giant Door Shield",
        "image": "Shields/Giant Door Shield.png",
        "primaryColor": "#958672",
        "secondaryColors": [
            "#857562",
            "#675a4c"
        ]
    },
    {
        "name": "Golden Falcon Shield",
        "image": "Shields/Golden Falcon Shield.png",
        "primaryColor": "#8b744d",
        "secondaryColors": [
            "#726245",
            "#614d30"
        ]
    },
    {
        "name": "Golden Wing Crest Shield",
        "image": "Shields/Golden Wing Crest Shield.png",
        "primaryColor": "#a9a28d",
        "secondaryColors": [
            "#938a73",
            "#847964"
        ]
    },
    {
        "name": "Grass Crest Shield",
        "image": "Shields/Grass Crest Shield.png",
        "primaryColor": "#dbdcdd",
        "secondaryColors": [
            "#d6d2a0",
            "#9d9e99"
        ]
    },
    {
        "name": "Greatshield of Glory",
        "image": "Shields/Greatshield of Glory.png",
        "primaryColor": "#8d8e90",
        "secondaryColors": [
            "#595a5a",
            "#545455"
        ]
    },
    {
        "name": "Havel's Greatshield",
        "image": "Shields/Havel's Greatshield.png",
        "primaryColor": "#92918d",
        "secondaryColors": [
            "#84827d",
            "#817d7a"
        ]
    },
    {
        "name": "Hawkwood's Shield",
        "image": "Shields/Hawkwood's Shield.png",
        "primaryColor": "#c6b49d",
        "secondaryColors": [
            "#9e9b94",
            "#958776"
        ]
    },
    {
        "name": "Iron Round Shield",
        "image": "Shields/Iron Round Shield.png",
        "primaryColor": "#979694",
        "secondaryColors": [
            "#605750",
            "#4f433a"
        ]
    },
    {
        "name": "Kite Shield",
        "image": "Shields/Kite Shield.png",
        "primaryColor": "#cecece",
        "secondaryColors": [
            "#9a9a9b",
            "#5e5e5f"
        ]
    },
    {
        "name": "Knight Shield",
        "image": "Shields/Knight Shield.png",
        "primaryColor": "#dcdada",
        "secondaryColors": [
            "#9d9a9a",
            "#857870"
        ]
    },
    {
        "name": "Large Leather Shield",
        "image": "Shields/Large Leather Shield.png",
        "primaryColor": "#cba58e",
        "secondaryColors": [
            "#c49279",
            "#b39385"
        ]
    },
    {
        "name": "Leather Shield",
        "image": "Shields/Leather Shield.png",
        "primaryColor": "#dfdcd7",
        "secondaryColors": [
            "#a39c91",
            "#8d8579"
        ]
    },
    {
        "name": "Llewellyn Shield",
        "image": "Shields/Llewellyn Shield.png",
        "primaryColor": "#d7d5d2",
        "secondaryColors": [
            "#9c9a98",
            "#5c5c5a"
        ]
    },
    {
        "name": "Lothric Knight Greatshield",
        "image": "Shields/Lothric Knight Greatshield.png",
        "primaryColor": "#98989a",
        "secondaryColors": [
            "#5e5d5e",
            "#413d3c"
        ]
    },
    {
        "name": "Lothric Knight Shield",
        "image": "Shields/Lothric Knight Shield.png",
        "primaryColor": "#d5d3d1",
        "secondaryColors": [
            "#c6c4b8",
            "#a19e9b"
        ]
    },
    {
        "name": "Moaning Shield",
        "image": "Shields/Moaning Shield.png",
        "primaryColor": "#90908f",
        "secondaryColors": [
            "#52504c",
            "#47423b"
        ]
    },
    {
        "name": "Pierce Shield",
        "image": "Shields/Pierce Shield.png",
        "primaryColor": "#887567",
        "secondaryColors": [
            "#595551",
            "#50433b"
        ]
    },
    {
        "name": "Plank Shield",
        "image": "Shields/Plank Shield.png",
        "primaryColor": "#dcc9b2",
        "secondaryColors": [
            "#cab299",
            "#b1a08e"
        ]
    },
    {
        "name": "Pontiff Knight Shield",
        "image": "Shields/Pontiff Knight Shield.png",
        "primaryColor": "#8a8d93",
        "secondaryColors": [
            "#7d8188",
            "#787c83"
        ]
    },
    {
        "name": "Porcine Shield",
        "image": "Shields/Porcine Shield.png",
        "primaryColor": "#a49158",
        "secondaryColors": [
            "#8a7746",
            "#7a6c44"
        ]
    },
    {
        "name": "Red and White Shield",
        "image": "Shields/Red and White Shield.png",
        "primaryColor": "#f1e1d5",
        "secondaryColors": [
            "#e3cab4",
            "#d5ab9a"
        ]
    },
    {
        "name": "Round Shield",
        "image": "Shields/Round Shield.png",
        "primaryColor": "#989691",
        "secondaryColors": [
            "#89847a",
            "#655e55"
        ]
    },
    {
        "name": "Sacred Bloom Shield",
        "image": "Shields/Sacred Bloom Shield.png",
        "primaryColor": "#dde4e7",
        "secondaryColors": [
            "#a0b5c9",
            "#989ea3"
        ]
    },
    {
        "name": "Shield of Want",
        "image": "Shields/Shield of Want.png",
        "primaryColor": "#99969b",
        "secondaryColors": [
            "#5c5756",
            "#4a433c"
        ]
    },
    {
        "name": "Silver Eagle Kite Shield",
        "image": "Shields/Silver Eagle Kite Shield.png",
        "primaryColor": "#9d999e",
        "secondaryColors": [
            "#877273",
            "#62595c"
        ]
    },
    {
        "name": "Silver Knight Shield",
        "image": "Shields/Silver Knight Shield.png",
        "primaryColor": "#9a9790",
        "secondaryColors": [
            "#5d5953",
            "#46423c"
        ]
    },
    {
        "name": "Small Leather Shield",
        "image": "Shields/Small Leather Shield.png",
        "primaryColor": "#97999b",
        "secondaryColors": [
            "#8a624e",
            "#675750"
        ]
    },
    {
        "name": "Spider Shield",
        "image": "Shields/Spider Shield.png",
        "primaryColor": "#c86d62",
        "secondaryColors": [
            "#9f5c54",
            "#8e473c"
        ]
    },
    {
        "name": "Spiked Shield",
        "image": "Shields/Spiked Shield.png",
        "primaryColor": "#857578",
        "secondaryColors": [
            "#594e52",
            "#463d41"
        ]
    },
    {
        "name": "Spirit Tree Crest Shield",
        "image": "Shields/Spirit Tree Crest Shield.png",
        "primaryColor": "#8c909d",
        "secondaryColors": [
            "#7c8496",
            "#707687"
        ]
    },
    {
        "name": "Stone Greatshield",
        "image": "Shields/Stone Greatshield.png",
        "primaryColor": "#9f9c91",
        "secondaryColors": [
            "#8d9565",
            "#798853"
        ]
    },
    {
        "name": "Stone Parma",
        "image": "Shields/Stone Parma.png",
        "primaryColor": "#969792",
        "secondaryColors": [
            "#82837d",
            "#5f605c"
        ]
    },
    {
        "name": "Sunlight Shield",
        "image": "Shields/Sunlight Shield.png",
        "primaryColor": "#9e9b96",
        "secondaryColors": [
            "#8e8b73",
            "#85736c"
        ]
    },
    {
        "name": "Sunset Shield",
        "image": "Shields/Sunset Shield.png",
        "primaryColor": "#9b8b72",
        "secondaryColors": [
            "#87765f",
            "#605951"
        ]
    },
    {
        "name": "Target Shield",
        "image": "Shields/Target Shield.png",
        "primaryColor": "#d5d6d8",
        "secondaryColors": [
            "#9a9c9e",
            "#5c5c5d"
        ]
    },
    {
        "name": "Twin Dragon Greatshield",
        "image": "Shields/Twin Dragon Greatshield.png",
        "primaryColor": "#a39990",
        "secondaryColors": [
            "#9d8a6f",
            "#8a735f"
        ]
    },
    {
        "name": "Wargod Wooden Shield",
        "image": "Shields/Wargod Wooden Shield.png",
        "primaryColor": "#aa9f8e",
        "secondaryColors": [
            "#a28c6f",
            "#907258"
        ]
    },
    {
        "name": "Warrior's Round Shield",
        "image": "Shields/Warrior's Round Shield.png",
        "primaryColor": "#dad9e4",
        "secondaryColors": [
            "#9c8fa3",
            "#8a7893"
        ]
    },
    {
        "name": "Wolf Knight's Greatshield",
        "image": "Shields/Wolf Knight's Greatshield.png",
        "primaryColor": "#95999b",
        "secondaryColors": [
            "#575657",
            "#49413c"
        ]
    },
    {
        "name": "Wooden Shield",
        "image": "Shields/Wooden Shield.png",
        "primaryColor": "#d4d0d2",
        "secondaryColors": [
            "#9f9798",
            "#90837a"
        ]
    },
    {
        "name": "Yhorm's Greatshield",
        "image": "Shields/Yhorm's Greatshield.png",
        "primaryColor": "#8c6d64",
        "secondaryColors": [
            "#5c504d",
            "#50423c"
        ]
    },
    {
        "name": "Anri's Straight Sword",
        "image": "Weapons/Anri's Straight Sword.png",
        "primaryColor": "#50575d",
        "secondaryColors": [
            "#4c5760",
            "#4c555d"
        ]
    },
    {
        "name": "Aquamarine Dagger",
        "image": "Weapons/Aquamarine Dagger.png",
        "primaryColor": "#5b5651",
        "secondaryColors": [
            "#505554",
            "#374c5c"
        ]
    },
    {
        "name": "Arbalest",
        "image": "Weapons/Arbalest.png",
        "primaryColor": "#8e715a",
        "secondaryColors": [
            "#675a4f",
            "#544639"
        ]
    },
    {
        "name": "Archdeacon's Great Staff",
        "image": "Weapons/Archdeacon's Great Staff.png",
        "primaryColor": "#605952",
        "secondaryColors": [
            "#60584c",
            "#5c554b"
        ]
    },
    {
        "name": "Arstor's Spear",
        "image": "Weapons/Arstor's Spear.png",
        "primaryColor": "#675e58",
        "secondaryColors": [
            "#59524e",
            "#49423b"
        ]
    },
    {
        "name": "Astora Greatsword",
        "image": "Weapons/Astora Greatsword.png",
        "primaryColor": "#8f959b",
        "secondaryColors": [
            "#615f5e",
            "#4c4533"
        ]
    },
    {
        "name": "Astora Straight Sword",
        "image": "Weapons/Astora Straight Sword.png",
        "primaryColor": "#696e6d",
        "secondaryColors": [
            "#64615b",
            "#62605c"
        ]
    },
    {
        "name": "Avelyn",
        "image": "Weapons/Avelyn.png",
        "primaryColor": "#906d56",
        "secondaryColors": [
            "#715b4a",
            "#5f4a37"
        ]
    },
    {
        "name": "Bandit's Knife",
        "image": "Weapons/Bandit's Knife.png",
        "primaryColor": "#d0d6dc",
        "secondaryColors": [
            "#95999e",
            "#896e62"
        ]
    },
    {
        "name": "Barbed Straight Sword",
        "image": "Weapons/Barbed Straight Sword.png",
        "primaryColor": "#9a9199",
        "secondaryColors": [
            "#5d555a",
            "#5d5459"
        ]
    },
    {
        "name": "Bastard Sword",
        "image": "Weapons/Bastard Sword.png",
        "primaryColor": "#5f6267",
        "secondaryColors": [
            "#5e6063",
            "#545659"
        ]
    },
    {
        "name": "Battle Axe",
        "image": "Weapons/Battle Axe.png",
        "primaryColor": "#9c9ea2",
        "secondaryColors": [
            "#555556",
            "#545354"
        ]
    },
    {
        "name": "Black Blade",
        "image": "Weapons/Black Blade.png",
        "primaryColor": "#84898d",
        "secondaryColors": [
            "#5f6061",
            "#5e5f60"
        ]
    },
    {
        "name": "Black Bow of Pharis",
        "image": "Weapons/Black Bow of Pharis.png",
        "primaryColor": "#a2a2a3",
        "secondaryColors": [
            "#919192",
            "#686565"
        ]
    },
    {
        "name": "Black Knight Glaive",
        "image": "Weapons/Black Knight Glaive.png",
        "primaryColor": "#999597",
        "secondaryColors": [
            "#5d5754",
            "#48423c"
        ]
    },
    {
        "name": "Black Knight Greataxe",
        "image": "Weapons/Black Knight Greataxe.png",
        "primaryColor": "#a79991",
        "secondaryColors": [
            "#60534b",
            "#50453c"
        ]
    },
    {
        "name": "Black Knight Greatsword",
        "image": "Weapons/Black Knight Greatsword.png",
        "primaryColor": "#877558",
        "secondaryColors": [
            "#685749",
            "#544737"
        ]
    },
    {
        "name": "Black Knight Sword",
        "image": "Weapons/Black Knight Sword.png",
        "primaryColor": "#98928f",
        "secondaryColors": [
            "#615751",
            "#4c433b"
        ]
    },
    {
        "name": "Blacksmith Hammer",
        "image": "Weapons/Blacksmith Hammer.png",
        "primaryColor": "#625c54",
        "secondaryColors": [
            "#5b5753",
            "#4a433c"
        ]
    },
    {
        "name": "Bloodlust",
        "image": "Weapons/Bloodlust.png",
        "primaryColor": "#999a8c",
        "secondaryColors": [
            "#878777",
            "#6a6a66"
        ]
    },
    {
        "name": "Brigand Axe",
        "image": "Weapons/Brigand Axe.png",
        "primaryColor": "#94979a",
        "secondaryColors": [
            "#93705c",
            "#5d5b5a"
        ]
    },
    {
        "name": "Brigand Twindaggers",
        "image": "Weapons/Brigand Twindaggers.png",
        "primaryColor": "#5f5a57",
        "secondaryColors": [
            "#5a5651",
            "#49433b"
        ]
    },
    {
        "name": "Broadsword",
        "image": "Weapons/Broadsword.png",
        "primaryColor": "#979da2",
        "secondaryColors": [
            "#5c5f64",
            "#5a5c5d"
        ]
    },
    {
        "name": "Broken Straight Sword",
        "image": "Weapons/Broken Straight Sword.png",
        "primaryColor": "#9e9489",
        "secondaryColors": [
            "#958577",
            "#666056"
        ]
    },
    {
        "name": "Butcher Knife",
        "image": "Weapons/Butcher Knife.png",
        "primaryColor": "#5c5756",
        "secondaryColors": [
            "#534f4c",
            "#46413e"
        ]
    },
    {
        "name": "Caestus",
        "image": "Weapons/Caestus.png",
        "primaryColor": "#909290",
        "secondaryColors": [
            "#615550",
            "#5b4439"
        ]
    },
    {
        "name": "Caitha's Chime",
        "image": "Weapons/Caitha's Chime.png",
        "primaryColor": "#999395",
        "secondaryColors": [
            "#675955",
            "#635856"
        ]
    },
    {
        "name": "Carthus Curved Greatsword",
        "image": "Weapons/Carthus Curved Greatsword.png",
        "primaryColor": "#67605d",
        "secondaryColors": [
            "#62605e",
            "#615e5a"
        ]
    },
    {
        "name": "Carthus Curved Sword",
        "image": "Weapons/Carthus Curved Sword.png",
        "primaryColor": "#565657",
        "secondaryColors": [
            "#545455",
            "#515458"
        ]
    },
    {
        "name": "Carthus Shotel",
        "image": "Weapons/Carthus Shotel.png",
        "primaryColor": "#5f5f61",
        "secondaryColors": [
            "#5c5a5c",
            "#5e585b"
        ]
    },
    {
        "name": "Cathedral Knight Greatsword",
        "image": "Weapons/Cathedral Knight Greatsword.png",
        "primaryColor": "#838479",
        "secondaryColors": [
            "#5e5e58",
            "#5d5c55"
        ]
    },
    {
        "name": "Chaos Blade",
        "image": "Weapons/Chaos Blade.png",
        "primaryColor": "#525152",
        "secondaryColors": [
            "#4e4e51",
            "#4c4c50"
        ]
    },
    {
        "name": "Claw",
        "image": "Weapons/Claw.png",
        "primaryColor": "#5a5959",
        "secondaryColors": [
            "#4f4d4b",
            "#4d423b"
        ]
    },
    {
        "name": "Claymore",
        "image": "Weapons/Claymore.png",
        "primaryColor": "#8f9598",
        "secondaryColors": [
            "#625f5a",
            "#5a5a54"
        ]
    },
    {
        "name": "Cleric's Candlestick",
        "image": "Weapons/Cleric's Candlestick.png",
        "primaryColor": "#676151",
        "secondaryColors": [
            "#645f51",
            "#4d4839"
        ]
    },
    {
        "name": "Cleric's Sacred Chime",
        "image": "Weapons/Cleric's Sacred Chime.png",
        "primaryColor": "#998b74",
        "secondaryColors": [
            "#675e4e",
            "#4f4639"
        ]
    },
    {
        "name": "Club",
        "image": "Weapons/Club.png",
        "primaryColor": "#6a5c4d",
        "secondaryColors": [
            "#675647",
            "#574739"
        ]
    },
    {
        "name": "Composite Bow",
        "image": "Weapons/Composite Bow.png",
        "primaryColor": "#695b51",
        "secondaryColors": [
            "#64564d",
            "#68544c"
        ]
    },
    {
        "name": "Corvian Greatknife",
        "image": "Weapons/Corvian Greatknife.png",
        "primaryColor": "#665b54",
        "secondaryColors": [
            "#605a56",
            "#51473b"
        ]
    },
    {
        "name": "Court Sorcerer's Staff",
        "image": "Weapons/Court Sorcerer's Staff.png",
        "primaryColor": "#6b5f4d",
        "secondaryColors": [
            "#685b46",
            "#534837"
        ]
    },
    {
        "name": "Crescent Axe",
        "image": "Weapons/Crescent Axe.png",
        "primaryColor": "#8d6e54",
        "secondaryColors": [
            "#715b47",
            "#5e4938"
        ]
    },
    {
        "name": "Crescent Moon Sword",
        "image": "Weapons/Crescent Moon Sword.png",
        "primaryColor": "#969da2",
        "secondaryColors": [
            "#585c5f",
            "#545b5d"
        ]
    },
    {
        "name": "Crow Quills",
        "image": "Weapons/Crow Quills.png",
        "primaryColor": "#91989d",
        "secondaryColors": [
            "#585a5f",
            "#53575b"
        ]
    },
    {
        "name": "Crow Talons",
        "image": "Weapons/Crow Talons.png",
        "primaryColor": "#5f5c5f",
        "secondaryColors": [
            "#5a5759",
            "#5a5757"
        ]
    },
    {
        "name": "Crucifix of the Mad King",
        "image": "Weapons/Crucifix of the Mad King.png",
        "primaryColor": "#8e8e89",
        "secondaryColors": [
            "#64625d",
            "#605f59"
        ]
    },
    {
        "name": "Crystal Chime",
        "image": "Weapons/Crystal Chime.png",
        "primaryColor": "#969c9b",
        "secondaryColors": [
            "#595f5d",
            "#5a5e5a"
        ]
    },
    {
        "name": "Crystal Sage's Rapier",
        "image": "Weapons/Crystal Sage's Rapier.png",
        "primaryColor": "#a09f9c",
        "secondaryColors": [
            "#6a675f",
            "#69665f"
        ]
    },
    {
        "name": "Dagger",
        "image": "Weapons/Dagger.png",
        "primaryColor": "#939aa2",
        "secondaryColors": [
            "#976355",
            "#5d5857"
        ]
    },
    {
        "name": "Dancer's Enchanted Swords",
        "image": "Weapons/Dancer's Enchanted Swords.png",
        "primaryColor": "#a09896",
        "secondaryColors": [
            "#5c595b",
            "#59555d"
        ]
    },
    {
        "name": "Dark Hand",
        "image": "Weapons/Dark Hand.png",
        "primaryColor": "#900107",
        "secondaryColors": [
            "#5a080c",
            "#500a0d"
        ]
    },
    {
        "name": "Dark Sword",
        "image": "Weapons/Dark Sword.png",
        "primaryColor": "#959492",
        "secondaryColors": [
            "#616161",
            "#595955"
        ]
    },
    {
        "name": "Darkdrift",
        "image": "Weapons/Darkdrift.png",
        "primaryColor": "#879eac",
        "secondaryColors": [
            "#788e9a",
            "#585c5b"
        ]
    },
    {
        "name": "Darkmoon Longbow",
        "image": "Weapons/Darkmoon Longbow.png",
        "primaryColor": "#958b6f",
        "secondaryColors": [
            "#6a604b",
            "#514735"
        ]
    },
    {
        "name": "Demon's Fist",
        "image": "Weapons/Demon's Fist.png",
        "primaryColor": "#938d8c",
        "secondaryColors": [
            "#676363",
            "#615c5b"
        ]
    },
    {
        "name": "Demon's Greataxe",
        "image": "Weapons/Demon's Greataxe.png",
        "primaryColor": "#9a9695",
        "secondaryColors": [
            "#847a75",
            "#68625f"
        ]
    },
    {
        "name": "Demon's Scar",
        "image": "Weapons/Demon's Scar.png",
        "primaryColor": "#fae89b",
        "secondaryColors": [
            "#f9d669",
            "#db6c18"
        ]
    },
    {
        "name": "Dragon Tooth",
        "image": "Weapons/Dragon Tooth.png",
        "primaryColor": "#8f8c8b",
        "secondaryColors": [
            "#625e5b",
            "#575556"
        ]
    },
    {
        "name": "Dragonrider Bow",
        "image": "Weapons/Dragonrider Bow.png",
        "primaryColor": "#999690",
        "secondaryColors": [
            "#5d5b59",
            "#5a5956"
        ]
    },
    {
        "name": "Dragonslayer Greataxe",
        "image": "Weapons/Dragonslayer Greataxe.png",
        "primaryColor": "#93989d",
        "secondaryColors": [
            "#7d8287",
            "#56595a"
        ]
    },
    {
        "name": "Dragonslayer Greatbow",
        "image": "Weapons/Dragonslayer Greatbow.png",
        "primaryColor": "#af9a86",
        "secondaryColors": [
            "#9f8975",
            "#8b7766"
        ]
    },
    {
        "name": "Dragonslayer Spear",
        "image": "Weapons/Dragonslayer Spear.png",
        "primaryColor": "#65708d",
        "secondaryColors": [
            "#5b5957",
            "#504736"
        ]
    },
    {
        "name": "Dragonslayer Swordspear",
        "image": "Weapons/Dragonslayer Swordspear.png",
        "primaryColor": "#aea396",
        "secondaryColors": [
            "#988770",
            "#89745c"
        ]
    },
    {
        "name": "Dragonslayer's Axe",
        "image": "Weapons/Dragonslayer's Axe.png",
        "primaryColor": "#9da1a4",
        "secondaryColors": [
            "#605c59",
            "#595552"
        ]
    },
    {
        "name": "Drakeblood Greatsword",
        "image": "Weapons/Drakeblood Greatsword.png",
        "primaryColor": "#929496",
        "secondaryColors": [
            "#5d5d5c",
            "#5c5d5b"
        ]
    },
    {
        "name": "Drang Hammers",
        "image": "Weapons/Drang Hammers.png",
        "primaryColor": "#909190",
        "secondaryColors": [
            "#525153",
            "#403d3d"
        ]
    },
    {
        "name": "Drang Twinspears",
        "image": "Weapons/Drang Twinspears.png",
        "primaryColor": "#9c9e9e",
        "secondaryColors": [
            "#585a59",
            "#575858"
        ]
    },
    {
        "name": "Earth Seeker",
        "image": "Weapons/Earth Seeker.png",
        "primaryColor": "#768a85",
        "secondaryColors": [
            "#55625c",
            "#3b4945"
        ]
    },
    {
        "name": "Eleonora",
        "image": "Weapons/Eleonora.png",
        "primaryColor": "#aaa491",
        "secondaryColors": [
            "#908875",
            "#837a68"
        ]
    },
    {
        "name": "Estoc",
        "image": "Weapons/Estoc.png",
        "primaryColor": "#989da2",
        "secondaryColors": [
            "#5c5856",
            "#5b5856"
        ]
    },
    {
        "name": "Executioner's Greatsword",
        "image": "Weapons/Executioner's Greatsword.png",
        "primaryColor": "#5f5b50",
        "secondaryColors": [
            "#5e5a51",
            "#494438"
        ]
    },
    {
        "name": "Exile Greatsword",
        "image": "Weapons/Exile Greatsword.png",
        "primaryColor": "#9e9c91",
        "secondaryColors": [
            "#878479",
            "#625a56"
        ]
    },
    {
        "name": "Falchion",
        "image": "Weapons/Falchion.png",
        "primaryColor": "#62615d",
        "secondaryColors": [
            "#5f5f5c",
            "#5e5e5b"
        ]
    },
    {
        "name": "Farron Greatsword",
        "image": "Weapons/Farron Greatsword.png",
        "primaryColor": "#94989b",
        "secondaryColors": [
            "#535250",
            "#4f4638"
        ]
    },
    {
        "name": "Firelink Greatsword",
        "image": "Weapons/Firelink Greatsword.png",
        "primaryColor": "#5d5351",
        "secondaryColors": [
            "#634338",
            "#4e352c"
        ]
    },
    {
        "name": "Flamberge",
        "image": "Weapons/Flamberge.png",
        "primaryColor": "#5e5f5e",
        "secondaryColors": [
            "#56585a",
            "#555654"
        ]
    },
    {
        "name": "Follower Javelin",
        "image": "Weapons/Follower Javelin.png",
        "primaryColor": "#dde0e2",
        "secondaryColors": [
            "#94989f",
            "#545763"
        ]
    },
    {
        "name": "Follower Sabre",
        "image": "Weapons/Follower Sabre.png",
        "primaryColor": "#8c9599",
        "secondaryColors": [
            "#5c5f5d",
            "#595b58"
        ]
    },
    {
        "name": "Follower Torch",
        "image": "Weapons/Follower Torch.png",
        "primaryColor": "#fcf75a",
        "secondaryColors": [
            "#fae41c",
            "#f7a614"
        ]
    },
    {
        "name": "Four-Pronged Plow",
        "image": "Weapons/Four-Pronged Plow.png",
        "primaryColor": "#625b58",
        "secondaryColors": [
            "#5e5853",
            "#524439"
        ]
    },
    {
        "name": "Frayed Blade",
        "image": "Weapons/Frayed Blade.png",
        "primaryColor": "#4c4e51",
        "secondaryColors": [
            "#494c4e",
            "#4a4b4c"
        ]
    },
    {
        "name": "Friede's Great Scythe",
        "image": "Weapons/Friede's Great Scythe.png",
        "primaryColor": "#8d9ca8",
        "secondaryColors": [
            "#798692",
            "#5b6060"
        ]
    },
    {
        "name": "Fume Ultra Greatsword",
        "image": "Weapons/Fume Ultra Greatsword.png",
        "primaryColor": "#505154",
        "secondaryColors": [
            "#4c4f52",
            "#3e4143"
        ]
    },
    {
        "name": "Gael's Greatsword",
        "image": "Weapons/Gael's Greatsword.png",
        "primaryColor": "#8a635c",
        "secondaryColors": [
            "#64524e",
            "#5c443a"
        ]
    },
    {
        "name": "Gargoyle Flame Hammer",
        "image": "Weapons/Gargoyle Flame Hammer.png",
        "primaryColor": "#929496",
        "secondaryColors": [
            "#5b5b5b",
            "#555555"
        ]
    },
    {
        "name": "Gargoyle Flame Spear",
        "image": "Weapons/Gargoyle Flame Spear.png",
        "primaryColor": "#909091",
        "secondaryColors": [
            "#595958",
            "#585858"
        ]
    },
    {
        "name": "Glaive",
        "image": "Weapons/Glaive.png",
        "primaryColor": "#a69c99",
        "secondaryColors": [
            "#8c7264",
            "#5b514d"
        ]
    },
    {
        "name": "Golden Ritual Spear",
        "image": "Weapons/Golden Ritual Spear.png",
        "primaryColor": "#87775b",
        "secondaryColors": [
            "#6c614b",
            "#564935"
        ]
    },
    {
        "name": "Gotthard Twinswords",
        "image": "Weapons/Gotthard Twinswords.png",
        "primaryColor": "#898c8c",
        "secondaryColors": [
            "#68655c",
            "#534a35"
        ]
    },
    {
        "name": "Great Club",
        "image": "Weapons/Great Club.png",
        "primaryColor": "#b09f8b",
        "secondaryColors": [
            "#9c8976",
            "#897664"
        ]
    },
    {
        "name": "Great Corvian Scythe",
        "image": "Weapons/Great Corvian Scythe.png",
        "primaryColor": "#5d5653",
        "secondaryColors": [
            "#575554",
            "#4c423c"
        ]
    },
    {
        "name": "Great Mace",
        "image": "Weapons/Great Mace.png",
        "primaryColor": "#5e5c5d",
        "secondaryColors": [
            "#595554",
            "#585554"
        ]
    },
    {
        "name": "Great Machete",
        "image": "Weapons/Great Machete.png",
        "primaryColor": "#675c59",
        "secondaryColors": [
            "#64554f",
            "#5a5250"
        ]
    },
    {
        "name": "Great Scythe",
        "image": "Weapons/Great Scythe.png",
        "primaryColor": "#956b4e",
        "secondaryColors": [
            "#545253",
            "#654935"
        ]
    },
    {
        "name": "Great Wooden Hammer",
        "image": "Weapons/Great Wooden Hammer.png",
        "primaryColor": "#715c48",
        "secondaryColors": [
            "#5e4935",
            "#52342a"
        ]
    },
    {
        "name": "Greataxe",
        "image": "Weapons/Greataxe.png",
        "primaryColor": "#d2d4d6",
        "secondaryColors": [
            "#959698",
            "#636262"
        ]
    },
    {
        "name": "Greatlance",
        "image": "Weapons/Greatlance.png",
        "primaryColor": "#8b8f95",
        "secondaryColors": [
            "#615f5c",
            "#5c5d60"
        ]
    },
    {
        "name": "Greatsword of Judgment",
        "image": "Weapons/Greatsword of Judgment.png",
        "primaryColor": "#9097a0",
        "secondaryColors": [
            "#717886",
            "#56595c"
        ]
    },
    {
        "name": "Greatsword",
        "image": "Weapons/Greatsword.png",
        "primaryColor": "#5e5b59",
        "secondaryColors": [
            "#5c5956",
            "#514f4d"
        ]
    },
    {
        "name": "Gundyr's Halberd",
        "image": "Weapons/Gundyr's Halberd.png",
        "primaryColor": "#989a9b",
        "secondaryColors": [
            "#5d5d5b",
            "#565655"
        ]
    },
    {
        "name": "Halberd",
        "image": "Weapons/Halberd.png",
        "primaryColor": "#d9dde2",
        "secondaryColors": [
            "#94979b",
            "#64615f"
        ]
    },
    {
        "name": "Hand Axe",
        "image": "Weapons/Hand Axe.png",
        "primaryColor": "#8e9093",
        "secondaryColors": [
            "#8a6f60",
            "#635c59"
        ]
    },
    {
        "name": "Handmaid's Dagger",
        "image": "Weapons/Handmaid's Dagger.png",
        "primaryColor": "#a3918f",
        "secondaryColors": [
            "#92726c",
            "#615a5a"
        ]
    },
    {
        "name": "Harald Curved Greatsword",
        "image": "Weapons/Harald Curved Greatsword.png",
        "primaryColor": "#857462",
        "secondaryColors": [
            "#615951",
            "#55473b"
        ]
    },
    {
        "name": "Harpe",
        "image": "Weapons/Harpe.png",
        "primaryColor": "#a29b9c",
        "secondaryColors": [
            "#625753",
            "#5c5857"
        ]
    },
    {
        "name": "Heavy Crossbow",
        "image": "Weapons/Heavy Crossbow.png",
        "primaryColor": "#8b6a56",
        "secondaryColors": [
            "#5d5958",
            "#5d5653"
        ]
    },
    {
        "name": "Heretic's Staff",
        "image": "Weapons/Heretic's Staff.png",
        "primaryColor": "#aea48f",
        "secondaryColors": [
            "#948a76",
            "#656559"
        ]
    },
    {
        "name": "Heysel Pick",
        "image": "Weapons/Heysel Pick.png",
        "primaryColor": "#9f8d65",
        "secondaryColors": [
            "#877656",
            "#6a6048"
        ]
    },
    {
        "name": "Hollowslayer Greatsword",
        "image": "Weapons/Hollowslayer Greatsword.png",
        "primaryColor": "#867466",
        "secondaryColors": [
            "#655950",
            "#615751"
        ]
    },
    {
        "name": "Immolation Tinder",
        "image": "Weapons/Immolation Tinder.png",
        "primaryColor": "#909499",
        "secondaryColors": [
            "#5a5a5b",
            "#535558"
        ]
    },
    {
        "name": "Irithyll Rapier",
        "image": "Weapons/Irithyll Rapier.png",
        "primaryColor": "#5a5859",
        "secondaryColors": [
            "#585655",
            "#4f4c4b"
        ]
    },
    {
        "name": "Irithyll Straight Sword",
        "image": "Weapons/Irithyll Straight Sword.png",
        "primaryColor": "#ccd6e0",
        "secondaryColors": [
            "#aeb9c6",
            "#959ea7"
        ]
    },
    {
        "name": "Izalith Staff",
        "image": "Weapons/Izalith Staff.png",
        "primaryColor": "#665f5a",
        "secondaryColors": [
            "#605955",
            "#49433b"
        ]
    },
    {
        "name": "Knight's Crossbow",
        "image": "Weapons/Knight's Crossbow.png",
        "primaryColor": "#94959a",
        "secondaryColors": [
            "#685c58",
            "#574638"
        ]
    },
    {
        "name": "Large Club",
        "image": "Weapons/Large Club.png",
        "primaryColor": "#a0896c",
        "secondaryColors": [
            "#8a755b",
            "#705f4a"
        ]
    },
    {
        "name": "Ledo's Great Hammer",
        "image": "Weapons/Ledo's Great Hammer.png",
        "primaryColor": "#514f4f",
        "secondaryColors": [
            "#4e4d4c",
            "#484338"
        ]
    },
    {
        "name": "Light Crossbow",
        "image": "Weapons/Light Crossbow.png",
        "primaryColor": "#8c6b49",
        "secondaryColors": [
            "#655c54",
            "#5d5854"
        ]
    },
    {
        "name": "Long Sword",
        "image": "Weapons/Long Sword.png",
        "primaryColor": "#64686f",
        "secondaryColors": [
            "#606467",
            "#5e6166"
        ]
    },
    {
        "name": "Longbow",
        "image": "Weapons/Longbow.png",
        "primaryColor": "#686458",
        "secondaryColors": [
            "#5d5b4e",
            "#615448"
        ]
    },
    {
        "name": "Lorian's Greatsword",
        "image": "Weapons/Lorian's Greatsword.png",
        "primaryColor": "#56514d",
        "secondaryColors": [
            "#574539",
            "#4b372f"
        ]
    },
    {
        "name": "Lothric Knight Greatsword",
        "image": "Weapons/Lothric Knight Greatsword.png",
        "primaryColor": "#919396",
        "secondaryColors": [
            "#64615f",
            "#4a4438"
        ]
    },
    {
        "name": "Lothric Knight Long Spear",
        "image": "Weapons/Lothric Knight Long Spear.png",
        "primaryColor": "#99979a",
        "secondaryColors": [
            "#635d5d",
            "#635a58"
        ]
    },
    {
        "name": "Lothric Knight Sword",
        "image": "Weapons/Lothric Knight Sword.png",
        "primaryColor": "#d4d8dc",
        "secondaryColors": [
            "#9a9b9a",
            "#63615a"
        ]
    },
    {
        "name": "Lothric War Banner",
        "image": "Weapons/Lothric War Banner.png",
        "primaryColor": "#66524e",
        "secondaryColors": [
            "#64514d",
            "#4a3630"
        ]
    },
    {
        "name": "Lothric's Holy Sword",
        "image": "Weapons/Lothric's Holy Sword.png",
        "primaryColor": "#d4d1cd",
        "secondaryColors": [
            "#a19e9a",
            "#857869"
        ]
    },
    {
        "name": "Lucerne",
        "image": "Weapons/Lucerne.png",
        "primaryColor": "#9b9da2",
        "secondaryColors": [
            "#606166",
            "#555557"
        ]
    },
    {
        "name": "Mace",
        "image": "Weapons/Mace.png",
        "primaryColor": "#989a9d",
        "secondaryColors": [
            "#5c5a5f",
            "#575353"
        ]
    },
    {
        "name": "Mail Breaker",
        "image": "Weapons/Mail Breaker.png",
        "primaryColor": "#9e9f94",
        "secondaryColors": [
            "#605f5e",
            "#5f5e5d"
        ]
    },
    {
        "name": "Man Serpent Hatchet",
        "image": "Weapons/Man Serpent Hatchet.png",
        "primaryColor": "#5b5a59",
        "secondaryColors": [
            "#595756",
            "#575755"
        ]
    },
    {
        "name": "Man-grub's Staff",
        "image": "Weapons/Man-grub's Staff.png",
        "primaryColor": "#867753",
        "secondaryColors": [
            "#6d6147",
            "#584c35"
        ]
    },
    {
        "name": "Manikin Claws",
        "image": "Weapons/Manikin Claws.png",
        "primaryColor": "#5b5a5e",
        "secondaryColors": [
            "#545455",
            "#525252"
        ]
    },
    {
        "name": "Mendicant's Staff",
        "image": "Weapons/Mendicant's Staff.png",
        "primaryColor": "#695f50",
        "secondaryColors": [
            "#675c4f",
            "#544733"
        ]
    },
    {
        "name": "Millwood Battle Axe",
        "image": "Weapons/Millwood Battle Axe.png",
        "primaryColor": "#969591",
        "secondaryColors": [
            "#575b5a",
            "#5a5959"
        ]
    },
    {
        "name": "Millwood Greatbow",
        "image": "Weapons/Millwood Greatbow.png",
        "primaryColor": "#524f49",
        "secondaryColors": [
            "#53502e",
            "#46433c"
        ]
    },
    {
        "name": "Moonlight Greatsword",
        "image": "Weapons/Moonlight Greatsword.png",
        "primaryColor": "#6e8791",
        "secondaryColors": [
            "#627a84",
            "#556162"
        ]
    },
    {
        "name": "Morion Blade",
        "image": "Weapons/Morion Blade.png",
        "primaryColor": "#595956",
        "secondaryColors": [
            "#585758",
            "#565556"
        ]
    },
    {
        "name": "Morne's Great Hammer",
        "image": "Weapons/Morne's Great Hammer.png",
        "primaryColor": "#58595a",
        "secondaryColors": [
            "#535151",
            "#514f50"
        ]
    },
    {
        "name": "Morning Star",
        "image": "Weapons/Morning Star.png",
        "primaryColor": "#919295",
        "secondaryColors": [
            "#5e5e60",
            "#5a5a5b"
        ]
    },
    {
        "name": "Murakumo",
        "image": "Weapons/Murakumo.png",
        "primaryColor": "#6f6863",
        "secondaryColors": [
            "#615b59",
            "#4b423d"
        ]
    },
    {
        "name": "Murky Hand Scythe",
        "image": "Weapons/Murky Hand Scythe.png",
        "primaryColor": "#5d5b58",
        "secondaryColors": [
            "#545454",
            "#515252"
        ]
    },
    {
        "name": "Murky Longstaff",
        "image": "Weapons/Murky Longstaff.png",
        "primaryColor": "#65615e",
        "secondaryColors": [
            "#625e59",
            "#595753"
        ]
    },
    {
        "name": "Notched Whip",
        "image": "Weapons/Notched Whip.png",
        "primaryColor": "#53535a",
        "secondaryColors": [
            "#525157",
            "#525153"
        ]
    },
    {
        "name": "Old King's Great Hammer",
        "image": "Weapons/Old King's Great Hammer.png",
        "primaryColor": "#8c7165",
        "secondaryColors": [
            "#615f5e",
            "#5e5755"
        ]
    },
    {
        "name": "Old Wolf Curved Sword",
        "image": "Weapons/Old Wolf Curved Sword.png",
        "primaryColor": "#625f5b",
        "secondaryColors": [
            "#595551",
            "#585552"
        ]
    },
    {
        "name": "Onikiri and Ubadachi",
        "image": "Weapons/Onikiri and Ubadachi.png",
        "primaryColor": "#a38c6b",
        "secondaryColors": [
            "#8a7559",
            "#676257"
        ]
    },
    {
        "name": "Onislayer Greatbow",
        "image": "Weapons/Onislayer Greatbow.png",
        "primaryColor": "#888d90",
        "secondaryColors": [
            "#5b5f62",
            "#575b5e"
        ]
    },
    {
        "name": "Onyx Blade",
        "image": "Weapons/Onyx Blade.png",
        "primaryColor": "#656157",
        "secondaryColors": [
            "#5f594c",
            "#4f4639"
        ]
    },
    {
        "name": "Painting Guardian's Curved Sword",
        "image": "Weapons/Painting Guardian's Curved Sword.png",
        "primaryColor": "#989086",
        "secondaryColors": [
            "#676462",
            "#65625d"
        ]
    },
    {
        "name": "Parrying Dagger",
        "image": "Weapons/Parrying Dagger.png",
        "primaryColor": "#9da2a4",
        "secondaryColors": [
            "#675d52",
            "#4e4437"
        ]
    },
    {
        "name": "Partizan",
        "image": "Weapons/Partizan.png",
        "primaryColor": "#e0e2e3",
        "secondaryColors": [
            "#9c9ea0",
            "#89534d"
        ]
    },
    {
        "name": "Pickaxe",
        "image": "Weapons/Pickaxe.png",
        "primaryColor": "#928f8b",
        "secondaryColors": [
            "#645a51",
            "#53463b"
        ]
    },
    {
        "name": "Pike (DaSIII)",
        "image": "Weapons/Pike (DaSIII).png",
        "primaryColor": "#e1ded5",
        "secondaryColors": [
            "#c6c3b9",
            "#a3a199"
        ]
    },
    {
        "name": "Pontiff Knight Curved Sword",
        "image": "Weapons/Pontiff Knight Curved Sword.png",
        "primaryColor": "#595b5c",
        "secondaryColors": [
            "#595a5b",
            "#545455"
        ]
    },
    {
        "name": "Pontiff Knight Great Scythe",
        "image": "Weapons/Pontiff Knight Great Scythe.png",
        "primaryColor": "#94979d",
        "secondaryColors": [
            "#5f6367",
            "#5f6164"
        ]
    },
    {
        "name": "Preacher's Right Arm",
        "image": "Weapons/Preacher's Right Arm.png",
        "primaryColor": "#9a9896",
        "secondaryColors": [
            "#9c9793",
            "#625f5d"
        ]
    },
    {
        "name": "Priest's Chime",
        "image": "Weapons/Priest's Chime.png",
        "primaryColor": "#9b8f71",
        "secondaryColors": [
            "#665f4e",
            "#534833"
        ]
    },
    {
        "name": "Profaned Greatsword",
        "image": "Weapons/Profaned Greatsword.png",
        "primaryColor": "#857966",
        "secondaryColors": [
            "#685e4f",
            "#4f4537"
        ]
    },
    {
        "name": "Pyromancer's Parting Flame",
        "image": "Weapons/Pyromancer's Parting Flame.png",
        "primaryColor": "#e6a852",
        "secondaryColors": [
            "#d0602c",
            "#a6552b"
        ]
    },
    {
        "name": "Pyromancy Flame",
        "image": "Weapons/Pyromancy Flame.png",
        "primaryColor": "#e1581b",
        "secondaryColors": [
            "#a94c2f",
            "#d42b10"
        ]
    },
    {
        "name": "Quakestone Hammer",
        "image": "Weapons/Quakestone Hammer.png",
        "primaryColor": "#645f5c",
        "secondaryColors": [
            "#575650",
            "#43423c"
        ]
    },
    {
        "name": "Rapier",
        "image": "Weapons/Rapier.png",
        "primaryColor": "#939498",
        "secondaryColors": [
            "#5d5f62",
            "#5f5d5c"
        ]
    },
    {
        "name": "Red Hilted Halberd",
        "image": "Weapons/Red Hilted Halberd.png",
        "primaryColor": "#909092",
        "secondaryColors": [
            "#615e5c",
            "#555452"
        ]
    },
    {
        "name": "Reinforced Club",
        "image": "Weapons/Reinforced Club.png",
        "primaryColor": "#ad9d91",
        "secondaryColors": [
            "#958579",
            "#605852"
        ]
    },
    {
        "name": "Repeating Crossbow",
        "image": "Weapons/Repeating Crossbow.png",
        "primaryColor": "#605353",
        "secondaryColors": [
            "#594e4b",
            "#54433b"
        ]
    },
    {
        "name": "Ricard's Rapier",
        "image": "Weapons/Ricard's Rapier.png",
        "primaryColor": "#6a5e4a",
        "secondaryColors": [
            "#5b4d35",
            "#584c35"
        ]
    },
    {
        "name": "Ringed Knight Paired Greatswords",
        "image": "Weapons/Ringed Knight Paired Greatswords.png",
        "primaryColor": "#595754",
        "secondaryColors": [
            "#575450",
            "#4f433b"
        ]
    },
    {
        "name": "Ringed Knight Spear",
        "image": "Weapons/Ringed Knight Spear.png",
        "primaryColor": "#919496",
        "secondaryColors": [
            "#5f5e5e",
            "#515150"
        ]
    },
    {
        "name": "Ringed Knight Straight Sword",
        "image": "Weapons/Ringed Knight Straight Sword.png",
        "primaryColor": "#515552",
        "secondaryColors": [
            "#4a4a49",
            "#474847"
        ]
    },
    {
        "name": "Rose of Ariandel",
        "image": "Weapons/Rose of Ariandel.png",
        "primaryColor": "#615a53",
        "secondaryColors": [
            "#5d544e",
            "#4c433c"
        ]
    },
    {
        "name": "Rotten Ghru Curved Sword",
        "image": "Weapons/Rotten Ghru Curved Sword.png",
        "primaryColor": "#8a6f62",
        "secondaryColors": [
            "#695851",
            "#57453b"
        ]
    },
    {
        "name": "Rotten Ghru Dagger",
        "image": "Weapons/Rotten Ghru Dagger.png",
        "primaryColor": "#887269",
        "secondaryColors": [
            "#675853",
            "#5a504c"
        ]
    },
    {
        "name": "Rotten Ghru Spear",
        "image": "Weapons/Rotten Ghru Spear.png",
        "primaryColor": "#655d59",
        "secondaryColors": [
            "#665a54",
            "#605956"
        ]
    },
    {
        "name": "Sacred Chime of Filianore",
        "image": "Weapons/Sacred Chime of Filianore.png",
        "primaryColor": "#d2dadd",
        "secondaryColors": [
            "#979ea3",
            "#565b5c"
        ]
    },
    {
        "name": "Sage's Crystal Staff",
        "image": "Weapons/Sage's Crystal Staff.png",
        "primaryColor": "#5f5d5c",
        "secondaryColors": [
            "#5a5855",
            "#585653"
        ]
    },
    {
        "name": "Saint Bident",
        "image": "Weapons/Saint Bident.png",
        "primaryColor": "#9b9b99",
        "secondaryColors": [
            "#656460",
            "#5e5d5b"
        ]
    },
    {
        "name": "Saint-tree Bellvine",
        "image": "Weapons/Saint-tree Bellvine.png",
        "primaryColor": "#ede3d3",
        "secondaryColors": [
            "#a89b8f",
            "#857871"
        ]
    },
    {
        "name": "Scholar's Candlestick",
        "image": "Weapons/Scholar's Candlestick.png",
        "primaryColor": "#eaddcd",
        "secondaryColors": [
            "#decab4",
            "#ccb39a"
        ]
    },
    {
        "name": "Scimitar",
        "image": "Weapons/Scimitar.png",
        "primaryColor": "#9a9ea0",
        "secondaryColors": [
            "#8a7362",
            "#625f5d"
        ]
    },
    {
        "name": "Sellsword Twinblades",
        "image": "Weapons/Sellsword Twinblades.png",
        "primaryColor": "#595857",
        "secondaryColors": [
            "#54514d",
            "#484339"
        ]
    },
    {
        "name": "Short Bow",
        "image": "Weapons/Short Bow.png",
        "primaryColor": "#afa89b",
        "secondaryColors": [
            "#ada08b",
            "#a49f92"
        ]
    },
    {
        "name": "Shortsword",
        "image": "Weapons/Shortsword.png",
        "primaryColor": "#8a8f92",
        "secondaryColors": [
            "#636265",
            "#5e5e5b"
        ]
    },
    {
        "name": "Shotel",
        "image": "Weapons/Shotel.png",
        "primaryColor": "#64605d",
        "secondaryColors": [
            "#635b55",
            "#5b5754"
        ]
    },
    {
        "name": "Smough's Great Hammer",
        "image": "Weapons/Smough's Great Hammer.png",
        "primaryColor": "#9a9169",
        "secondaryColors": [
            "#67614b",
            "#524a36"
        ]
    },
    {
        "name": "Sniper Crossbow",
        "image": "Weapons/Sniper Crossbow.png",
        "primaryColor": "#9b9995",
        "secondaryColors": [
            "#5e5c5b",
            "#5e5956"
        ]
    },
    {
        "name": "Soldering Iron",
        "image": "Weapons/Soldering Iron.png",
        "primaryColor": "#ae4514",
        "secondaryColors": [
            "#953310",
            "#621d13"
        ]
    },
    {
        "name": "Sorcerer's Staff",
        "image": "Weapons/Sorcerer's Staff.png",
        "primaryColor": "#63574d",
        "secondaryColors": [
            "#60544a",
            "#4f453b"
        ]
    },
    {
        "name": "Spear",
        "image": "Weapons/Spear.png",
        "primaryColor": "#9399a0",
        "secondaryColors": [
            "#645351",
            "#614a3a"
        ]
    },
    {
        "name": "Spiked Mace",
        "image": "Weapons/Spiked Mace.png",
        "primaryColor": "#919396",
        "secondaryColors": [
            "#585657",
            "#525354"
        ]
    },
    {
        "name": "Splitleaf Greatsword",
        "image": "Weapons/Splitleaf Greatsword.png",
        "primaryColor": "#555047",
        "secondaryColors": [
            "#45433b",
            "#3d4139"
        ]
    },
    {
        "name": "Spotted Whip",
        "image": "Weapons/Spotted Whip.png",
        "primaryColor": "#a09795",
        "secondaryColors": [
            "#5c5553",
            "#544539"
        ]
    },
    {
        "name": "Storm Curved Sword",
        "image": "Weapons/Storm Curved Sword.png",
        "primaryColor": "#dfe2e3",
        "secondaryColors": [
            "#9ea29f",
            "#545557"
        ]
    },
    {
        "name": "Storm Ruler",
        "image": "Weapons/Storm Ruler.png",
        "primaryColor": "#555454",
        "secondaryColors": [
            "#525453",
            "#525151"
        ]
    },
    {
        "name": "Storyteller's Staff",
        "image": "Weapons/Storyteller's Staff.png",
        "primaryColor": "#9c8b73",
        "secondaryColors": [
            "#877865",
            "#655c50"
        ]
    },
    {
        "name": "Sunlight Straight Sword",
        "image": "Weapons/Sunlight Straight Sword.png",
        "primaryColor": "#9d9d9b",
        "secondaryColors": [
            "#666665",
            "#605d5a"
        ]
    },
    {
        "name": "Tailbone Short Sword",
        "image": "Weapons/Tailbone Short Sword.png",
        "primaryColor": "#9c9e9b",
        "secondaryColors": [
            "#5e6158",
            "#5f5f57"
        ]
    },
    {
        "name": "Tailbone Spear",
        "image": "Weapons/Tailbone Spear.png",
        "primaryColor": "#e1e0e2",
        "secondaryColors": [
            "#9ea09d",
            "#5b5b56"
        ]
    },
    {
        "name": "Thrall Axe",
        "image": "Weapons/Thrall Axe.png",
        "primaryColor": "#9b9996",
        "secondaryColors": [
            "#86736f",
            "#6a615c"
        ]
    },
    {
        "name": "Torch",
        "image": "Weapons/Torch.png",
        "primaryColor": "#fcf95a",
        "secondaryColors": [
            "#fae419",
            "#f7a512"
        ]
    },
    {
        "name": "Twin Princes' Greatsword",
        "image": "Weapons/Twin Princes' Greatsword.png",
        "primaryColor": "#99968e",
        "secondaryColors": [
            "#635c57",
            "#4b433b"
        ]
    },
    {
        "name": "Uchigatana",
        "image": "Weapons/Uchigatana.png",
        "primaryColor": "#636263",
        "secondaryColors": [
            "#626263",
            "#636162"
        ]
    },
    {
        "name": "Valorheart",
        "image": "Weapons/Valorheart.png",
        "primaryColor": "#a19e92",
        "secondaryColors": [
            "#8d8775",
            "#635f55"
        ]
    },
    {
        "name": "Vordt's Great Hammer",
        "image": "Weapons/Vordt's Great Hammer.png",
        "primaryColor": "#585759",
        "secondaryColors": [
            "#585758",
            "#515153"
        ]
    },
    {
        "name": "Warden Twinblades",
        "image": "Weapons/Warden Twinblades.png",
        "primaryColor": "#948e8f",
        "secondaryColors": [
            "#605e5d",
            "#5f5857"
        ]
    },
    {
        "name": "Warpick",
        "image": "Weapons/Warpick.png",
        "primaryColor": "#5d5b5c",
        "secondaryColors": [
            "#585352",
            "#56443b"
        ]
    },
    {
        "name": "Washing Pole",
        "image": "Weapons/Washing Pole.png",
        "primaryColor": "#585753",
        "secondaryColors": [
            "#555554",
            "#56524b"
        ]
    },
    {
        "name": "Whip",
        "image": "Weapons/Whip.png",
        "primaryColor": "#9f8e89",
        "secondaryColors": [
            "#887773",
            "#635855"
        ]
    },
    {
        "name": "White Birch Bow",
        "image": "Weapons/White Birch Bow.png",
        "primaryColor": "#aea48a",
        "secondaryColors": [
            "#998e72",
            "#6a6760"
        ]
    },
    {
        "name": "Winged Knight Halberd",
        "image": "Weapons/Winged Knight Halberd.png",
        "primaryColor": "#979ba1",
        "secondaryColors": [
            "#615b5a",
            "#463b35"
        ]
    },
    {
        "name": "Winged Knight Twinaxes",
        "image": "Weapons/Winged Knight Twinaxes.png",
        "primaryColor": "#989a9d",
        "secondaryColors": [
            "#5b5957",
            "#47423b"
        ]
    },
    {
        "name": "Winged Spear",
        "image": "Weapons/Winged Spear.png",
        "primaryColor": "#94979c",
        "secondaryColors": [
            "#656260",
            "#5b5550"
        ]
    },
    {
        "name": "Witch's Locks",
        "image": "Weapons/Witch's Locks.png",
        "primaryColor": "#8a8a89",
        "secondaryColors": [
            "#575656",
            "#47423e"
        ]
    },
    {
        "name": "Witchtree Branch",
        "image": "Weapons/Witchtree Branch.png",
        "primaryColor": "#a6a39d",
        "secondaryColors": [
            "#a5a19c",
            "#a39e99"
        ]
    },
    {
        "name": "Wolf Knight's Greatsword",
        "image": "Weapons/Wolf Knight's Greatsword.png",
        "primaryColor": "#57565a",
        "secondaryColors": [
            "#525152",
            "#45423d"
        ]
    },
    {
        "name": "Wolnir's Holy Sword",
        "image": "Weapons/Wolnir's Holy Sword.png",
        "primaryColor": "#676052",
        "secondaryColors": [
            "#605d53",
            "#5d5a52"
        ]
    },
    {
        "name": "Yhorm's Great Machete",
        "image": "Weapons/Yhorm's Great Machete.png",
        "primaryColor": "#94908e",
        "secondaryColors": [
            "#605b5b",
            "#45423d"
        ]
    },
    {
        "name": "Yorshka's Chime",
        "image": "Weapons/Yorshka's Chime.png",
        "primaryColor": "#d3cbb1",
        "secondaryColors": [
            "#aba594",
            "#6a614f"
        ]
    },
    {
        "name": "Yorshka's Spear",
        "image": "Weapons/Yorshka's Spear.png",
        "primaryColor": "#a39b91",
        "secondaryColors": [
            "#63594f",
            "#50443a"
        ]
    },
    {
        "name": "Zweihander",
        "image": "Weapons/Zweihander.png",
        "primaryColor": "#8f9093",
        "secondaryColors": [
            "#5c5959",
            "#5a5757"
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