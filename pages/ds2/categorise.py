import json

# Your JSON data as a list of dictionaries
data = [
    {
        "name": "Alberich's Robe (Altered)",
        "image": "Chest/Alberich's Robe (Altered).png",
        "primaryColor": "#56534e",
        "secondaryColors": [
            "#514e49",
            "#4f4539"
        ]
    },
    {
        "name": "Alberich's Robe",
        "image": "Chest/Alberich's Robe.png",
        "primaryColor": "#8a6b52",
        "secondaryColors": [
            "#635849",
            "#554937"
        ]
    },
    {
        "name": "All-Knowing Armor (Altered)",
        "image": "Chest/All-Knowing Armor (Altered).png",
        "primaryColor": "#a49f96",
        "secondaryColors": [
            "#605c54",
            "#47433c"
        ]
    },
    {
        "name": "All-Knowing Armor",
        "image": "Chest/All-Knowing Armor.png",
        "primaryColor": "#a29d94",
        "secondaryColors": [
            "#605b53",
            "#48433b"
        ]
    },
    {
        "name": "Aristocrat Coat",
        "image": "Chest/Aristocrat Coat.png",
        "primaryColor": "#8e8670",
        "secondaryColors": [
            "#645b4c",
            "#4f463a"
        ]
    },
    {
        "name": "Aristocrat Garb (Altered)",
        "image": "Chest/Aristocrat Garb (Altered).png",
        "primaryColor": "#96866c",
        "secondaryColors": [
            "#87765c",
            "#6f614c"
        ]
    },
    {
        "name": "Aristocrat Garb",
        "image": "Chest/Aristocrat Garb.png",
        "primaryColor": "#96876e",
        "secondaryColors": [
            "#87765b",
            "#6f614c"
        ]
    },
    {
        "name": "Astrologer Robe (Altered)",
        "image": "Chest/Astrologer Robe (Altered).png",
        "primaryColor": "#a7a091",
        "secondaryColors": [
            "#65534a",
            "#594437"
        ]
    },
    {
        "name": "Astrologer Robe",
        "image": "Chest/Astrologer Robe.png",
        "primaryColor": "#958c8a",
        "secondaryColors": [
            "#88776e",
            "#685d58"
        ]
    },
    {
        "name": "Azur's Glintstone Robe",
        "image": "Chest/Azur's Glintstone Robe.png",
        "primaryColor": "#222527",
        "secondaryColors": [
            "#009a7d",
            "#8a6248"
        ]
    },
    {
        "name": "Bandit Garb",
        "image": "Chest/Bandit Garb.png",
        "primaryColor": "#645950",
        "secondaryColors": [
            "#5a524c",
            "#4a423c"
        ]
    },
    {
        "name": "Banished Knight Armor (Altered)",
        "image": "Chest/Banished Knight Armor (Altered).png",
        "primaryColor": "#a69e92",
        "secondaryColors": [
            "#8d8579",
            "#645e54"
        ]
    },
    {
        "name": "Banished Knight Armor",
        "image": "Chest/Banished Knight Armor.png",
        "primaryColor": "#a29b91",
        "secondaryColors": [
            "#615e58",
            "#4b4439"
        ]
    },
    {
        "name": "Battlemage Robe",
        "image": "Chest/Battlemage Robe.png",
        "primaryColor": "#2d2b35",
        "secondaryColors": [
            "#89332b",
            "#97695c"
        ]
    },
    {
        "name": "Beast Champion Armor (Altered)",
        "image": "Chest/Beast Champion Armor (Altered).png",
        "primaryColor": "#969593",
        "secondaryColors": [
            "#5d5b58",
            "#48433b"
        ]
    },
    {
        "name": "Beast Champion Armor",
        "image": "Chest/Beast Champion Armor.png",
        "primaryColor": "#979693",
        "secondaryColors": [
            "#5d5b58",
            "#0d1f30"
        ]
    },
    {
        "name": "Black Knife Armor (Altered)",
        "image": "Chest/Black Knife Armor (Altered).png",
        "primaryColor": "#8d9397",
        "secondaryColors": [
            "#555b5f",
            "#3b4348"
        ]
    },
    {
        "name": "Black Knife Armor",
        "image": "Chest/Black Knife Armor.png",
        "primaryColor": "#8c9396",
        "secondaryColors": [
            "#51575a",
            "#3b4348"
        ]
    },
    {
        "name": "Blackflame Monk Armor",
        "image": "Chest/Blackflame Monk Armor.png",
        "primaryColor": "#9d998f",
        "secondaryColors": [
            "#8d8576",
            "#847a6b"
        ]
    },
    {
        "name": "Blaidd's Armor (Altered)",
        "image": "Chest/Blaidd's Armor (Altered).png",
        "primaryColor": "#939490",
        "secondaryColors": [
            "#5f5e5a",
            "#47433c"
        ]
    },
    {
        "name": "Blaidd's Armor",
        "image": "Chest/Blaidd's Armor.png",
        "primaryColor": "#919192",
        "secondaryColors": [
            "#60605f",
            "#595859"
        ]
    },
    {
        "name": "Bloodhound Knight Armor (Altered)",
        "image": "Chest/Bloodhound Knight Armor (Altered).png",
        "primaryColor": "#a79d91",
        "secondaryColors": [
            "#867767",
            "#695d50"
        ]
    },
    {
        "name": "Bloodhound Knight Armor",
        "image": "Chest/Bloodhound Knight Armor.png",
        "primaryColor": "#867767",
        "secondaryColors": [
            "#695d50",
            "#574737"
        ]
    },
    {
        "name": "Bloodsoaked Tabard",
        "image": "Chest/Bloodsoaked Tabard.png",
        "primaryColor": "#86776a",
        "secondaryColors": [
            "#655e4e",
            "#4f4739"
        ]
    },
    {
        "name": "Blue Cloth Vest",
        "image": "Chest/Blue Cloth Vest.png",
        "primaryColor": "#3b444c",
        "secondaryColors": [
            "#4b433b",
            "#585a5d"
        ]
    },
    {
        "name": "Blue Festive Garb",
        "image": "Chest/Blue Festive Garb.png",
        "primaryColor": "#afa393",
        "secondaryColors": [
            "#9a8975",
            "#887663"
        ]
    },
    {
        "name": "Blue Silver Mail Armor (Altered)",
        "image": "Chest/Blue Silver Mail Armor (Altered).png",
        "primaryColor": "#475664",
        "secondaryColors": [
            "#717d7a",
            "#3c4245"
        ]
    },
    {
        "name": "Blue Silver Mail Armor",
        "image": "Chest/Blue Silver Mail Armor.png",
        "primaryColor": "#475664",
        "secondaryColors": [
            "#717d7a",
            "#41474f"
        ]
    },
    {
        "name": "Briar Armor (Altered)",
        "image": "Chest/Briar Armor (Altered).png",
        "primaryColor": "#877063",
        "secondaryColors": [
            "#6d392c",
            "#53433a"
        ]
    },
    {
        "name": "Briar Armor",
        "image": "Chest/Briar Armor.png",
        "primaryColor": "#876d5e",
        "secondaryColors": [
            "#6d392c",
            "#030303"
        ]
    },
    {
        "name": "Bull-Goat Armor",
        "image": "Chest/Bull-Goat Armor.png",
        "primaryColor": "#a1988d",
        "secondaryColors": [
            "#847a6e",
            "#635b53"
        ]
    },
    {
        "name": "Carian Knight Armor (Altered)",
        "image": "Chest/Carian Knight Armor (Altered).png",
        "primaryColor": "#696d6f",
        "secondaryColors": [
            "#4a433b",
            "#384052"
        ]
    },
    {
        "name": "Carian Knight Armor",
        "image": "Chest/Carian Knight Armor.png",
        "primaryColor": "#696d6f",
        "secondaryColors": [
            "#4b443b",
            "#384052"
        ]
    },
    {
        "name": "Chain Armor (Female)",
        "image": "Chest/Chain Armor (Female).png",
        "primaryColor": "#a9a492",
        "secondaryColors": [
            "#55534d",
            "#47443a"
        ]
    },
    {
        "name": "Chain Armor (Male)",
        "image": "Chest/Chain Armor (Male).png",
        "primaryColor": "#68635d",
        "secondaryColors": [
            "#5b564f",
            "#47433b"
        ]
    },
    {
        "name": "Chain-Draped Tabard",
        "image": "Chest/Chain-Draped Tabard.png",
        "primaryColor": "#837970",
        "secondaryColors": [
            "#625953",
            "#4a423b"
        ]
    },
    {
        "name": "Champion Pauldron",
        "image": "Chest/Champion Pauldron.png",
        "primaryColor": "#5e5a53",
        "secondaryColors": [
            "#812c2c",
            "#4f433b"
        ]
    },
    {
        "name": "Cleanrot Armor (Altered)",
        "image": "Chest/Cleanrot Armor (Altered).png",
        "primaryColor": "#a48b6e",
        "secondaryColors": [
            "#8d7257",
            "#6e5d4a"
        ]
    },
    {
        "name": "Cleanrot Armor",
        "image": "Chest/Cleanrot Armor.png",
        "primaryColor": "#aba196",
        "secondaryColors": [
            "#9d8871",
            "#2a0502"
        ]
    },
    {
        "name": "Cloth Garb",
        "image": "Chest/Cloth Garb.png",
        "primaryColor": "#a79a8e",
        "secondaryColors": [
            "#928679",
            "#86796d"
        ]
    },
    {
        "name": "Commoner's Garb (Altered)",
        "image": "Chest/Commoner's Garb (Altered).png",
        "primaryColor": "#a39a8f",
        "secondaryColors": [
            "#908577",
            "#85796b"
        ]
    },
    {
        "name": "Commoner's Garb",
        "image": "Chest/Commoner's Garb.png",
        "primaryColor": "#a39a8e",
        "secondaryColors": [
            "#908576",
            "#85796b"
        ]
    },
    {
        "name": "Commoner's Simple Garb (Altered)",
        "image": "Chest/Commoner's Simple Garb (Altered).png",
        "primaryColor": "#9e968d",
        "secondaryColors": [
            "#8d8479",
            "#84786b"
        ]
    },
    {
        "name": "Commoner's Simple Garb",
        "image": "Chest/Commoner's Simple Garb.png",
        "primaryColor": "#8e8576",
        "secondaryColors": [
            "#84796c",
            "#665f54"
        ]
    },
    {
        "name": "Confessor Armor (Altered)",
        "image": "Chest/Confessor Armor (Altered).png",
        "primaryColor": "#867667",
        "secondaryColors": [
            "#59544e",
            "#48433c"
        ]
    },
    {
        "name": "Confessor Armor",
        "image": "Chest/Confessor Armor.png",
        "primaryColor": "#877768",
        "secondaryColors": [
            "#58534c",
            "#48423c"
        ]
    },
    {
        "name": "Consort's Robe",
        "image": "Chest/Consort's Robe.png",
        "primaryColor": "#afa58f",
        "secondaryColors": [
            "#9b8e72",
            "#867860"
        ]
    },
    {
        "name": "Corhyn's Robe",
        "image": "Chest/Corhyn's Robe.png",
        "primaryColor": "#897050",
        "secondaryColors": [
            "#6e5d48",
            "#5e4b33"
        ]
    },
    {
        "name": "Crucible Axe Armor (Altered)",
        "image": "Chest/Crucible Axe Armor (Altered).png",
        "primaryColor": "#8e6b57",
        "secondaryColors": [
            "#605146",
            "#584639"
        ]
    },
    {
        "name": "Crucible Axe Armor",
        "image": "Chest/Crucible Axe Armor.png",
        "primaryColor": "#8e6c57",
        "secondaryColors": [
            "#605147",
            "#574539"
        ]
    },
    {
        "name": "Crucible Tree Armor (Altered)",
        "image": "Chest/Crucible Tree Armor (Altered).png",
        "primaryColor": "#8e6a56",
        "secondaryColors": [
            "#61574d",
            "#554539"
        ]
    },
    {
        "name": "Crucible Tree Armor",
        "image": "Chest/Crucible Tree Armor.png",
        "primaryColor": "#8c6a56",
        "secondaryColors": [
            "#60564c",
            "#544539"
        ]
    },
    {
        "name": "Cuckoo Knight Armor (Altered)",
        "image": "Chest/Cuckoo Knight Armor (Altered).png",
        "primaryColor": "#5e5958",
        "secondaryColors": [
            "#495f94",
            "#924139"
        ]
    },
    {
        "name": "Cuckoo Knight Armor",
        "image": "Chest/Cuckoo Knight Armor.png",
        "primaryColor": "#99999a",
        "secondaryColors": [
            "#495f94",
            "#924139"
        ]
    },
    {
        "name": "Cuckoo Surcoat",
        "image": "Chest/Cuckoo Surcoat.png",
        "primaryColor": "#635c55",
        "secondaryColors": [
            "#495f94",
            "#924139"
        ]
    },
    {
        "name": "Deathbed Dress",
        "image": "Chest/Deathbed Dress.png",
        "primaryColor": "#939292",
        "secondaryColors": [
            "#7d7c81",
            "#616062"
        ]
    },
    {
        "name": "Depraved Perfumer Robe (Altered)",
        "image": "Chest/Depraved Perfumer Robe (Altered).png",
        "primaryColor": "#978871",
        "secondaryColors": [
            "#87765f",
            "#695a4f"
        ]
    },
    {
        "name": "Depraved Perfumer Robe",
        "image": "Chest/Depraved Perfumer Robe.png",
        "primaryColor": "#867660",
        "secondaryColors": [
            "#675b4e",
            "#584737"
        ]
    },
    {
        "name": "Dirty Chainmail",
        "image": "Chest/Dirty Chainmail.png",
        "primaryColor": "#877567",
        "secondaryColors": [
            "#685b52",
            "#55463a"
        ]
    },
    {
        "name": "Drake Knight Armor (Altered)",
        "image": "Chest/Drake Knight Armor (Altered).png",
        "primaryColor": "#0e1615",
        "secondaryColors": [
            "#5f5b57",
            "#a84f3b"
        ]
    },
    {
        "name": "Drake Knight Armor",
        "image": "Chest/Drake Knight Armor.png",
        "primaryColor": "#0e1615",
        "secondaryColors": [
            "#a84f3b",
            "#5f4539"
        ]
    },
    {
        "name": "Eccentric's Armor",
        "image": "Chest/Eccentric's Armor.png",
        "primaryColor": "#9e8b6f",
        "secondaryColors": [
            "#5f5854",
            "#51453a"
        ]
    },
    {
        "name": "Elden Lord Armor (Altered)",
        "image": "Chest/Elden Lord Armor (Altered).png",
        "primaryColor": "#a69d91",
        "secondaryColors": [
            "#857667",
            "#665b4f"
        ]
    },
    {
        "name": "Elden Lord Armor",
        "image": "Chest/Elden Lord Armor.png",
        "primaryColor": "#a89f92",
        "secondaryColors": [
            "#918576",
            "#050d11"
        ]
    },
    {
        "name": "Erdtree Surcoat",
        "image": "Chest/Erdtree Surcoat.png",
        "primaryColor": "#9f8d65",
        "secondaryColors": [
            "#8b7554",
            "#8e6e2f"
        ]
    },
    {
        "name": "Errant Sorcerer Robe (Altered)",
        "image": "Chest/Errant Sorcerer Robe (Altered).png",
        "primaryColor": "#6a5247",
        "secondaryColors": [
            "#59443a",
            "#3b423a"
        ]
    },
    {
        "name": "Errant Sorcerer Robe",
        "image": "Chest/Errant Sorcerer Robe.png",
        "primaryColor": "#695247",
        "secondaryColors": [
            "#5b4f48",
            "#58443a"
        ]
    },
    {
        "name": "Exile Armor",
        "image": "Chest/Exile Armor.png",
        "primaryColor": "#87746c",
        "secondaryColors": [
            "#604c49",
            "#412523"
        ]
    },
    {
        "name": "Eye Surcoat",
        "image": "Chest/Eye Surcoat.png",
        "primaryColor": "#867465",
        "secondaryColors": [
            "#665a4f",
            "#584637"
        ]
    },
    {
        "name": "Fell Omen Cloak",
        "image": "Chest/Fell Omen Cloak.png",
        "primaryColor": "#877562",
        "secondaryColors": [
            "#685b4e",
            "#52453a"
        ]
    },
    {
        "name": "Festive Garb (Altered)",
        "image": "Chest/Festive Garb (Altered).png",
        "primaryColor": "#aba194",
        "secondaryColors": [
            "#958776",
            "#887664"
        ]
    },
    {
        "name": "Festive Garb",
        "image": "Chest/Festive Garb.png",
        "primaryColor": "#aba193",
        "secondaryColors": [
            "#978875",
            "#887664"
        ]
    },
    {
        "name": "Fia's Robe (Altered)",
        "image": "Chest/Fia's Robe (Altered).png",
        "primaryColor": "#383830",
        "secondaryColors": [
            "#9e9f9d",
            "#585b54"
        ]
    },
    {
        "name": "Fia's Robe (Altered)_()",
        "image": "Chest/Fia's Robe (Altered)_().png",
        "primaryColor": "#383830",
        "secondaryColors": [
            "#9e9f9d",
            "#585b54"
        ]
    },
    {
        "name": "Fia's Robe",
        "image": "Chest/Fia's Robe.png",
        "primaryColor": "#383830",
        "secondaryColors": [
            "#9e9f9d",
            "#565853"
        ]
    },
    {
        "name": "Finger Maiden Robe (Altered)",
        "image": "Chest/Finger Maiden Robe (Altered).png",
        "primaryColor": "#a29790",
        "secondaryColors": [
            "#85766f",
            "#675953"
        ]
    },
    {
        "name": "Finger Maiden Robe",
        "image": "Chest/Finger Maiden Robe.png",
        "primaryColor": "#a3978f",
        "secondaryColors": [
            "#85766e",
            "#675953"
        ]
    },
    {
        "name": "Fingerprint Armor (Altered)",
        "image": "Chest/Fingerprint Armor (Altered).png",
        "primaryColor": "#949098",
        "secondaryColors": [
            "#5b565a",
            "#49433b"
        ]
    },
    {
        "name": "Fingerprint Armor",
        "image": "Chest/Fingerprint Armor.png",
        "primaryColor": "#96929a",
        "secondaryColors": [
            "#585456",
            "#47423b"
        ]
    },
    {
        "name": "Fire Monk Armor",
        "image": "Chest/Fire Monk Armor.png",
        "primaryColor": "#8e3c2f",
        "secondaryColors": [
            "#605a59",
            "#c76625"
        ]
    },
    {
        "name": "Fire Prelate Armor (Altered)",
        "image": "Chest/Fire Prelate Armor (Altered).png",
        "primaryColor": "#d8d8da",
        "secondaryColors": [
            "#99989a",
            "#5a5859"
        ]
    },
    {
        "name": "Fire Prelate Armor",
        "image": "Chest/Fire Prelate Armor.png",
        "primaryColor": "#ad4537",
        "secondaryColors": [
            "#58524c",
            "#903027"
        ]
    },
    {
        "name": "Foot Soldier Tabard",
        "image": "Chest/Foot Soldier Tabard.png",
        "primaryColor": "#837a71",
        "secondaryColors": [
            "#625a54",
            "#4a433b"
        ]
    },
    {
        "name": "Fur Raiment",
        "image": "Chest/Fur Raiment.png",
        "primaryColor": "#a09c93",
        "secondaryColors": [
            "#625b50",
            "#4e4539"
        ]
    },
    {
        "name": "Gelmir Knight Armor (Altered)",
        "image": "Chest/Gelmir Knight Armor (Altered).png",
        "primaryColor": "#9c9996",
        "secondaryColors": [
            "#2a2929",
            "#4d443a"
        ]
    },
    {
        "name": "Gelmir Knight Armor",
        "image": "Chest/Gelmir Knight Armor.png",
        "primaryColor": "#a39d97",
        "secondaryColors": [
            "#2a2929",
            "#546c54"
        ]
    },
    {
        "name": "Godrick Knight Armor (Altered)",
        "image": "Chest/Godrick Knight Armor (Altered).png",
        "primaryColor": "#a59d8d",
        "secondaryColors": [
            "#9b4217",
            "#546c54"
        ]
    },
    {
        "name": "Godrick Knight Armor",
        "image": "Chest/Godrick Knight Armor.png",
        "primaryColor": "#a79f8e",
        "secondaryColors": [
            "#9b4217",
            "#546c54"
        ]
    },
    {
        "name": "Godskin Apostle Robe",
        "image": "Chest/Godskin Apostle Robe.png",
        "primaryColor": "#a79f94",
        "secondaryColors": [
            "#908579",
            "#857a6f"
        ]
    },
    {
        "name": "Godskin Noble Robe",
        "image": "Chest/Godskin Noble Robe.png",
        "primaryColor": "#a9a298",
        "secondaryColors": [
            "#918777",
            "#86796a"
        ]
    },
    {
        "name": "Goldmask's Rags",
        "image": "Chest/Goldmask's Rags.png",
        "primaryColor": "#aea195",
        "secondaryColors": [
            "#64584e",
            "#4f453a"
        ]
    },
    {
        "name": "Gravekeeper Cloak",
        "image": "Chest/Gravekeeper Cloak.png",
        "primaryColor": "#5c544c",
        "secondaryColors": [
            "#50423c",
            "#463834"
        ]
    },
    {
        "name": "Guardian Garb (Full Bloom)",
        "image": "Chest/Guardian Garb (Full Bloom).png",
        "primaryColor": "#948b70",
        "secondaryColors": [
            "#b65c59",
            "#6f644b"
        ]
    },
    {
        "name": "Guardian Garb",
        "image": "Chest/Guardian Garb.png",
        "primaryColor": "#948a6c",
        "secondaryColors": [
            "#86764d",
            "#70684a"
        ]
    },
    {
        "name": "Haligtree Crest Surcoat",
        "image": "Chest/Haligtree Crest Surcoat.png",
        "primaryColor": "#aba48e",
        "secondaryColors": [
            "#988b6e",
            "#87775a"
        ]
    },
    {
        "name": "Haligtree Knight Armor (Altered)",
        "image": "Chest/Haligtree Knight Armor (Altered).png",
        "primaryColor": "#aca494",
        "secondaryColors": [
            "#958c74",
            "#676153"
        ]
    },
    {
        "name": "Haligtree Knight Armor",
        "image": "Chest/Haligtree Knight Armor.png",
        "primaryColor": "#aca493",
        "secondaryColors": [
            "#958c74",
            "#857966"
        ]
    },
    {
        "name": "High Page Clothes (Altered)",
        "image": "Chest/High Page Clothes (Altered).png",
        "primaryColor": "#ada48f",
        "secondaryColors": [
            "#988d76",
            "#655e50"
        ]
    },
    {
        "name": "High Page Clothes",
        "image": "Chest/High Page Clothes.png",
        "primaryColor": "#ada490",
        "secondaryColors": [
            "#988c76",
            "#645d4e"
        ]
    },
    {
        "name": "Highwayman Cloth Armor",
        "image": "Chest/Highwayman Cloth Armor.png",
        "primaryColor": "#877361",
        "secondaryColors": [
            "#67584b",
            "#51453a"
        ]
    },
    {
        "name": "Hoslow's Armor (Altered)",
        "image": "Chest/Hoslow's Armor (Altered).png",
        "primaryColor": "#4f5051",
        "secondaryColors": [
            "#4f2c26",
            "#48433b"
        ]
    },
    {
        "name": "Hoslow's Armor",
        "image": "Chest/Hoslow's Armor.png",
        "primaryColor": "#4f5051",
        "secondaryColors": [
            "#4f2c26",
            "#48433c"
        ]
    },
    {
        "name": "Ivory-Draped Tabard",
        "image": "Chest/Ivory-Draped Tabard.png",
        "primaryColor": "#a99f8f",
        "secondaryColors": [
            "#988775",
            "#897565"
        ]
    },
    {
        "name": "Juvenile Scholar Robe",
        "image": "Chest/Juvenile Scholar Robe.png",
        "primaryColor": "#4f5154",
        "secondaryColors": [
            "#5d4d2e",
            "#3c4148"
        ]
    },
    {
        "name": "Kaiden Armor",
        "image": "Chest/Kaiden Armor.png",
        "primaryColor": "#a29c91",
        "secondaryColors": [
            "#605b52",
            "#4a433a"
        ]
    },
    {
        "name": "Knight Armor",
        "image": "Chest/Knight Armor.png",
        "primaryColor": "#7c7777",
        "secondaryColors": [
            "#146074",
            "#5d5d5c"
        ]
    },
    {
        "name": "Land of Reeds Armor (Altered)",
        "image": "Chest/Land of Reeds Armor (Altered).png",
        "primaryColor": "#804b30",
        "secondaryColors": [
            "#605652",
            "#624537"
        ]
    },
    {
        "name": "Land of Reeds Armor",
        "image": "Chest/Land of Reeds Armor.png",
        "primaryColor": "#804b30",
        "secondaryColors": [
            "#615953",
            "#624636"
        ]
    },
    {
        "name": "Lazuli Robe",
        "image": "Chest/Lazuli Robe.png",
        "primaryColor": "#959d9d",
        "secondaryColors": [
            "#798787",
            "#58605e"
        ]
    },
    {
        "name": "Leather Armor",
        "image": "Chest/Leather Armor.png",
        "primaryColor": "#857865",
        "secondaryColors": [
            "#5f5b50",
            "#4f463a"
        ]
    },
    {
        "name": "Leather Armor_ (2)",
        "image": "Chest/Leather Armor_ (2).png",
        "primaryColor": "#928772",
        "secondaryColors": [
            "#605b52",
            "#50463a"
        ]
    },
    {
        "name": "Leather-Draped Tabard",
        "image": "Chest/Leather-Draped Tabard.png",
        "primaryColor": "#90896a",
        "secondaryColors": [
            "#84785d",
            "#695e4c"
        ]
    },
    {
        "name": "Leyndell Knight Armor (Altered)",
        "image": "Chest/Leyndell Knight Armor (Altered).png",
        "primaryColor": "#a78f59",
        "secondaryColors": [
            "#8e764d",
            "#8d6d34"
        ]
    },
    {
        "name": "Leyndell Knight Armor",
        "image": "Chest/Leyndell Knight Armor.png",
        "primaryColor": "#a48e58",
        "secondaryColors": [
            "#8d764e",
            "#8c6d34"
        ]
    },
    {
        "name": "Lionel's Armor (Altered)",
        "image": "Chest/Lionel's Armor (Altered).png",
        "primaryColor": "#575453",
        "secondaryColors": [
            "#58463a",
            "#3c4244"
        ]
    },
    {
        "name": "Lionel's Armor",
        "image": "Chest/Lionel's Armor.png",
        "primaryColor": "#886559",
        "secondaryColors": [
            "#585553",
            "#594639"
        ]
    },
    {
        "name": "Lord of Blood's Robe (Altered)",
        "image": "Chest/Lord of Blood's Robe (Altered).png",
        "primaryColor": "#94604e",
        "secondaryColors": [
            "#5f534e",
            "#5a4735"
        ]
    },
    {
        "name": "Lord of Blood's Robe",
        "image": "Chest/Lord of Blood's Robe.png",
        "primaryColor": "#8a5f51",
        "secondaryColors": [
            "#67594a",
            "#564736"
        ]
    },
    {
        "name": "Lusat's Robe",
        "image": "Chest/Lusat's Robe.png",
        "primaryColor": "#744e2b",
        "secondaryColors": [
            "#2b467a",
            "#26282b"
        ]
    },
    {
        "name": "Malenia's Armor (Altered)",
        "image": "Chest/Malenia's Armor (Altered).png",
        "primaryColor": "#857769",
        "secondaryColors": [
            "#64594c",
            "#504639"
        ]
    },
    {
        "name": "Malenia's Armor",
        "image": "Chest/Malenia's Armor.png",
        "primaryColor": "#856b5b",
        "secondaryColors": [
            "#65594c",
            "#514538"
        ]
    },
    {
        "name": "Malformed Dragon Armor",
        "image": "Chest/Malformed Dragon Armor.png",
        "primaryColor": "#a59064",
        "secondaryColors": [
            "#8b764d",
            "#6d624a"
        ]
    },
    {
        "name": "Maliketh's Armor (Altered)",
        "image": "Chest/Maliketh's Armor (Altered).png",
        "primaryColor": "#1c1c1c",
        "secondaryColors": [
            "#87765a",
            "#4f4638"
        ]
    },
    {
        "name": "Maliketh's Armor",
        "image": "Chest/Maliketh's Armor.png",
        "primaryColor": "#1c1c1c",
        "secondaryColors": [
            "#87765a",
            "#4f4638"
        ]
    },
    {
        "name": "Marai's Robe",
        "image": "Chest/Marai's Robe.png",
        "primaryColor": "#646569",
        "secondaryColors": [
            "#312e2a",
            "#ab7d51"
        ]
    },
    {
        "name": "Marionette Soldier Armor",
        "image": "Chest/Marionette Soldier Armor.png",
        "primaryColor": "#88746a",
        "secondaryColors": [
            "#65594d",
            "#524638"
        ]
    },
    {
        "name": "Mausoleum Knight Armor (Altered)",
        "image": "Chest/Mausoleum Knight Armor (Altered).png",
        "primaryColor": "#979896",
        "secondaryColors": [
            "#7b7639",
            "#524f5c"
        ]
    },
    {
        "name": "Mausoleum Knight Armor",
        "image": "Chest/Mausoleum Knight Armor.png",
        "primaryColor": "#989897",
        "secondaryColors": [
            "#7b7639",
            "#524f5c"
        ]
    },
    {
        "name": "Mausoleum Surcoat",
        "image": "Chest/Mausoleum Surcoat.png",
        "primaryColor": "#97948d",
        "secondaryColors": [
            "#625d53",
            "#56575a"
        ]
    },
    {
        "name": "Mushroom Body",
        "image": "Chest/Mushroom Body.png",
        "primaryColor": "#9d9a93",
        "secondaryColors": [
            "#a98a72",
            "#90705b"
        ]
    },
    {
        "name": "Night Maiden Armor",
        "image": "Chest/Night Maiden Armor.png",
        "primaryColor": "#e0ded7",
        "secondaryColors": [
            "#ccc8b7",
            "#aba699"
        ]
    },
    {
        "name": "Nights Cavalry Armor (Altered)",
        "image": "Chest/Nights Cavalry Armor (Altered).png",
        "primaryColor": "#212021",
        "secondaryColors": [
            "#56534f",
            "#44413d"
        ]
    },
    {
        "name": "Nights Cavalry Armor",
        "image": "Chest/Nights Cavalry Armor.png",
        "primaryColor": "#212021",
        "secondaryColors": [
            "#535150",
            "#43413d"
        ]
    },
    {
        "name": "Noble's Traveling Garb",
        "image": "Chest/Noble's Traveling Garb.png",
        "primaryColor": "#9f9b93",
        "secondaryColors": [
            "#89847b",
            "#827c74"
        ]
    },
    {
        "name": "Nomadic Merchant's Finery (Altered)",
        "image": "Chest/Nomadic Merchant's Finery (Altered).png",
        "primaryColor": "#9d918d",
        "secondaryColors": [
            "#857674",
            "#615754"
        ]
    },
    {
        "name": "Nomadic Merchant's Finery",
        "image": "Chest/Nomadic Merchant's Finery.png",
        "primaryColor": "#9f9692",
        "secondaryColors": [
            "#867774",
            "#625955"
        ]
    },
    {
        "name": "Nox Monk Armor (Altered)",
        "image": "Chest/Nox Monk Armor (Altered).png",
        "primaryColor": "#837a6c",
        "secondaryColors": [
            "#625a50",
            "#4c433a"
        ]
    },
    {
        "name": "Nox Monk Armor",
        "image": "Chest/Nox Monk Armor.png",
        "primaryColor": "#a7a298",
        "secondaryColors": [
            "#59564b",
            "#49443b"
        ]
    },
    {
        "name": "Nox Swordstres's Armor (Altered)",
        "image": "Chest/Nox Swordstres's Armor (Altered).png",
        "primaryColor": "#85796e",
        "secondaryColors": [
            "#65594e",
            "#50443a"
        ]
    },
    {
        "name": "Nox Swordstres's Armor",
        "image": "Chest/Nox Swordstres's Armor.png",
        "primaryColor": "#d5d3cd",
        "secondaryColors": [
            "#aaa79d",
            "#5a584d"
        ]
    },
    {
        "name": "Official's Attire",
        "image": "Chest/Official's Attire.png",
        "primaryColor": "#8d8b89",
        "secondaryColors": [
            "#5c5c5b",
            "#4d443b"
        ]
    },
    {
        "name": "Old Aristocrat Gown",
        "image": "Chest/Old Aristocrat Gown.png",
        "primaryColor": "#896e53",
        "secondaryColors": [
            "#735c46",
            "#5e4936"
        ]
    },
    {
        "name": "Omen Armor",
        "image": "Chest/Omen Armor.png",
        "primaryColor": "#a46058",
        "secondaryColors": [
            "#e0b390",
            "#6b534c"
        ]
    },
    {
        "name": "Omenkiller Robe",
        "image": "Chest/Omenkiller Robe.png",
        "primaryColor": "#a38968",
        "secondaryColors": [
            "#8b7056",
            "#6e615b"
        ]
    },
    {
        "name": "Page Garb (Altered)",
        "image": "Chest/Page Garb (Altered).png",
        "primaryColor": "#877764",
        "secondaryColors": [
            "#5e5550",
            "#50473a"
        ]
    },
    {
        "name": "Page Garb",
        "image": "Chest/Page Garb.png",
        "primaryColor": "#877764",
        "secondaryColors": [
            "#5e5550",
            "#4f473a"
        ]
    },
    {
        "name": "Perfumer Robe (Altered)",
        "image": "Chest/Perfumer Robe (Altered).png",
        "primaryColor": "#887354",
        "secondaryColors": [
            "#645b4c",
            "#584b33"
        ]
    },
    {
        "name": "Perfumer Robe",
        "image": "Chest/Perfumer Robe.png",
        "primaryColor": "#dfddd5",
        "secondaryColors": [
            "#a9a598",
            "#887455"
        ]
    },
    {
        "name": "Perfumer's Traveling Garb (Altered)",
        "image": "Chest/Perfumer's Traveling Garb (Altered).png",
        "primaryColor": "#8c8773",
        "secondaryColors": [
            "#887253",
            "#6c6553"
        ]
    },
    {
        "name": "Perfumer's Traveling Garb",
        "image": "Chest/Perfumer's Traveling Garb.png",
        "primaryColor": "#8c8774",
        "secondaryColors": [
            "#887255",
            "#856338"
        ]
    },
    {
        "name": "Preceptor's Long Gown (Altered)",
        "image": "Chest/Preceptor's Long Gown (Altered).png",
        "primaryColor": "#201b18",
        "secondaryColors": [
            "#6c534a",
            "#4e433b"
        ]
    },
    {
        "name": "Preceptor's Long Gown",
        "image": "Chest/Preceptor's Long Gown.png",
        "primaryColor": "#04284d",
        "secondaryColors": [
            "#1e1e1d",
            "#443b35"
        ]
    },
    {
        "name": "Prisoner Clothing",
        "image": "Chest/Prisoner Clothing.png",
        "primaryColor": "#656059",
        "secondaryColors": [
            "#5b564f",
            "#4b443b"
        ]
    },
    {
        "name": "Prophet Robe (Altered)",
        "image": "Chest/Prophet Robe (Altered).png",
        "primaryColor": "#a58a65",
        "secondaryColors": [
            "#8b714f",
            "#6f5e49"
        ]
    },
    {
        "name": "Prophet Robe",
        "image": "Chest/Prophet Robe.png",
        "primaryColor": "#a58b66",
        "secondaryColors": [
            "#8b714f",
            "#6f5e49"
        ]
    },
    {
        "name": "Queen's Robe",
        "image": "Chest/Queen's Robe.png",
        "primaryColor": "#182028",
        "secondaryColors": [
            "#4d1611",
            "#51422d"
        ]
    },
    {
        "name": "Radahn's Lion Armor (Altered)",
        "image": "Chest/Radahn's Lion Armor (Altered).png",
        "primaryColor": "#9a8b6d",
        "secondaryColors": [
            "#877459",
            "#6d5f4a"
        ]
    },
    {
        "name": "Radahn's Lion Armor",
        "image": "Chest/Radahn's Lion Armor.png",
        "primaryColor": "#86755c",
        "secondaryColors": [
            "#6a5e4a",
            "#3e2721"
        ]
    },
    {
        "name": "Raging Wolf Armor (Altered)",
        "image": "Chest/Raging Wolf Armor (Altered).png",
        "primaryColor": "#9e9797",
        "secondaryColors": [
            "#804138",
            "#59433c"
        ]
    },
    {
        "name": "Raging Wolf Armor",
        "image": "Chest/Raging Wolf Armor.png",
        "primaryColor": "#9e9797",
        "secondaryColors": [
            "#804138",
            "#55423b"
        ]
    },
    {
        "name": "Raptor's Black Feathers",
        "image": "Chest/Raptor's Black Feathers.png",
        "primaryColor": "#4c4a4d",
        "secondaryColors": [
            "#4a433b",
            "#3c3c43"
        ]
    },
    {
        "name": "Raya Lucarian Robe",
        "image": "Chest/Raya Lucarian Robe.png",
        "primaryColor": "#2c2c3c",
        "secondaryColors": [
            "#843a39",
            "#584830"
        ]
    },
    {
        "name": "Redmane Knight Armor (Altered)",
        "image": "Chest/Redmane Knight Armor (Altered).png",
        "primaryColor": "#a44c46",
        "secondaryColors": [
            "#574470",
            "#4e433b"
        ]
    },
    {
        "name": "Redmane Knight Armor",
        "image": "Chest/Redmane Knight Armor.png",
        "primaryColor": "#a44c46",
        "secondaryColors": [
            "#574470",
            "#4d443b"
        ]
    },
    {
        "name": "Redmane Surcoat",
        "image": "Chest/Redmane Surcoat.png",
        "primaryColor": "#9b343b",
        "secondaryColors": [
            "#543c52",
            "#554638"
        ]
    },
    {
        "name": "Ronin's Armor (Altered)",
        "image": "Chest/Ronin's Armor (Altered).png",
        "primaryColor": "#877363",
        "secondaryColors": [
            "#60574f",
            "#534639"
        ]
    },
    {
        "name": "Ronin's Armor",
        "image": "Chest/Ronin's Armor.png",
        "primaryColor": "#897463",
        "secondaryColors": [
            "#625850",
            "#534639"
        ]
    },
    {
        "name": "Rotten Gravekeeper Cloak (Altered)",
        "image": "Chest/Rotten Gravekeeper Cloak (Altered).png",
        "primaryColor": "#701812",
        "secondaryColors": [
            "#2e0703",
            "#4c2b1e"
        ]
    },
    {
        "name": "Rotten Gravekeeper Cloak",
        "image": "Chest/Rotten Gravekeeper Cloak.png",
        "primaryColor": "#701812",
        "secondaryColors": [
            "#2e0703",
            "#4c2b1e"
        ]
    },
    {
        "name": "Royal Knight Armor (Altered)",
        "image": "Chest/Royal Knight Armor (Altered).png",
        "primaryColor": "#dad9d9",
        "secondaryColors": [
            "#999998",
            "#5e81a1"
        ]
    },
    {
        "name": "Royal Knight Armor",
        "image": "Chest/Royal Knight Armor.png",
        "primaryColor": "#dadad9",
        "secondaryColors": [
            "#5e81a1",
            "#60605b"
        ]
    },
    {
        "name": "Royal Remains Armor",
        "image": "Chest/Royal Remains Armor.png",
        "primaryColor": "#a18c6f",
        "secondaryColors": [
            "#5f5950",
            "#574739"
        ]
    },
    {
        "name": "Ruler's Robe",
        "image": "Chest/Ruler's Robe.png",
        "primaryColor": "#5a5354",
        "secondaryColors": [
            "#514738",
            "#423d42"
        ]
    },
    {
        "name": "Sage Robe",
        "image": "Chest/Sage Robe.png",
        "primaryColor": "#713230",
        "secondaryColors": [
            "#3b2f2a",
            "#5d423a"
        ]
    },
    {
        "name": "Sanguine Noble Robe",
        "image": "Chest/Sanguine Noble Robe.png",
        "primaryColor": "#2d2826",
        "secondaryColors": [
            "#74100e",
            "#8b7467"
        ]
    },
    {
        "name": "Scale Armor",
        "image": "Chest/Scale Armor.png",
        "primaryColor": "#908676",
        "secondaryColors": [
            "#847869",
            "#645d52"
        ]
    },
    {
        "name": "Scaled Armor (Altered)",
        "image": "Chest/Scaled Armor (Altered).png",
        "primaryColor": "#a39b92",
        "secondaryColors": [
            "#8b7260",
            "#635b52"
        ]
    },
    {
        "name": "Scaled Armor",
        "image": "Chest/Scaled Armor.png",
        "primaryColor": "#a39b92",
        "secondaryColors": [
            "#8c7361",
            "#635b52"
        ]
    },
    {
        "name": "Scarlet Tabard",
        "image": "Chest/Scarlet Tabard.png",
        "primaryColor": "#866e60",
        "secondaryColors": [
            "#665249",
            "#58453a"
        ]
    },
    {
        "name": "Shaman Furs",
        "image": "Chest/Shaman Furs.png",
        "primaryColor": "#84786a",
        "secondaryColors": [
            "#5c564f",
            "#4a433b"
        ]
    },
    {
        "name": "Snow Witch Robe (Altered)",
        "image": "Chest/Snow Witch Robe (Altered).png",
        "primaryColor": "#c9cece",
        "secondaryColors": [
            "#bcc2c2",
            "#9ca2a1"
        ]
    },
    {
        "name": "Snow Witch Robe",
        "image": "Chest/Snow Witch Robe.png",
        "primaryColor": "#9ba09f",
        "secondaryColors": [
            "#7d8281",
            "#5c5f5c"
        ]
    },
    {
        "name": "Spellblade's Traveling Attire (Altered)",
        "image": "Chest/Spellblade's Traveling Attire (Altered).png",
        "primaryColor": "#a0915f",
        "secondaryColors": [
            "#3e7266",
            "#443e36"
        ]
    },
    {
        "name": "Spellblade's Traveling Attire",
        "image": "Chest/Spellblade's Traveling Attire.png",
        "primaryColor": "#a09161",
        "secondaryColors": [
            "#3e7266",
            "#443e36"
        ]
    },
    {
        "name": "Traveler's Clothes",
        "image": "Chest/Traveler's Clothes.png",
        "primaryColor": "#a7a09a",
        "secondaryColors": [
            "#87827b",
            "#817c76"
        ]
    },
    {
        "name": "Traveling Maiden Robe (Altered)",
        "image": "Chest/Traveling Maiden Robe (Altered).png",
        "primaryColor": "#9e908a",
        "secondaryColors": [
            "#91827c",
            "#877671"
        ]
    },
    {
        "name": "Traveling Maiden Robe",
        "image": "Chest/Traveling Maiden Robe.png",
        "primaryColor": "#ab968e",
        "secondaryColors": [
            "#9b8578",
            "#8a6f65"
        ]
    },
    {
        "name": "Tree Sentinel Armor (Altered)",
        "image": "Chest/Tree Sentinel Armor (Altered).png",
        "primaryColor": "#b2a48e",
        "secondaryColors": [
            "#9d8c70",
            "#887357"
        ]
    },
    {
        "name": "Tree Sentinel Armor",
        "image": "Chest/Tree Sentinel Armor.png",
        "primaryColor": "#b0a38e",
        "secondaryColors": [
            "#9a896f",
            "#877459"
        ]
    },
    {
        "name": "Tree Surcoat",
        "image": "Chest/Tree Surcoat.png",
        "primaryColor": "#353b51",
        "secondaryColors": [
            "#585753",
            "#3f2a28"
        ]
    },
    {
        "name": "Tree-and-Beast Surcoat",
        "image": "Chest/Tree-and-Beast Surcoat.png",
        "primaryColor": "#87715a",
        "secondaryColors": [
            "#082c18",
            "#803617"
        ]
    },
    {
        "name": "Twinned Armor (Altered)",
        "image": "Chest/Twinned Armor (Altered).png",
        "primaryColor": "#9a9899",
        "secondaryColors": [
            "#5d5a5a",
            "#4a433a"
        ]
    },
    {
        "name": "Twinned Armor",
        "image": "Chest/Twinned Armor.png",
        "primaryColor": "#9a9899",
        "secondaryColors": [
            "#5d5a5a",
            "#4c443a"
        ]
    },
    {
        "name": "Upper-Class Robe",
        "image": "Chest/Upper-Class Robe.png",
        "primaryColor": "#7f845e",
        "secondaryColors": [
            "#9d9d69",
            "#504d36"
        ]
    },
    {
        "name": "Vagabond Knight Armor (Altered)",
        "image": "Chest/Vagabond Knight Armor (Altered).png",
        "primaryColor": "#a19a92",
        "secondaryColors": [
            "#5e5952",
            "#223940"
        ]
    },
    {
        "name": "Vagabond Knight Armor",
        "image": "Chest/Vagabond Knight Armor.png",
        "primaryColor": "#a59d91",
        "secondaryColors": [
            "#5f5850",
            "#4c443a"
        ]
    },
    {
        "name": "Veteran's Armor (Altered)",
        "image": "Chest/Veteran's Armor (Altered).png",
        "primaryColor": "#a39b91",
        "secondaryColors": [
            "#86756a",
            "#563631"
        ]
    },
    {
        "name": "Veteran's Armor",
        "image": "Chest/Veteran's Armor.png",
        "primaryColor": "#9f9a94",
        "secondaryColors": [
            "#625b54",
            "#563631"
        ]
    },
    {
        "name": "Vulgar Militia Armor",
        "image": "Chest/Vulgar Militia Armor.png",
        "primaryColor": "#887668",
        "secondaryColors": [
            "#62594e",
            "#4f4539"
        ]
    },
    {
        "name": "War Surgeon Gown (Altered)",
        "image": "Chest/War Surgeon Gown (Altered).png",
        "primaryColor": "#827a76",
        "secondaryColors": [
            "#615b59",
            "#4a413c"
        ]
    },
    {
        "name": "War Surgeon Gown",
        "image": "Chest/War Surgeon Gown.png",
        "primaryColor": "#969290",
        "secondaryColors": [
            "#615c59",
            "#49413d"
        ]
    },
    {
        "name": "White Reed Armor",
        "image": "Chest/White Reed Armor.png",
        "primaryColor": "#a1968e",
        "secondaryColors": [
            "#683625",
            "#8e7f45"
        ]
    },
    {
        "name": "Zamor Armor",
        "image": "Chest/Zamor Armor.png",
        "primaryColor": "#a6a292",
        "secondaryColors": [
            "#8e8876",
            "#645d51"
        ]
    },
    {
        "name": "Ansbach's Attire (Altered)",
        "image": "Chest\\SOTE/Ansbach's Attire (Altered).png",
        "primaryColor": "#232422",
        "secondaryColors": [
            "#494745",
            "#46413d"
        ]
    },
    {
        "name": "Ansbach's Attire",
        "image": "Chest\\SOTE/Ansbach's Attire.png",
        "primaryColor": "#232422",
        "secondaryColors": [
            "#4f4c47",
            "#49423b"
        ]
    },
    {
        "name": "Armor of Night",
        "image": "Chest\\SOTE/Armor of Night.png",
        "primaryColor": "#1f1e1f",
        "secondaryColors": [
            "#585554",
            "#49433b"
        ]
    },
    {
        "name": "Armor of Solitude (Altered)",
        "image": "Chest\\SOTE/Armor of Solitude (Altered).png",
        "primaryColor": "#999998",
        "secondaryColors": [
            "#5c5c5b",
            "#595958"
        ]
    },
    {
        "name": "Armor of Solitude",
        "image": "Chest\\SOTE/Armor of Solitude.png",
        "primaryColor": "#9b9a99",
        "secondaryColors": [
            "#616160",
            "#585857"
        ]
    },
    {
        "name": "Black Knight Armor",
        "image": "Chest\\SOTE/Black Knight Armor.png",
        "primaryColor": "#191719",
        "secondaryColors": [
            "#5a544e",
            "#47423b"
        ]
    },
    {
        "name": "Braided Cord Robe",
        "image": "Chest\\SOTE/Braided Cord Robe.png",
        "primaryColor": "#837a6e",
        "secondaryColors": [
            "#5e584e",
            "#47433b"
        ]
    },
    {
        "name": "Common Soldier Cloth Armor",
        "image": "Chest\\SOTE/Common Soldier Cloth Armor.png",
        "primaryColor": "#6c644f",
        "secondaryColors": [
            "#695f49",
            "#514832"
        ]
    },
    {
        "name": "Dancer's Dress (Altered)",
        "image": "Chest\\SOTE/Dancer's Dress (Altered).png",
        "primaryColor": "#584e2c",
        "secondaryColors": [
            "#47454a",
            "#3d3c41"
        ]
    },
    {
        "name": "Dancer's Dress",
        "image": "Chest\\SOTE/Dancer's Dress.png",
        "primaryColor": "#791813",
        "secondaryColors": [
            "#a29f8d",
            "#3e2f27"
        ]
    },
    {
        "name": "Death Knight Armor",
        "image": "Chest\\SOTE/Death Knight Armor.png",
        "primaryColor": "#575653",
        "secondaryColors": [
            "#514c45",
            "#4b4439"
        ]
    },
    {
        "name": "Divine Beast Warrior Armor",
        "image": "Chest\\SOTE/Divine Beast Warrior Armor.png",
        "primaryColor": "#a8a18f",
        "secondaryColors": [
            "#918975",
            "#837b68"
        ]
    },
    {
        "name": "Divine Bird Warrior Armor",
        "image": "Chest\\SOTE/Divine Bird Warrior Armor.png",
        "primaryColor": "#887553",
        "secondaryColors": [
            "#716145",
            "#5a4c33"
        ]
    },
    {
        "name": "Dryleaf Robe (Altered)",
        "image": "Chest\\SOTE/Dryleaf Robe (Altered).png",
        "primaryColor": "#847362",
        "secondaryColors": [
            "#5d5249",
            "#4f443a"
        ]
    },
    {
        "name": "Dryleaf Robe",
        "image": "Chest\\SOTE/Dryleaf Robe.png",
        "primaryColor": "#857563",
        "secondaryColors": [
            "#695d51",
            "#50453a"
        ]
    },
    {
        "name": "Finger Robe",
        "image": "Chest\\SOTE/Finger Robe.png",
        "primaryColor": "#8c8b8f",
        "secondaryColors": [
            "#5d5b5b",
            "#5b5757"
        ]
    },
    {
        "name": "Fire Knight Armor (Altered)",
        "image": "Chest\\SOTE/Fire Knight Armor (Altered).png",
        "primaryColor": "#55514f",
        "secondaryColors": [
            "#5d4949",
            "#42403e"
        ]
    },
    {
        "name": "Fire Knight Armor",
        "image": "Chest\\SOTE/Fire Knight Armor.png",
        "primaryColor": "#575350",
        "secondaryColors": [
            "#4d433a",
            "#682727"
        ]
    },
    {
        "name": "Freyja's Armor (Altered)",
        "image": "Chest\\SOTE/Freyja's Armor (Altered).png",
        "primaryColor": "#9f8b6d",
        "secondaryColors": [
            "#897457",
            "#6e5e48"
        ]
    },
    {
        "name": "Freyja's Armor",
        "image": "Chest\\SOTE/Freyja's Armor.png",
        "primaryColor": "#897558",
        "secondaryColors": [
            "#6e5e48",
            "#594834"
        ]
    },
    {
        "name": "Gaius's Armor",
        "image": "Chest\\SOTE/Gaius's Armor.png",
        "primaryColor": "#999490",
        "secondaryColors": [
            "#5a5652",
            "#4e423c"
        ]
    },
    {
        "name": "Gloried Attire",
        "image": "Chest\\SOTE/Gloried Attire.png",
        "primaryColor": "#804947",
        "secondaryColors": [
            "#263e50",
            "#c2b49a"
        ]
    },
    {
        "name": "Gravebird Armor",
        "image": "Chest\\SOTE/Gravebird Armor.png",
        "primaryColor": "#868578",
        "secondaryColors": [
            "#585a54",
            "#45443a"
        ]
    },
    {
        "name": "Gravebird's Blackquill Armor",
        "image": "Chest\\SOTE/Gravebird's Blackquill Armor.png",
        "primaryColor": "#858477",
        "secondaryColors": [
            "#545551",
            "#44443c"
        ]
    },
    {
        "name": "High Priest Robe",
        "image": "Chest\\SOTE/High Priest Robe.png",
        "primaryColor": "#554e4c",
        "secondaryColors": [
            "#504737",
            "#443d40"
        ]
    },
    {
        "name": "Highland Attire",
        "image": "Chest\\SOTE/Highland Attire.png",
        "primaryColor": "#9e907a",
        "secondaryColors": [
            "#365b6a",
            "#544737"
        ]
    },
    {
        "name": "Horned Warrior Armor",
        "image": "Chest\\SOTE/Horned Warrior Armor.png",
        "primaryColor": "#98885a",
        "secondaryColors": [
            "#87764d",
            "#6b604b"
        ]
    },
    {
        "name": "Igon's Armor (Altered)",
        "image": "Chest\\SOTE/Igon's Armor (Altered).png",
        "primaryColor": "#847465",
        "secondaryColors": [
            "#60564f",
            "#544639"
        ]
    },
    {
        "name": "Igon's Armor",
        "image": "Chest\\SOTE/Igon's Armor.png",
        "primaryColor": "#847364",
        "secondaryColors": [
            "#60564f",
            "#534539"
        ]
    },
    {
        "name": "Iron Rivet Armor",
        "image": "Chest\\SOTE/Iron Rivet Armor.png",
        "primaryColor": "#645b50",
        "secondaryColors": [
            "#5f574e",
            "#4c443b"
        ]
    },
    {
        "name": "Leda's Armor",
        "image": "Chest\\SOTE/Leda's Armor.png",
        "primaryColor": "#cbc5b8",
        "secondaryColors": [
            "#3f3737",
            "#948976"
        ]
    },
    {
        "name": "Messmer Soldier Armor (Altered)",
        "image": "Chest\\SOTE/Messmer Soldier Armor (Altered).png",
        "primaryColor": "#848371",
        "secondaryColors": [
            "#5c564c",
            "#48443a"
        ]
    },
    {
        "name": "Messmer Soldier Armor",
        "image": "Chest\\SOTE/Messmer Soldier Armor.png",
        "primaryColor": "#615d52",
        "secondaryColors": [
            "#5b554a",
            "#49443a"
        ]
    },
    {
        "name": "Messmer's Armor",
        "image": "Chest\\SOTE/Messmer's Armor.png",
        "primaryColor": "#721f1e",
        "secondaryColors": [
            "#554438",
            "#62554d"
        ]
    },
    {
        "name": "Oathseeker Knight Armor",
        "image": "Chest\\SOTE/Oathseeker Knight Armor.png",
        "primaryColor": "#a79994",
        "secondaryColors": [
            "#615751",
            "#4b433b"
        ]
    },
    {
        "name": "Rakshasa Armor",
        "image": "Chest\\SOTE/Rakshasa Armor.png",
        "primaryColor": "#601e15",
        "secondaryColors": [
            "#6b514a",
            "#5d423c"
        ]
    },
    {
        "name": "Rellana's Armor",
        "image": "Chest\\SOTE/Rellana's Armor.png",
        "primaryColor": "#969896",
        "secondaryColors": [
            "#1c203f",
            "#4b433b"
        ]
    },
    {
        "name": "Shadow Militiaman Armor",
        "image": "Chest\\SOTE/Shadow Militiaman Armor.png",
        "primaryColor": "#5a504d",
        "secondaryColors": [
            "#564b47",
            "#4e413c"
        ]
    },
    {
        "name": "Thiollier's Garb (Altered)",
        "image": "Chest\\SOTE/Thiollier's Garb (Altered).png",
        "primaryColor": "#575451",
        "secondaryColors": [
            "#564f4c",
            "#4b423c"
        ]
    },
    {
        "name": "Thiollier's Garb",
        "image": "Chest\\SOTE/Thiollier's Garb.png",
        "primaryColor": "#99979a",
        "secondaryColors": [
            "#5e5b5a",
            "#4c423c"
        ]
    },
    {
        "name": "Verdigris Armor",
        "image": "Chest\\SOTE/Verdigris Armor.png",
        "primaryColor": "#565b56",
        "secondaryColors": [
            "#42443d",
            "#3b4444"
        ]
    },
    {
        "name": "Young Lion's Armor (Altered)",
        "image": "Chest\\SOTE/Young Lion's Armor (Altered).png",
        "primaryColor": "#a9905b",
        "secondaryColors": [
            "#a32933",
            "#635647"
        ]
    },
    {
        "name": "Young Lion's Armor",
        "image": "Chest\\SOTE/Young Lion's Armor.png",
        "primaryColor": "#a9905b",
        "secondaryColors": [
            "#a32933",
            "#635647"
        ]
    },
    {
        "name": "Alberich's Bracers",
        "image": "Hands/Alberich's Bracers.png",
        "primaryColor": "#9a8e8c",
        "secondaryColors": [
            "#916967",
            "#655957"
        ]
    },
    {
        "name": "All-Knowing Gauntlets",
        "image": "Hands/All-Knowing Gauntlets.png",
        "primaryColor": "#dddad5",
        "secondaryColors": [
            "#a29d94",
            "#8d8677"
        ]
    },
    {
        "name": "Astrologer Gloves",
        "image": "Hands/Astrologer Gloves.png",
        "primaryColor": "#d2cbc3",
        "secondaryColors": [
            "#cac3ba",
            "#c3bbb2"
        ]
    },
    {
        "name": "Azur's Manchettes",
        "image": "Hands/Azur's Manchettes.png",
        "primaryColor": "#9c9592",
        "secondaryColors": [
            "#2aa695",
            "#646160"
        ]
    },
    {
        "name": "Bandit Manchettes",
        "image": "Hands/Bandit Manchettes.png",
        "primaryColor": "#9c9890",
        "secondaryColors": [
            "#8e8677",
            "#857669"
        ]
    },
    {
        "name": "Banished Knight Gauntlets",
        "image": "Hands/Banished Knight Gauntlets.png",
        "primaryColor": "#e2ded8",
        "secondaryColors": [
            "#a39d93",
            "#8d8679"
        ]
    },
    {
        "name": "Battlemage Manchettes",
        "image": "Hands/Battlemage Manchettes.png",
        "primaryColor": "#a29f97",
        "secondaryColors": [
            "#8b857a",
            "#837b71"
        ]
    },
    {
        "name": "Beast Champion Gauntlets",
        "image": "Hands/Beast Champion Gauntlets.png",
        "primaryColor": "#d4d5d6",
        "secondaryColors": [
            "#999998",
            "#908776"
        ]
    },
    {
        "name": "Black Knife Gauntlets",
        "image": "Hands/Black Knife Gauntlets.png",
        "primaryColor": "#ced1d4",
        "secondaryColors": [
            "#96999c",
            "#585a5b"
        ]
    },
    {
        "name": "Blackflame Monk Gauntlets",
        "image": "Hands/Blackflame Monk Gauntlets.png",
        "primaryColor": "#a99c8e",
        "secondaryColors": [
            "#968776",
            "#867768"
        ]
    },
    {
        "name": "Blaidd's Gauntlets",
        "image": "Hands/Blaidd's Gauntlets.png",
        "primaryColor": "#9a9896",
        "secondaryColors": [
            "#615d59",
            "#48433b"
        ]
    },
    {
        "name": "Bloodhound Knight Gauntlets",
        "image": "Hands/Bloodhound Knight Gauntlets.png",
        "primaryColor": "#a29a92",
        "secondaryColors": [
            "#85776c",
            "#625a54"
        ]
    },
    {
        "name": "Bloodsoaked Manchettes",
        "image": "Hands/Bloodsoaked Manchettes.png",
        "primaryColor": "#a6978c",
        "secondaryColors": [
            "#968579",
            "#89766a"
        ]
    },
    {
        "name": "Blue Silver Bracelets",
        "image": "Hands/Blue Silver Bracelets.png",
        "primaryColor": "#9295a5",
        "secondaryColors": [
            "#798594",
            "#6f7687"
        ]
    },
    {
        "name": "Briar Gauntlets",
        "image": "Hands/Briar Gauntlets.png",
        "primaryColor": "#8c6b63",
        "secondaryColors": [
            "#62544e",
            "#57433a"
        ]
    },
    {
        "name": "Bull-Goat Gauntlets",
        "image": "Hands/Bull-Goat Gauntlets.png",
        "primaryColor": "#9b9694",
        "secondaryColors": [
            "#837b76",
            "#615d5b"
        ]
    },
    {
        "name": "Carian Knight Gauntlets",
        "image": "Hands/Carian Knight Gauntlets.png",
        "primaryColor": "#9d9a98",
        "secondaryColors": [
            "#5d5854",
            "#4c443b"
        ]
    },
    {
        "name": "Chain Gauntlets",
        "image": "Hands/Chain Gauntlets.png",
        "primaryColor": "#9d998c",
        "secondaryColors": [
            "#8d8877",
            "#837b71"
        ]
    },
    {
        "name": "Chain Gauntlets_ (2)",
        "image": "Hands/Chain Gauntlets_ (2).png",
        "primaryColor": "#88746a",
        "secondaryColors": [
            "#645752",
            "#52433c"
        ]
    },
    {
        "name": "Champion Bracers",
        "image": "Hands/Champion Bracers.png",
        "primaryColor": "#8c8f93",
        "secondaryColors": [
            "#8c7162",
            "#565555"
        ]
    },
    {
        "name": "Cleanrot Gauntlets",
        "image": "Hands/Cleanrot Gauntlets.png",
        "primaryColor": "#c6b59b",
        "secondaryColors": [
            "#ac9e8d",
            "#a08c73"
        ]
    },
    {
        "name": "Confessor Gloves",
        "image": "Hands/Confessor Gloves.png",
        "primaryColor": "#9c9896",
        "secondaryColors": [
            "#867668",
            "#5f5a57"
        ]
    },
    {
        "name": "Crucible Gauntlets",
        "image": "Hands/Crucible Gauntlets.png",
        "primaryColor": "#8a725e",
        "secondaryColors": [
            "#6b584b",
            "#5c4737"
        ]
    },
    {
        "name": "Cuckoo Knight Gauntlets",
        "image": "Hands/Cuckoo Knight Gauntlets.png",
        "primaryColor": "#7d8790",
        "secondaryColors": [
            "#969a9f",
            "#7c8187"
        ]
    },
    {
        "name": "Depraved Perfumer Gloves",
        "image": "Hands/Depraved Perfumer Gloves.png",
        "primaryColor": "#866657",
        "secondaryColors": [
            "#70544a",
            "#664639"
        ]
    },
    {
        "name": "Drake Knight Gauntlets",
        "image": "Hands/Drake Knight Gauntlets.png",
        "primaryColor": "#0e1615",
        "secondaryColors": [
            "#803b2d",
            "#644339"
        ]
    },
    {
        "name": "Eccentric's Manchettes",
        "image": "Hands/Eccentric's Manchettes.png",
        "primaryColor": "#a29f9c",
        "secondaryColors": [
            "#9e9a97",
            "#8b8d91"
        ]
    },
    {
        "name": "Elden Lord Bracers",
        "image": "Hands/Elden Lord Bracers.png",
        "primaryColor": "#a09c95",
        "secondaryColors": [
            "#8f8578",
            "#625e57"
        ]
    },
    {
        "name": "Errant Sorcerer Manchettes",
        "image": "Hands/Errant Sorcerer Manchettes.png",
        "primaryColor": "#886e60",
        "secondaryColors": [
            "#695852",
            "#54433b"
        ]
    },
    {
        "name": "Exile Gauntlets",
        "image": "Hands/Exile Gauntlets.png",
        "primaryColor": "#dcd6d0",
        "secondaryColors": [
            "#a8a19a",
            "#605a54"
        ]
    },
    {
        "name": "Fingerprint Gauntlets",
        "image": "Hands/Fingerprint Gauntlets.png",
        "primaryColor": "#9594a1",
        "secondaryColors": [
            "#777786",
            "#57565f"
        ]
    },
    {
        "name": "Fire Monk Gauntlets",
        "image": "Hands/Fire Monk Gauntlets.png",
        "primaryColor": "#999298",
        "secondaryColors": [
            "#887573",
            "#5d575b"
        ]
    },
    {
        "name": "Fire Prelate Gauntlets",
        "image": "Hands/Fire Prelate Gauntlets.png",
        "primaryColor": "#d2d4d5",
        "secondaryColors": [
            "#98999b",
            "#5b5b5c"
        ]
    },
    {
        "name": "Foot Soldier Gauntlets",
        "image": "Hands/Foot Soldier Gauntlets.png",
        "primaryColor": "#afa18f",
        "secondaryColors": [
            "#9f8b73",
            "#8a755e"
        ]
    },
    {
        "name": "Gelmir Knight Gauntlets",
        "image": "Hands/Gelmir Knight Gauntlets.png",
        "primaryColor": "#d6d6d9",
        "secondaryColors": [
            "#9a989c",
            "#5c5a5b"
        ]
    },
    {
        "name": "Godrick Knight Gauntlets",
        "image": "Hands/Godrick Knight Gauntlets.png",
        "primaryColor": "#aaa392",
        "secondaryColors": [
            "#8f8875",
            "#655e50"
        ]
    },
    {
        "name": "Godrick Soldier Gauntlets",
        "image": "Hands/Godrick Soldier Gauntlets.png",
        "primaryColor": "#a1998e",
        "secondaryColors": [
            "#918578",
            "#877766"
        ]
    },
    {
        "name": "Godskin Apostle Bracelets",
        "image": "Hands/Godskin Apostle Bracelets.png",
        "primaryColor": "#a69f94",
        "secondaryColors": [
            "#8e8577",
            "#5e5a50"
        ]
    },
    {
        "name": "Godskin Noble Bracelets",
        "image": "Hands/Godskin Noble Bracelets.png",
        "primaryColor": "#e0dedb",
        "secondaryColors": [
            "#a19f9a",
            "#8c8679"
        ]
    },
    {
        "name": "Gold Bracelets",
        "image": "Hands/Gold Bracelets.png",
        "primaryColor": "#afa38e",
        "secondaryColors": [
            "#9f8e72",
            "#87775e"
        ]
    },
    {
        "name": "Gravekeeper Cloak (Altered)",
        "image": "Hands/Gravekeeper Cloak (Altered).png",
        "primaryColor": "#5f5f55",
        "secondaryColors": [
            "#5a5d54",
            "#47443c"
        ]
    },
    {
        "name": "Gravekeeper Cloak (Altered)_()",
        "image": "Hands/Gravekeeper Cloak (Altered)_().png",
        "primaryColor": "#5f5f55",
        "secondaryColors": [
            "#5a5d54",
            "#47443c"
        ]
    },
    {
        "name": "Guardian Bracers",
        "image": "Hands/Guardian Bracers.png",
        "primaryColor": "#9d9169",
        "secondaryColors": [
            "#867954",
            "#716849"
        ]
    },
    {
        "name": "Haligtree Gauntlets",
        "image": "Hands/Haligtree Gauntlets.png",
        "primaryColor": "#98908e",
        "secondaryColors": [
            "#8d827a",
            "#847972"
        ]
    },
    {
        "name": "Haligtree Knight Gauntlets",
        "image": "Hands/Haligtree Knight Gauntlets.png",
        "primaryColor": "#a8a293",
        "secondaryColors": [
            "#8f8877",
            "#635d50"
        ]
    },
    {
        "name": "Highwayman Gauntlets",
        "image": "Hands/Highwayman Gauntlets.png",
        "primaryColor": "#9f9791",
        "secondaryColors": [
            "#867469",
            "#635550"
        ]
    },
    {
        "name": "Hoslow's Gauntlets",
        "image": "Hands/Hoslow's Gauntlets.png",
        "primaryColor": "#d5d5d5",
        "secondaryColors": [
            "#9d9d9d",
            "#5d5d5c"
        ]
    },
    {
        "name": "Iron Gauntlets",
        "image": "Hands/Iron Gauntlets.png",
        "primaryColor": "#e0dedc",
        "secondaryColors": [
            "#a39e9a",
            "#655d53"
        ]
    },
    {
        "name": "Kaiden Gauntlets",
        "image": "Hands/Kaiden Gauntlets.png",
        "primaryColor": "#a99a8e",
        "secondaryColors": [
            "#9b8875",
            "#8e6f5f"
        ]
    },
    {
        "name": "Knight Gauntlets",
        "image": "Hands/Knight Gauntlets.png",
        "primaryColor": "#dbd8d7",
        "secondaryColors": [
            "#9e9b9b",
            "#5d5958"
        ]
    },
    {
        "name": "Land of Reeds Gauntlets",
        "image": "Hands/Land of Reeds Gauntlets.png",
        "primaryColor": "#a89c94",
        "secondaryColors": [
            "#99685e",
            "#635654"
        ]
    },
    {
        "name": "Leather Gloves",
        "image": "Hands/Leather Gloves.png",
        "primaryColor": "#958576",
        "secondaryColors": [
            "#897668",
            "#685b50"
        ]
    },
    {
        "name": "Leyndell Knight Gauntlets",
        "image": "Hands/Leyndell Knight Gauntlets.png",
        "primaryColor": "#b1a48c",
        "secondaryColors": [
            "#988a71",
            "#6c614e"
        ]
    },
    {
        "name": "Leyndell Soldier Gauntlets",
        "image": "Hands/Leyndell Soldier Gauntlets.png",
        "primaryColor": "#a0978d",
        "secondaryColors": [
            "#918678",
            "#857a6d"
        ]
    },
    {
        "name": "Lionel's Gauntlets",
        "image": "Hands/Lionel's Gauntlets.png",
        "primaryColor": "#1c2227",
        "secondaryColors": [
            "#565859",
            "#3b4347"
        ]
    },
    {
        "name": "Lusat's Manchettes",
        "image": "Hands/Lusat's Manchettes.png",
        "primaryColor": "#999290",
        "secondaryColors": [
            "#847b77",
            "#566a98"
        ]
    },
    {
        "name": "Malenia's Gauntlet",
        "image": "Hands/Malenia's Gauntlet.png",
        "primaryColor": "#b8ab8a",
        "secondaryColors": [
            "#aea68e",
            "#978d71"
        ]
    },
    {
        "name": "Malformed Dragon Gauntlets",
        "image": "Hands/Malformed Dragon Gauntlets.png",
        "primaryColor": "#302b24",
        "secondaryColors": [
            "#5c5c53",
            "#474539"
        ]
    },
    {
        "name": "Maliketh's Gauntlets",
        "image": "Hands/Maliketh's Gauntlets.png",
        "primaryColor": "#1c1c1c",
        "secondaryColors": [
            "#615a4d",
            "#514837"
        ]
    },
    {
        "name": "Mausoleum Gauntlets",
        "image": "Hands/Mausoleum Gauntlets.png",
        "primaryColor": "#9e9891",
        "secondaryColors": [
            "#928576",
            "#877869"
        ]
    },
    {
        "name": "Mausoleum Knight Gauntlets",
        "image": "Hands/Mausoleum Knight Gauntlets.png",
        "primaryColor": "#767877",
        "secondaryColors": [
            "#9b9d9e",
            "#5a5b5a"
        ]
    },
    {
        "name": "Mushroom Arms",
        "image": "Hands/Mushroom Arms.png",
        "primaryColor": "#a89f96",
        "secondaryColors": [
            "#a09f9c",
            "#907261"
        ]
    },
    {
        "name": "Nights Cavalry Gauntlets",
        "image": "Hands/Nights Cavalry Gauntlets.png",
        "primaryColor": "#212021",
        "secondaryColors": [
            "#585553",
            "#44413d"
        ]
    },
    {
        "name": "Noble's Gloves",
        "image": "Hands/Noble's Gloves.png",
        "primaryColor": "#a9a3a0",
        "secondaryColors": [
            "#89685a",
            "#6f554b"
        ]
    },
    {
        "name": "Nox Monk Bracelets",
        "image": "Hands/Nox Monk Bracelets.png",
        "primaryColor": "#a5a298",
        "secondaryColors": [
            "#8a8578",
            "#676057"
        ]
    },
    {
        "name": "Omen Gauntlets",
        "image": "Hands/Omen Gauntlets.png",
        "primaryColor": "#9a8f8a",
        "secondaryColors": [
            "#8f6a5d",
            "#675753"
        ]
    },
    {
        "name": "Omenkiller Long Gloves",
        "image": "Hands/Omenkiller Long Gloves.png",
        "primaryColor": "#ae928e",
        "secondaryColors": [
            "#a98579",
            "#936b66"
        ]
    },
    {
        "name": "Perfumer Gloves",
        "image": "Hands/Perfumer Gloves.png",
        "primaryColor": "#5f534b",
        "secondaryColors": [
            "#5a4a36",
            "#50443b"
        ]
    },
    {
        "name": "Preceptor's Gloves",
        "image": "Hands/Preceptor's Gloves.png",
        "primaryColor": "#4c4b49",
        "secondaryColors": [
            "#44413d",
            "#403d3a"
        ]
    },
    {
        "name": "Queen's Bracelets",
        "image": "Hands/Queen's Bracelets.png",
        "primaryColor": "#9e9298",
        "secondaryColors": [
            "#5d5c5a",
            "#4a453a"
        ]
    },
    {
        "name": "Radahn Soldier Gauntlets",
        "image": "Hands/Radahn Soldier Gauntlets.png",
        "primaryColor": "#a09a8f",
        "secondaryColors": [
            "#918676",
            "#857766"
        ]
    },
    {
        "name": "Radahn's Gauntlets",
        "image": "Hands/Radahn's Gauntlets.png",
        "primaryColor": "#988974",
        "secondaryColors": [
            "#897462",
            "#34302d"
        ]
    },
    {
        "name": "Raging Wolf Gauntlets",
        "image": "Hands/Raging Wolf Gauntlets.png",
        "primaryColor": "#9c9692",
        "secondaryColors": [
            "#8c827b",
            "#837a74"
        ]
    },
    {
        "name": "Raya Lucarian Gauntlets",
        "image": "Hands/Raya Lucarian Gauntlets.png",
        "primaryColor": "#a19a91",
        "secondaryColors": [
            "#918577",
            "#857869"
        ]
    },
    {
        "name": "Redmane Knight Gauntlets",
        "image": "Hands/Redmane Knight Gauntlets.png",
        "primaryColor": "#d8d5d3",
        "secondaryColors": [
            "#a29c99",
            "#5c5754"
        ]
    },
    {
        "name": "Ronin's Gauntlets",
        "image": "Hands/Ronin's Gauntlets.png",
        "primaryColor": "#dad9d6",
        "secondaryColors": [
            "#9f9c98",
            "#89837b"
        ]
    },
    {
        "name": "Royal Knight Gauntlets",
        "image": "Hands/Royal Knight Gauntlets.png",
        "primaryColor": "#e2ded5",
        "secondaryColors": [
            "#aaa293",
            "#918776"
        ]
    },
    {
        "name": "Royal Remains Gauntlets",
        "image": "Hands/Royal Remains Gauntlets.png",
        "primaryColor": "#151e21",
        "secondaryColors": [
            "#8b735c",
            "#5e5953"
        ]
    },
    {
        "name": "Scaled Gauntlets",
        "image": "Hands/Scaled Gauntlets.png",
        "primaryColor": "#d9d7d3",
        "secondaryColors": [
            "#a29e97",
            "#615e58"
        ]
    },
    {
        "name": "Sorcerer Manchettes",
        "image": "Hands/Sorcerer Manchettes.png",
        "primaryColor": "#929089",
        "secondaryColors": [
            "#86847b",
            "#817d75"
        ]
    },
    {
        "name": "Spellblade's Gloves",
        "image": "Hands/Spellblade's Gloves.png",
        "primaryColor": "#c3b9ab",
        "secondaryColors": [
            "#aba194",
            "#928877"
        ]
    },
    {
        "name": "Traveler's Gloves",
        "image": "Hands/Traveler's Gloves.png",
        "primaryColor": "#9b8c6e",
        "secondaryColors": [
            "#87785d",
            "#59575b"
        ]
    },
    {
        "name": "Traveler's Manchettes",
        "image": "Hands/Traveler's Manchettes.png",
        "primaryColor": "#a09091",
        "secondaryColors": [
            "#887472",
            "#665656"
        ]
    },
    {
        "name": "Traveling Maiden Gloves",
        "image": "Hands/Traveling Maiden Gloves.png",
        "primaryColor": "#4e5254",
        "secondaryColors": [
            "#a88777",
            "#3d4148"
        ]
    },
    {
        "name": "Tree Sentinel Gauntlets",
        "image": "Hands/Tree Sentinel Gauntlets.png",
        "primaryColor": "#a18d6e",
        "secondaryColors": [
            "#897457",
            "#726149"
        ]
    },
    {
        "name": "Twinned Gauntlets",
        "image": "Hands/Twinned Gauntlets.png",
        "primaryColor": "#9c8a71",
        "secondaryColors": [
            "#88765f",
            "#6b5d4d"
        ]
    },
    {
        "name": "Vagabond Knight Gauntlets",
        "image": "Hands/Vagabond Knight Gauntlets.png",
        "primaryColor": "#a69f96",
        "secondaryColors": [
            "#908679",
            "#5e5952"
        ]
    },
    {
        "name": "Veteran's Gauntlets",
        "image": "Hands/Veteran's Gauntlets.png",
        "primaryColor": "#a69e92",
        "secondaryColors": [
            "#908678",
            "#86786b"
        ]
    },
    {
        "name": "Vulgar Militia Gauntlets",
        "image": "Hands/Vulgar Militia Gauntlets.png",
        "primaryColor": "#867064",
        "secondaryColors": [
            "#6d574e",
            "#57443a"
        ]
    },
    {
        "name": "War Surgeon Gloves",
        "image": "Hands/War Surgeon Gloves.png",
        "primaryColor": "#5a4b49",
        "secondaryColors": [
            "#52413d",
            "#483834"
        ]
    },
    {
        "name": "Warrior Gauntlets",
        "image": "Hands/Warrior Gauntlets.png",
        "primaryColor": "#999592",
        "secondaryColors": [
            "#887266",
            "#685b55"
        ]
    },
    {
        "name": "White Reed Gauntlets",
        "image": "Hands/White Reed Gauntlets.png",
        "primaryColor": "#ddd8d6",
        "secondaryColors": [
            "#a69a97",
            "#4e85af"
        ]
    },
    {
        "name": "Zamor Bracelets",
        "image": "Hands/Zamor Bracelets.png",
        "primaryColor": "#a29f95",
        "secondaryColors": [
            "#8b8677",
            "#666359"
        ]
    },
    {
        "name": "Ansbach's Manchettes",
        "image": "Hands\\SOTE/Ansbach's Manchettes.png",
        "primaryColor": "#655543",
        "secondaryColors": [
            "#544636",
            "#453a2e"
        ]
    },
    {
        "name": "Ascetic's Wrist Guards",
        "image": "Hands\\SOTE/Ascetic's Wrist Guards.png",
        "primaryColor": "#938775",
        "secondaryColors": [
            "#847868",
            "#695e4f"
        ]
    },
    {
        "name": "Black Knight Gauntlets",
        "image": "Hands\\SOTE/Black Knight Gauntlets.png",
        "primaryColor": "#222221",
        "secondaryColors": [
            "#605a53",
            "#4d4639"
        ]
    },
    {
        "name": "Braided Arm Wraps",
        "image": "Hands\\SOTE/Braided Arm Wraps.png",
        "primaryColor": "#857a6b",
        "secondaryColors": [
            "#61594e",
            "#4a443b"
        ]
    },
    {
        "name": "Common Soldier Gauntlets",
        "image": "Hands\\SOTE/Common Soldier Gauntlets.png",
        "primaryColor": "#a29a94",
        "secondaryColors": [
            "#645b56",
            "#51433b"
        ]
    },
    {
        "name": "Dancer's Bracer",
        "image": "Hands\\SOTE/Dancer's Bracer.png",
        "primaryColor": "#9b978e",
        "secondaryColors": [
            "#5e5a51",
            "#47443b"
        ]
    },
    {
        "name": "Death Knight Gauntlets",
        "image": "Hands\\SOTE/Death Knight Gauntlets.png",
        "primaryColor": "#8c7256",
        "secondaryColors": [
            "#685b4e",
            "#5b4936"
        ]
    },
    {
        "name": "Divine Bird Warrior Gauntlets",
        "image": "Hands\\SOTE/Divine Bird Warrior Gauntlets.png",
        "primaryColor": "#9f8f65",
        "secondaryColors": [
            "#88764f",
            "#766746"
        ]
    },
    {
        "name": "Dryleaf Arm Wraps",
        "image": "Hands\\SOTE/Dryleaf Arm Wraps.png",
        "primaryColor": "#847661",
        "secondaryColors": [
            "#695b4a",
            "#554738"
        ]
    },
    {
        "name": "Fire Knight Gauntlets",
        "image": "Hands\\SOTE/Fire Knight Gauntlets.png",
        "primaryColor": "#9b968d",
        "secondaryColors": [
            "#5f5b55",
            "#48433b"
        ]
    },
    {
        "name": "Freyja's Gauntlets",
        "image": "Hands\\SOTE/Freyja's Gauntlets.png",
        "primaryColor": "#896f5b",
        "secondaryColors": [
            "#62564a",
            "#5a4839"
        ]
    },
    {
        "name": "Gaius's Gauntlets",
        "image": "Hands\\SOTE/Gaius's Gauntlets.png",
        "primaryColor": "#393434",
        "secondaryColors": [
            "#5c5553",
            "#47413d"
        ]
    },
    {
        "name": "Gauntlets of Night",
        "image": "Hands\\SOTE/Gauntlets of Night.png",
        "primaryColor": "#0c0c0d",
        "secondaryColors": [
            "#43413d",
            "#423c37"
        ]
    },
    {
        "name": "Gauntlets of Solitude",
        "image": "Hands\\SOTE/Gauntlets of Solitude.png",
        "primaryColor": "#939291",
        "secondaryColors": [
            "#575655",
            "#41403e"
        ]
    },
    {
        "name": "Gravebird Bracelets",
        "image": "Hands\\SOTE/Gravebird Bracelets.png",
        "primaryColor": "#9c9c8d",
        "secondaryColors": [
            "#878777",
            "#686859"
        ]
    },
    {
        "name": "High Priest Gloves",
        "image": "Hands\\SOTE/High Priest Gloves.png",
        "primaryColor": "#5a4e46",
        "secondaryColors": [
            "#51443a",
            "#3e3c40"
        ]
    },
    {
        "name": "Horned Warrior Gauntlets",
        "image": "Hands\\SOTE/Horned Warrior Gauntlets.png",
        "primaryColor": "#a39d8f",
        "secondaryColors": [
            "#8f8775",
            "#837b68"
        ]
    },
    {
        "name": "Igon's Gauntlets",
        "image": "Hands\\SOTE/Igon's Gauntlets.png",
        "primaryColor": "#565050",
        "secondaryColors": [
            "#4b413c",
            "#443b38"
        ]
    },
    {
        "name": "Iron Rivet Gauntlets",
        "image": "Hands\\SOTE/Iron Rivet Gauntlets.png",
        "primaryColor": "#a19c93",
        "secondaryColors": [
            "#85746b",
            "#665a52"
        ]
    },
    {
        "name": "Leather Arm Wraps",
        "image": "Hands\\SOTE/Leather Arm Wraps.png",
        "primaryColor": "#b29f8b",
        "secondaryColors": [
            "#a08872",
            "#864949"
        ]
    },
    {
        "name": "Messmer Soldier Gauntlets",
        "image": "Hands\\SOTE/Messmer Soldier Gauntlets.png",
        "primaryColor": "#96928d",
        "secondaryColors": [
            "#85827b",
            "#5f5c57"
        ]
    },
    {
        "name": "Messmer's Gauntlets",
        "image": "Hands\\SOTE/Messmer's Gauntlets.png",
        "primaryColor": "#a29890",
        "secondaryColors": [
            "#5f5651",
            "#4d423b"
        ]
    },
    {
        "name": "Oathseeker Knight Gauntlets",
        "image": "Hands\\SOTE/Oathseeker Knight Gauntlets.png",
        "primaryColor": "#171415",
        "secondaryColors": [
            "#5f5242",
            "#4d4439"
        ]
    },
    {
        "name": "Rakshasa Gauntlets",
        "image": "Hands\\SOTE/Rakshasa Gauntlets.png",
        "primaryColor": "#601e15",
        "secondaryColors": [
            "#6b504a",
            "#60433c"
        ]
    },
    {
        "name": "Rellana's Gloves",
        "image": "Hands\\SOTE/Rellana's Gloves.png",
        "primaryColor": "#846f62",
        "secondaryColors": [
            "#67554d",
            "#54433c"
        ]
    },
    {
        "name": "Shadow Militiaman Gauntlets",
        "image": "Hands\\SOTE/Shadow Militiaman Gauntlets.png",
        "primaryColor": "#82786d",
        "secondaryColors": [
            "#645a52",
            "#50453a"
        ]
    },
    {
        "name": "Thiollier's Gloves",
        "image": "Hands\\SOTE/Thiollier's Gloves.png",
        "primaryColor": "#827a6f",
        "secondaryColors": [
            "#5c514c",
            "#4f433c"
        ]
    },
    {
        "name": "Verdigris Gauntlets",
        "image": "Hands\\SOTE/Verdigris Gauntlets.png",
        "primaryColor": "#565955",
        "secondaryColors": [
            "#42433d",
            "#3d4341"
        ]
    },
    {
        "name": "Young Lion's Gauntlets",
        "image": "Hands\\SOTE/Young Lion's Gauntlets.png",
        "primaryColor": "#8a6837",
        "secondaryColors": [
            "#696049",
            "#634c2c"
        ]
    },
    {
        "name": "Alberich's Pointed Hat (Altered)",
        "image": "Head/Alberich's Pointed Hat (Altered).png",
        "primaryColor": "#966556",
        "secondaryColors": [
            "#555853",
            "#d85c37"
        ]
    },
    {
        "name": "Alberich's Pointed Hat",
        "image": "Head/Alberich's Pointed Hat.png",
        "primaryColor": "#54514d",
        "secondaryColors": [
            "#504d4b",
            "#d85c37"
        ]
    },
    {
        "name": "Albinauric Mask",
        "image": "Head/Albinauric Mask.png",
        "primaryColor": "#d1d0d5",
        "secondaryColors": [
            "#a09da0",
            "#5e5a5a"
        ]
    },
    {
        "name": "All-Knowing Helm",
        "image": "Head/All-Knowing Helm.png",
        "primaryColor": "#9e9991",
        "secondaryColors": [
            "#89847a",
            "#635e56"
        ]
    },
    {
        "name": "Aristocrat Hat",
        "image": "Head/Aristocrat Hat.png",
        "primaryColor": "#8f8773",
        "secondaryColors": [
            "#837b69",
            "#656156"
        ]
    },
    {
        "name": "Aristocrat Headband",
        "image": "Head/Aristocrat Headband.png",
        "primaryColor": "#887451",
        "secondaryColors": [
            "#6e6047",
            "#584c35"
        ]
    },
    {
        "name": "Ash-of-War Scarab",
        "image": "Head/Ash-of-War Scarab.png",
        "primaryColor": "#9d9b9a",
        "secondaryColors": [
            "#887454",
            "#615d58"
        ]
    },
    {
        "name": "Astrologer Hood",
        "image": "Head/Astrologer Hood.png",
        "primaryColor": "#5a4c4a",
        "secondaryColors": [
            "#564947",
            "#4c403e"
        ]
    },
    {
        "name": "Azur's Glintstone Crown",
        "image": "Head/Azur's Glintstone Crown.png",
        "primaryColor": "#87766a",
        "secondaryColors": [
            "#675d52",
            "#14654e"
        ]
    },
    {
        "name": "Bandit Mask",
        "image": "Head/Bandit Mask.png",
        "primaryColor": "#5d5c5d",
        "secondaryColors": [
            "#595959",
            "#535253"
        ]
    },
    {
        "name": "Banished Knight Helm (Altered)",
        "image": "Head/Banished Knight Helm (Altered).png",
        "primaryColor": "#a7a093",
        "secondaryColors": [
            "#8e8678",
            "#837b6d"
        ]
    },
    {
        "name": "Banished Knight Helm",
        "image": "Head/Banished Knight Helm.png",
        "primaryColor": "#8b6e5d",
        "secondaryColors": [
            "#6d5849",
            "#5a4739"
        ]
    },
    {
        "name": "Beast Champion Helm",
        "image": "Head/Beast Champion Helm.png",
        "primaryColor": "#d3d3d4",
        "secondaryColors": [
            "#9a9a99",
            "#5d5d5b"
        ]
    },
    {
        "name": "Black Dumpling",
        "image": "Head/Black Dumpling.png",
        "primaryColor": "#857778",
        "secondaryColors": [
            "#5e5154",
            "#4b3d41"
        ]
    },
    {
        "name": "Black Hood",
        "image": "Head/Black Hood.png",
        "primaryColor": "#565459",
        "secondaryColors": [
            "#4f4e54",
            "#403e43"
        ]
    },
    {
        "name": "Black Knife Hood",
        "image": "Head/Black Knife Hood.png",
        "primaryColor": "#585960",
        "secondaryColors": [
            "#4f5259",
            "#3e4047"
        ]
    },
    {
        "name": "Black Wolf Mask",
        "image": "Head/Black Wolf Mask.png",
        "primaryColor": "#96928f",
        "secondaryColors": [
            "#5f5d5a",
            "#5f5b59"
        ]
    },
    {
        "name": "Blackflame Monk Hood",
        "image": "Head/Blackflame Monk Hood.png",
        "primaryColor": "#928b87",
        "secondaryColors": [
            "#837974",
            "#6b625d"
        ]
    },
    {
        "name": "Blackguard's Iron Mask",
        "image": "Head/Blackguard's Iron Mask.png",
        "primaryColor": "#ac9e8d",
        "secondaryColors": [
            "#a08972",
            "#8b735d"
        ]
    },
    {
        "name": "Bloodhound Knight Helm",
        "image": "Head/Bloodhound Knight Helm.png",
        "primaryColor": "#9c9286",
        "secondaryColors": [
            "#a59d91",
            "#8e8578"
        ]
    },
    {
        "name": "Bloodsoaked Mask",
        "image": "Head/Bloodsoaked Mask.png",
        "primaryColor": "#b19d8d",
        "secondaryColors": [
            "#a28976",
            "#8d7361"
        ]
    },
    {
        "name": "Blue Cloth Cowl",
        "image": "Head/Blue Cloth Cowl.png",
        "primaryColor": "#908d8a",
        "secondaryColors": [
            "#6b7884",
            "#616161"
        ]
    },
    {
        "name": "Blue Festive Hood",
        "image": "Head/Blue Festive Hood.png",
        "primaryColor": "#797883",
        "secondaryColors": [
            "#625d61",
            "#4f4638"
        ]
    },
    {
        "name": "Blue Silver Mail Hood",
        "image": "Head/Blue Silver Mail Hood.png",
        "primaryColor": "#8a8e8d",
        "secondaryColors": [
            "#7d8282",
            "#5c5f5d"
        ]
    },
    {
        "name": "Briar Helm",
        "image": "Head/Briar Helm.png",
        "primaryColor": "#8c6c5e",
        "secondaryColors": [
            "#6a584d",
            "#5d4539"
        ]
    },
    {
        "name": "Bull-Goat Helm",
        "image": "Head/Bull-Goat Helm.png",
        "primaryColor": "#a79e90",
        "secondaryColors": [
            "#948975",
            "#857967"
        ]
    },
    {
        "name": "Carian Knight Helm",
        "image": "Head/Carian Knight Helm.png",
        "primaryColor": "#e1e0e0",
        "secondaryColors": [
            "#9c9a98",
            "#5f5d59"
        ]
    },
    {
        "name": "Cerulean Tear Scarab",
        "image": "Head/Cerulean Tear Scarab.png",
        "primaryColor": "#9c8b68",
        "secondaryColors": [
            "#8a7450",
            "#555a60"
        ]
    },
    {
        "name": "Chain Coif (Female)",
        "image": "Head/Chain Coif (Female).png",
        "primaryColor": "#595955",
        "secondaryColors": [
            "#595954",
            "#545450"
        ]
    },
    {
        "name": "Chain Coif (Male)",
        "image": "Head/Chain Coif (Male).png",
        "primaryColor": "#847a71",
        "secondaryColors": [
            "#5f5b54",
            "#47423c"
        ]
    },
    {
        "name": "Champion Headband",
        "image": "Head/Champion Headband.png",
        "primaryColor": "#514d4a",
        "secondaryColors": [
            "#514a46",
            "#46413d"
        ]
    },
    {
        "name": "Cleanrot Helm (Altered)",
        "image": "Head/Cleanrot Helm (Altered).png",
        "primaryColor": "#a09c92",
        "secondaryColors": [
            "#9d8973",
            "#89725d"
        ]
    },
    {
        "name": "Cleanrot Helm",
        "image": "Head/Cleanrot Helm.png",
        "primaryColor": "#a09c91",
        "secondaryColors": [
            "#9d8973",
            "#ab3924"
        ]
    },
    {
        "name": "Commoner's Headband (Altered)",
        "image": "Head/Commoner's Headband (Altered).png",
        "primaryColor": "#a19f94",
        "secondaryColors": [
            "#5f5d54",
            "#5d5b52"
        ]
    },
    {
        "name": "Commoner's Headband",
        "image": "Head/Commoner's Headband.png",
        "primaryColor": "#c4baae",
        "secondaryColors": [
            "#aea396",
            "#655d52"
        ]
    },
    {
        "name": "Confessor Hood (Altered)",
        "image": "Head/Confessor Hood (Altered).png",
        "primaryColor": "#9c958c",
        "secondaryColors": [
            "#8a8478",
            "#837c70"
        ]
    },
    {
        "name": "Confessor Hood",
        "image": "Head/Confessor Hood.png",
        "primaryColor": "#4e4c4a",
        "secondaryColors": [
            "#45413d",
            "#3d3e40"
        ]
    },
    {
        "name": "Consort's Mask",
        "image": "Head/Consort's Mask.png",
        "primaryColor": "#9a9690",
        "secondaryColors": [
            "#887051",
            "#70614c"
        ]
    },
    {
        "name": "Crimson Hood",
        "image": "Head/Crimson Hood.png",
        "primaryColor": "#78111e",
        "secondaryColors": [
            "#6e564d",
            "#57443b"
        ]
    },
    {
        "name": "Crimson Tear Scarab",
        "image": "Head/Crimson Tear Scarab.png",
        "primaryColor": "#9f8c69",
        "secondaryColors": [
            "#8e6c59",
            "#704f48"
        ]
    },
    {
        "name": "Crucible Axe Helm",
        "image": "Head/Crucible Axe Helm.png",
        "primaryColor": "#8e6a51",
        "secondaryColors": [
            "#695346",
            "#634735"
        ]
    },
    {
        "name": "Crucible Tree Helm",
        "image": "Head/Crucible Tree Helm.png",
        "primaryColor": "#afa28e",
        "secondaryColors": [
            "#89705b",
            "#6e5e4c"
        ]
    },
    {
        "name": "Cuckoo Knight Helm",
        "image": "Head/Cuckoo Knight Helm.png",
        "primaryColor": "#9a9a9c",
        "secondaryColors": [
            "#3f3f68",
            "#5e5e60"
        ]
    },
    {
        "name": "Depraved Perfumer Headscarf",
        "image": "Head/Depraved Perfumer Headscarf.png",
        "primaryColor": "#61574c",
        "secondaryColors": [
            "#635348",
            "#52443b"
        ]
    },
    {
        "name": "Diallos's Mask",
        "image": "Head/Diallos's Mask.png",
        "primaryColor": "#999897",
        "secondaryColors": [
            "#993532",
            "#47413d"
        ]
    },
    {
        "name": "Drake Knight Helm (Altered)",
        "image": "Head/Drake Knight Helm (Altered).png",
        "primaryColor": "#0e1615",
        "secondaryColors": [
            "#a84f3b",
            "#565557"
        ]
    },
    {
        "name": "Drake Knight Helm (Altered)_()",
        "image": "Head/Drake Knight Helm (Altered)_().png",
        "primaryColor": "#0e1615",
        "secondaryColors": [
            "#a84f3b",
            "#565557"
        ]
    },
    {
        "name": "Drake Knight Helm",
        "image": "Head/Drake Knight Helm.png",
        "primaryColor": "#0e1615",
        "secondaryColors": [
            "#a84f3b",
            "#54443a"
        ]
    },
    {
        "name": "Duelist Helm",
        "image": "Head/Duelist Helm.png",
        "primaryColor": "#999b92",
        "secondaryColors": [
            "#8c8478",
            "#605f56"
        ]
    },
    {
        "name": "Eccentric's Hood (Altered)",
        "image": "Head/Eccentric's Hood (Altered).png",
        "primaryColor": "#454341",
        "secondaryColors": [
            "#9e9895",
            "#857973"
        ]
    },
    {
        "name": "Eccentric's Hood (Altered)_()",
        "image": "Head/Eccentric's Hood (Altered)_().png",
        "primaryColor": "#454341",
        "secondaryColors": [
            "#9e9895",
            "#857973"
        ]
    },
    {
        "name": "Eccentric's Hood",
        "image": "Head/Eccentric's Hood.png",
        "primaryColor": "#5a5652",
        "secondaryColors": [
            "#5d544e",
            "#4d423c"
        ]
    },
    {
        "name": "Elden Lord Crown",
        "image": "Head/Elden Lord Crown.png",
        "primaryColor": "#a0978d",
        "secondaryColors": [
            "#928578",
            "#86786a"
        ]
    },
    {
        "name": "Envoy Crown",
        "image": "Head/Envoy Crown.png",
        "primaryColor": "#d2d1d0",
        "secondaryColors": [
            "#a5a5a0",
            "#5a5952"
        ]
    },
    {
        "name": "Exile Hood",
        "image": "Head/Exile Hood.png",
        "primaryColor": "#694c49",
        "secondaryColors": [
            "#5d423c",
            "#4b3331"
        ]
    },
    {
        "name": "Festive Hood (Altered)",
        "image": "Head/Festive Hood (Altered).png",
        "primaryColor": "#604d5e",
        "secondaryColors": [
            "#4a3a4a",
            "#493531"
        ]
    },
    {
        "name": "Festive Hood (Altered)_()",
        "image": "Head/Festive Hood (Altered)_().png",
        "primaryColor": "#604d5e",
        "secondaryColors": [
            "#4a3a4a",
            "#493531"
        ]
    },
    {
        "name": "Festive Hood",
        "image": "Head/Festive Hood.png",
        "primaryColor": "#9c8b6a",
        "secondaryColors": [
            "#887459",
            "#705f4c"
        ]
    },
    {
        "name": "Fia's Hood",
        "image": "Head/Fia's Hood.png",
        "primaryColor": "#8d9387",
        "secondaryColors": [
            "#585a55",
            "#555750"
        ]
    },
    {
        "name": "Finger Maiden Fillet",
        "image": "Head/Finger Maiden Fillet.png",
        "primaryColor": "#d8cfc7",
        "secondaryColors": [
            "#cdc4ba",
            "#c4bab0"
        ]
    },
    {
        "name": "Fingerprint Helm",
        "image": "Head/Fingerprint Helm.png",
        "primaryColor": "#d1cfd6",
        "secondaryColors": [
            "#9995a0",
            "#787586"
        ]
    },
    {
        "name": "Fire Monk Hood",
        "image": "Head/Fire Monk Hood.png",
        "primaryColor": "#896b5f",
        "secondaryColors": [
            "#645348",
            "#5d4937"
        ]
    },
    {
        "name": "Fire Prelate Helm",
        "image": "Head/Fire Prelate Helm.png",
        "primaryColor": "#a19496",
        "secondaryColors": [
            "#857778",
            "#605555"
        ]
    },
    {
        "name": "Foot Soldier Cap",
        "image": "Head/Foot Soldier Cap.png",
        "primaryColor": "#ab9e90",
        "secondaryColors": [
            "#988777",
            "#887766"
        ]
    },
    {
        "name": "Foot Soldier Helm",
        "image": "Head/Foot Soldier Helm.png",
        "primaryColor": "#e1dad7",
        "secondaryColors": [
            "#a69b95",
            "#87756b"
        ]
    },
    {
        "name": "Foot Soldier Helmet",
        "image": "Head/Foot Soldier Helmet.png",
        "primaryColor": "#c6b49d",
        "secondaryColors": [
            "#a78d6f",
            "#8d7155"
        ]
    },
    {
        "name": "Gelmir Knight Helm",
        "image": "Head/Gelmir Knight Helm.png",
        "primaryColor": "#a7aaaf",
        "secondaryColors": [
            "#a2957a",
            "#7d4544"
        ]
    },
    {
        "name": "Gilded Foot Soldier Cap",
        "image": "Head/Gilded Foot Soldier Cap.png",
        "primaryColor": "#d1c7b4",
        "secondaryColors": [
            "#b0a590",
            "#9c8a70"
        ]
    },
    {
        "name": "Glintstone Scarab",
        "image": "Head/Glintstone Scarab.png",
        "primaryColor": "#897452",
        "secondaryColors": [
            "#58655b",
            "#644e34"
        ]
    },
    {
        "name": "Godrick Knight Helm",
        "image": "Head/Godrick Knight Helm.png",
        "primaryColor": "#9d906f",
        "secondaryColors": [
            "#605f5c",
            "#625d51"
        ]
    },
    {
        "name": "Godrick Soldier Helm",
        "image": "Head/Godrick Soldier Helm.png",
        "primaryColor": "#aca18d",
        "secondaryColors": [
            "#978a75",
            "#867863"
        ]
    },
    {
        "name": "Godskin Apostle Hood",
        "image": "Head/Godskin Apostle Hood.png",
        "primaryColor": "#c2bbaf",
        "secondaryColors": [
            "#aea79a",
            "#3a2c44"
        ]
    },
    {
        "name": "Godskin Noble Hood",
        "image": "Head/Godskin Noble Hood.png",
        "primaryColor": "#ccc4b6",
        "secondaryColors": [
            "#c3b9aa",
            "#b4a896"
        ]
    },
    {
        "name": "Great Horned Headband",
        "image": "Head/Great Horned Headband.png",
        "primaryColor": "#8a6d5b",
        "secondaryColors": [
            "#66564c",
            "#56443a"
        ]
    },
    {
        "name": "Greathelm",
        "image": "Head/Greathelm.png",
        "primaryColor": "#9d988f",
        "secondaryColors": [
            "#89837a",
            "#827b72"
        ]
    },
    {
        "name": "Greathood",
        "image": "Head/Greathood.png",
        "primaryColor": "#696a83",
        "secondaryColors": [
            "#595b68",
            "#52536c"
        ]
    },
    {
        "name": "Guardian Mask",
        "image": "Head/Guardian Mask.png",
        "primaryColor": "#aba38c",
        "secondaryColors": [
            "#948c73",
            "#847a61"
        ]
    },
    {
        "name": "Guilty Hood",
        "image": "Head/Guilty Hood.png",
        "primaryColor": "#857756",
        "secondaryColors": [
            "#736647",
            "#5a4e35"
        ]
    },
    {
        "name": "Haima Glintstone Crown",
        "image": "Head/Haima Glintstone Crown.png",
        "primaryColor": "#4b4b50",
        "secondaryColors": [
            "#3e404b",
            "#403e48"
        ]
    },
    {
        "name": "Haligtree Helm",
        "image": "Head/Haligtree Helm.png",
        "primaryColor": "#9c9165",
        "secondaryColors": [
            "#857960",
            "#68604f"
        ]
    },
    {
        "name": "Haligtree Knight Helm",
        "image": "Head/Haligtree Knight Helm.png",
        "primaryColor": "#d9cea5",
        "secondaryColors": [
            "#a3946c",
            "#867858"
        ]
    },
    {
        "name": "Hieroda's Glintstone Crown",
        "image": "Head/Hieroda's Glintstone Crown.png",
        "primaryColor": "#a29b93",
        "secondaryColors": [
            "#8e8579",
            "#847a70"
        ]
    },
    {
        "name": "High Page Hood",
        "image": "Head/High Page Hood.png",
        "primaryColor": "#d4c8b0",
        "secondaryColors": [
            "#c5b9a0",
            "#b1a58b"
        ]
    },
    {
        "name": "Highwayman Hood",
        "image": "Head/Highwayman Hood.png",
        "primaryColor": "#9c8a72",
        "secondaryColors": [
            "#877661",
            "#685a4c"
        ]
    },
    {
        "name": "Hoslow's Helm",
        "image": "Head/Hoslow's Helm.png",
        "primaryColor": "#9c9c9a",
        "secondaryColors": [
            "#605e5a",
            "#46433b"
        ]
    },
    {
        "name": "Iji's Mirrorhelm",
        "image": "Head/Iji's Mirrorhelm.png",
        "primaryColor": "#9e9694",
        "secondaryColors": [
            "#9f8876",
            "#8b6f5f"
        ]
    },
    {
        "name": "Imp Head (Cat)",
        "image": "Head/Imp Head (Cat).png",
        "primaryColor": "#a5a692",
        "secondaryColors": [
            "#8d9071",
            "#7a8363"
        ]
    },
    {
        "name": "Imp Head (Corpse)",
        "image": "Head/Imp Head (Corpse).png",
        "primaryColor": "#d2d2ca",
        "secondaryColors": [
            "#a4a695",
            "#8d9074"
        ]
    },
    {
        "name": "Imp Head (Elder)",
        "image": "Head/Imp Head (Elder).png",
        "primaryColor": "#a5a494",
        "secondaryColors": [
            "#8c8d73",
            "#798460"
        ]
    },
    {
        "name": "Imp Head (Fanged)",
        "image": "Head/Imp Head (Fanged).png",
        "primaryColor": "#d1ccab",
        "secondaryColors": [
            "#a9a88f",
            "#95936e"
        ]
    },
    {
        "name": "Imp Head (Long-Tongued)",
        "image": "Head/Imp Head (Long-Tongued).png",
        "primaryColor": "#a5a891",
        "secondaryColors": [
            "#8c9371",
            "#79845c"
        ]
    },
    {
        "name": "Imp Head (Wolf)",
        "image": "Head/Imp Head (Wolf).png",
        "primaryColor": "#a5a891",
        "secondaryColors": [
            "#a4a696",
            "#898e75"
        ]
    },
    {
        "name": "Incantation Scarab",
        "image": "Head/Incantation Scarab.png",
        "primaryColor": "#a9925d",
        "secondaryColors": [
            "#8e754b",
            "#886d38"
        ]
    },
    {
        "name": "Iron Helmet",
        "image": "Head/Iron Helmet.png",
        "primaryColor": "#969e9d",
        "secondaryColors": [
            "#9f9e9b",
            "#5a5755"
        ]
    },
    {
        "name": "Iron Kasa",
        "image": "Head/Iron Kasa.png",
        "primaryColor": "#909194",
        "secondaryColors": [
            "#7c7d81",
            "#606264"
        ]
    },
    {
        "name": "Jar",
        "image": "Head/Jar.png",
        "primaryColor": "#b3a38b",
        "secondaryColors": [
            "#9d8c74",
            "#887762"
        ]
    },
    {
        "name": "Juvenile Scholar Cap",
        "image": "Head/Juvenile Scholar Cap.png",
        "primaryColor": "#585a5d",
        "secondaryColors": [
            "#575a5f",
            "#5f582b"
        ]
    },
    {
        "name": "Kaiden Helm",
        "image": "Head/Kaiden Helm.png",
        "primaryColor": "#a5a096",
        "secondaryColors": [
            "#8c8579",
            "#666056"
        ]
    },
    {
        "name": "Karolo's Glintstone Crown",
        "image": "Head/Karolo's Glintstone Crown.png",
        "primaryColor": "#979c97",
        "secondaryColors": [
            "#85867a",
            "#616157"
        ]
    },
    {
        "name": "Knight Helm",
        "image": "Head/Knight Helm.png",
        "primaryColor": "#e1dfe0",
        "secondaryColors": [
            "#a49f9e",
            "#5b5751"
        ]
    },
    {
        "name": "Land of Reeds Helm",
        "image": "Head/Land of Reeds Helm.png",
        "primaryColor": "#9e9690",
        "secondaryColors": [
            "#86756a",
            "#675c55"
        ]
    },
    {
        "name": "Lazuli Glintstone Crown",
        "image": "Head/Lazuli Glintstone Crown.png",
        "primaryColor": "#949897",
        "secondaryColors": [
            "#6e83bf",
            "#5e5f5e"
        ]
    },
    {
        "name": "Leyndell Knight Helm",
        "image": "Head/Leyndell Knight Helm.png",
        "primaryColor": "#a4926e",
        "secondaryColors": [
            "#8a7354",
            "#706148"
        ]
    },
    {
        "name": "Leyndell Soldier Helm",
        "image": "Head/Leyndell Soldier Helm.png",
        "primaryColor": "#9c9686",
        "secondaryColors": [
            "#948972",
            "#89755a"
        ]
    },
    {
        "name": "Lionel's Helm",
        "image": "Head/Lionel's Helm.png",
        "primaryColor": "#8d9294",
        "secondaryColors": [
            "#545758",
            "#4c4d4c"
        ]
    },
    {
        "name": "Lusat's Glintstone Crown",
        "image": "Head/Lusat's Glintstone Crown.png",
        "primaryColor": "#00416f",
        "secondaryColors": [
            "#c2a29a",
            "#615758"
        ]
    },
    {
        "name": "Malenia's Winged Helm",
        "image": "Head/Malenia's Winged Helm.png",
        "primaryColor": "#afa78d",
        "secondaryColors": [
            "#a16152",
            "#6d624d"
        ]
    },
    {
        "name": "Malformed Dragon Helm",
        "image": "Head/Malformed Dragon Helm.png",
        "primaryColor": "#8a744b",
        "secondaryColors": [
            "#746345",
            "#634f2f"
        ]
    },
    {
        "name": "Maliketh's Helm",
        "image": "Head/Maliketh's Helm.png",
        "primaryColor": "#1c1c1c",
        "secondaryColors": [
            "#8a8a8d",
            "#84765b"
        ]
    },
    {
        "name": "Marai's Mask",
        "image": "Head/Marai's Mask.png",
        "primaryColor": "#a59e98",
        "secondaryColors": [
            "#978872",
            "#877967"
        ]
    },
    {
        "name": "Marionette Soldier Birdhelm",
        "image": "Head/Marionette Soldier Birdhelm.png",
        "primaryColor": "#dcd9d5",
        "secondaryColors": [
            "#a29d97",
            "#5f5a53"
        ]
    },
    {
        "name": "Marionette Soldier Helm",
        "image": "Head/Marionette Soldier Helm.png",
        "primaryColor": "#a69b91",
        "secondaryColors": [
            "#948677",
            "#877565"
        ]
    },
    {
        "name": "Mask of Confidence",
        "image": "Head/Mask of Confidence.png",
        "primaryColor": "#9e9c96",
        "secondaryColors": [
            "#59504d",
            "#4b443b"
        ]
    },
    {
        "name": "Mushroom Crown",
        "image": "Head/Mushroom Crown.png",
        "primaryColor": "#ac9f8f",
        "secondaryColors": [
            "#9b8a76",
            "#897564"
        ]
    },
    {
        "name": "Mushroom Head",
        "image": "Head/Mushroom Head.png",
        "primaryColor": "#c8a78a",
        "secondaryColors": [
            "#b48b6d",
            "#9a6d53"
        ]
    },
    {
        "name": "Navy Hood",
        "image": "Head/Navy Hood.png",
        "primaryColor": "#001b41",
        "secondaryColors": [
            "#5d5d5d",
            "#344b6a"
        ]
    },
    {
        "name": "Night Maiden Twin Crown",
        "image": "Head/Night Maiden Twin Crown.png",
        "primaryColor": "#d8d6d0",
        "secondaryColors": [
            "#aca496",
            "#988974"
        ]
    },
    {
        "name": "Nights Cavalry Helm (Altered)",
        "image": "Head/Nights Cavalry Helm (Altered).png",
        "primaryColor": "#212021",
        "secondaryColors": [
            "#87837b",
            "#5a5752"
        ]
    },
    {
        "name": "Nights Cavalry Helm",
        "image": "Head/Nights Cavalry Helm.png",
        "primaryColor": "#212021",
        "secondaryColors": [
            "#53514e",
            "#43413d"
        ]
    },
    {
        "name": "Nomadic Merchant's Chapeau",
        "image": "Head/Nomadic Merchant's Chapeau.png",
        "primaryColor": "#dcd6cd",
        "secondaryColors": [
            "#cdc5b8",
            "#ada599"
        ]
    },
    {
        "name": "Nox Mirrorhelm",
        "image": "Head/Nox Mirrorhelm.png",
        "primaryColor": "#d8d7d8",
        "secondaryColors": [
            "#9d9a9b",
            "#857876"
        ]
    },
    {
        "name": "Nox Monk Hood (Altered)",
        "image": "Head/Nox Monk Hood (Altered).png",
        "primaryColor": "#5e5a52",
        "secondaryColors": [
            "#58544e",
            "#48443a"
        ]
    },
    {
        "name": "Nox Monk Hood",
        "image": "Head/Nox Monk Hood.png",
        "primaryColor": "#d3d1cb",
        "secondaryColors": [
            "#c6c3bb",
            "#aaa79f"
        ]
    },
    {
        "name": "Nox Swordstress Crown (Altered)",
        "image": "Head/Nox Swordstress Crown (Altered).png",
        "primaryColor": "#5b5a56",
        "secondaryColors": [
            "#5a5952",
            "#585753"
        ]
    },
    {
        "name": "Nox Swordstress Crown",
        "image": "Head/Nox Swordstress Crown.png",
        "primaryColor": "#d8d7d1",
        "secondaryColors": [
            "#c5c3ba",
            "#a8a69d"
        ]
    },
    {
        "name": "Octopus Head",
        "image": "Head/Octopus Head.png",
        "primaryColor": "#a29790",
        "secondaryColors": [
            "#86786c",
            "#5f5a56"
        ]
    },
    {
        "name": "Okina Mask",
        "image": "Head/Okina Mask.png",
        "primaryColor": "#9a9490",
        "secondaryColors": [
            "#938577",
            "#86796d"
        ]
    },
    {
        "name": "Old Aristocrat Cowl",
        "image": "Head/Old Aristocrat Cowl.png",
        "primaryColor": "#a69d8c",
        "secondaryColors": [
            "#928c68",
            "#857b66"
        ]
    },
    {
        "name": "Olivinu's Glintstone Crown",
        "image": "Head/Olivinu's Glintstone Crown.png",
        "primaryColor": "#a2a097",
        "secondaryColors": [
            "#8c8676",
            "#646157"
        ]
    },
    {
        "name": "Omen Helm",
        "image": "Head/Omen Helm.png",
        "primaryColor": "#923d37",
        "secondaryColors": [
            "#725047",
            "#684439"
        ]
    },
    {
        "name": "Omensmirk Mask",
        "image": "Head/Omensmirk Mask.png",
        "primaryColor": "#a0a08e",
        "secondaryColors": [
            "#8f8b74",
            "#946554"
        ]
    },
    {
        "name": "Page Hood",
        "image": "Head/Page Hood.png",
        "primaryColor": "#857466",
        "secondaryColors": [
            "#5d5249",
            "#4d433b"
        ]
    },
    {
        "name": "Perfumer Hood",
        "image": "Head/Perfumer Hood.png",
        "primaryColor": "#cfcbc5",
        "secondaryColors": [
            "#c8c3ba",
            "#a9a497"
        ]
    },
    {
        "name": "Preceptor's Big Hat",
        "image": "Head/Preceptor's Big Hat.png",
        "primaryColor": "#726a5b",
        "secondaryColors": [
            "#6c675b",
            "#665e4e"
        ]
    },
    {
        "name": "Prisoner Iron Mask",
        "image": "Head/Prisoner Iron Mask.png",
        "primaryColor": "#d6d1ce",
        "secondaryColors": [
            "#a39a94",
            "#86766d"
        ]
    },
    {
        "name": "Prophet Blindfold",
        "image": "Head/Prophet Blindfold.png",
        "primaryColor": "#988f86",
        "secondaryColors": [
            "#8e847a",
            "#85796f"
        ]
    },
    {
        "name": "Pumpkin Helm",
        "image": "Head/Pumpkin Helm.png",
        "primaryColor": "#a48f6b",
        "secondaryColors": [
            "#8a7355",
            "#746147"
        ]
    },
    {
        "name": "Queen's Crescent Crown",
        "image": "Head/Queen's Crescent Crown.png",
        "primaryColor": "#867754",
        "secondaryColors": [
            "#6c6046",
            "#574b35"
        ]
    },
    {
        "name": "Radahn Soldier Helm",
        "image": "Head/Radahn Soldier Helm.png",
        "primaryColor": "#a39e94",
        "secondaryColors": [
            "#928874",
            "#8c705c"
        ]
    },
    {
        "name": "Radahn's Redmane Helm",
        "image": "Head/Radahn's Redmane Helm.png",
        "primaryColor": "#e2c096",
        "secondaryColors": [
            "#5c1715",
            "#9e8e74"
        ]
    },
    {
        "name": "Radiant Gold Mask",
        "image": "Head/Radiant Gold Mask.png",
        "primaryColor": "#a68e54",
        "secondaryColors": [
            "#917646",
            "#8d6d36"
        ]
    },
    {
        "name": "Raging Wolf Helm",
        "image": "Head/Raging Wolf Helm.png",
        "primaryColor": "#9b9997",
        "secondaryColors": [
            "#625f5a",
            "#47433b"
        ]
    },
    {
        "name": "Raya Lucarian Helm",
        "image": "Head/Raya Lucarian Helm.png",
        "primaryColor": "#9c9a94",
        "secondaryColors": [
            "#8b705e",
            "#605c54"
        ]
    },
    {
        "name": "Redmane Knight Helm",
        "image": "Head/Redmane Knight Helm.png",
        "primaryColor": "#9f9992",
        "secondaryColors": [
            "#635b54",
            "#4d443b"
        ]
    },
    {
        "name": "Rotten Duelist Helm",
        "image": "Head/Rotten Duelist Helm.png",
        "primaryColor": "#942c1c",
        "secondaryColors": [
            "#9f4935",
            "#695951"
        ]
    },
    {
        "name": "Royal Knight Helm",
        "image": "Head/Royal Knight Helm.png",
        "primaryColor": "#9f9e9b",
        "secondaryColors": [
            "#867755",
            "#676152"
        ]
    },
    {
        "name": "Royal Remains Helm",
        "image": "Head/Royal Remains Helm.png",
        "primaryColor": "#867660",
        "secondaryColors": [
            "#635b4f",
            "#524738"
        ]
    },
    {
        "name": "Ruler's Mask",
        "image": "Head/Ruler's Mask.png",
        "primaryColor": "#d8d5d1",
        "secondaryColors": [
            "#a29e99",
            "#918675"
        ]
    },
    {
        "name": "Sacred Crown Helm",
        "image": "Head/Sacred Crown Helm.png",
        "primaryColor": "#aea38e",
        "secondaryColors": [
            "#9e8c6e",
            "#8d7354"
        ]
    },
    {
        "name": "Sage Hood",
        "image": "Head/Sage Hood.png",
        "primaryColor": "#855652",
        "secondaryColors": [
            "#724b47",
            "#62423c"
        ]
    },
    {
        "name": "Sanguine Noble Hood",
        "image": "Head/Sanguine Noble Hood.png",
        "primaryColor": "#2d2826",
        "secondaryColors": [
            "#ac9379",
            "#4a433a"
        ]
    },
    {
        "name": "Scaled Helm",
        "image": "Head/Scaled Helm.png",
        "primaryColor": "#e2dfdb",
        "secondaryColors": [
            "#a39c93",
            "#8c847a"
        ]
    },
    {
        "name": "Shining Horned Headband",
        "image": "Head/Shining Horned Headband.png",
        "primaryColor": "#cc956d",
        "secondaryColors": [
            "#9c6e53",
            "#6b5a51"
        ]
    },
    {
        "name": "Silver Tear Mask",
        "image": "Head/Silver Tear Mask.png",
        "primaryColor": "#dfdfdf",
        "secondaryColors": [
            "#989997",
            "#5a5b57"
        ]
    },
    {
        "name": "Skeletal Mask",
        "image": "Head/Skeletal Mask.png",
        "primaryColor": "#8d8577",
        "secondaryColors": [
            "#847a6d",
            "#514f4c"
        ]
    },
    {
        "name": "Snow Witch Hat",
        "image": "Head/Snow Witch Hat.png",
        "primaryColor": "#c9ced1",
        "secondaryColors": [
            "#bbc2c6",
            "#b5bdc1"
        ]
    },
    {
        "name": "Spellblade's Pointed Hat",
        "image": "Head/Spellblade's Pointed Hat.png",
        "primaryColor": "#73644e",
        "secondaryColors": [
            "#6a5e4c",
            "#544839"
        ]
    },
    {
        "name": "Traveler's Hat",
        "image": "Head/Traveler's Hat.png",
        "primaryColor": "#a99c8e",
        "secondaryColors": [
            "#938678",
            "#86796b"
        ]
    },
    {
        "name": "Traveling Maiden Hood",
        "image": "Head/Traveling Maiden Hood.png",
        "primaryColor": "#c6b4ac",
        "secondaryColors": [
            "#a79790",
            "#93827b"
        ]
    },
    {
        "name": "Tree Sentinel Helm",
        "image": "Head/Tree Sentinel Helm.png",
        "primaryColor": "#968d67",
        "secondaryColors": [
            "#857958",
            "#706449"
        ]
    },
    {
        "name": "Twinned Helm",
        "image": "Head/Twinned Helm.png",
        "primaryColor": "#a99e8c",
        "secondaryColors": [
            "#928775",
            "#857969"
        ]
    },
    {
        "name": "Twinsage Glintstone Crown",
        "image": "Head/Twinsage Glintstone Crown.png",
        "primaryColor": "#979694",
        "secondaryColors": [
            "#4d8d81",
            "#0f323d"
        ]
    },
    {
        "name": "Vagabond Knight Helm",
        "image": "Head/Vagabond Knight Helm.png",
        "primaryColor": "#dcdad7",
        "secondaryColors": [
            "#9d9993",
            "#625d56"
        ]
    },
    {
        "name": "Veteran's Helm",
        "image": "Head/Veteran's Helm.png",
        "primaryColor": "#9c9894",
        "secondaryColors": [
            "#5e5a55",
            "#48433a"
        ]
    },
    {
        "name": "Vulgar Militia Helm",
        "image": "Head/Vulgar Militia Helm.png",
        "primaryColor": "#a19d94",
        "secondaryColors": [
            "#5b564e",
            "#4b433b"
        ]
    },
    {
        "name": "White Mask",
        "image": "Head/White Mask.png",
        "primaryColor": "#98989a",
        "secondaryColors": [
            "#8b827c",
            "#837a78"
        ]
    },
    {
        "name": "Witch's Glintstone Crown",
        "image": "Head/Witch's Glintstone Crown.png",
        "primaryColor": "#a2a095",
        "secondaryColors": [
            "#888878",
            "#56824c"
        ]
    },
    {
        "name": "Zamor Mask",
        "image": "Head/Zamor Mask.png",
        "primaryColor": "#a09d95",
        "secondaryColors": [
            "#605c54",
            "#4a4539"
        ]
    },
    {
        "name": "Black Knight Helm",
        "image": "Head\\SOTE/Black Knight Helm.png",
        "primaryColor": "#999892",
        "secondaryColors": [
            "#5f5c56",
            "#4c4639"
        ]
    },
    {
        "name": "Caterpillar Mask",
        "image": "Head\\SOTE/Caterpillar Mask.png",
        "primaryColor": "#908678",
        "secondaryColors": [
            "#847a6d",
            "#655d53"
        ]
    },
    {
        "name": "Circlet of Light",
        "image": "Head\\SOTE/Circlet of Light.png",
        "primaryColor": "#9a8a63",
        "secondaryColors": [
            "#89784d",
            "#73664b"
        ]
    },
    {
        "name": "Common Soldier Helm",
        "image": "Head\\SOTE/Common Soldier Helm.png",
        "primaryColor": "#dcd7d0",
        "secondaryColors": [
            "#a9a097",
            "#5f564f"
        ]
    },
    {
        "name": "Crucible Hammer-helm",
        "image": "Head\\SOTE/Crucible Hammer-helm.png",
        "primaryColor": "#8d7261",
        "secondaryColors": [
            "#65564b",
            "#584539"
        ]
    },
    {
        "name": "Curseblade Mask",
        "image": "Head\\SOTE/Curseblade Mask.png",
        "primaryColor": "#a29691",
        "secondaryColors": [
            "#8d7268",
            "#645b56"
        ]
    },
    {
        "name": "Dancer's Hood",
        "image": "Head\\SOTE/Dancer's Hood.png",
        "primaryColor": "#902720",
        "secondaryColors": [
            "#5e4935",
            "#675a4a"
        ]
    },
    {
        "name": "Dane's Hat",
        "image": "Head\\SOTE/Dane's Hat.png",
        "primaryColor": "#86765e",
        "secondaryColors": [
            "#726654",
            "#514739"
        ]
    },
    {
        "name": "Death Knight Helm",
        "image": "Head\\SOTE/Death Knight Helm.png",
        "primaryColor": "#615f5a",
        "secondaryColors": [
            "#605e59",
            "#625b4e"
        ]
    },
    {
        "name": "Death Mask Helm",
        "image": "Head\\SOTE/Death Mask Helm.png",
        "primaryColor": "#88725f",
        "secondaryColors": [
            "#742c2f",
            "#594738"
        ]
    },
    {
        "name": "Divine Beast Head",
        "image": "Head\\SOTE/Divine Beast Head.png",
        "primaryColor": "#99958d",
        "secondaryColors": [
            "#605b55",
            "#49433b"
        ]
    },
    {
        "name": "Divine Beast Helm",
        "image": "Head\\SOTE/Divine Beast Helm.png",
        "primaryColor": "#635e57",
        "secondaryColors": [
            "#5e5d57",
            "#5c5a55"
        ]
    },
    {
        "name": "Divine Bird Helm",
        "image": "Head\\SOTE/Divine Bird Helm.png",
        "primaryColor": "#a18d65",
        "secondaryColors": [
            "#897551",
            "#756546"
        ]
    },
    {
        "name": "Fang Helm",
        "image": "Head\\SOTE/Fang Helm.png",
        "primaryColor": "#9c9993",
        "secondaryColors": [
            "#595751",
            "#46433c"
        ]
    },
    {
        "name": "Fire Knight Helm",
        "image": "Head\\SOTE/Fire Knight Helm.png",
        "primaryColor": "#7c2c2b",
        "secondaryColors": [
            "#6b5d48",
            "#8d6f57"
        ]
    },
    {
        "name": "Freyja's Helm",
        "image": "Head\\SOTE/Freyja's Helm.png",
        "primaryColor": "#9e8b70",
        "secondaryColors": [
            "#89755d",
            "#6b5e4d"
        ]
    },
    {
        "name": "Gaiuss Helm",
        "image": "Head\\SOTE/Gaiuss Helm.png",
        "primaryColor": "#9d9894",
        "secondaryColors": [
            "#5c5854",
            "#46423d"
        ]
    },
    {
        "name": "Gravebird Helm",
        "image": "Head\\SOTE/Gravebird Helm.png",
        "primaryColor": "#9d9c91",
        "secondaryColors": [
            "#868579",
            "#69685d"
        ]
    },
    {
        "name": "Greatjar",
        "image": "Head\\SOTE/Greatjar.png",
        "primaryColor": "#aea18e",
        "secondaryColors": [
            "#978975",
            "#867866"
        ]
    },
    {
        "name": "Helm of Night",
        "image": "Head\\SOTE/Helm of Night.png",
        "primaryColor": "#1f1e1f",
        "secondaryColors": [
            "#5c5a58",
            "#565453"
        ]
    },
    {
        "name": "Helm of Solitude",
        "image": "Head\\SOTE/Helm of Solitude.png",
        "primaryColor": "#939292",
        "secondaryColors": [
            "#555453",
            "#41403e"
        ]
    },
    {
        "name": "High Priest Hat",
        "image": "Head\\SOTE/High Priest Hat.png",
        "primaryColor": "#a2a09a",
        "secondaryColors": [
            "#645e50",
            "#4f4837"
        ]
    },
    {
        "name": "Horned Warrior Helm",
        "image": "Head\\SOTE/Horned Warrior Helm.png",
        "primaryColor": "#a89f8d",
        "secondaryColors": [
            "#958a75",
            "#655e52"
        ]
    },
    {
        "name": "Igon's Helm (Altered)",
        "image": "Head\\SOTE/Igon's Helm (Altered).png",
        "primaryColor": "#a3988d",
        "secondaryColors": [
            "#877469",
            "#6b5d53"
        ]
    },
    {
        "name": "Igon's Helm",
        "image": "Head\\SOTE/Igon's Helm.png",
        "primaryColor": "#a6988c",
        "secondaryColors": [
            "#86776a",
            "#675e54"
        ]
    },
    {
        "name": "Imp Head (Lion)",
        "image": "Head\\SOTE/Imp Head (Lion).png",
        "primaryColor": "#a2a28c",
        "secondaryColors": [
            "#8a8c71",
            "#656752"
        ]
    },
    {
        "name": "Leather Crown",
        "image": "Head\\SOTE/Leather Crown.png",
        "primaryColor": "#aca197",
        "secondaryColors": [
            "#9d8576",
            "#8b6f60"
        ]
    },
    {
        "name": "Leather Headband",
        "image": "Head\\SOTE/Leather Headband.png",
        "primaryColor": "#c4bab1",
        "secondaryColors": [
            "#ada399",
            "#88745e"
        ]
    },
    {
        "name": "Messmer Soldier Helm",
        "image": "Head\\SOTE/Messmer Soldier Helm.png",
        "primaryColor": "#9c9a99",
        "secondaryColors": [
            "#625d56",
            "#504739"
        ]
    },
    {
        "name": "Messmer's Helm (Altered)",
        "image": "Head\\SOTE/Messmer's Helm (Altered).png",
        "primaryColor": "#857770",
        "secondaryColors": [
            "#5c5553",
            "#4e423b"
        ]
    },
    {
        "name": "Messmer's Helm",
        "image": "Head\\SOTE/Messmer's Helm.png",
        "primaryColor": "#5c5452",
        "secondaryColors": [
            "#8b3623",
            "#562b20"
        ]
    },
    {
        "name": "Oathseeker Helm",
        "image": "Head\\SOTE/Oathseeker Helm.png",
        "primaryColor": "#867665",
        "secondaryColors": [
            "#6a5c4f",
            "#504539"
        ]
    },
    {
        "name": "Pelt of Ralva",
        "image": "Head\\SOTE/Pelt of Ralva.png",
        "primaryColor": "#65554e",
        "secondaryColors": [
            "#604339",
            "#4f342c"
        ]
    },
    {
        "name": "Rakshasa Helm",
        "image": "Head\\SOTE/Rakshasa Helm.png",
        "primaryColor": "#601e15",
        "secondaryColors": [
            "#6e4f49",
            "#63433c"
        ]
    },
    {
        "name": "Rellana's Helm",
        "image": "Head\\SOTE/Rellana's Helm.png",
        "primaryColor": "#d8d9da",
        "secondaryColors": [
            "#9ea1a2",
            "#5b5d5c"
        ]
    },
    {
        "name": "Salza's Hood",
        "image": "Head\\SOTE/Salza's Hood.png",
        "primaryColor": "#ac403d",
        "secondaryColors": [
            "#923330",
            "#601f1d"
        ]
    },
    {
        "name": "Shadow Militia Helm",
        "image": "Head\\SOTE/Shadow Militia Helm.png",
        "primaryColor": "#484748",
        "secondaryColors": [
            "#48443a",
            "#403e41"
        ]
    },
    {
        "name": "St. Trina's Blossom",
        "image": "Head\\SOTE/St. Trina's Blossom.png",
        "primaryColor": "#8c6cd2",
        "secondaryColors": [
            "#6c5bcd",
            "#604dab"
        ]
    },
    {
        "name": "Thiollier's Mask",
        "image": "Head\\SOTE/Thiollier's Mask.png",
        "primaryColor": "#c3bbae",
        "secondaryColors": [
            "#a4a09e",
            "#998a72"
        ]
    },
    {
        "name": "Verdigris Helm",
        "image": "Head\\SOTE/Verdigris Helm.png",
        "primaryColor": "#8f978e",
        "secondaryColors": [
            "#585e58",
            "#3c4542"
        ]
    },
    {
        "name": "Winged Serpent Helm",
        "image": "Head\\SOTE/Winged Serpent Helm.png",
        "primaryColor": "#85796e",
        "secondaryColors": [
            "#625951",
            "#4b433b"
        ]
    },
    {
        "name": "Wise Man's Mask",
        "image": "Head\\SOTE/Wise Man's Mask.png",
        "primaryColor": "#898886",
        "secondaryColors": [
            "#5c5c58",
            "#575756"
        ]
    },
    {
        "name": "Young Lion Helm",
        "image": "Head\\SOTE/Young Lion Helm.png",
        "primaryColor": "#634d2e",
        "secondaryColors": [
            "#952928",
            "#58231d"
        ]
    },
    {
        "name": "Alberich's Trousers",
        "image": "Legs/Alberich's Trousers.png",
        "primaryColor": "#87745d",
        "secondaryColors": [
            "#6f5f4e",
            "#5e4b34"
        ]
    },
    {
        "name": "All-Knowing Greaves",
        "image": "Legs/All-Knowing Greaves.png",
        "primaryColor": "#a09b92",
        "secondaryColors": [
            "#89847a",
            "#827c73"
        ]
    },
    {
        "name": "Aristocrat Boots",
        "image": "Legs/Aristocrat Boots.png",
        "primaryColor": "#948575",
        "secondaryColors": [
            "#877666",
            "#6c5d50"
        ]
    },
    {
        "name": "Astrologer Trousers",
        "image": "Legs/Astrologer Trousers.png",
        "primaryColor": "#8d6c63",
        "secondaryColors": [
            "#6b534a",
            "#59443b"
        ]
    },
    {
        "name": "Bandit Boots",
        "image": "Legs/Bandit Boots.png",
        "primaryColor": "#84796e",
        "secondaryColors": [
            "#625a53",
            "#48423c"
        ]
    },
    {
        "name": "Banished Knight Greaves",
        "image": "Legs/Banished Knight Greaves.png",
        "primaryColor": "#a59e93",
        "secondaryColors": [
            "#625a4f",
            "#4e4639"
        ]
    },
    {
        "name": "Battlemage Legwraps",
        "image": "Legs/Battlemage Legwraps.png",
        "primaryColor": "#9f938d",
        "secondaryColors": [
            "#8f827a",
            "#867872"
        ]
    },
    {
        "name": "Beast Champion Greaves",
        "image": "Legs/Beast Champion Greaves.png",
        "primaryColor": "#949495",
        "secondaryColors": [
            "#5d5b5a",
            "#5a5b5e"
        ]
    },
    {
        "name": "Black Knife Greaves",
        "image": "Legs/Black Knife Greaves.png",
        "primaryColor": "#969195",
        "secondaryColors": [
            "#5a5557",
            "#423c3b"
        ]
    },
    {
        "name": "Blackflame Monk Greaves",
        "image": "Legs/Blackflame Monk Greaves.png",
        "primaryColor": "#665d52",
        "secondaryColors": [
            "#655a4d",
            "#50463a"
        ]
    },
    {
        "name": "Blaidd's Greaves",
        "image": "Legs/Blaidd's Greaves.png",
        "primaryColor": "#928a73",
        "secondaryColors": [
            "#5d5850",
            "#48423b"
        ]
    },
    {
        "name": "Bloodhound Knight Greaves",
        "image": "Legs/Bloodhound Knight Greaves.png",
        "primaryColor": "#867568",
        "secondaryColors": [
            "#645951",
            "#564638"
        ]
    },
    {
        "name": "Blue Silver Mail Skirt",
        "image": "Legs/Blue Silver Mail Skirt.png",
        "primaryColor": "#4f5758",
        "secondaryColors": [
            "#4a504e",
            "#3c4345"
        ]
    },
    {
        "name": "Briar Greaves",
        "image": "Legs/Briar Greaves.png",
        "primaryColor": "#897060",
        "secondaryColors": [
            "#66574e",
            "#5a443a"
        ]
    },
    {
        "name": "Bull-Goat Greaves",
        "image": "Legs/Bull-Goat Greaves.png",
        "primaryColor": "#a79c8e",
        "secondaryColors": [
            "#655b4f",
            "#504639"
        ]
    },
    {
        "name": "Carian Knight Greaves",
        "image": "Legs/Carian Knight Greaves.png",
        "primaryColor": "#867562",
        "secondaryColors": [
            "#605850",
            "#504539"
        ]
    },
    {
        "name": "Chain Leggings",
        "image": "Legs/Chain Leggings.png",
        "primaryColor": "#59544c",
        "secondaryColors": [
            "#58544c",
            "#47433b"
        ]
    },
    {
        "name": "Champion Gaiters",
        "image": "Legs/Champion Gaiters.png",
        "primaryColor": "#846b59",
        "secondaryColors": [
            "#6c5548",
            "#5d4639"
        ]
    },
    {
        "name": "Cleanrot Greaves",
        "image": "Legs/Cleanrot Greaves.png",
        "primaryColor": "#9e8c74",
        "secondaryColors": [
            "#877360",
            "#6b5d4f"
        ]
    },
    {
        "name": "Cloth Trousers",
        "image": "Legs/Cloth Trousers.png",
        "primaryColor": "#a5968c",
        "secondaryColors": [
            "#94857a",
            "#87786d"
        ]
    },
    {
        "name": "Commoner's Shoes",
        "image": "Legs/Commoner's Shoes.png",
        "primaryColor": "#867565",
        "secondaryColors": [
            "#6b5a4d",
            "#594639"
        ]
    },
    {
        "name": "Confessor Boots",
        "image": "Legs/Confessor Boots.png",
        "primaryColor": "#ada194",
        "secondaryColors": [
            "#85796c",
            "#665c53"
        ]
    },
    {
        "name": "Consort's Trousers",
        "image": "Legs/Consort's Trousers.png",
        "primaryColor": "#a8a09c",
        "secondaryColors": [
            "#88765f",
            "#665b51"
        ]
    },
    {
        "name": "Crucible Greaves",
        "image": "Legs/Crucible Greaves.png",
        "primaryColor": "#8a725f",
        "secondaryColors": [
            "#6c5849",
            "#5c4738"
        ]
    },
    {
        "name": "Cuckoo Knight Greaves",
        "image": "Legs/Cuckoo Knight Greaves.png",
        "primaryColor": "#9c9ea1",
        "secondaryColors": [
            "#555655",
            "#535452"
        ]
    },
    {
        "name": "Deathbed Smalls",
        "image": "Legs/Deathbed Smalls.png",
        "primaryColor": "#9e9e9a",
        "secondaryColors": [
            "#636259",
            "#636159"
        ]
    },
    {
        "name": "Depraved Perfumer Trousers",
        "image": "Legs/Depraved Perfumer Trousers.png",
        "primaryColor": "#8f8677",
        "secondaryColors": [
            "#896a5e",
            "#6b5d50"
        ]
    },
    {
        "name": "Drake Knight Greaves",
        "image": "Legs/Drake Knight Greaves.png",
        "primaryColor": "#0e1615",
        "secondaryColors": [
            "#a84f3b",
            "#56443a"
        ]
    },
    {
        "name": "Duelist Greaves",
        "image": "Legs/Duelist Greaves.png",
        "primaryColor": "#a09795",
        "secondaryColors": [
            "#857871",
            "#605b55"
        ]
    },
    {
        "name": "Eccentric's Breeches",
        "image": "Legs/Eccentric's Breeches.png",
        "primaryColor": "#a48f61",
        "secondaryColors": [
            "#711a18",
            "#2a2e62"
        ]
    },
    {
        "name": "Elden Lord Greaves",
        "image": "Legs/Elden Lord Greaves.png",
        "primaryColor": "#887361",
        "secondaryColors": [
            "#695b4d",
            "#554639"
        ]
    },
    {
        "name": "Errant Sorcerer Boots",
        "image": "Legs/Errant Sorcerer Boots.png",
        "primaryColor": "#94908a",
        "secondaryColors": [
            "#685c53",
            "#5a463a"
        ]
    },
    {
        "name": "Exile Greaves",
        "image": "Legs/Exile Greaves.png",
        "primaryColor": "#5d564e",
        "secondaryColors": [
            "#4c4e50",
            "#4b443a"
        ]
    },
    {
        "name": "Finger Maiden Shoes",
        "image": "Legs/Finger Maiden Shoes.png",
        "primaryColor": "#9e8d8d",
        "secondaryColors": [
            "#877774",
            "#665a57"
        ]
    },
    {
        "name": "Fingerprint Greaves",
        "image": "Legs/Fingerprint Greaves.png",
        "primaryColor": "#999297",
        "secondaryColors": [
            "#5f5a59",
            "#5b5658"
        ]
    },
    {
        "name": "Fire Monk Greaves",
        "image": "Legs/Fire Monk Greaves.png",
        "primaryColor": "#8f8d96",
        "secondaryColors": [
            "#595558",
            "#575153"
        ]
    },
    {
        "name": "Fire Prelate Greaves",
        "image": "Legs/Fire Prelate Greaves.png",
        "primaryColor": "#969193",
        "secondaryColors": [
            "#59585a",
            "#565455"
        ]
    },
    {
        "name": "Foot Soldier Greaves",
        "image": "Legs/Foot Soldier Greaves.png",
        "primaryColor": "#867365",
        "secondaryColors": [
            "#64584d",
            "#50443a"
        ]
    },
    {
        "name": "Fur Leggings",
        "image": "Legs/Fur Leggings.png",
        "primaryColor": "#877162",
        "secondaryColors": [
            "#695a4f",
            "#54453a"
        ]
    },
    {
        "name": "Gelmir Knight Greaves",
        "image": "Legs/Gelmir Knight Greaves.png",
        "primaryColor": "#a39ea0",
        "secondaryColors": [
            "#59524f",
            "#48423c"
        ]
    },
    {
        "name": "Godrick Knight Greaves",
        "image": "Legs/Godrick Knight Greaves.png",
        "primaryColor": "#ece8db",
        "secondaryColors": [
            "#625a4c",
            "#4d4637"
        ]
    },
    {
        "name": "Godrick Soldier Greaves",
        "image": "Legs/Godrick Soldier Greaves.png",
        "primaryColor": "#b09f8e",
        "secondaryColors": [
            "#8c725f",
            "#685b4a"
        ]
    },
    {
        "name": "Godskin Apostle Trousers",
        "image": "Legs/Godskin Apostle Trousers.png",
        "primaryColor": "#ada18e",
        "secondaryColors": [
            "#988a75",
            "#675e4d"
        ]
    },
    {
        "name": "Godskin Noble Trousers",
        "image": "Legs/Godskin Noble Trousers.png",
        "primaryColor": "#a49c8d",
        "secondaryColors": [
            "#928677",
            "#86796a"
        ]
    },
    {
        "name": "Gold Waistwrap",
        "image": "Legs/Gold Waistwrap.png",
        "primaryColor": "#897558",
        "secondaryColors": [
            "#71624a",
            "#5a4a33"
        ]
    },
    {
        "name": "Guardian Greaves",
        "image": "Legs/Guardian Greaves.png",
        "primaryColor": "#938b66",
        "secondaryColors": [
            "#837b59",
            "#6f6a4e"
        ]
    },
    {
        "name": "Haligtree Greaves",
        "image": "Legs/Haligtree Greaves.png",
        "primaryColor": "#887260",
        "secondaryColors": [
            "#62584b",
            "#514538"
        ]
    },
    {
        "name": "Haligtree Knight Greaves",
        "image": "Legs/Haligtree Knight Greaves.png",
        "primaryColor": "#edeade",
        "secondaryColors": [
            "#61594d",
            "#4d4537"
        ]
    },
    {
        "name": "Hoslow's Greaves",
        "image": "Legs/Hoslow's Greaves.png",
        "primaryColor": "#969695",
        "secondaryColors": [
            "#5c5a57",
            "#45433c"
        ]
    },
    {
        "name": "Kaiden Trousers",
        "image": "Legs/Kaiden Trousers.png",
        "primaryColor": "#8e8675",
        "secondaryColors": [
            "#847968",
            "#696355"
        ]
    },
    {
        "name": "Knight Greaves",
        "image": "Legs/Knight Greaves.png",
        "primaryColor": "#9c918b",
        "secondaryColors": [
            "#8a7467",
            "#655e59"
        ]
    },
    {
        "name": "Land of Reeds Greaves",
        "image": "Legs/Land of Reeds Greaves.png",
        "primaryColor": "#635b53",
        "secondaryColors": [
            "#615a54",
            "#4f443a"
        ]
    },
    {
        "name": "Leather Boots",
        "image": "Legs/Leather Boots.png",
        "primaryColor": "#857367",
        "secondaryColors": [
            "#625a51",
            "#4c453b"
        ]
    },
    {
        "name": "Leather Trousers",
        "image": "Legs/Leather Trousers.png",
        "primaryColor": "#837568",
        "secondaryColors": [
            "#685b4d",
            "#524639"
        ]
    },
    {
        "name": "Leyndell Knight Greaves",
        "image": "Legs/Leyndell Knight Greaves.png",
        "primaryColor": "#887056",
        "secondaryColors": [
            "#6e5c47",
            "#584934"
        ]
    },
    {
        "name": "Leyndell Soldier Greaves",
        "image": "Legs/Leyndell Soldier Greaves.png",
        "primaryColor": "#a28c6f",
        "secondaryColors": [
            "#8a7259",
            "#675948"
        ]
    },
    {
        "name": "Lionel's Greaves",
        "image": "Legs/Lionel's Greaves.png",
        "primaryColor": "#9f8c6d",
        "secondaryColors": [
            "#887459",
            "#625a50"
        ]
    },
    {
        "name": "Malenia's Greaves",
        "image": "Legs/Malenia's Greaves.png",
        "primaryColor": "#a9a18b",
        "secondaryColors": [
            "#948973",
            "#867965"
        ]
    },
    {
        "name": "Malformed Dragon Greaves",
        "image": "Legs/Malformed Dragon Greaves.png",
        "primaryColor": "#aa9e8e",
        "secondaryColors": [
            "#6b5d4b",
            "#594a35"
        ]
    },
    {
        "name": "Maliketh's Greaves",
        "image": "Legs/Maliketh's Greaves.png",
        "primaryColor": "#080604",
        "secondaryColors": [
            "#594922",
            "#4f4637"
        ]
    },
    {
        "name": "Mausoleum Greaves",
        "image": "Legs/Mausoleum Greaves.png",
        "primaryColor": "#a19995",
        "secondaryColors": [
            "#5e584e",
            "#4b4639"
        ]
    },
    {
        "name": "Mausoleum Knight Greaves",
        "image": "Legs/Mausoleum Knight Greaves.png",
        "primaryColor": "#9d9e9e",
        "secondaryColors": [
            "#575752",
            "#44433a"
        ]
    },
    {
        "name": "Mushroom Legs",
        "image": "Legs/Mushroom Legs.png",
        "primaryColor": "#96725c",
        "secondaryColors": [
            "#615951",
            "#544539"
        ]
    },
    {
        "name": "Nights Cavalry Greaves",
        "image": "Legs/Nights Cavalry Greaves.png",
        "primaryColor": "#212021",
        "secondaryColors": [
            "#585350",
            "#45413d"
        ]
    },
    {
        "name": "Noble's Trousers",
        "image": "Legs/Noble's Trousers.png",
        "primaryColor": "#a09fa0",
        "secondaryColors": [
            "#675d57",
            "#584439"
        ]
    },
    {
        "name": "Nomadic Merchant's Trousers",
        "image": "Legs/Nomadic Merchant's Trousers.png",
        "primaryColor": "#4e4e53",
        "secondaryColors": [
            "#4a4c50",
            "#47433c"
        ]
    },
    {
        "name": "Nox Monk Greaves",
        "image": "Legs/Nox Monk Greaves.png",
        "primaryColor": "#b19e8a",
        "secondaryColors": [
            "#9c8974",
            "#887663"
        ]
    },
    {
        "name": "Old Aristocrat Shoes",
        "image": "Legs/Old Aristocrat Shoes.png",
        "primaryColor": "#a78565",
        "secondaryColors": [
            "#8e6e53",
            "#765a46"
        ]
    },
    {
        "name": "Old Sorcerer's Legwraps",
        "image": "Legs/Old Sorcerer's Legwraps.png",
        "primaryColor": "#837b75",
        "secondaryColors": [
            "#625b57",
            "#585350"
        ]
    },
    {
        "name": "Omen Greaves",
        "image": "Legs/Omen Greaves.png",
        "primaryColor": "#916554",
        "secondaryColors": [
            "#705249",
            "#674639"
        ]
    },
    {
        "name": "Omenkiller Boots",
        "image": "Legs/Omenkiller Boots.png",
        "primaryColor": "#9e8578",
        "secondaryColors": [
            "#8d6d65",
            "#6b574f"
        ]
    },
    {
        "name": "Page Trousers",
        "image": "Legs/Page Trousers.png",
        "primaryColor": "#887261",
        "secondaryColors": [
            "#5e544b",
            "#504539"
        ]
    },
    {
        "name": "Perfumer Sarong",
        "image": "Legs/Perfumer Sarong.png",
        "primaryColor": "#a5a196",
        "secondaryColors": [
            "#8a8579",
            "#665e53"
        ]
    },
    {
        "name": "Preceptor's Trousers",
        "image": "Legs/Preceptor's Trousers.png",
        "primaryColor": "#5e636a",
        "secondaryColors": [
            "#575350",
            "#48423c"
        ]
    },
    {
        "name": "Prisoner Trousers",
        "image": "Legs/Prisoner Trousers.png",
        "primaryColor": "#896d5a",
        "secondaryColors": [
            "#5c4e4b",
            "#604639"
        ]
    },
    {
        "name": "Prophet Trousers",
        "image": "Legs/Prophet Trousers.png",
        "primaryColor": "#9b9186",
        "secondaryColors": [
            "#908478",
            "#86786c"
        ]
    },
    {
        "name": "Queen's Leggings",
        "image": "Legs/Queen's Leggings.png",
        "primaryColor": "#988b89",
        "secondaryColors": [
            "#8d817c",
            "#857974"
        ]
    },
    {
        "name": "Radahn Soldier Greaves",
        "image": "Legs/Radahn Soldier Greaves.png",
        "primaryColor": "#887465",
        "secondaryColors": [
            "#645a4c",
            "#504637"
        ]
    },
    {
        "name": "Radahn's Greaves",
        "image": "Legs/Radahn's Greaves.png",
        "primaryColor": "#847563",
        "secondaryColors": [
            "#685d4f",
            "#534738"
        ]
    },
    {
        "name": "Raging Wolf Greaves",
        "image": "Legs/Raging Wolf Greaves.png",
        "primaryColor": "#5e5853",
        "secondaryColors": [
            "#555453",
            "#4c443b"
        ]
    },
    {
        "name": "Raya Lucarian Greaves",
        "image": "Legs/Raya Lucarian Greaves.png",
        "primaryColor": "#a29895",
        "secondaryColors": [
            "#5f564e",
            "#4c4439"
        ]
    },
    {
        "name": "Redmane Knight Greaves",
        "image": "Legs/Redmane Knight Greaves.png",
        "primaryColor": "#a29a93",
        "secondaryColors": [
            "#5d5750",
            "#48423b"
        ]
    },
    {
        "name": "Ronin's Greaves",
        "image": "Legs/Ronin's Greaves.png",
        "primaryColor": "#9a9995",
        "secondaryColors": [
            "#5d5952",
            "#45433c"
        ]
    },
    {
        "name": "Rotten Duelist Greaves",
        "image": "Legs/Rotten Duelist Greaves.png",
        "primaryColor": "#9b4536",
        "secondaryColors": [
            "#5d504a",
            "#8c3a2d"
        ]
    },
    {
        "name": "Royal Knight Greaves",
        "image": "Legs/Royal Knight Greaves.png",
        "primaryColor": "#a49e93",
        "secondaryColors": [
            "#5e5a53",
            "#4b4639"
        ]
    },
    {
        "name": "Royal Remains Greaves",
        "image": "Legs/Royal Remains Greaves.png",
        "primaryColor": "#89745e",
        "secondaryColors": [
            "#5c564f",
            "#544638"
        ]
    },
    {
        "name": "Sage Trousers",
        "image": "Legs/Sage Trousers.png",
        "primaryColor": "#5d544d",
        "secondaryColors": [
            "#53443a",
            "#463931"
        ]
    },
    {
        "name": "Sanguine Noble Waistcloth",
        "image": "Legs/Sanguine Noble Waistcloth.png",
        "primaryColor": "#2d2826",
        "secondaryColors": [
            "#ac9379",
            "#46423c"
        ]
    },
    {
        "name": "Scaled Greaves",
        "image": "Legs/Scaled Greaves.png",
        "primaryColor": "#a59f95",
        "secondaryColors": [
            "#62594f",
            "#4c4439"
        ]
    },
    {
        "name": "Shaman Leggings",
        "image": "Legs/Shaman Leggings.png",
        "primaryColor": "#847764",
        "secondaryColors": [
            "#665d4e",
            "#514738"
        ]
    },
    {
        "name": "Snow Witch Skirt",
        "image": "Legs/Snow Witch Skirt.png",
        "primaryColor": "#9e9f9f",
        "secondaryColors": [
            "#9d9e9f",
            "#9d9e9e"
        ]
    },
    {
        "name": "Sorcerer Leggings",
        "image": "Legs/Sorcerer Leggings.png",
        "primaryColor": "#5c5952",
        "secondaryColors": [
            "#595751",
            "#44423c"
        ]
    },
    {
        "name": "Spellblade's Trousers",
        "image": "Legs/Spellblade's Trousers.png",
        "primaryColor": "#8e8772",
        "secondaryColors": [
            "#87785b",
            "#686153"
        ]
    },
    {
        "name": "Traveler's Boots",
        "image": "Legs/Traveler's Boots.png",
        "primaryColor": "#9d938f",
        "secondaryColors": [
            "#867774",
            "#645652"
        ]
    },
    {
        "name": "Traveler's Slops",
        "image": "Legs/Traveler's Slops.png",
        "primaryColor": "#8e735a",
        "secondaryColors": [
            "#655a4c",
            "#50453a"
        ]
    },
    {
        "name": "Traveling Maiden Boots",
        "image": "Legs/Traveling Maiden Boots.png",
        "primaryColor": "#a39898",
        "secondaryColors": [
            "#857a79",
            "#615b57"
        ]
    },
    {
        "name": "Tree Sentinel Greaves",
        "image": "Legs/Tree Sentinel Greaves.png",
        "primaryColor": "#a08c6e",
        "secondaryColors": [
            "#897457",
            "#716049"
        ]
    },
    {
        "name": "Twinned Greaves",
        "image": "Legs/Twinned Greaves.png",
        "primaryColor": "#97969a",
        "secondaryColors": [
            "#5f5954",
            "#52473a"
        ]
    },
    {
        "name": "Vagabond Knight Greaves",
        "image": "Legs/Vagabond Knight Greaves.png",
        "primaryColor": "#897064",
        "secondaryColors": [
            "#61584f",
            "#4c443b"
        ]
    },
    {
        "name": "Veteran's Greaves",
        "image": "Legs/Veteran's Greaves.png",
        "primaryColor": "#a69d93",
        "secondaryColors": [
            "#85786c",
            "#685d54"
        ]
    },
    {
        "name": "Vulgar Militia Greaves",
        "image": "Legs/Vulgar Militia Greaves.png",
        "primaryColor": "#89725d",
        "secondaryColors": [
            "#61584d",
            "#4e463a"
        ]
    },
    {
        "name": "War Surgeon Trousers",
        "image": "Legs/War Surgeon Trousers.png",
        "primaryColor": "#555251",
        "secondaryColors": [
            "#514c48",
            "#48413d"
        ]
    },
    {
        "name": "Warrior Greaves",
        "image": "Legs/Warrior Greaves.png",
        "primaryColor": "#a49f95",
        "secondaryColors": [
            "#655d52",
            "#52463a"
        ]
    },
    {
        "name": "White Reed Greaves",
        "image": "Legs/White Reed Greaves.png",
        "primaryColor": "#877661",
        "secondaryColors": [
            "#63594e",
            "#514539"
        ]
    },
    {
        "name": "Zamor Legwraps",
        "image": "Legs/Zamor Legwraps.png",
        "primaryColor": "#635d50",
        "secondaryColors": [
            "#615c50",
            "#4a453a"
        ]
    },
    {
        "name": "Ansbach's Boots",
        "image": "Legs\\SOTE/Ansbach's Boots.png",
        "primaryColor": "#454442",
        "secondaryColors": [
            "#45413d",
            "#423c37"
        ]
    },
    {
        "name": "Ascetic's Ankle Guards",
        "image": "Legs\\SOTE/Ascetic's Ankle Guards.png",
        "primaryColor": "#645849",
        "secondaryColors": [
            "#5d544f",
            "#514738"
        ]
    },
    {
        "name": "Ascetic's Loincloth",
        "image": "Legs\\SOTE/Ascetic's Loincloth.png",
        "primaryColor": "#86755e",
        "secondaryColors": [
            "#6c5b49",
            "#594837"
        ]
    },
    {
        "name": "Black Knight Greaves",
        "image": "Legs\\SOTE/Black Knight Greaves.png",
        "primaryColor": "#0f0d0c",
        "secondaryColors": [
            "#595553",
            "#5a5550"
        ]
    },
    {
        "name": "Common Soldier Greaves",
        "image": "Legs\\SOTE/Common Soldier Greaves.png",
        "primaryColor": "#5a5049",
        "secondaryColors": [
            "#514439",
            "#45382d"
        ]
    },
    {
        "name": "Dancer's Trousers",
        "image": "Legs\\SOTE/Dancer's Trousers.png",
        "primaryColor": "#5c4e2e",
        "secondaryColors": [
            "#5e482c",
            "#493921"
        ]
    },
    {
        "name": "Death Knight Greaves",
        "image": "Legs\\SOTE/Death Knight Greaves.png",
        "primaryColor": "#887359",
        "secondaryColors": [
            "#6e5f49",
            "#534633"
        ]
    },
    {
        "name": "Divine Bird Warrior Greaves",
        "image": "Legs\\SOTE/Divine Bird Warrior Greaves.png",
        "primaryColor": "#a19064",
        "secondaryColors": [
            "#89764b",
            "#5f4d2d"
        ]
    },
    {
        "name": "Dryleaf Cuissardes",
        "image": "Legs\\SOTE/Dryleaf Cuissardes.png",
        "primaryColor": "#6f674e",
        "secondaryColors": [
            "#6a6049",
            "#554b37"
        ]
    },
    {
        "name": "Fire Knight Greaves",
        "image": "Legs\\SOTE/Fire Knight Greaves.png",
        "primaryColor": "#575552",
        "secondaryColors": [
            "#4e4338",
            "#473329"
        ]
    },
    {
        "name": "Freyja's Greaves",
        "image": "Legs\\SOTE/Freyja's Greaves.png",
        "primaryColor": "#6a5446",
        "secondaryColors": [
            "#594438",
            "#49362b"
        ]
    },
    {
        "name": "Gaius's Greaves",
        "image": "Legs\\SOTE/Gaius's Greaves.png",
        "primaryColor": "#65534e",
        "secondaryColors": [
            "#5c433b",
            "#51302d"
        ]
    },
    {
        "name": "Gravebird Anklets",
        "image": "Legs\\SOTE/Gravebird Anklets.png",
        "primaryColor": "#9b978d",
        "secondaryColors": [
            "#635f54",
            "#48443a"
        ]
    },
    {
        "name": "Greaves of Night",
        "image": "Legs\\SOTE/Greaves of Night.png",
        "primaryColor": "#0d0b0a",
        "secondaryColors": [
            "#43403e",
            "#433e41"
        ]
    },
    {
        "name": "Greaves of Solitude",
        "image": "Legs\\SOTE/Greaves of Solitude.png",
        "primaryColor": "#a09e9c",
        "secondaryColors": [
            "#555350",
            "#42403e"
        ]
    },
    {
        "name": "High Priest Undergarments",
        "image": "Legs\\SOTE/High Priest Undergarments.png",
        "primaryColor": "#949392",
        "secondaryColors": [
            "#61605e",
            "#45423b"
        ]
    },
    {
        "name": "Horned Warrior Greaves",
        "image": "Legs\\SOTE/Horned Warrior Greaves.png",
        "primaryColor": "#847965",
        "secondaryColors": [
            "#655c4c",
            "#4e4637"
        ]
    },
    {
        "name": "Igon's Loincloth",
        "image": "Legs\\SOTE/Igon's Loincloth.png",
        "primaryColor": "#5c5d5e",
        "secondaryColors": [
            "#565151",
            "#524539"
        ]
    },
    {
        "name": "Iron Rivet Greaves",
        "image": "Legs\\SOTE/Iron Rivet Greaves.png",
        "primaryColor": "#665a4b",
        "secondaryColors": [
            "#655a48",
            "#514738"
        ]
    },
    {
        "name": "Leather Leg Wraps",
        "image": "Legs\\SOTE/Leather Leg Wraps.png",
        "primaryColor": "#867462",
        "secondaryColors": [
            "#6b5e4f",
            "#514538"
        ]
    },
    {
        "name": "Messmer Soldier Greaves",
        "image": "Legs\\SOTE/Messmer Soldier Greaves.png",
        "primaryColor": "#635748",
        "secondaryColors": [
            "#4f4730",
            "#4f4533"
        ]
    },
    {
        "name": "Messmer's Greaves",
        "image": "Legs\\SOTE/Messmer's Greaves.png",
        "primaryColor": "#5d574f",
        "secondaryColors": [
            "#5a514b",
            "#4c433b"
        ]
    },
    {
        "name": "Oathseeker Knight Greaves",
        "image": "Legs\\SOTE/Oathseeker Knight Greaves.png",
        "primaryColor": "#5a5a5a",
        "secondaryColors": [
            "#59544e",
            "#4a433b"
        ]
    },
    {
        "name": "Rakshasa Greaves",
        "image": "Legs\\SOTE/Rahshasa Greaves.png",
        "primaryColor": "#601e15",
        "secondaryColors": [
            "#5c433b",
            "#522d28"
        ]
    },
    {
        "name": "Rellana's Greaves",
        "image": "Legs\\SOTE/Rellana's Greaves.png",
        "primaryColor": "#dbdcdb",
        "secondaryColors": [
            "#9c9e9d",
            "#535552"
        ]
    },
    {
        "name": "Shadow Militiaman Greaves",
        "image": "Legs\\SOTE/Shadow Militiaman Greaves.png",
        "primaryColor": "#514b4a",
        "secondaryColors": [
            "#4c4745",
            "#48423c"
        ]
    },
    {
        "name": "Soiled Loincloth",
        "image": "Legs\\SOTE/Soiled Loincloth.png",
        "primaryColor": "#74604d",
        "secondaryColors": [
            "#6a5747",
            "#564638"
        ]
    },
    {
        "name": "Thiollier's Trousers",
        "image": "Legs\\SOTE/Thiollier's Trousers.png",
        "primaryColor": "#514a47",
        "secondaryColors": [
            "#4a413e",
            "#3d3e40"
        ]
    },
    {
        "name": "Verdigris Greaves",
        "image": "Legs\\SOTE/Verdigris Greaves.png",
        "primaryColor": "#4e524c",
        "secondaryColors": [
            "#42443d",
            "#3e4541"
        ]
    },
    {
        "name": "Young Lion's Greaves",
        "image": "Legs\\SOTE/Young Lion's Greaves.png",
        "primaryColor": "#5d554b",
        "secondaryColors": [
            "#574731",
            "#4b4931"
        ]
    },
    {
        "name": "Albinauric Shield",
        "image": "Shields/Albinauric Shield.png",
        "primaryColor": "#938d7e",
        "secondaryColors": [
            "#9d9c98",
            "#8c8578"
        ]
    },
    {
        "name": "Ant's Skull Plate",
        "image": "Shields/Ant's Skull Plate.png",
        "primaryColor": "#5a5057",
        "secondaryColors": [
            "#694337",
            "#393944"
        ]
    },
    {
        "name": "Banished Knight's Shield",
        "image": "Shields/Banished Knight's Shield.png",
        "primaryColor": "#a59c90",
        "secondaryColors": [
            "#948873",
            "#867963"
        ]
    },
    {
        "name": "Beast Crest Heater Shield",
        "image": "Shields/Beast Crest Heater Shield.png",
        "primaryColor": "#af9f88",
        "secondaryColors": [
            "#9d8b72",
            "#887762"
        ]
    },
    {
        "name": "Beastman's Jar Shield",
        "image": "Shields/Beastman's Jar Shield.png",
        "primaryColor": "#a59c8f",
        "secondaryColors": [
            "#928773",
            "#857965"
        ]
    },
    {
        "name": "Black Leather Shield",
        "image": "Shields/Black Leather Shield.png",
        "primaryColor": "#2f3440",
        "secondaryColors": [
            "#51525a",
            "#76695b"
        ]
    },
    {
        "name": "Blue Crest Heater Shield",
        "image": "Shields/Blue Crest Heater Shield.png",
        "primaryColor": "#555252",
        "secondaryColors": [
            "#50525e",
            "#44403e"
        ]
    },
    {
        "name": "Blue-Gold Kite Shield",
        "image": "Shields/Blue-Gold Kite Shield.png",
        "primaryColor": "#c9b690",
        "secondaryColors": [
            "#c5ad72",
            "#af9767"
        ]
    },
    {
        "name": "Blue-White Wooden Shield",
        "image": "Shields/Blue-White Wooden Shield.png",
        "primaryColor": "#b3c4ba",
        "secondaryColors": [
            "#a0aba3",
            "#50748b"
        ]
    },
    {
        "name": "Brass Shield",
        "image": "Shields/Brass Shield.png",
        "primaryColor": "#9d8864",
        "secondaryColors": [
            "#88724f",
            "#876839"
        ]
    },
    {
        "name": "Briar Greatshield",
        "image": "Shields/Briar Greatshield.png",
        "primaryColor": "#aa8b65",
        "secondaryColors": [
            "#8d6d50",
            "#69554a"
        ]
    },
    {
        "name": "Buckler",
        "image": "Shields/Buckler.png",
        "primaryColor": "#9d989e",
        "secondaryColors": [
            "#6e7487",
            "#5c575b"
        ]
    },
    {
        "name": "Candletree Wooden Shield",
        "image": "Shields/Candletree Wooden Shield.png",
        "primaryColor": "#c9c9ca",
        "secondaryColors": [
            "#929ca8",
            "#798695"
        ]
    },
    {
        "name": "Carian Knight's Shield",
        "image": "Shields/Carian Knight's Shield.png",
        "primaryColor": "#9b9997",
        "secondaryColors": [
            "#8b8379",
            "#837a6f"
        ]
    },
    {
        "name": "Coil Shield",
        "image": "Shields/Coil Shield.png",
        "primaryColor": "#93a498",
        "secondaryColors": [
            "#759389",
            "#718577"
        ]
    },
    {
        "name": "Crossed Tree Towershield",
        "image": "Shields/Crossed Tree Towershield.png",
        "primaryColor": "#94a6a2",
        "secondaryColors": [
            "#748d8c",
            "#556257"
        ]
    },
    {
        "name": "Crucible Hornshield",
        "image": "Shields/Crucible Hornshield.png",
        "primaryColor": "#cca691",
        "secondaryColors": [
            "#b08873",
            "#936959"
        ]
    },
    {
        "name": "Cuckoo Greatshield",
        "image": "Shields/Cuckoo Greatshield.png",
        "primaryColor": "#969697",
        "secondaryColors": [
            "#8c8478",
            "#7a8495"
        ]
    },
    {
        "name": "Distinguished Greatshield",
        "image": "Shields/Distinguished Greatshield.png",
        "primaryColor": "#a49ea0",
        "secondaryColors": [
            "#8f8478",
            "#965e5b"
        ]
    },
    {
        "name": "Dragon Towershield",
        "image": "Shields/Dragon Towershield.png",
        "primaryColor": "#9a9399",
        "secondaryColors": [
            "#88756b",
            "#665a58"
        ]
    },
    {
        "name": "Dragonclaw Shield",
        "image": "Shields/Dragonclaw Shield.png",
        "primaryColor": "#97938e",
        "secondaryColors": [
            "#867764",
            "#655e55"
        ]
    },
    {
        "name": "Eclipse Crest Greatshield",
        "image": "Shields/Eclipse Crest Greatshield.png",
        "primaryColor": "#707787",
        "secondaryColors": [
            "#515258",
            "#3d4049"
        ]
    },
    {
        "name": "Eclipse Crest Heater Shield",
        "image": "Shields/Eclipse Crest Heater Shield.png",
        "primaryColor": "#d1cfce",
        "secondaryColors": [
            "#a5a5a6",
            "#51575d"
        ]
    },
    {
        "name": "Erdtree Greatshield",
        "image": "Shields/Erdtree Greatshield.png",
        "primaryColor": "#ab9f91",
        "secondaryColors": [
            "#978875",
            "#887561"
        ]
    },
    {
        "name": "Fingerprint Stone Shield",
        "image": "Shields/Fingerprint Stone Shield.png",
        "primaryColor": "#989290",
        "secondaryColors": [
            "#837b78",
            "#5b5453"
        ]
    },
    {
        "name": "Flame Crest Wooden Shield",
        "image": "Shields/Flame Crest Wooden Shield.png",
        "primaryColor": "#916130",
        "secondaryColors": [
            "#684a31",
            "#4a4544"
        ]
    },
    {
        "name": "Gilded Greatshield",
        "image": "Shields/Gilded Greatshield.png",
        "primaryColor": "#e4dbd8",
        "secondaryColors": [
            "#9b9898",
            "#8c6e5a"
        ]
    },
    {
        "name": "Gilded Iron Shield",
        "image": "Shields/Gilded Iron Shield.png",
        "primaryColor": "#e6da9f",
        "secondaryColors": [
            "#a6935a",
            "#645b48"
        ]
    },
    {
        "name": "Golden Beast Crest Shield",
        "image": "Shields/Golden Beast Crest Shield.png",
        "primaryColor": "#a28d5e",
        "secondaryColors": [
            "#88714b",
            "#83653a"
        ]
    },
    {
        "name": "Golden Greatshield",
        "image": "Shields/Golden Greatshield.png",
        "primaryColor": "#dbdbd9",
        "secondaryColors": [
            "#a29f98",
            "#837562"
        ]
    },
    {
        "name": "Great Turtle Shell",
        "image": "Shields/Great Turtle Shell.png",
        "primaryColor": "#a1928d",
        "secondaryColors": [
            "#988478",
            "#8a746c"
        ]
    },
    {
        "name": "Haligtree Crest Greatshield",
        "image": "Shields/Haligtree Crest Greatshield.png",
        "primaryColor": "#9c9990",
        "secondaryColors": [
            "#8f8776",
            "#857b66"
        ]
    },
    {
        "name": "Hawk Crest Wooden Shield",
        "image": "Shields/Hawk Crest Wooden Shield.png",
        "primaryColor": "#9d8663",
        "secondaryColors": [
            "#887458",
            "#64574e"
        ]
    },
    {
        "name": "Heater Shield",
        "image": "Shields/Heater Shield.png",
        "primaryColor": "#8e8e93",
        "secondaryColors": [
            "#89837c",
            "#827a75"
        ]
    },
    {
        "name": "Horse Crest Wooden Shield",
        "image": "Shields/Horse Crest Wooden Shield.png",
        "primaryColor": "#9a8875",
        "secondaryColors": [
            "#887566",
            "#6d5b51"
        ]
    },
    {
        "name": "Ice Crest Shield",
        "image": "Shields/Ice Crest Shield.png",
        "primaryColor": "#929ea5",
        "secondaryColors": [
            "#748a96",
            "#627786"
        ]
    },
    {
        "name": "Icon Shield",
        "image": "Shields/Icon Shield.png",
        "primaryColor": "#9aa9aa",
        "secondaryColors": [
            "#a6905e",
            "#897026"
        ]
    },
    {
        "name": "Inverted Hawk Heater Shield",
        "image": "Shields/Inverted Hawk Heater Shield.png",
        "primaryColor": "#894e4f",
        "secondaryColors": [
            "#764747",
            "#6e413c"
        ]
    },
    {
        "name": "Inverted Hawk Towershield",
        "image": "Shields/Inverted Hawk Towershield.png",
        "primaryColor": "#67728b",
        "secondaryColors": [
            "#515055",
            "#49423c"
        ]
    },
    {
        "name": "Iron Roundshield",
        "image": "Shields/Iron Roundshield.png",
        "primaryColor": "#d6d3d7",
        "secondaryColors": [
            "#9a949b",
            "#5b555a"
        ]
    },
    {
        "name": "Jellyfish Shield",
        "image": "Shields/Jellyfish Shield.png",
        "primaryColor": "#91adca",
        "secondaryColors": [
            "#748ca8",
            "#718aa4"
        ]
    },
    {
        "name": "Kite Shield",
        "image": "Shields/Kite Shield.png",
        "primaryColor": "#958c8d",
        "secondaryColors": [
            "#90827c",
            "#857876"
        ]
    },
    {
        "name": "Large Leather Shield",
        "image": "Shields/Large Leather Shield.png",
        "primaryColor": "#87685a",
        "secondaryColors": [
            "#875236",
            "#69534c"
        ]
    },
    {
        "name": "Lordsworn's Shield",
        "image": "Shields/Lordsworn's Shield.png",
        "primaryColor": "#9195a1",
        "secondaryColors": [
            "#727586",
            "#595559"
        ]
    },
    {
        "name": "Man-Serpent's Shield",
        "image": "Shields/Man-Serpent's Shield.png",
        "primaryColor": "#ad8b6a",
        "secondaryColors": [
            "#946b51",
            "#8a5735"
        ]
    },
    {
        "name": "Manor Towershield",
        "image": "Shields/Manor Towershield.png",
        "primaryColor": "#a5b1ca",
        "secondaryColors": [
            "#8b95b0",
            "#6b728d"
        ]
    },
    {
        "name": "Marred Leather Shield",
        "image": "Shields/Marred Leather Shield.png",
        "primaryColor": "#978873",
        "secondaryColors": [
            "#88725c",
            "#6c5d4c"
        ]
    },
    {
        "name": "Marred Wooden Shield",
        "image": "Shields/Marred Wooden Shield.png",
        "primaryColor": "#5d5a4c",
        "secondaryColors": [
            "#63574b",
            "#51463a"
        ]
    },
    {
        "name": "One-Eyed Shield",
        "image": "Shields/One-Eyed Shield.png",
        "primaryColor": "#a19a97",
        "secondaryColors": [
            "#8b827c",
            "#897270"
        ]
    },
    {
        "name": "Perfumer's Shield",
        "image": "Shields/Perfumer's Shield.png",
        "primaryColor": "#a4885f",
        "secondaryColors": [
            "#917149",
            "#8b6735"
        ]
    },
    {
        "name": "Pillory Shield",
        "image": "Shields/Pillory Shield.png",
        "primaryColor": "#8b6f5f",
        "secondaryColors": [
            "#6d5649",
            "#5d4539"
        ]
    },
    {
        "name": "Red Crest Heater Shield",
        "image": "Shields/Red Crest Heater Shield.png",
        "primaryColor": "#c3b3a8",
        "secondaryColors": [
            "#aa9b92",
            "#93847a"
        ]
    },
    {
        "name": "Red Thorn Roundshield",
        "image": "Shields/Red Thorn Roundshield.png",
        "primaryColor": "#8b6e56",
        "secondaryColors": [
            "#924d35",
            "#6d5a49"
        ]
    },
    {
        "name": "Redmane Greatshield",
        "image": "Shields/Redmane Greatshield.png",
        "primaryColor": "#555255",
        "secondaryColors": [
            "#514538",
            "#3b434f"
        ]
    },
    {
        "name": "Rickety Shield",
        "image": "Shields/Rickety Shield.png",
        "primaryColor": "#988771",
        "secondaryColors": [
            "#887461",
            "#695a4e"
        ]
    },
    {
        "name": "Rift Shield",
        "image": "Shields/Rift Shield.png",
        "primaryColor": "#9c9495",
        "secondaryColors": [
            "#847774",
            "#645a59"
        ]
    },
    {
        "name": "Riveted Wooden Shield",
        "image": "Shields/Riveted Wooden Shield.png",
        "primaryColor": "#978f8e",
        "secondaryColors": [
            "#886c55",
            "#6c5a50"
        ]
    },
    {
        "name": "Round Shield",
        "image": "Shields/Round Shield.png",
        "primaryColor": "#938974",
        "secondaryColors": [
            "#847867",
            "#655a4d"
        ]
    },
    {
        "name": "Scorpion Kite Shield",
        "image": "Shields/Scorpion Kite Shield.png",
        "primaryColor": "#171616",
        "secondaryColors": [
            "#b28931",
            "#96702a"
        ]
    },
    {
        "name": "Scripture Wooden Shield",
        "image": "Shields/Scripture Wooden Shield.png",
        "primaryColor": "#9f8863",
        "secondaryColors": [
            "#8a714f",
            "#87643a"
        ]
    },
    {
        "name": "Shield of the Guilty",
        "image": "Shields/Shield of the Guilty.png",
        "primaryColor": "#d3d2ae",
        "secondaryColors": [
            "#9fa796",
            "#968f68"
        ]
    },
    {
        "name": "Silver Mirrorshield",
        "image": "Shields/Silver Mirrorshield.png",
        "primaryColor": "#dddddf",
        "secondaryColors": [
            "#9b9a9a",
            "#625c56"
        ]
    },
    {
        "name": "Smoldering Shield",
        "image": "Shields/Smoldering Shield.png",
        "primaryColor": "#51545e",
        "secondaryColors": [
            "#3c424c",
            "#373b44"
        ]
    },
    {
        "name": "Spiked Palisade Shield",
        "image": "Shields/Spiked Palisade Shield.png",
        "primaryColor": "#8a6b5b",
        "secondaryColors": [
            "#5e5854",
            "#5f4536"
        ]
    },
    {
        "name": "Spiralhorn Shield",
        "image": "Shields/Spiralhorn Shield.png",
        "primaryColor": "#a79b94",
        "secondaryColors": [
            "#89746d",
            "#655854"
        ]
    },
    {
        "name": "Sun Realm Shield",
        "image": "Shields/Sun Realm Shield.png",
        "primaryColor": "#99928f",
        "secondaryColors": [
            "#857568",
            "#625750"
        ]
    },
    {
        "name": "Twinbird Kite Shield",
        "image": "Shields/Twinbird Kite Shield.png",
        "primaryColor": "#cd9270",
        "secondaryColors": [
            "#a1998d",
            "#a28a6e"
        ]
    },
    {
        "name": "Visage Shield",
        "image": "Shields/Visage Shield.png",
        "primaryColor": "#a2a18d",
        "secondaryColors": [
            "#968b72",
            "#8c745b"
        ]
    },
    {
        "name": "Wooden Greatshield",
        "image": "Shields/Wooden Greatshield.png",
        "primaryColor": "#5c4f50",
        "secondaryColors": [
            "#544339",
            "#473c42"
        ]
    },
    {
        "name": "Black Steel Greatshield",
        "image": "Shields\\SOTE/Black Steel Greatshield.png",
        "primaryColor": "#0f0f0f",
        "secondaryColors": [
            "#4b4436",
            "#3d4147"
        ]
    },
    {
        "name": "Golden Lion Shield",
        "image": "Shields\\SOTE/Golden Lion Shield.png",
        "primaryColor": "#a49e8f",
        "secondaryColors": [
            "#958a72",
            "#867962"
        ]
    },
    {
        "name": "Messmer Soldier Shield",
        "image": "Shields\\SOTE/Messmer Soldier Shield.png",
        "primaryColor": "#272828",
        "secondaryColors": [
            "#4d535c",
            "#3c434b"
        ]
    },
    {
        "name": "Serpent Crest Shield",
        "image": "Shields\\SOTE/Serpent Crest Shield.png",
        "primaryColor": "#57515a",
        "secondaryColors": [
            "#51433a",
            "#493b46"
        ]
    },
    {
        "name": "Shield of Night",
        "image": "Shields\\SOTE/Shield of Night.png",
        "primaryColor": "#030302",
        "secondaryColors": [
            "#5d5e63",
            "#585658"
        ]
    },
    {
        "name": "Smithscript Shield",
        "image": "Shields\\SOTE/Smithscript Shield.png",
        "primaryColor": "#301f1d",
        "secondaryColors": [
            "#8b7168",
            "#5f5256"
        ]
    },
    {
        "name": "Verdigris Greatshield",
        "image": "Shields\\SOTE/Verdigris Greatshield.png",
        "primaryColor": "#5b7288",
        "secondaryColors": [
            "#495863",
            "#394652"
        ]
    },
    {
        "name": "Wolf Crest Shield",
        "image": "Shields\\SOTE/Wolf Crest Shield.png",
        "primaryColor": "#5e6a8e",
        "secondaryColors": [
            "#4e505b",
            "#3c425a"
        ]
    },
    {
        "name": "Academy Glintstone Staff",
        "image": "Weapons/Academy Glintstone Staff.png",
        "primaryColor": "#9d979a",
        "secondaryColors": [
            "#635857",
            "#5d5354"
        ]
    },
    {
        "name": "Alabaster Lord's Sword",
        "image": "Weapons/Alabaster Lord's Sword.png",
        "primaryColor": "#567192",
        "secondaryColors": [
            "#535861",
            "#374758"
        ]
    },
    {
        "name": "Albinauric Bow",
        "image": "Weapons/Albinauric Bow.png",
        "primaryColor": "#989899",
        "secondaryColors": [
            "#5f5a58",
            "#5b5752"
        ]
    },
    {
        "name": "Albinauric Staff",
        "image": "Weapons/Albinauric Staff.png",
        "primaryColor": "#8c93a2",
        "secondaryColors": [
            "#697388",
            "#4f5462"
        ]
    },
    {
        "name": "Antspur Rapier",
        "image": "Weapons/Antspur Rapier.png",
        "primaryColor": "#87755f",
        "secondaryColors": [
            "#6f604e",
            "#930601"
        ]
    },
    {
        "name": "Arbalest",
        "image": "Weapons/Arbalest.png",
        "primaryColor": "#a5866a",
        "secondaryColors": [
            "#8b6f59",
            "#685950"
        ]
    },
    {
        "name": "Astrologer's Staff",
        "image": "Weapons/Astrologer's Staff.png",
        "primaryColor": "#a19ea1",
        "secondaryColors": [
            "#695955",
            "#684533"
        ]
    },
    {
        "name": "Axe of Godfrey",
        "image": "Weapons/Axe of Godfrey.png",
        "primaryColor": "#5c524f",
        "secondaryColors": [
            "#585251",
            "#4e433c"
        ]
    },
    {
        "name": "Axe of Godrick",
        "image": "Weapons/Axe of Godrick.png",
        "primaryColor": "#685f55",
        "secondaryColors": [
            "#625d55",
            "#554836"
        ]
    },
    {
        "name": "Azur's Glintstone Staff",
        "image": "Weapons/Azur's Glintstone Staff.png",
        "primaryColor": "#289c90",
        "secondaryColors": [
            "#5f6163",
            "#1b5e57"
        ]
    },
    {
        "name": "Bandit's Curved Sword",
        "image": "Weapons/Bandit's Curved Sword.png",
        "primaryColor": "#655b55",
        "secondaryColors": [
            "#5b5552",
            "#55463b"
        ]
    },
    {
        "name": "Banished Knight's Greatsword",
        "image": "Weapons/Banished Knight's Greatsword.png",
        "primaryColor": "#9a9d91",
        "secondaryColors": [
            "#858676",
            "#616153"
        ]
    },
    {
        "name": "Banished Knight's Halberd",
        "image": "Weapons/Banished Knight's Halberd.png",
        "primaryColor": "#a9a59a",
        "secondaryColors": [
            "#847757",
            "#655e4d"
        ]
    },
    {
        "name": "Bastard Sword",
        "image": "Weapons/Bastard Sword.png",
        "primaryColor": "#d4dbe1",
        "secondaryColors": [
            "#94989e",
            "#767c83"
        ]
    },
    {
        "name": "Bastard's Stars",
        "image": "Weapons/Bastard's Stars.png",
        "primaryColor": "#99999b",
        "secondaryColors": [
            "#5c708d",
            "#6d6c6e"
        ]
    },
    {
        "name": "Battle Axe",
        "image": "Weapons/Battle Axe.png",
        "primaryColor": "#8d969f",
        "secondaryColors": [
            "#767b83",
            "#595c63"
        ]
    },
    {
        "name": "Battle Hammer",
        "image": "Weapons/Battle Hammer.png",
        "primaryColor": "#918f96",
        "secondaryColors": [
            "#5e5659",
            "#51433b"
        ]
    },
    {
        "name": "Beast-Repellent Torch",
        "image": "Weapons/Beast-Repellent Torch.png",
        "primaryColor": "#f1a35a",
        "secondaryColors": [
            "#d8662d",
            "#92674b"
        ]
    },
    {
        "name": "Beastclaw Greathammer",
        "image": "Weapons/Beastclaw Greathammer.png",
        "primaryColor": "#857660",
        "secondaryColors": [
            "#6c5e4d",
            "#594934"
        ]
    },
    {
        "name": "Beastman's Cleaver",
        "image": "Weapons/Beastman's Cleaver.png",
        "primaryColor": "#999a9d",
        "secondaryColors": [
            "#5a595a",
            "#4d4539"
        ]
    },
    {
        "name": "Beastman's Curved Sword",
        "image": "Weapons/Beastman's Curved Sword.png",
        "primaryColor": "#575452",
        "secondaryColors": [
            "#504636",
            "#433b31"
        ]
    },
    {
        "name": "Black Bow",
        "image": "Weapons/Black Bow.png",
        "primaryColor": "#585a60",
        "secondaryColors": [
            "#53555c",
            "#505258"
        ]
    },
    {
        "name": "Black Knife",
        "image": "Weapons/Black Knife.png",
        "primaryColor": "#9d9da1",
        "secondaryColors": [
            "#606466",
            "#59595b"
        ]
    },
    {
        "name": "Blade of Calling",
        "image": "Weapons/Blade of Calling.png",
        "primaryColor": "#9f9997",
        "secondaryColors": [
            "#857a73",
            "#68605f"
        ]
    },
    {
        "name": "Blasphemous Blade",
        "image": "Weapons/Blasphemous Blade.png",
        "primaryColor": "#5e4837",
        "secondaryColors": [
            "#4c2a26",
            "#49292a"
        ]
    },
    {
        "name": "Bloodhound Claws",
        "image": "Weapons/Bloodhound Claws.png",
        "primaryColor": "#99989f",
        "secondaryColors": [
            "#89746b",
            "#767885"
        ]
    },
    {
        "name": "Bloodhound's Fang",
        "image": "Weapons/Bloodhound's Fang.png",
        "primaryColor": "#5f5a57",
        "secondaryColors": [
            "#5f5751",
            "#4f443a"
        ]
    },
    {
        "name": "Bloodstained Dagger",
        "image": "Weapons/Bloodstained Dagger.png",
        "primaryColor": "#877666",
        "secondaryColors": [
            "#635c58",
            "#53453a"
        ]
    },
    {
        "name": "Bloody Helice",
        "image": "Weapons/Bloody Helice.png",
        "primaryColor": "#625852",
        "secondaryColors": [
            "#655652",
            "#5e4937"
        ]
    },
    {
        "name": "Bolt of Gransax",
        "image": "Weapons/Bolt of Gransax.png",
        "primaryColor": "#9c8b70",
        "secondaryColors": [
            "#685f54",
            "#6a5e4d"
        ]
    },
    {
        "name": "Brick Hammer",
        "image": "Weapons/Brick Hammer.png",
        "primaryColor": "#9a9796",
        "secondaryColors": [
            "#897569",
            "#5f5957"
        ]
    },
    {
        "name": "Broadsword",
        "image": "Weapons/Broadsword.png",
        "primaryColor": "#999798",
        "secondaryColors": [
            "#83796c",
            "#737884"
        ]
    },
    {
        "name": "Butchering Knife",
        "image": "Weapons/Butchering Knife.png",
        "primaryColor": "#5d5c5e",
        "secondaryColors": [
            "#575456",
            "#48413c"
        ]
    },
    {
        "name": "Caestus",
        "image": "Weapons/Caestus.png",
        "primaryColor": "#9e8475",
        "secondaryColors": [
            "#8b6e5d",
            "#665652"
        ]
    },
    {
        "name": "Cane Sword",
        "image": "Weapons/Cane Sword.png",
        "primaryColor": "#8d929f",
        "secondaryColors": [
            "#727889",
            "#68615e"
        ]
    },
    {
        "name": "Carian Glintblade Staff",
        "image": "Weapons/Carian Glintblade Staff.png",
        "primaryColor": "#968e91",
        "secondaryColors": [
            "#5c565b",
            "#57545a"
        ]
    },
    {
        "name": "Carian Glintstone Staff",
        "image": "Weapons/Carian Glintstone Staff.png",
        "primaryColor": "#5d5050",
        "secondaryColors": [
            "#584f51",
            "#453936"
        ]
    },
    {
        "name": "Carian Knight's Sword",
        "image": "Weapons/Carian Knight's Sword.png",
        "primaryColor": "#abb6ca",
        "secondaryColors": [
            "#99989b",
            "#5e5856"
        ]
    },
    {
        "name": "Carian Regal Scepter",
        "image": "Weapons/Carian Regal Scepter.png",
        "primaryColor": "#90949b",
        "secondaryColors": [
            "#69748b",
            "#67676a"
        ]
    },
    {
        "name": "Celebrant's Cleaver",
        "image": "Weapons/Celebrant's Cleaver.png",
        "primaryColor": "#b8c3d3",
        "secondaryColors": [
            "#acb7c7",
            "#979aa4"
        ]
    },
    {
        "name": "Celebrant's Rib-Rake",
        "image": "Weapons/Celebrant's Rib-Rake.png",
        "primaryColor": "#a29996",
        "secondaryColors": [
            "#655e5f",
            "#625e61"
        ]
    },
    {
        "name": "Celebrant's Sickle",
        "image": "Weapons/Celebrant's Sickle.png",
        "primaryColor": "#a8998f",
        "secondaryColors": [
            "#a08a6f",
            "#897562"
        ]
    },
    {
        "name": "Celebrant's Skull",
        "image": "Weapons/Celebrant's Skull.png",
        "primaryColor": "#9f8a74",
        "secondaryColors": [
            "#89735e",
            "#665a52"
        ]
    },
    {
        "name": "Chainlink Flail",
        "image": "Weapons/Chainlink Flail.png",
        "primaryColor": "#887269",
        "secondaryColors": [
            "#5f5150",
            "#57433c"
        ]
    },
    {
        "name": "Cinquedea",
        "image": "Weapons/Cinquedea.png",
        "primaryColor": "#92928f",
        "secondaryColors": [
            "#565758",
            "#564733"
        ]
    },
    {
        "name": "Cipher Pita",
        "image": "Weapons/Cipher Pita.png",
        "primaryColor": "#e7e2d7",
        "secondaryColors": [
            "#dfd9b7",
            "#d5cbb7"
        ]
    },
    {
        "name": "Clawmark Seal",
        "image": "Weapons/Clawmark Seal.png",
        "primaryColor": "#a39e93",
        "secondaryColors": [
            "#8c8578",
            "#5e5b59"
        ]
    },
    {
        "name": "Clayman's Harpoon",
        "image": "Weapons/Clayman's Harpoon.png",
        "primaryColor": "#5a504c",
        "secondaryColors": [
            "#584639",
            "#473933"
        ]
    },
    {
        "name": "Claymore",
        "image": "Weapons/Claymore.png",
        "primaryColor": "#a89f99",
        "secondaryColors": [
            "#867568",
            "#6a6057"
        ]
    },
    {
        "name": "Cleanrot Knight's Sword",
        "image": "Weapons/Cleanrot Knight's Sword.png",
        "primaryColor": "#95949a",
        "secondaryColors": [
            "#6d645e",
            "#564437"
        ]
    },
    {
        "name": "Cleanrot Spear",
        "image": "Weapons/Cleanrot Spear.png",
        "primaryColor": "#63564f",
        "secondaryColors": [
            "#504d54",
            "#584637"
        ]
    },
    {
        "name": "Clinging Bone",
        "image": "Weapons/Clinging Bone.png",
        "primaryColor": "#b18963",
        "secondaryColors": [
            "#966d4f",
            "#725849"
        ]
    },
    {
        "name": "Club",
        "image": "Weapons/Club.png",
        "primaryColor": "#877160",
        "secondaryColors": [
            "#65574c",
            "#55453a"
        ]
    },
    {
        "name": "Coded Sword",
        "image": "Weapons/Coded Sword.png",
        "primaryColor": "#efe7de",
        "secondaryColors": [
            "#d8d1b6",
            "#ccc4b4"
        ]
    },
    {
        "name": "Commander's Standard",
        "image": "Weapons/Commander's Standard.png",
        "primaryColor": "#67625c",
        "secondaryColors": [
            "#62564d",
            "#554735"
        ]
    },
    {
        "name": "Composite Bow",
        "image": "Weapons/Composite Bow.png",
        "primaryColor": "#665c50",
        "secondaryColors": [
            "#62584b",
            "#5a5352"
        ]
    },
    {
        "name": "Cranial Vessel Candlestand",
        "image": "Weapons/Cranial Vessel Candlestand.png",
        "primaryColor": "#56525c",
        "secondaryColors": [
            "#433d46",
            "#433735"
        ]
    },
    {
        "name": "Crepus's Black-Key Crossbow",
        "image": "Weapons/Crepus's Black-Key Crossbow.png",
        "primaryColor": "#6c7687",
        "secondaryColors": [
            "#595b60",
            "#56575c"
        ]
    },
    {
        "name": "Crescent Moon Axe",
        "image": "Weapons/Crescent Moon Axe.png",
        "primaryColor": "#aba39a",
        "secondaryColors": [
            "#685a50",
            "#54453a"
        ]
    },
    {
        "name": "Cross-Naginata",
        "image": "Weapons/Cross-Naginata.png",
        "primaryColor": "#8c6853",
        "secondaryColors": [
            "#69584d",
            "#6a4837"
        ]
    },
    {
        "name": "Crystal Knife",
        "image": "Weapons/Crystal Knife.png",
        "primaryColor": "#648d9f",
        "secondaryColors": [
            "#52748a",
            "#545e60"
        ]
    },
    {
        "name": "Crystal Spear",
        "image": "Weapons/Crystal Spear.png",
        "primaryColor": "#7488a9",
        "secondaryColors": [
            "#63739f",
            "#5e6e92"
        ]
    },
    {
        "name": "Crystal Staff",
        "image": "Weapons/Crystal Staff.png",
        "primaryColor": "#4c649e",
        "secondaryColors": [
            "#314d9f",
            "#243a96"
        ]
    },
    {
        "name": "Crystal Sword",
        "image": "Weapons/Crystal Sword.png",
        "primaryColor": "#576396",
        "secondaryColors": [
            "#48506a",
            "#3b436c"
        ]
    },
    {
        "name": "Curved Club",
        "image": "Weapons/Curved Club.png",
        "primaryColor": "#887463",
        "secondaryColors": [
            "#61554e",
            "#524539"
        ]
    },
    {
        "name": "Curved Great Club",
        "image": "Weapons/Curved Great Club.png",
        "primaryColor": "#887660",
        "secondaryColors": [
            "#63564c",
            "#534739"
        ]
    },
    {
        "name": "Dagger",
        "image": "Weapons/Dagger.png",
        "primaryColor": "#8f95a4",
        "secondaryColors": [
            "#625d5b",
            "#4f453b"
        ]
    },
    {
        "name": "Dark Moon Greatsword",
        "image": "Weapons/Dark Moon Greatsword.png",
        "primaryColor": "#5b7587",
        "secondaryColors": [
            "#4c5967",
            "#37475a"
        ]
    },
    {
        "name": "Death Ritual Spear",
        "image": "Weapons/Death Ritual Spear.png",
        "primaryColor": "#535663",
        "secondaryColors": [
            "#4f515e",
            "#515158"
        ]
    },
    {
        "name": "Death's Poker",
        "image": "Weapons/Death's Poker.png",
        "primaryColor": "#a68c72",
        "secondaryColors": [
            "#8a7362",
            "#685b54"
        ]
    },
    {
        "name": "Demi-Human Queen's Staff",
        "image": "Weapons/Demi-Human Queen's Staff.png",
        "primaryColor": "#969092",
        "secondaryColors": [
            "#5c5b61",
            "#5c5a60"
        ]
    },
    {
        "name": "Devourer's Scepter",
        "image": "Weapons/Devourer's Scepter.png",
        "primaryColor": "#93979c",
        "secondaryColors": [
            "#687288",
            "#545861"
        ]
    },
    {
        "name": "Digger's Staff",
        "image": "Weapons/Digger's Staff.png",
        "primaryColor": "#5e5b57",
        "secondaryColors": [
            "#565553",
            "#4f525d"
        ]
    },
    {
        "name": "Dismounter",
        "image": "Weapons/Dismounter.png",
        "primaryColor": "#929594",
        "secondaryColors": [
            "#5b554f",
            "#4d453a"
        ]
    },
    {
        "name": "Dragon Communion Seal",
        "image": "Weapons/Dragon Communion Seal.png",
        "primaryColor": "#696666",
        "secondaryColors": [
            "#8c2b28",
            "#912824"
        ]
    },
    {
        "name": "Dragon Greatclaw",
        "image": "Weapons/Dragon Greatclaw.png",
        "primaryColor": "#a08a71",
        "secondaryColors": [
            "#8a735f",
            "#645751"
        ]
    },
    {
        "name": "Dragon Halberd",
        "image": "Weapons/Dragon Halberd.png",
        "primaryColor": "#979595",
        "secondaryColors": [
            "#615d59",
            "#5c5a5a"
        ]
    },
    {
        "name": "Dragon King's Cragblade",
        "image": "Weapons/Dragon King's Cragblade.png",
        "primaryColor": "#9b896d",
        "secondaryColors": [
            "#8a765c",
            "#666563"
        ]
    },
    {
        "name": "Dragonscale Blade",
        "image": "Weapons/Dragonscale Blade.png",
        "primaryColor": "#635f60",
        "secondaryColors": [
            "#5b575a",
            "#575557"
        ]
    },
    {
        "name": "Duelist Greataxe",
        "image": "Weapons/Duelist Greataxe.png",
        "primaryColor": "#565155",
        "secondaryColors": [
            "#505157",
            "#443d42"
        ]
    },
    {
        "name": "Eclipse Shotel",
        "image": "Weapons/Eclipse Shotel.png",
        "primaryColor": "#91959f",
        "secondaryColors": [
            "#57585a",
            "#575556"
        ]
    },
    {
        "name": "Eleonora's Poleblade",
        "image": "Weapons/Eleonora's Poleblade.png",
        "primaryColor": "#5c544a",
        "secondaryColors": [
            "#591e1b",
            "#501b1b"
        ]
    },
    {
        "name": "Envoy's Greathorn",
        "image": "Weapons/Envoy's Greathorn.png",
        "primaryColor": "#a39163",
        "secondaryColors": [
            "#8d764c",
            "#896c39"
        ]
    },
    {
        "name": "Envoy's Horn",
        "image": "Weapons/Envoy's Horn.png",
        "primaryColor": "#a49163",
        "secondaryColors": [
            "#8d754b",
            "#8b6a33"
        ]
    },
    {
        "name": "Envoy's Long Horn",
        "image": "Weapons/Envoy's Long Horn.png",
        "primaryColor": "#a08e67",
        "secondaryColors": [
            "#8a754d",
            "#746547"
        ]
    },
    {
        "name": "Erdsteel Dagger",
        "image": "Weapons/Erdsteel Dagger.png",
        "primaryColor": "#88755a",
        "secondaryColors": [
            "#695c4e",
            "#5c4b37"
        ]
    },
    {
        "name": "Erdtree Bow",
        "image": "Weapons/Erdtree Bow.png",
        "primaryColor": "#a8998a",
        "secondaryColors": [
            "#9d8973",
            "#8a7660"
        ]
    },
    {
        "name": "Erdtree Greatbow",
        "image": "Weapons/Erdtree Greatbow.png",
        "primaryColor": "#89755e",
        "secondaryColors": [
            "#675b4e",
            "#584937"
        ]
    },
    {
        "name": "Erdtree Seal",
        "image": "Weapons/Erdtree Seal.png",
        "primaryColor": "#fdc875",
        "secondaryColors": [
            "#fcc774",
            "#ebce5d"
        ]
    },
    {
        "name": "Estoc",
        "image": "Weapons/Estoc.png",
        "primaryColor": "#dce5f1",
        "secondaryColors": [
            "#8f929c",
            "#655f5d"
        ]
    },
    {
        "name": "Executioner's Greataxe",
        "image": "Weapons/Executioner's Greataxe.png",
        "primaryColor": "#595153",
        "secondaryColors": [
            "#5d4d49",
            "#5d4439"
        ]
    },
    {
        "name": "Falchion",
        "image": "Weapons/Falchion.png",
        "primaryColor": "#9b9899",
        "secondaryColors": [
            "#8f8577",
            "#847a6c"
        ]
    },
    {
        "name": "Fallingstar Beast Jaw",
        "image": "Weapons/Fallingstar Beast Jaw.png",
        "primaryColor": "#9b9997",
        "secondaryColors": [
            "#5a595b",
            "#4f5360"
        ]
    },
    {
        "name": "Family Heads",
        "image": "Weapons/Family Heads.png",
        "primaryColor": "#969491",
        "secondaryColors": [
            "#636055",
            "#554837"
        ]
    },
    {
        "name": "Finger Seal",
        "image": "Weapons/Finger Seal.png",
        "primaryColor": "#959091",
        "secondaryColors": [
            "#827a76",
            "#645e5c"
        ]
    },
    {
        "name": "Flail",
        "image": "Weapons/Flail.png",
        "primaryColor": "#916d55",
        "secondaryColors": [
            "#645552",
            "#584f52"
        ]
    },
    {
        "name": "Flamberge",
        "image": "Weapons/Flamberge.png",
        "primaryColor": "#5b5a5c",
        "secondaryColors": [
            "#5c5754",
            "#4e453a"
        ]
    },
    {
        "name": "Flowing Curved Sword",
        "image": "Weapons/Flowing Curved Sword.png",
        "primaryColor": "#9c9e9e",
        "secondaryColors": [
            "#605c52",
            "#4f4838"
        ]
    },
    {
        "name": "Forked Greatsword",
        "image": "Weapons/Forked Greatsword.png",
        "primaryColor": "#5a5756",
        "secondaryColors": [
            "#55555a",
            "#4a463b"
        ]
    },
    {
        "name": "Forked Hatchet",
        "image": "Weapons/Forked Hatchet.png",
        "primaryColor": "#a08a71",
        "secondaryColors": [
            "#565455",
            "#4f4539"
        ]
    },
    {
        "name": "Frenzied Flame Seal",
        "image": "Weapons/Frenzied Flame Seal.png",
        "primaryColor": "#f0d22e",
        "secondaryColors": [
            "#e6a525",
            "#f95d27"
        ]
    },
    {
        "name": "Frozen Needle",
        "image": "Weapons/Frozen Needle.png",
        "primaryColor": "#9099a6",
        "secondaryColors": [
            "#6597b0",
            "#6293ad"
        ]
    },
    {
        "name": "Full Moon Crossbow",
        "image": "Weapons/Full Moon Crossbow.png",
        "primaryColor": "#a1a39b",
        "secondaryColors": [
            "#988b75",
            "#686059"
        ]
    },
    {
        "name": "Gargoyle's Black Axe",
        "image": "Weapons/Gargoyle's Black Axe.png",
        "primaryColor": "#8b6f5b",
        "secondaryColors": [
            "#61514e",
            "#604735"
        ]
    },
    {
        "name": "Gargoyle's Black Blades",
        "image": "Weapons/Gargoyle's Black Blades.png",
        "primaryColor": "#65574b",
        "secondaryColors": [
            "#594838",
            "#483a2c"
        ]
    },
    {
        "name": "Gargoyle's Black Halberd",
        "image": "Weapons/Gargoyle's Black Halberd.png",
        "primaryColor": "#ac8a64",
        "secondaryColors": [
            "#926f51",
            "#986238"
        ]
    },
    {
        "name": "Gargoyle's Blackblade",
        "image": "Weapons/Gargoyle's Blackblade.png",
        "primaryColor": "#948875",
        "secondaryColors": [
            "#635a53",
            "#50443a"
        ]
    },
    {
        "name": "Gargoyle's Great Axe",
        "image": "Weapons/Gargoyle's Great Axe.png",
        "primaryColor": "#8a715d",
        "secondaryColors": [
            "#6a574e",
            "#644a32"
        ]
    },
    {
        "name": "Gargoyle's Greatsword",
        "image": "Weapons/Gargoyle's Greatsword.png",
        "primaryColor": "#98744c",
        "secondaryColors": [
            "#5d5a5a",
            "#664a32"
        ]
    },
    {
        "name": "Gargoyle's Halberd",
        "image": "Weapons/Gargoyle's Halberd.png",
        "primaryColor": "#ab8d6b",
        "secondaryColors": [
            "#937053",
            "#95562e"
        ]
    },
    {
        "name": "Gargoyle's Twinblade",
        "image": "Weapons/Gargoyle's Twinblade.png",
        "primaryColor": "#926e50",
        "secondaryColors": [
            "#5e5652",
            "#604835"
        ]
    },
    {
        "name": "Gelmir Glintstone Staff",
        "image": "Weapons/Gelmir Glintstone Staff.png",
        "primaryColor": "#8d6e49",
        "secondaryColors": [
            "#866339",
            "#686160"
        ]
    },
    {
        "name": "Ghiza's Wheel",
        "image": "Weapons/Ghiza's Wheel.png",
        "primaryColor": "#a19c8f",
        "secondaryColors": [
            "#5e5853",
            "#4e453a"
        ]
    },
    {
        "name": "Ghostflame Torch",
        "image": "Weapons/Ghostflame Torch.png",
        "primaryColor": "#1e1410",
        "secondaryColors": [
            "#739ba1",
            "#758a8e"
        ]
    },
    {
        "name": "Giant's Red Braid",
        "image": "Weapons/Giant's Red Braid.png",
        "primaryColor": "#8e5434",
        "secondaryColors": [
            "#5c5c54",
            "#664633"
        ]
    },
    {
        "name": "Giant's Seal",
        "image": "Weapons/Giant's Seal.png",
        "primaryColor": "#93582e",
        "secondaryColors": [
            "#5e524f",
            "#6b462b"
        ]
    },
    {
        "name": "Giant-Crusher - MENU_Knowledge_10891",
        "image": "Weapons/Giant-Crusher - MENU_Knowledge_10891.png",
        "primaryColor": "#97918e",
        "secondaryColors": [
            "#5b5452",
            "#4f433c"
        ]
    },
    {
        "name": "Glaive",
        "image": "Weapons/Glaive.png",
        "primaryColor": "#5b5655",
        "secondaryColors": [
            "#525255",
            "#4b4339"
        ]
    },
    {
        "name": "Glintstone Kris",
        "image": "Weapons/Glintstone Kris.png",
        "primaryColor": "#978a65",
        "secondaryColors": [
            "#877753",
            "#686456"
        ]
    },
    {
        "name": "Glintstone Staff",
        "image": "Weapons/Glintstone Staff.png",
        "primaryColor": "#8f6a63",
        "secondaryColors": [
            "#67504f",
            "#655053"
        ]
    },
    {
        "name": "Godskin Peeler",
        "image": "Weapons/Godskin Peeler.png",
        "primaryColor": "#9f9a98",
        "secondaryColors": [
            "#8c8376",
            "#82786b"
        ]
    },
    {
        "name": "Godskin Stitcher",
        "image": "Weapons/Godskin Stitcher.png",
        "primaryColor": "#9c9a99",
        "secondaryColors": [
            "#675f55",
            "#635e55"
        ]
    },
    {
        "name": "Godslayer's Greatsword",
        "image": "Weapons/Godslayer's Greatsword.png",
        "primaryColor": "#999595",
        "secondaryColors": [
            "#635d5b",
            "#5e5a57"
        ]
    },
    {
        "name": "Godslayer's Seal",
        "image": "Weapons/Godslayer's Seal.png",
        "primaryColor": "#9d968b",
        "secondaryColors": [
            "#8f8577",
            "#847a6c"
        ]
    },
    {
        "name": "Golden Epitaph",
        "image": "Weapons/Golden Epitaph.png",
        "primaryColor": "#877159",
        "secondaryColors": [
            "#6f5e4c",
            "#604933"
        ]
    },
    {
        "name": "Golden Halberd",
        "image": "Weapons/Golden Halberd.png",
        "primaryColor": "#887561",
        "secondaryColors": [
            "#6c5c4c",
            "#5b4733"
        ]
    },
    {
        "name": "Golden Order Greatsword",
        "image": "Weapons/Golden Order Greatsword.png",
        "primaryColor": "#716248",
        "secondaryColors": [
            "#645131",
            "#5f5325"
        ]
    },
    {
        "name": "Golden Order Seal",
        "image": "Weapons/Golden Order Seal.png",
        "primaryColor": "#dea65f",
        "secondaryColors": [
            "#dc9524",
            "#6e641b"
        ]
    },
    {
        "name": "Golem Greatbow",
        "image": "Weapons/Golem Greatbow.png",
        "primaryColor": "#615a55",
        "secondaryColors": [
            "#5c504d",
            "#4b433c"
        ]
    },
    {
        "name": "Golem's Halberd",
        "image": "Weapons/Golem's Halberd.png",
        "primaryColor": "#535152",
        "secondaryColors": [
            "#4e515e",
            "#383a43"
        ]
    },
    {
        "name": "Grafted Blade Greatsword",
        "image": "Weapons/Grafted Blade Greatsword.png",
        "primaryColor": "#877063",
        "secondaryColors": [
            "#5d5253",
            "#55443a"
        ]
    },
    {
        "name": "Grafted Dragon",
        "image": "Weapons/Grafted Dragon.png",
        "primaryColor": "#8b6957",
        "secondaryColors": [
            "#64534e",
            "#614837"
        ]
    },
    {
        "name": "Grave Scythe",
        "image": "Weapons/Grave Scythe.png",
        "primaryColor": "#89715c",
        "secondaryColors": [
            "#61554f",
            "#55453b"
        ]
    },
    {
        "name": "Gravel Stone Seal",
        "image": "Weapons/Gravel Stone Seal.png",
        "primaryColor": "#97918e",
        "secondaryColors": [
            "#8b7657",
            "#645d56"
        ]
    },
    {
        "name": "Great Club",
        "image": "Weapons/Great Club.png",
        "primaryColor": "#867865",
        "secondaryColors": [
            "#5f5750",
            "#514737"
        ]
    },
    {
        "name": "Great Knife",
        "image": "Weapons/Great Knife.png",
        "primaryColor": "#8e8d8e",
        "secondaryColors": [
            "#84796f",
            "#635d55"
        ]
    },
    {
        "name": "Great Mace",
        "image": "Weapons/Great Mace.png",
        "primaryColor": "#9b9696",
        "secondaryColors": [
            "#625956",
            "#534538"
        ]
    },
    {
        "name": "Great Omenkiller Cleaver",
        "image": "Weapons/Great Omenkiller Cleaver.png",
        "primaryColor": "#b0998a",
        "secondaryColors": [
            "#9d8678",
            "#8a7467"
        ]
    },
    {
        "name": "Great Stars",
        "image": "Weapons/Great Stars.png",
        "primaryColor": "#8a6556",
        "secondaryColors": [
            "#6c524a",
            "#64463a"
        ]
    },
    {
        "name": "Great \u00c9p\u00e9e",
        "image": "Weapons/Great \u00c9p\u00e9e.png",
        "primaryColor": "#5e5958",
        "secondaryColors": [
            "#50525b",
            "#505055"
        ]
    },
    {
        "name": "Greataxe",
        "image": "Weapons/Greataxe.png",
        "primaryColor": "#989a99",
        "secondaryColors": [
            "#635b53",
            "#514539"
        ]
    },
    {
        "name": "Greatbow",
        "image": "Weapons/Greatbow.png",
        "primaryColor": "#5b4e57",
        "secondaryColors": [
            "#523634",
            "#4e3230"
        ]
    },
    {
        "name": "Greathorn Hammer",
        "image": "Weapons/Greathorn Hammer.png",
        "primaryColor": "#887169",
        "secondaryColors": [
            "#605451",
            "#544439"
        ]
    },
    {
        "name": "Greatsword",
        "image": "Weapons/Greatsword.png",
        "primaryColor": "#8f93a3",
        "secondaryColors": [
            "#575256",
            "#4b423a"
        ]
    },
    {
        "name": "Grossmesser",
        "image": "Weapons/Grossmesser.png",
        "primaryColor": "#70695a",
        "secondaryColors": [
            "#5c544a",
            "#4e4439"
        ]
    },
    {
        "name": "Guardian's Swordspear",
        "image": "Weapons/Guardian's Swordspear.png",
        "primaryColor": "#6c6b5e",
        "secondaryColors": [
            "#6b5d47",
            "#5f4d34"
        ]
    },
    {
        "name": "Halberd",
        "image": "Weapons/Halberd.png",
        "primaryColor": "#67594b",
        "secondaryColors": [
            "#554f58",
            "#54443a"
        ]
    },
    {
        "name": "Halo Scythe",
        "image": "Weapons/Halo Scythe.png",
        "primaryColor": "#524f51",
        "secondaryColors": [
            "#433734",
            "#313848"
        ]
    },
    {
        "name": "Hammer",
        "image": "Weapons/Hammer.png",
        "primaryColor": "#a09794",
        "secondaryColors": [
            "#897569",
            "#645854"
        ]
    },
    {
        "name": "Hand Axe",
        "image": "Weapons/Hand Axe.png",
        "primaryColor": "#9c9799",
        "secondaryColors": [
            "#897268",
            "#58565c"
        ]
    },
    {
        "name": "Hand Ballista",
        "image": "Weapons/Hand Ballista.png",
        "primaryColor": "#b09c89",
        "secondaryColors": [
            "#a18a77",
            "#8a7666"
        ]
    },
    {
        "name": "Hand of Malenia",
        "image": "Weapons/Hand of Malenia.png",
        "primaryColor": "#999a93",
        "secondaryColors": [
            "#898374",
            "#827967"
        ]
    },
    {
        "name": "Harp Bow",
        "image": "Weapons/Harp Bow.png",
        "primaryColor": "#906755",
        "secondaryColors": [
            "#6e6562",
            "#6b6360"
        ]
    },
    {
        "name": "Heavy Crossbow",
        "image": "Weapons/Heavy Crossbow.png",
        "primaryColor": "#949ca2",
        "secondaryColors": [
            "#625956",
            "#534737"
        ]
    },
    {
        "name": "Helphen's Steeple",
        "image": "Weapons/Helphen's Steeple.png",
        "primaryColor": "#0e0b0d",
        "secondaryColors": [
            "#535257",
            "#4d515d"
        ]
    },
    {
        "name": "Highland Axe",
        "image": "Weapons/Highland Axe.png",
        "primaryColor": "#89725b",
        "secondaryColors": [
            "#605956",
            "#5a4837"
        ]
    },
    {
        "name": "Hookclaws",
        "image": "Weapons/Hookclaws.png",
        "primaryColor": "#bfd0dc",
        "secondaryColors": [
            "#a2b4ca",
            "#7d6050"
        ]
    },
    {
        "name": "Horn Bow",
        "image": "Weapons/Horn Bow.png",
        "primaryColor": "#956557",
        "secondaryColors": [
            "#695b54",
            "#6b5854"
        ]
    },
    {
        "name": "Hoslow's Petal Whip",
        "image": "Weapons/Hoslow's Petal Whip.png",
        "primaryColor": "#95969b",
        "secondaryColors": [
            "#5c5d61",
            "#55585b"
        ]
    },
    {
        "name": "Icerind Hatchet",
        "image": "Weapons/Icerind Hatchet.png",
        "primaryColor": "#959fa6",
        "secondaryColors": [
            "#79858e",
            "#6c7984"
        ]
    },
    {
        "name": "Inquisitor's Girandole",
        "image": "Weapons/Inquisitor's Girandole.png",
        "primaryColor": "#a09c90",
        "secondaryColors": [
            "#6a6455",
            "#646258"
        ]
    },
    {
        "name": "Inseparable Sword",
        "image": "Weapons/Inseparable Sword.png",
        "primaryColor": "#969694",
        "secondaryColors": [
            "#8f8574",
            "#86765b"
        ]
    },
    {
        "name": "Iron Ball",
        "image": "Weapons/Iron Ball.png",
        "primaryColor": "#737c96",
        "secondaryColors": [
            "#9d979c",
            "#5d565a"
        ]
    },
    {
        "name": "Iron Cleaver",
        "image": "Weapons/Iron Cleaver.png",
        "primaryColor": "#58595e",
        "secondaryColors": [
            "#555357",
            "#423b39"
        ]
    },
    {
        "name": "Iron Greatsword",
        "image": "Weapons/Iron Greatsword.png",
        "primaryColor": "#6a728c",
        "secondaryColors": [
            "#55545d",
            "#585357"
        ]
    },
    {
        "name": "Iron Spear",
        "image": "Weapons/Iron Spear.png",
        "primaryColor": "#5b514f",
        "secondaryColors": [
            "#4a464c",
            "#4a423b"
        ]
    },
    {
        "name": "Ivory Sickle",
        "image": "Weapons/Ivory Sickle.png",
        "primaryColor": "#cbb097",
        "secondaryColors": [
            "#a69792",
            "#ac8b71"
        ]
    },
    {
        "name": "Jar Cannon",
        "image": "Weapons/Jar Cannon.png",
        "primaryColor": "#aba18f",
        "secondaryColors": [
            "#988a73",
            "#877762"
        ]
    },
    {
        "name": "Jawbone Axe",
        "image": "Weapons/Jawbone Axe.png",
        "primaryColor": "#a19a94",
        "secondaryColors": [
            "#887569",
            "#635b56"
        ]
    },
    {
        "name": "Katar",
        "image": "Weapons/Katar.png",
        "primaryColor": "#979a92",
        "secondaryColors": [
            "#857761",
            "#626357"
        ]
    },
    {
        "name": "Knight's Greatsword",
        "image": "Weapons/Knight's Greatsword.png",
        "primaryColor": "#676561",
        "secondaryColors": [
            "#5d5a59",
            "#555255"
        ]
    },
    {
        "name": "Lance",
        "image": "Weapons/Lance.png",
        "primaryColor": "#9098a4",
        "secondaryColors": [
            "#6f7685",
            "#58585e"
        ]
    },
    {
        "name": "Large Club",
        "image": "Weapons/Large Club.png",
        "primaryColor": "#877463",
        "secondaryColors": [
            "#61564d",
            "#51443b"
        ]
    },
    {
        "name": "Lazuli Glintstone Sword",
        "image": "Weapons/Lazuli Glintstone Sword.png",
        "primaryColor": "#565d99",
        "secondaryColors": [
            "#615753",
            "#4d443c"
        ]
    },
    {
        "name": "Light Crossbow",
        "image": "Weapons/Light Crossbow.png",
        "primaryColor": "#9a9598",
        "secondaryColors": [
            "#8e685a",
            "#675957"
        ]
    },
    {
        "name": "Lion Greatbow",
        "image": "Weapons/Lion Greatbow.png",
        "primaryColor": "#64656b",
        "secondaryColors": [
            "#676055",
            "#5f5b55"
        ]
    },
    {
        "name": "Longbow",
        "image": "Weapons/Longbow.png",
        "primaryColor": "#8a8375",
        "secondaryColors": [
            "#946e56",
            "#6f6862"
        ]
    },
    {
        "name": "Longhaft Axe",
        "image": "Weapons/Longhaft Axe.png",
        "primaryColor": "#585c5e",
        "secondaryColors": [
            "#4f4d4f",
            "#423c3b"
        ]
    },
    {
        "name": "Longsword",
        "image": "Weapons/Longsword.png",
        "primaryColor": "#9999a2",
        "secondaryColors": [
            "#5f5d5e",
            "#605b5c"
        ]
    },
    {
        "name": "Lordsworn's Greatsword",
        "image": "Weapons/Lordsworn's Greatsword.png",
        "primaryColor": "#545053",
        "secondaryColors": [
            "#544f52",
            "#4c4239"
        ]
    },
    {
        "name": "Lordsworn's Straight Sword",
        "image": "Weapons/Lordsworn's Straight Sword.png",
        "primaryColor": "#90919b",
        "secondaryColors": [
            "#645a54",
            "#534638"
        ]
    },
    {
        "name": "Loretta's War Sickle",
        "image": "Weapons/Loretta's War Sickle.png",
        "primaryColor": "#62625e",
        "secondaryColors": [
            "#575554",
            "#535354"
        ]
    },
    {
        "name": "Lucerne",
        "image": "Weapons/Lucerne.png",
        "primaryColor": "#635a51",
        "secondaryColors": [
            "#57535b",
            "#5c4f48"
        ]
    },
    {
        "name": "Lusat's Glintstone Staff",
        "image": "Weapons/Lusat's Glintstone Staff.png",
        "primaryColor": "#6b6663",
        "secondaryColors": [
            "#6e6460",
            "#5f585b"
        ]
    },
    {
        "name": "Mace",
        "image": "Weapons/Mace.png",
        "primaryColor": "#a19f9d",
        "secondaryColors": [
            "#5c5956",
            "#514639"
        ]
    },
    {
        "name": "Magma Blade",
        "image": "Weapons/Magma Blade.png",
        "primaryColor": "#efa754",
        "secondaryColors": [
            "#ea9629",
            "#dc5a25"
        ]
    },
    {
        "name": "Magma Whip Candlestick",
        "image": "Weapons/Magma Whip Candlestick.png",
        "primaryColor": "#eb982f",
        "secondaryColors": [
            "#df5a26",
            "#8e6e52"
        ]
    },
    {
        "name": "Magma Wyrm's Scalesword",
        "image": "Weapons/Magma Wyrm's Scalesword.png",
        "primaryColor": "#515357",
        "secondaryColors": [
            "#4c494a",
            "#423b3b"
        ]
    },
    {
        "name": "Maliketh's Black Blade",
        "image": "Weapons/Maliketh's Black Blade.png",
        "primaryColor": "#150e07",
        "secondaryColors": [
            "#575754",
            "#4b4539"
        ]
    },
    {
        "name": "Mantis Blade",
        "image": "Weapons/Mantis Blade.png",
        "primaryColor": "#090604",
        "secondaryColors": [
            "#4d4d4e",
            "#4a4b4e"
        ]
    },
    {
        "name": "Marais Executioner's Sword",
        "image": "Weapons/Marais Executioner's Sword.png",
        "primaryColor": "#605857",
        "secondaryColors": [
            "#4c2924",
            "#50433c"
        ]
    },
    {
        "name": "Marika's Hammer",
        "image": "Weapons/Marika's Hammer.png",
        "primaryColor": "#a09b8a",
        "secondaryColors": [
            "#918973",
            "#5d5a54"
        ]
    },
    {
        "name": "Meteoric Ore Blade",
        "image": "Weapons/Meteoric Ore Blade.png",
        "primaryColor": "#6d6852",
        "secondaryColors": [
            "#60635f",
            "#514834"
        ]
    },
    {
        "name": "Meteorite Staff",
        "image": "Weapons/Meteorite Staff.png",
        "primaryColor": "#666059",
        "secondaryColors": [
            "#685c51",
            "#65584d"
        ]
    },
    {
        "name": "Miquellan Knight's Sword",
        "image": "Weapons/Miquellan Knight's Sword.png",
        "primaryColor": "#64615d",
        "secondaryColors": [
            "#5d5751",
            "#524a36"
        ]
    },
    {
        "name": "Misbegotten Shortbow",
        "image": "Weapons/Misbegotten Shortbow.png",
        "primaryColor": "#a2998d",
        "secondaryColors": [
            "#646261",
            "#625d5c"
        ]
    },
    {
        "name": "Mis\u00e9ricorde",
        "image": "Weapons/Mis\u00e9ricorde.png",
        "primaryColor": "#677189",
        "secondaryColors": [
            "#5c5d64",
            "#515a6a"
        ]
    },
    {
        "name": "Mohgwyn's Sacred Spear",
        "image": "Weapons/Mohgwyn's Sacred Spear.png",
        "primaryColor": "#5a5553",
        "secondaryColors": [
            "#514f4f",
            "#574835"
        ]
    },
    {
        "name": "Monk's Flameblade",
        "image": "Weapons/Monk's Flameblade.png",
        "primaryColor": "#5a5453",
        "secondaryColors": [
            "#585458",
            "#4b423b"
        ]
    },
    {
        "name": "Monk's Flamemace",
        "image": "Weapons/Monk's Flamemace.png",
        "primaryColor": "#969398",
        "secondaryColors": [
            "#605b5d",
            "#4f433c"
        ]
    },
    {
        "name": "Moonveil",
        "image": "Weapons/Moonveil.png",
        "primaryColor": "#a69e8d",
        "secondaryColors": [
            "#97958d",
            "#5f6160"
        ]
    },
    {
        "name": "Morgott's Cursed Sword",
        "image": "Weapons/Morgott's Cursed Sword.png",
        "primaryColor": "#56565c",
        "secondaryColors": [
            "#4d4934",
            "#50344f"
        ]
    },
    {
        "name": "Morning Star",
        "image": "Weapons/Morning Star.png",
        "primaryColor": "#999a9b",
        "secondaryColors": [
            "#6e7886",
            "#616060"
        ]
    },
    {
        "name": "Nagakiba",
        "image": "Weapons/Nagakiba.png",
        "primaryColor": "#ede7d5",
        "secondaryColors": [
            "#a19b95",
            "#545457"
        ]
    },
    {
        "name": "Nightrider Flail",
        "image": "Weapons/Nightrider Flail.png",
        "primaryColor": "#5a5d60",
        "secondaryColors": [
            "#545455",
            "#413c3a"
        ]
    },
    {
        "name": "Nightrider Glaive",
        "image": "Weapons/Nightrider Glaive.png",
        "primaryColor": "#616162",
        "secondaryColors": [
            "#4e5056",
            "#504a4b"
        ]
    },
    {
        "name": "Noble's Estoc",
        "image": "Weapons/Noble's Estoc.png",
        "primaryColor": "#9a8c5a",
        "secondaryColors": [
            "#877646",
            "#876f39"
        ]
    },
    {
        "name": "Noble's Slender Sword",
        "image": "Weapons/Noble's Slender Sword.png",
        "primaryColor": "#908a6c",
        "secondaryColors": [
            "#847954",
            "#6f6a55"
        ]
    },
    {
        "name": "Nox Flowing Hammer",
        "image": "Weapons/Nox Flowing Hammer.png",
        "primaryColor": "#909ba5",
        "secondaryColors": [
            "#798696",
            "#65748a"
        ]
    },
    {
        "name": "Nox Flowing Sword",
        "image": "Weapons/Nox Flowing Sword.png",
        "primaryColor": "#8e97a1",
        "secondaryColors": [
            "#5c708f",
            "#5a5e60"
        ]
    },
    {
        "name": "Omen Cleaver",
        "image": "Weapons/Omen Cleaver.png",
        "primaryColor": "#93939e",
        "secondaryColors": [
            "#5e5657",
            "#54453a"
        ]
    },
    {
        "name": "Onyx Lord's Greatsword",
        "image": "Weapons/Onyx Lord's Greatsword.png",
        "primaryColor": "#a49a95",
        "secondaryColors": [
            "#6d6055",
            "#594833"
        ]
    },
    {
        "name": "Ordovis's Greatsword",
        "image": "Weapons/Ordovis's Greatsword.png",
        "primaryColor": "#936751",
        "secondaryColors": [
            "#6f5349",
            "#6b4635"
        ]
    },
    {
        "name": "Ornamental Straight Sword",
        "image": "Weapons/Ornamental Straight Sword.png",
        "primaryColor": "#918f93",
        "secondaryColors": [
            "#857260",
            "#6f6050"
        ]
    },
    {
        "name": "Parrying Dagger",
        "image": "Weapons/Parrying Dagger.png",
        "primaryColor": "#999b9e",
        "secondaryColors": [
            "#625c59",
            "#544639"
        ]
    },
    {
        "name": "Partisan",
        "image": "Weapons/Partisan.png",
        "primaryColor": "#554e4c",
        "secondaryColors": [
            "#594637",
            "#49342c"
        ]
    },
    {
        "name": "Pest's Glaive",
        "image": "Weapons/Pest's Glaive.png",
        "primaryColor": "#9d9597",
        "secondaryColors": [
            "#6d6d71",
            "#68605f"
        ]
    },
    {
        "name": "Pickaxe",
        "image": "Weapons/Pickaxe.png",
        "primaryColor": "#605751",
        "secondaryColors": [
            "#534639",
            "#443a34"
        ]
    },
    {
        "name": "Pike",
        "image": "Weapons/Pike.png",
        "primaryColor": "#525561",
        "secondaryColors": [
            "#525659",
            "#4c5359"
        ]
    },
    {
        "name": "Prelate's Inferno Crozier",
        "image": "Weapons/Prelate's Inferno Crozier.png",
        "primaryColor": "#6d494e",
        "secondaryColors": [
            "#992f35",
            "#582528"
        ]
    },
    {
        "name": "Prince of Death's Staff",
        "image": "Weapons/Prince of Death's Staff.png",
        "primaryColor": "#5b5351",
        "secondaryColors": [
            "#564f4f",
            "#443b38"
        ]
    },
    {
        "name": "Pulley Bow",
        "image": "Weapons/Pulley Bow.png",
        "primaryColor": "#635c52",
        "secondaryColors": [
            "#575252",
            "#564f4e"
        ]
    },
    {
        "name": "Pulley Crossbow",
        "image": "Weapons/Pulley Crossbow.png",
        "primaryColor": "#8e94a6",
        "secondaryColors": [
            "#737789",
            "#965d60"
        ]
    },
    {
        "name": "Rapier",
        "image": "Weapons/Rapier.png",
        "primaryColor": "#90949e",
        "secondaryColors": [
            "#616061",
            "#606063"
        ]
    },
    {
        "name": "Raptor Talons",
        "image": "Weapons/Raptor Talons.png",
        "primaryColor": "#959aa3",
        "secondaryColors": [
            "#5f5c5f",
            "#5a5c60"
        ]
    },
    {
        "name": "Red Branch Shortbow",
        "image": "Weapons/Red Branch Shortbow.png",
        "primaryColor": "#66656c",
        "secondaryColors": [
            "#665f5f",
            "#606064"
        ]
    },
    {
        "name": "Reduvia",
        "image": "Weapons/Reduvia.png",
        "primaryColor": "#a69595",
        "secondaryColors": [
            "#8c6c6c",
            "#6b5455"
        ]
    },
    {
        "name": "Regalia of Eochaid",
        "image": "Weapons/Regalia of Eochaid.png",
        "primaryColor": "#965b2c",
        "secondaryColors": [
            "#645154",
            "#674430"
        ]
    },
    {
        "name": "Ringed Finger",
        "image": "Weapons/Ringed Finger.png",
        "primaryColor": "#60595a",
        "secondaryColors": [
            "#5c4e31",
            "#493728"
        ]
    },
    {
        "name": "Ripple Blade",
        "image": "Weapons/Ripple Blade.png",
        "primaryColor": "#9698a2",
        "secondaryColors": [
            "#5c585b",
            "#4c423a"
        ]
    },
    {
        "name": "Ripple Crescent Halberd",
        "image": "Weapons/Ripple Crescent Halberd.png",
        "primaryColor": "#9794a0",
        "secondaryColors": [
            "#747489",
            "#695f62"
        ]
    },
    {
        "name": "Rivers of Blood",
        "image": "Weapons/Rivers of Blood.png",
        "primaryColor": "#590608",
        "secondaryColors": [
            "#5a514e",
            "#9a2526"
        ]
    },
    {
        "name": "Rogier's Rapier",
        "image": "Weapons/Rogier's Rapier.png",
        "primaryColor": "#8d8c91",
        "secondaryColors": [
            "#85796f",
            "#767883"
        ]
    },
    {
        "name": "Rosus_ Axe",
        "image": "Weapons/Rosus_ Axe.png",
        "primaryColor": "#9d9b9b",
        "secondaryColors": [
            "#5c5a57",
            "#594b37"
        ]
    },
    {
        "name": "Rotten Battle Hammer",
        "image": "Weapons/Rotten Battle Hammer.png",
        "primaryColor": "#9f8e90",
        "secondaryColors": [
            "#976763",
            "#615255"
        ]
    },
    {
        "name": "Rotten Crystal Spear",
        "image": "Weapons/Rotten Crystal Spear.png",
        "primaryColor": "#675d6b",
        "secondaryColors": [
            "#56515b",
            "#49394b"
        ]
    },
    {
        "name": "Rotten Crystal Staff",
        "image": "Weapons/Rotten Crystal Staff.png",
        "primaryColor": "#5c4f59",
        "secondaryColors": [
            "#554951",
            "#473a4a"
        ]
    },
    {
        "name": "Rotten Crystal Sword",
        "image": "Weapons/Rotten Crystal Sword.png",
        "primaryColor": "#614a5e",
        "secondaryColors": [
            "#4b364f",
            "#4d3132"
        ]
    },
    {
        "name": "Rotten Greataxe",
        "image": "Weapons/Rotten Greataxe.png",
        "primaryColor": "#5a5254",
        "secondaryColors": [
            "#933426",
            "#582622"
        ]
    },
    {
        "name": "Rotten Staff",
        "image": "Weapons/Rotten Staff.png",
        "primaryColor": "#9f9997",
        "secondaryColors": [
            "#575457",
            "#58463b"
        ]
    },
    {
        "name": "Royal Greatsword",
        "image": "Weapons/Royal Greatsword.png",
        "primaryColor": "#9d9797",
        "secondaryColors": [
            "#857973",
            "#635a56"
        ]
    },
    {
        "name": "Ruins Greatsword",
        "image": "Weapons/Ruins Greatsword.png",
        "primaryColor": "#555659",
        "secondaryColors": [
            "#3d4149",
            "#393c42"
        ]
    },
    {
        "name": "Rusted Anchor",
        "image": "Weapons/Rusted Anchor.png",
        "primaryColor": "#916b57",
        "secondaryColors": [
            "#6b544d",
            "#674738"
        ]
    },
    {
        "name": "Sacred Relic Sword",
        "image": "Weapons/Sacred Relic Sword.png",
        "primaryColor": "#85735c",
        "secondaryColors": [
            "#625c56",
            "#5b5857"
        ]
    },
    {
        "name": "Sacrificial Axe",
        "image": "Weapons/Sacrificial Axe.png",
        "primaryColor": "#9b9792",
        "secondaryColors": [
            "#555454",
            "#4a453a"
        ]
    },
    {
        "name": "Scavenger's Curved Sword",
        "image": "Weapons/Scavenger's Curved Sword.png",
        "primaryColor": "#9d9794",
        "secondaryColors": [
            "#625b5e",
            "#5b5759"
        ]
    },
    {
        "name": "Scepter of the All-Knowing",
        "image": "Weapons/Scepter of the All-Knowing.png",
        "primaryColor": "#9f9b90",
        "secondaryColors": [
            "#928773",
            "#6a6254"
        ]
    },
    {
        "name": "Scimitar",
        "image": "Weapons/Scimitar.png",
        "primaryColor": "#9c9590",
        "secondaryColors": [
            "#8d847a",
            "#84786e"
        ]
    },
    {
        "name": "Scorpion's Stinger",
        "image": "Weapons/Scorpion's Stinger.png",
        "primaryColor": "#985133",
        "secondaryColors": [
            "#5d5a5c",
            "#5b5859"
        ]
    },
    {
        "name": "Scythe",
        "image": "Weapons/Scythe.png",
        "primaryColor": "#867059",
        "secondaryColors": [
            "#65585e",
            "#67564a"
        ]
    },
    {
        "name": "Sentry's Torch",
        "image": "Weapons/Sentry's Torch.png",
        "primaryColor": "#f9e49a",
        "secondaryColors": [
            "#e3a856",
            "#a25a29"
        ]
    },
    {
        "name": "Serpent Bow",
        "image": "Weapons/Serpent Bow.png",
        "primaryColor": "#8d6f59",
        "secondaryColors": [
            "#67584f",
            "#5f4836"
        ]
    },
    {
        "name": "Serpent-God's Curved Sword",
        "image": "Weapons/Serpent-God's Curved Sword.png",
        "primaryColor": "#926755",
        "secondaryColors": [
            "#5f5753",
            "#614637"
        ]
    },
    {
        "name": "Serpent-Hunter",
        "image": "Weapons/Serpent-Hunter.png",
        "primaryColor": "#959095",
        "secondaryColors": [
            "#58555b",
            "#3b3b43"
        ]
    },
    {
        "name": "Serpentbone Blade",
        "image": "Weapons/Serpentbone Blade.png",
        "primaryColor": "#939392",
        "secondaryColors": [
            "#606264",
            "#615e5a"
        ]
    },
    {
        "name": "Shamshir",
        "image": "Weapons/Shamshir.png",
        "primaryColor": "#97979d",
        "secondaryColors": [
            "#66635d",
            "#655e5d"
        ]
    },
    {
        "name": "Short Spear",
        "image": "Weapons/Short Spear.png",
        "primaryColor": "#999ba2",
        "secondaryColors": [
            "#8e6f54",
            "#5d5e63"
        ]
    },
    {
        "name": "Short Sword",
        "image": "Weapons/Short Sword.png",
        "primaryColor": "#979598",
        "secondaryColors": [
            "#847261",
            "#695f57"
        ]
    },
    {
        "name": "Shortbow",
        "image": "Weapons/Shortbow.png",
        "primaryColor": "#b1a28e",
        "secondaryColors": [
            "#978773",
            "#877662"
        ]
    },
    {
        "name": "Shotel",
        "image": "Weapons/Shotel.png",
        "primaryColor": "#625d57",
        "secondaryColors": [
            "#605a54",
            "#514639"
        ]
    },
    {
        "name": "Siluria's Tree",
        "image": "Weapons/Siluria's Tree.png",
        "primaryColor": "#a2998d",
        "secondaryColors": [
            "#655d53",
            "#554838"
        ]
    },
    {
        "name": "Soldier's Crossbow",
        "image": "Weapons/Soldier's Crossbow.png",
        "primaryColor": "#a29992",
        "secondaryColors": [
            "#978776",
            "#877666"
        ]
    },
    {
        "name": "Spear",
        "image": "Weapons/Spear.png",
        "primaryColor": "#aa755b",
        "secondaryColors": [
            "#5e554e",
            "#5e4934"
        ]
    },
    {
        "name": "Spiked Caestus",
        "image": "Weapons/Spiked Caestus.png",
        "primaryColor": "#9e8475",
        "secondaryColors": [
            "#8b6e5d",
            "#665653"
        ]
    },
    {
        "name": "Spiked Club",
        "image": "Weapons/Spiked Club.png",
        "primaryColor": "#aa9a8f",
        "secondaryColors": [
            "#87766e",
            "#5e5353"
        ]
    },
    {
        "name": "Spiked Spear",
        "image": "Weapons/Spiked Spear.png",
        "primaryColor": "#a08b6e",
        "secondaryColors": [
            "#8b755e",
            "#60554d"
        ]
    },
    {
        "name": "St. Trina's Torch",
        "image": "Weapons/St. Trina's Torch.png",
        "primaryColor": "#a591a7",
        "secondaryColors": [
            "#8c7399",
            "#605551"
        ]
    },
    {
        "name": "Staff of Loss",
        "image": "Weapons/Staff of Loss.png",
        "primaryColor": "#6d6667",
        "secondaryColors": [
            "#5b5456",
            "#443c3c"
        ]
    },
    {
        "name": "Staff of the Avatar",
        "image": "Weapons/Staff of the Avatar.png",
        "primaryColor": "#877459",
        "secondaryColors": [
            "#695b4c",
            "#574936"
        ]
    },
    {
        "name": "Staff of the Guilty",
        "image": "Weapons/Staff of the Guilty.png",
        "primaryColor": "#625855",
        "secondaryColors": [
            "#61534c",
            "#53453b"
        ]
    },
    {
        "name": "Star Fist",
        "image": "Weapons/Star Fist.png",
        "primaryColor": "#9f989c",
        "secondaryColors": [
            "#5d555a",
            "#473833"
        ]
    },
    {
        "name": "Starscourge Greatsword",
        "image": "Weapons/Starscourge Greatsword.png",
        "primaryColor": "#64625d",
        "secondaryColors": [
            "#645c4d",
            "#514737"
        ]
    },
    {
        "name": "Steel-Wire Torch",
        "image": "Weapons/Steel-Wire Torch.png",
        "primaryColor": "#fae19b",
        "secondaryColors": [
            "#e0a45b",
            "#61504e"
        ]
    },
    {
        "name": "Stone Club",
        "image": "Weapons/Stone Club.png",
        "primaryColor": "#94979c",
        "secondaryColors": [
            "#595b60",
            "#3c424f"
        ]
    },
    {
        "name": "Stormhawk Axe",
        "image": "Weapons/Stormhawk Axe.png",
        "primaryColor": "#94939c",
        "secondaryColors": [
            "#635858",
            "#524438"
        ]
    },
    {
        "name": "Sword of Milos",
        "image": "Weapons/Sword of Milos.png",
        "primaryColor": "#86766e",
        "secondaryColors": [
            "#625856",
            "#605756"
        ]
    },
    {
        "name": "Sword of Night and Flame",
        "image": "Weapons/Sword of Night and Flame.png",
        "primaryColor": "#8b6f5d",
        "secondaryColors": [
            "#655e55",
            "#5d4835"
        ]
    },
    {
        "name": "Sword of St. Trina",
        "image": "Weapons/Sword of St. Trina.png",
        "primaryColor": "#958f91",
        "secondaryColors": [
            "#857974",
            "#6a615a"
        ]
    },
    {
        "name": "Thorned Whip",
        "image": "Weapons/Thorned Whip.png",
        "primaryColor": "#9b5259",
        "secondaryColors": [
            "#694b52",
            "#5e292a"
        ]
    },
    {
        "name": "Torch",
        "image": "Weapons/Torch.png",
        "primaryColor": "#fbe499",
        "secondaryColors": [
            "#f7cb75",
            "#e3a75d"
        ]
    },
    {
        "name": "Torchpole",
        "image": "Weapons/Torchpole.png",
        "primaryColor": "#f7df99",
        "secondaryColors": [
            "#88634e",
            "#6a5348"
        ]
    },
    {
        "name": "Treespear",
        "image": "Weapons/Treespear.png",
        "primaryColor": "#655e52",
        "secondaryColors": [
            "#5e5c56",
            "#544735"
        ]
    },
    {
        "name": "Troll Knight's Sword",
        "image": "Weapons/Troll Knight's Sword.png",
        "primaryColor": "#9197a4",
        "secondaryColors": [
            "#6a665e",
            "#5e5956"
        ]
    },
    {
        "name": "Troll's Golden Sword",
        "image": "Weapons/Troll's Golden Sword.png",
        "primaryColor": "#6f6054",
        "secondaryColors": [
            "#655a54",
            "#594636"
        ]
    },
    {
        "name": "Troll's Hammer",
        "image": "Weapons/Troll's Hammer.png",
        "primaryColor": "#938a6d",
        "secondaryColors": [
            "#615b4f",
            "#4e4937"
        ]
    },
    {
        "name": "Twinblade",
        "image": "Weapons/Twinblade.png",
        "primaryColor": "#9d8b6a",
        "secondaryColors": [
            "#8c6d4a",
            "#6b5d4d"
        ]
    },
    {
        "name": "Twinned Knight Swords",
        "image": "Weapons/Twinned Knight Swords.png",
        "primaryColor": "#a4a09d",
        "secondaryColors": [
            "#857a66",
            "#6a6156"
        ]
    },
    {
        "name": "Uchigatana",
        "image": "Weapons/Uchigatana.png",
        "primaryColor": "#cecbc9",
        "secondaryColors": [
            "#a29d98",
            "#827a6f"
        ]
    },
    {
        "name": "Urumi",
        "image": "Weapons/Urumi.png",
        "primaryColor": "#98969a",
        "secondaryColors": [
            "#615a57",
            "#594937"
        ]
    },
    {
        "name": "Varr\u00e9's Bouquet",
        "image": "Weapons/Varr\u00e9's Bouquet.png",
        "primaryColor": "#9e9899",
        "secondaryColors": [
            "#8d6c69",
            "#6a5c5c"
        ]
    },
    {
        "name": "Venomous Fang",
        "image": "Weapons/Venomous Fang.png",
        "primaryColor": "#94a297",
        "secondaryColors": [
            "#738e8c",
            "#718479"
        ]
    },
    {
        "name": "Veteran's Prosthesis",
        "image": "Weapons/Veteran's Prosthesis.png",
        "primaryColor": "#d4d3d6",
        "secondaryColors": [
            "#9c989b",
            "#615b5d"
        ]
    },
    {
        "name": "Vulgar Militia Saw",
        "image": "Weapons/Vulgar Militia Saw.png",
        "primaryColor": "#5c5d5f",
        "secondaryColors": [
            "#5b524c",
            "#4f453a"
        ]
    },
    {
        "name": "Vulgar Militia Shotel",
        "image": "Weapons/Vulgar Militia Shotel.png",
        "primaryColor": "#5f5651",
        "secondaryColors": [
            "#565255",
            "#4f443b"
        ]
    },
    {
        "name": "Vyke's War Spear",
        "image": "Weapons/Vyke's War Spear.png",
        "primaryColor": "#54555c",
        "secondaryColors": [
            "#544f5c",
            "#574c4f"
        ]
    },
    {
        "name": "Wakizashi",
        "image": "Weapons/Wakizashi.png",
        "primaryColor": "#a59d91",
        "secondaryColors": [
            "#867663",
            "#5c5652"
        ]
    },
    {
        "name": "Warhawk's Talon",
        "image": "Weapons/Warhawk's Talon.png",
        "primaryColor": "#8f9199",
        "secondaryColors": [
            "#615d5a",
            "#605a56"
        ]
    },
    {
        "name": "Warped Axe",
        "image": "Weapons/Warped Axe.png",
        "primaryColor": "#92949a",
        "secondaryColors": [
            "#59585a",
            "#48413c"
        ]
    },
    {
        "name": "Warpick",
        "image": "Weapons/Warpick.png",
        "primaryColor": "#9a9695",
        "secondaryColors": [
            "#5e5756",
            "#614b35"
        ]
    },
    {
        "name": "Watchdog's Greatsword",
        "image": "Weapons/Watchdog's Greatsword.png",
        "primaryColor": "#615f5c",
        "secondaryColors": [
            "#595755",
            "#48433b"
        ]
    },
    {
        "name": "Watchdog's Staff",
        "image": "Weapons/Watchdog's Staff.png",
        "primaryColor": "#999794",
        "secondaryColors": [
            "#5f5b57",
            "#4b4439"
        ]
    },
    {
        "name": "Weathered Straight Sword",
        "image": "Weapons/Weathered Straight Sword.png",
        "primaryColor": "#959297",
        "secondaryColors": [
            "#6b5e53",
            "#584838"
        ]
    },
    {
        "name": "Whip",
        "image": "Weapons/Whip.png",
        "primaryColor": "#8e5e50",
        "secondaryColors": [
            "#614b50",
            "#4a3331"
        ]
    },
    {
        "name": "Wing of Astel",
        "image": "Weapons/Wing of Astel.png",
        "primaryColor": "#959899",
        "secondaryColors": [
            "#536192",
            "#5f5c5d"
        ]
    },
    {
        "name": "Winged Greathorn",
        "image": "Weapons/Winged Greathorn.png",
        "primaryColor": "#8c6a62",
        "secondaryColors": [
            "#65524e",
            "#58463a"
        ]
    },
    {
        "name": "Winged Scythe",
        "image": "Weapons/Winged Scythe.png",
        "primaryColor": "#9c9991",
        "secondaryColors": [
            "#8c8572",
            "#837a65"
        ]
    },
    {
        "name": "Zamor Curved Sword",
        "image": "Weapons/Zamor Curved Sword.png",
        "primaryColor": "#9d9898",
        "secondaryColors": [
            "#625c56",
            "#524739"
        ]
    },
    {
        "name": "Zweihander",
        "image": "Weapons/Zweihander.png",
        "primaryColor": "#82756d",
        "secondaryColors": [
            "#69645a",
            "#6c6055"
        ]
    },
    {
        "name": "Ancient Meteoric Ore Greatsword",
        "image": "Weapons\\SOTE/Ancient Meteoric Ore Greatsword.png",
        "primaryColor": "#585c61",
        "secondaryColors": [
            "#525256",
            "#353946"
        ]
    },
    {
        "name": "Ansbach's Longbow",
        "image": "Weapons\\SOTE/Ansbach's Longbow.png",
        "primaryColor": "#545864",
        "secondaryColors": [
            "#4b4f59",
            "#3b424e"
        ]
    },
    {
        "name": "Anvil Hammer",
        "image": "Weapons\\SOTE/Anvil Hammer.png",
        "primaryColor": "#a9624a",
        "secondaryColors": [
            "#a8643a",
            "#554d4b"
        ]
    },
    {
        "name": "Backhand Blade",
        "image": "Weapons\\SOTE/Backhand Blade.png",
        "primaryColor": "#9097a9",
        "secondaryColors": [
            "#625e5f",
            "#5a595d"
        ]
    },
    {
        "name": "Barbed Staff-Spear",
        "image": "Weapons\\SOTE/Barbed Staff-Spear.png",
        "primaryColor": "#6e4e29",
        "secondaryColors": [
            "#684d2e",
            "#644928"
        ]
    },
    {
        "name": "Beast Claw",
        "image": "Weapons\\SOTE/Beast Claw.png",
        "primaryColor": "#939493",
        "secondaryColors": [
            "#5d5854",
            "#4b433c"
        ]
    },
    {
        "name": "Black Steel Greathammer",
        "image": "Weapons\\SOTE/Black Steel Greathammer.png",
        "primaryColor": "#5d5e5d",
        "secondaryColors": [
            "#59564f",
            "#4c4539"
        ]
    },
    {
        "name": "Black Steel Twinblade",
        "image": "Weapons\\SOTE/Black Steel Twinblade.png",
        "primaryColor": "#5e5e4f",
        "secondaryColors": [
            "#555329",
            "#514d37"
        ]
    },
    {
        "name": "Bloodfiend's Arm",
        "image": "Weapons\\SOTE/Bloodfiend's Arm.png",
        "primaryColor": "#64524e",
        "secondaryColors": [
            "#5c443a",
            "#493630"
        ]
    },
    {
        "name": "Bloodfiend's Fork",
        "image": "Weapons\\SOTE/Bloodfiend's Fork.png",
        "primaryColor": "#886e60",
        "secondaryColors": [
            "#62524a",
            "#59443b"
        ]
    },
    {
        "name": "Bloodfiend's Sacred Spear",
        "image": "Weapons\\SOTE/Bloodfiend's Sacred Spear.png",
        "primaryColor": "#6d554d",
        "secondaryColors": [
            "#6c554e",
            "#624339"
        ]
    },
    {
        "name": "Bone Bow",
        "image": "Weapons\\SOTE/Bone Bow.png",
        "primaryColor": "#595255",
        "secondaryColors": [
            "#544f53",
            "#534d4d"
        ]
    },
    {
        "name": "Carian Sorcery Sword",
        "image": "Weapons\\SOTE/Carian Sorcery Sword.png",
        "primaryColor": "#656d8d",
        "secondaryColors": [
            "#636a92",
            "#5f6064"
        ]
    },
    {
        "name": "Chilling Perfume Bottle",
        "image": "Weapons\\SOTE/Chilling Perfume Bottle.png",
        "primaryColor": "#335f98",
        "secondaryColors": [
            "#94a3a8",
            "#728a9f"
        ]
    },
    {
        "name": "Claws of Night",
        "image": "Weapons\\SOTE/Claws of Night.png",
        "primaryColor": "#5b5555",
        "secondaryColors": [
            "#544f4e",
            "#494444"
        ]
    },
    {
        "name": "Curseblade's Cirque",
        "image": "Weapons\\SOTE/Curseblade's Cirque.png",
        "primaryColor": "#54575c",
        "secondaryColors": [
            "#52555b",
            "#4e5258"
        ]
    },
    {
        "name": "Dancing Blade of Ranah",
        "image": "Weapons\\SOTE/Dancing Blade of Ranah.png",
        "primaryColor": "#695c50",
        "secondaryColors": [
            "#625a52",
            "#5b4933"
        ]
    },
    {
        "name": "Dane's Footwork",
        "image": "Weapons\\SOTE/Dane's Footwork.png",
        "primaryColor": "#837656",
        "secondaryColors": [
            "#5f584b",
            "#514836"
        ]
    },
    {
        "name": "Deadly Poison Perfume Bottle",
        "image": "Weapons\\SOTE/Deadly Poison Perfume Bottle.png",
        "primaryColor": "#93a32b",
        "secondaryColors": [
            "#586052",
            "#50591f"
        ]
    },
    {
        "name": "Death Knight's Longhaft Axe",
        "image": "Weapons\\SOTE/Death Knight's Longhaft Axe.png",
        "primaryColor": "#6d5b4c",
        "secondaryColors": [
            "#5c4835",
            "#4c3322"
        ]
    },
    {
        "name": "Death Knight's Twin Axes",
        "image": "Weapons\\SOTE/Death Knight's Twin Axes.png",
        "primaryColor": "#887261",
        "secondaryColors": [
            "#6a5a4e",
            "#5b4734"
        ]
    },
    {
        "name": "Devonia's Hammer",
        "image": "Weapons\\SOTE/Devonia's Hammer.png",
        "primaryColor": "#886e5e",
        "secondaryColors": [
            "#68534a",
            "#5d4639"
        ]
    },
    {
        "name": "Dragon-Hunter's Great Katana",
        "image": "Weapons\\SOTE/Dragon-Hunter's Great Katana.png",
        "primaryColor": "#8993aa",
        "secondaryColors": [
            "#53535f",
            "#443c44"
        ]
    },
    {
        "name": "Dryleaf Arts",
        "image": "Weapons\\SOTE/Dryleaf Arts.png",
        "primaryColor": "#585249",
        "secondaryColors": [
            "#4c4637",
            "#413c48"
        ]
    },
    {
        "name": "Dryleaf Seal",
        "image": "Weapons\\SOTE/Dryleaf Seal.png",
        "primaryColor": "#978b6c",
        "secondaryColors": [
            "#867759",
            "#6f644c"
        ]
    },
    {
        "name": "Euporia",
        "image": "Weapons\\SOTE/Euporia.png",
        "primaryColor": "#9c8b73",
        "secondaryColors": [
            "#8b745d",
            "#60574f"
        ]
    },
    {
        "name": "Falx",
        "image": "Weapons\\SOTE/Falx.png",
        "primaryColor": "#b4b1a6",
        "secondaryColors": [
            "#9f9b99",
            "#555355"
        ]
    },
    {
        "name": "Fire Knight's Greatsword",
        "image": "Weapons\\SOTE/Fire Knight's Greatsword.png",
        "primaryColor": "#655d53",
        "secondaryColors": [
            "#635c51",
            "#564a35"
        ]
    },
    {
        "name": "Fire Knight's Seal",
        "image": "Weapons\\SOTE/Fire Knight's Seal.png",
        "primaryColor": "#5f5c58",
        "secondaryColors": [
            "#5e574d",
            "#4d4438"
        ]
    },
    {
        "name": "Fire Knight's Shortsword",
        "image": "Weapons\\SOTE/Fire Knight's Shortsword.png",
        "primaryColor": "#645d55",
        "secondaryColors": [
            "#605e56",
            "#4e463a"
        ]
    },
    {
        "name": "Firespark Perfume Bottle",
        "image": "Weapons\\SOTE/Firespark Perfume Bottle.png",
        "primaryColor": "#a98b68",
        "secondaryColors": [
            "#8d725c",
            "#92652b"
        ]
    },
    {
        "name": "Flowerstone Gavel",
        "image": "Weapons\\SOTE/Flowerstone Gavel.png",
        "primaryColor": "#896e71",
        "secondaryColors": [
            "#645158",
            "#483a46"
        ]
    },
    {
        "name": "Forked-Tongue Hatchet",
        "image": "Weapons\\SOTE/Forked-Tongue Hatchet.png",
        "primaryColor": "#575a53",
        "secondaryColors": [
            "#47473b",
            "#3b4346"
        ]
    },
    {
        "name": "Frenzyflame Perfume Bottle",
        "image": "Weapons\\SOTE/Frenzyflame Perfume Bottle.png",
        "primaryColor": "#8a705a",
        "secondaryColors": [
            "#9c5826",
            "#6c5b4e"
        ]
    },
    {
        "name": "Freyja's Greatsword",
        "image": "Weapons\\SOTE/Freyja's Greatsword.png",
        "primaryColor": "#5f584b",
        "secondaryColors": [
            "#585349",
            "#554935"
        ]
    },
    {
        "name": "Gazing Finger",
        "image": "Weapons\\SOTE/Gazing Finger.png",
        "primaryColor": "#837675",
        "secondaryColors": [
            "#5e575b",
            "#443a39"
        ]
    },
    {
        "name": "Golem Fist",
        "image": "Weapons\\SOTE/Golem Fist.png",
        "primaryColor": "#8c6e5f",
        "secondaryColors": [
            "#62514c",
            "#5a443a"
        ]
    },
    {
        "name": "Great Katana",
        "image": "Weapons\\SOTE/Great Katana.png",
        "primaryColor": "#6e6559",
        "secondaryColors": [
            "#6d605a",
            "#5c5352"
        ]
    },
    {
        "name": "Greatsword of Damnation",
        "image": "Weapons\\SOTE/Greatsword of Damnation.png",
        "primaryColor": "#aa8d5c",
        "secondaryColors": [
            "#90714e",
            "#69502f"
        ]
    },
    {
        "name": "Greatsword of Radahn",
        "image": "Weapons\\SOTE/Greatsword of Radahn.png",
        "primaryColor": "#645c4d",
        "secondaryColors": [
            "#5e5d56",
            "#534835"
        ]
    },
    {
        "name": "Greatsword of Solitude",
        "image": "Weapons\\SOTE/Greatsword of Solitude.png",
        "primaryColor": "#545353",
        "secondaryColors": [
            "#525050",
            "#48423b"
        ]
    },
    {
        "name": "Horned Warrior's Greatsword",
        "image": "Weapons\\SOTE/Horned Warrior's Greatsword.png",
        "primaryColor": "#555456",
        "secondaryColors": [
            "#545150",
            "#48413c"
        ]
    },
    {
        "name": "Horned Warrior's Sword",
        "image": "Weapons\\SOTE/Horned Warrior's Sword.png",
        "primaryColor": "#8e9092",
        "secondaryColors": [
            "#5e5a58",
            "#4d4339"
        ]
    },
    {
        "name": "Igon's Greatbow",
        "image": "Weapons\\SOTE/Igon's Greatbow.png",
        "primaryColor": "#5f534d",
        "secondaryColors": [
            "#59514e",
            "#4f433b"
        ]
    },
    {
        "name": "Lamenting Visage",
        "image": "Weapons\\SOTE/Lamenting Visage.png",
        "primaryColor": "#887560",
        "secondaryColors": [
            "#5d5651",
            "#584737"
        ]
    },
    {
        "name": "Leda's Sword",
        "image": "Weapons\\SOTE/Leda's Sword.png",
        "primaryColor": "#938d89",
        "secondaryColors": [
            "#918676",
            "#857663"
        ]
    },
    {
        "name": "Lightning Perfume Bottle",
        "image": "Weapons\\SOTE/Lightning Perfume Bottle.png",
        "primaryColor": "#a79a56",
        "secondaryColors": [
            "#605d4e",
            "#564e2b"
        ]
    },
    {
        "name": "Lizard Greatsword",
        "image": "Weapons\\SOTE/Lizard Greatsword.png",
        "primaryColor": "#596053",
        "secondaryColors": [
            "#464c3b",
            "#3a4447"
        ]
    },
    {
        "name": "Madding Hand",
        "image": "Weapons\\SOTE/Madding Hand.png",
        "primaryColor": "#51484b",
        "secondaryColors": [
            "#5e4436",
            "#49352f"
        ]
    },
    {
        "name": "Main-gauche",
        "image": "Weapons\\SOTE/Main-gauche.png",
        "primaryColor": "#727784",
        "secondaryColors": [
            "#515359",
            "#4f525c"
        ]
    },
    {
        "name": "Maternal Staff",
        "image": "Weapons\\SOTE/Maternal Staff.png",
        "primaryColor": "#9b8f94",
        "secondaryColors": [
            "#645e60",
            "#5a555c"
        ]
    },
    {
        "name": "Messmer Soldier's Axe",
        "image": "Weapons\\SOTE/Messmer Soldier's Axe.png",
        "primaryColor": "#5a5052",
        "secondaryColors": [
            "#56433b",
            "#473733"
        ]
    },
    {
        "name": "Messmer Soldier's Spear",
        "image": "Weapons\\SOTE/Messmer Soldier's Spear.png",
        "primaryColor": "#646054",
        "secondaryColors": [
            "#55534e",
            "#4d4438"
        ]
    },
    {
        "name": "Milady",
        "image": "Weapons\\SOTE/Milady.png",
        "primaryColor": "#585c68",
        "secondaryColors": [
            "#4c4e57",
            "#4c4b4e"
        ]
    },
    {
        "name": "Nanaya's Torch",
        "image": "Weapons\\SOTE/Nanaya's Torch.png",
        "primaryColor": "#91592e",
        "secondaryColors": [
            "#78462b",
            "#68312b"
        ]
    },
    {
        "name": "Obsidian Lamina",
        "image": "Weapons\\SOTE/Obsidian Lamina.png",
        "primaryColor": "#4b4e4f",
        "secondaryColors": [
            "#494e50",
            "#4d4c48"
        ]
    },
    {
        "name": "Pata",
        "image": "Weapons\\SOTE/Pata.png",
        "primaryColor": "#555253",
        "secondaryColors": [
            "#4c423a",
            "#443a33"
        ]
    },
    {
        "name": "Poisoned Hand",
        "image": "Weapons\\SOTE/Poisoned Hand.png",
        "primaryColor": "#96949d",
        "secondaryColors": [
            "#6c7186",
            "#545366"
        ]
    },
    {
        "name": "Poleblade of the Bud",
        "image": "Weapons\\SOTE/Poleblade of the Bud.png",
        "primaryColor": "#69394c",
        "secondaryColors": [
            "#553444",
            "#552435"
        ]
    },
    {
        "name": "Putrescence Cleaver",
        "image": "Weapons\\SOTE/Putrescence Cleaver.png",
        "primaryColor": "#929190",
        "secondaryColors": [
            "#55575c",
            "#3d414b"
        ]
    },
    {
        "name": "Queelign's Greatsword",
        "image": "Weapons\\SOTE/Queelign's Greatsword.png",
        "primaryColor": "#5e5c55",
        "secondaryColors": [
            "#5b5b58",
            "#4e4736"
        ]
    },
    {
        "name": "Rabbath's Cannon",
        "image": "Weapons\\SOTE/Rabbath's Cannon.png",
        "primaryColor": "#a0a197",
        "secondaryColors": [
            "#585a56",
            "#39454b"
        ]
    },
    {
        "name": "Rakshasa's Great Katana",
        "image": "Weapons\\SOTE/Rakshasa's Great Katana.png",
        "primaryColor": "#641e16",
        "secondaryColors": [
            "#611e16",
            "#5a1e17"
        ]
    },
    {
        "name": "Red Bear's Claw",
        "image": "Weapons\\SOTE/Red Bear's Claw.png",
        "primaryColor": "#5a575c",
        "secondaryColors": [
            "#4a2d2c",
            "#4f2a2a"
        ]
    },
    {
        "name": "Rellana's Twin Blades",
        "image": "Weapons\\SOTE/Rellana's Twin Blades.png",
        "primaryColor": "#5f5e5d",
        "secondaryColors": [
            "#524f50",
            "#4a433a"
        ]
    },
    {
        "name": "Repeating Crossbow",
        "image": "Weapons\\SOTE/Repeating Crossbow.png",
        "primaryColor": "#9c9894",
        "secondaryColors": [
            "#5e5957",
            "#4a423c"
        ]
    },
    {
        "name": "Serpent Flail",
        "image": "Weapons\\SOTE/Serpent Flail.png",
        "primaryColor": "#85775d",
        "secondaryColors": [
            "#635c4f",
            "#524738"
        ]
    },
    {
        "name": "Shadow Sunflower Blossom",
        "image": "Weapons\\SOTE/Shadow Sunflower Blossom.png",
        "primaryColor": "#5d6065",
        "secondaryColors": [
            "#515355",
            "#3d414a"
        ]
    },
    {
        "name": "Smithscript Axe",
        "image": "Weapons\\SOTE/Smithscript Axe.png",
        "primaryColor": "#595456",
        "secondaryColors": [
            "#5a4d4d",
            "#443c42"
        ]
    },
    {
        "name": "Smithscript Cirque",
        "image": "Weapons\\SOTE/Smithscript Cirque.png",
        "primaryColor": "#5f5256",
        "secondaryColors": [
            "#594736",
            "#463c43"
        ]
    },
    {
        "name": "Smithscript Dagger",
        "image": "Weapons\\SOTE/Smithscript Dagger.png",
        "primaryColor": "#a6999a",
        "secondaryColors": [
            "#8a7268",
            "#6a5755"
        ]
    },
    {
        "name": "Smithscript Hammer",
        "image": "Weapons\\SOTE/Smithscript Hammer.png",
        "primaryColor": "#645a56",
        "secondaryColors": [
            "#5e534d",
            "#584e4c"
        ]
    },
    {
        "name": "Smithscript Spear",
        "image": "Weapons\\SOTE/Smithscript Spear.png",
        "primaryColor": "#5f5a62",
        "secondaryColors": [
            "#594c4c",
            "#473934"
        ]
    },
    {
        "name": "Spear of the Impaler",
        "image": "Weapons\\SOTE/Spear of the Impaler.png",
        "primaryColor": "#60605d",
        "secondaryColors": [
            "#545553",
            "#4e5050"
        ]
    },
    {
        "name": "Spiraltree Seal",
        "image": "Weapons\\SOTE/Spiraltree Seal.png",
        "primaryColor": "#867868",
        "secondaryColors": [
            "#675e58",
            "#63482d"
        ]
    },
    {
        "name": "Spirit Glaive",
        "image": "Weapons\\SOTE/Spirit Glaive.png",
        "primaryColor": "#55586b",
        "secondaryColors": [
            "#494a50",
            "#3d424e"
        ]
    },
    {
        "name": "Spirit Sword",
        "image": "Weapons\\SOTE/Spirit Sword.png",
        "primaryColor": "#525762",
        "secondaryColors": [
            "#51525b",
            "#433a37"
        ]
    },
    {
        "name": "Spread Crossbow",
        "image": "Weapons\\SOTE/Spread Crossbow.png",
        "primaryColor": "#a29b97",
        "secondaryColors": [
            "#897463",
            "#635b56"
        ]
    },
    {
        "name": "Staff of the Great Beyond",
        "image": "Weapons\\SOTE/Staff of the Great Beyond.png",
        "primaryColor": "#9a9397",
        "secondaryColors": [
            "#59555c",
            "#44393a"
        ]
    },
    {
        "name": "Star-lined Sword",
        "image": "Weapons\\SOTE/Star-lined Sword.png",
        "primaryColor": "#68645f",
        "secondaryColors": [
            "#5c5a5b",
            "#5c5855"
        ]
    },
    {
        "name": "Stone-Sheathed Sword",
        "image": "Weapons\\SOTE/Stone-Sheathed Sword.png",
        "primaryColor": "#a49a8c",
        "secondaryColors": [
            "#988974",
            "#887664"
        ]
    },
    {
        "name": "Swift Spear",
        "image": "Weapons\\SOTE/Swift Spear.png",
        "primaryColor": "#5f5c56",
        "secondaryColors": [
            "#575755",
            "#545351"
        ]
    },
    {
        "name": "Sword Lance",
        "image": "Weapons\\SOTE/Sword Lance.png",
        "primaryColor": "#5c6068",
        "secondaryColors": [
            "#4f5155",
            "#494339"
        ]
    },
    {
        "name": "Sword of Darkness",
        "image": "Weapons\\SOTE/Sword of Darkness.png",
        "primaryColor": "#5b565a",
        "secondaryColors": [
            "#54565d",
            "#574535"
        ]
    },
    {
        "name": "Sword of Light",
        "image": "Weapons\\SOTE/Sword of Light.png",
        "primaryColor": "#9e9a9a",
        "secondaryColors": [
            "#918578",
            "#867a6d"
        ]
    },
    {
        "name": "Sword of Night",
        "image": "Weapons\\SOTE/Sword of Night.png",
        "primaryColor": "#010102",
        "secondaryColors": [
            "#434343",
            "#353940"
        ]
    },
    {
        "name": "Thiollier's Hidden Needle",
        "image": "Weapons\\SOTE/Thiollier's Hidden Needle.png",
        "primaryColor": "#686887",
        "secondaryColors": [
            "#575460",
            "#585253"
        ]
    },
    {
        "name": "Tooth Whip",
        "image": "Weapons\\SOTE/Tooth Whip.png",
        "primaryColor": "#887461",
        "secondaryColors": [
            "#615654",
            "#5c4934"
        ]
    },
    {
        "name": "Velvet Sword of St. Trina",
        "image": "Weapons\\SOTE/Velvet Sword of St. Trina.png",
        "primaryColor": "#5a5759",
        "secondaryColors": [
            "#565160",
            "#453b52"
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