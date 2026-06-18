"""
bs_negi_questions.py
─────────────────────────────────────────────────────────────────────────────
Comprehensive bilingual (Hindi + English) MCQ bank based on
B.S. Negi's Uttarakhand — A Complete Study Material (5th Edition)
Units 1 through 7.

Each question has:
  - text_hi  : Question in Hindi
  - text_en  : Question in English
  - options  : 4 answer choices (the same options work for both languages
                because names/numbers don't change; only phrasing differs)
  - correct_answer : Correct option string
  - explanation_hi : Explanation in Hindi
  - explanation_en : Explanation in English
  - unit      : 1-7 (matches the PDF unit)
  - chapter   : Chapter/topic heading within that unit
  - id: (auto-generated index for progress tracking)
"""
import random # Keep random for shuffling options

BS_NEGI_UNITS_METADATA = {
    1: {
        "title_hi": "उत्तराखण्ड: सामान्य परिचय",
        "title_en": "Uttarakhand: General Introduction"
    },
    2: {
        "title_hi": "भौतिक संरचना, जलवायु, नदियाँ, झीलें और पर्वत",
        "title_en": "Physical Structure, Climate, Rivers, Lakes & Mountains"
    },
    3: {
        "title_hi": "उत्तराखण्ड का इतिहास (प्राचीन काल से राज्य गठन)",
        "title_en": "History of Uttarakhand (Ancient to State Formation)"
    },
    4: {
        "title_hi": "अर्थव्यवस्था, कृषि, वन और खनिज संसाधन",
        "title_en": "Economy, Agriculture, Forests & Mineral Resources"
    },
    5: {
        "title_hi": "कला, संस्कृति, मेले और त्योहार",
        "title_en": "Art, Culture, Fairs & Festivals"
    },
    6: {
        "title_hi": "पर्यटन, शिक्षा और प्रशासनिक ढांचा",
        "title_en": "Tourism, Education & Administrative Structure"
    },
    7: {
        "title_hi": "उत्तराखण्ड की जनजातियाँ व विविध तथ्य",
        "title_en": "Tribes of Uttarakhand & Miscellaneous Facts"
    }
}

BS_NEGI_QUESTION_BANK = [

    # ══════════════════════════════════════════════════════════════════
    # UNIT 1 — उत्तराखण्ड : सामान्य परिचय (General Introduction)
    # ══════════════════════════════════════════════════════════════════

    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड राज्य की स्थापना किस तिथि को हुई थी?",
        "text_en": "On which date was the state of Uttarakhand established?",
        "options": ["9 नवम्बर 2000 / 9 November 2000",
                    "15 नवम्बर 2000 / 15 November 2000",
                    "26 जनवरी 2001 / 26 January 2001",
                    "1 अक्टूबर 2000 / 1 October 2000"],
        "correct_answer": "9 नवम्बर 2000 / 9 November 2000",
        "explanation_hi": "उत्तर प्रदेश पुनर्गठन अधिनियम 2000 के अंतर्गत 9 नवम्बर 2000 को उत्तराखण्ड (तब उत्तरांचल) का गठन हुआ।",
        "explanation_en": "Under the UP Reorganization Act 2000, Uttarakhand (then Uttaranchal) was carved out on 9 November 2000."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड को 'देवभूमि' क्यों कहा जाता है?",
        "text_en": "Why is Uttarakhand called 'Devbhoomi'?",
        "options": ["अत्यधिक वन सम्पदा के कारण / Due to dense forests",
                    "असंख्य देवी-देवताओं के तीर्थ स्थलों के कारण / Due to numerous religious shrines",
                    "ऊँचे पर्वतों के कारण / Due to high mountains",
                    "राज्य की आधिकारिक भाषा संस्कृत होने के कारण / Because Sanskrit is official language"],
        "correct_answer": "असंख्य देवी-देवताओं के तीर्थ स्थलों के कारण / Due to numerous religious shrines",
        "explanation_hi": "चार धाम (बदरीनाथ, केदारनाथ, गंगोत्री, यमुनोत्री) सहित असंख्य तीर्थस्थल होने के कारण इसे देवभूमि कहा जाता है।",
        "explanation_en": "Uttarakhand is called Devbhoomi (Land of Gods) due to the presence of the Char Dham (Badrinath, Kedarnath, Gangotri, Yamunotri) and countless other shrines."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड की राजधानी कौन सी है?",
        "text_en": "What is the capital of Uttarakhand?",
        "options": ["देहरादून / Dehradun",
                    "हरिद्वार / Haridwar",
                    "नैनीताल / Nainital",
                    "गैरसैंण / Gairsain"],
        "correct_answer": "देहरादून / Dehradun",
        "explanation_hi": "देहरादून उत्तराखण्ड की अंतरिम (प्रशासनिक) राजधानी है। गैरसैंण को ग्रीष्मकालीन राजधानी घोषित किया गया है।",
        "explanation_en": "Dehradun is the interim (administrative) capital of Uttarakhand. Gairsain has been declared the summer capital."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड राज्य का क्षेत्रफल कितना है?",
        "text_en": "What is the area of Uttarakhand state?",
        "options": ["53,483 वर्ग किमी / sq km",
                    "60,245 वर्ग किमी / sq km",
                    "44,212 वर्ग किमी / sq km",
                    "72,660 वर्ग किमी / sq km"],
        "correct_answer": "53,483 वर्ग किमी / sq km",
        "explanation_hi": "उत्तराखण्ड का कुल क्षेत्रफल 53,483 वर्ग किमी है, जो देश के कुल क्षेत्रफल का लगभग 1.63% है।",
        "explanation_en": "The total area of Uttarakhand is 53,483 sq km, which is about 1.63% of India's total area."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड में कुल कितने जिले हैं?",
        "text_en": "How many districts are there in Uttarakhand?",
        "options": ["13", "11", "15", "12"],
        "correct_answer": "13",
        "explanation_hi": "उत्तराखण्ड में कुल 13 जिले हैं — गढ़वाल मण्डल में 7 और कुमाऊँ मण्डल में 6।",
        "explanation_en": "Uttarakhand has 13 districts — 7 in Garhwal division and 6 in Kumaon division."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड में कौन से दो मण्डल हैं?",
        "text_en": "Which are the two divisions of Uttarakhand?",
        "options": ["गढ़वाल और कुमाऊँ / Garhwal and Kumaon",
                    "देहरादून और नैनीताल / Dehradun and Nainital",
                    "रुद्रप्रयाग और चमोली / Rudraprayag and Chamoli",
                    "पिथौरागढ़ और अल्मोड़ा / Pithoragarh and Almora"],
        "correct_answer": "गढ़वाल और कुमाऊँ / Garhwal and Kumaon",
        "explanation_hi": "उत्तराखण्ड दो मण्डलों में विभाजित है — गढ़वाल मण्डल (मुख्यालय: पौड़ी) और कुमाऊँ मण्डल (मुख्यालय: नैनीताल)।",
        "explanation_en": "Uttarakhand is divided into two divisions — Garhwal Division (HQ: Pauri) and Kumaon Division (HQ: Nainital)."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड की उत्तर में कौन सी अंतर्राष्ट्रीय सीमाएं हैं?",
        "text_en": "Which countries share international borders with Uttarakhand in the north?",
        "options": ["चीन (तिब्बत) और नेपाल / China (Tibet) and Nepal",
                    "चीन और भूटान / China and Bhutan",
                    "नेपाल और पाकिस्तान / Nepal and Pakistan",
                    "भूटान और बांग्लादेश / Bhutan and Bangladesh"],
        "correct_answer": "चीन (तिब्बत) और नेपाल / China (Tibet) and Nepal",
        "explanation_hi": "उत्तराखण्ड उत्तर में चीन (तिब्बत) से और पूर्व में नेपाल से अंतर्राष्ट्रीय सीमा साझा करता है।",
        "explanation_en": "Uttarakhand shares an international border with China (Tibet) in the north and Nepal in the east."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड की 2011 की जनसंख्या कितनी थी?",
        "text_en": "What was the population of Uttarakhand as per Census 2011?",
        "options": ["1,00,86,292", "85,49,820", "1,20,41,303", "92,76,115"],
        "correct_answer": "1,00,86,292",
        "explanation_hi": "2011 की जनगणना के अनुसार उत्तराखण्ड की कुल जनसंख्या 1,00,86,292 थी।",
        "explanation_en": "As per the 2011 Census, the total population of Uttarakhand was 1,00,86,292."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड का राजकीय पक्षी कौन सा है?",
        "text_en": "What is the state bird of Uttarakhand?",
        "options": ["मोनाल / Monal", "बुलबुल / Bulbul", "मयूर / Peacock", "तोता / Parrot"],
        "correct_answer": "मोनाल / Monal",
        "explanation_hi": "हिमालयन मोनाल (Lophophorus impejanus) उत्तराखण्ड का राजकीय पक्षी है।",
        "explanation_en": "The Himalayan Monal (Lophophorus impejanus) is the state bird of Uttarakhand."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड का राजकीय वृक्ष कौन सा है?",
        "text_en": "What is the state tree of Uttarakhand?",
        "options": ["बुरांश / Buransh (Rhododendron)",
                    "देवदार / Deodar",
                    "बांज / Oak",
                    "चीड़ / Pine"],
        "correct_answer": "बुरांश / Buransh (Rhododendron)",
        "explanation_hi": "बुरांश (Rhododendron arboreum) उत्तराखण्ड का राजकीय वृक्ष है।",
        "explanation_en": "Buransh (Rhododendron arboreum) is the state tree of Uttarakhand."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड का राजकीय फूल कौन सा है?",
        "text_en": "What is the state flower of Uttarakhand?",
        "options": ["ब्रह्मकमल / Brahma Kamal",
                    "गुलाब / Rose",
                    "कमल / Lotus",
                    "बुरांश / Buransh"],
        "correct_answer": "ब्रह्मकमल / Brahma Kamal",
        "explanation_hi": "ब्रह्मकमल (Saussurea obvallata) उत्तराखण्ड का राजकीय पुष्प है।",
        "explanation_en": "Brahma Kamal (Saussurea obvallata) is the state flower of Uttarakhand."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड का राजकीय पशु कौन सा है?",
        "text_en": "What is the state animal of Uttarakhand?",
        "options": ["Alpine Musk Deer / कस्तूरी मृग",
                    "Snow Leopard / हिम तेंदुआ",
                    "Royal Bengal Tiger / बाघ",
                    "Asiatic Elephant / हाथी"],
        "correct_answer": "Alpine Musk Deer / कस्तूरी मृग",
        "explanation_hi": "कस्तूरी मृग (Moschus chrysogaster) उत्तराखण्ड का राजकीय पशु है।",
        "explanation_en": "The Alpine Musk Deer (Moschus chrysogaster) is the state animal of Uttarakhand."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड विधानसभा में कुल कितनी सीटें हैं?",
        "text_en": "How many seats are there in the Uttarakhand Legislative Assembly?",
        "options": ["70", "80", "60", "100"],
        "correct_answer": "70",
        "explanation_hi": "उत्तराखण्ड विधानसभा में 70 सीटें हैं जिनमें 5 सीटें अनुसूचित जाति और 2 सीटें अनुसूचित जनजाति के लिए आरक्षित हैं।",
        "explanation_en": "Uttarakhand Legislative Assembly has 70 seats — 5 reserved for SC and 2 for ST."
    },
    {
        "unit": 1, "chapter": "सामान्य परिचय / General Introduction",
        "text_hi": "उत्तराखण्ड का राज्य गीत कौन सा है?",
        "text_en": "What is the state song of Uttarakhand?",
        "options": ["उत्तराखण्ड देवभूमि, मातृभूमि / Uttarakhand Devbhoomi Matribhoomi",
                    "जय हो उत्तराखण्ड / Jai Ho Uttarakhand",
                    "मेरी देवभूमि / Meri Devbhoomi",
                    "वन्दे मातरम् / Vande Mataram"],
        "correct_answer": "उत्तराखण्ड देवभूमि, मातृभूमि / Uttarakhand Devbhoomi Matribhoomi",
        "explanation_hi": "हेमन्त बिष्ट द्वारा रचित 'उत्तराखण्ड देवभूमि मातृभूमि' राज्य का आधिकारिक गीत है।",
        "explanation_en": "'Uttarakhand Devbhoomi Matribhoomi' composed by Hemant Bisht is the official state song."
    },

    # ══════════════════════════════════════════════════════════════════
    # UNIT 2 — भौगोलिक संरचना (Geographical Structure)
    # ══════════════════════════════════════════════════════════════════

    {
        "unit": 2, "chapter": "पर्वत शृंखलाएँ / Mountain Ranges",
        "text_hi": "उत्तराखण्ड की सबसे ऊँची चोटी कौन सी है?",
        "text_en": "Which is the highest peak of Uttarakhand?",
        "options": ["नन्दा देवी / Nanda Devi (7816 m)",
                    "त्रिशूल / Trishul (7120 m)",
                    "बद्रीनाथ / Badrinath (7138 m)",
                    "कामेत / Kamet (7756 m)"],
        "correct_answer": "नन्दा देवी / Nanda Devi (7816 m)",
        "explanation_hi": "नन्दा देवी (7816 मीटर) उत्तराखण्ड की सर्वोच्च चोटी है तथा यह भारत की दूसरी सबसे ऊँची चोटी है।",
        "explanation_en": "Nanda Devi (7816 m) is Uttarakhand's highest and India's second-highest peak."
    },
    {
        "unit": 2, "chapter": "पर्वत शृंखलाएँ / Mountain Ranges",
        "text_hi": "उत्तराखण्ड में हिमालय की कितनी श्रेणियाँ पाई जाती हैं?",
        "text_en": "How many ranges of the Himalayas are found in Uttarakhand?",
        "options": ["3", "4", "2", "5"],
        "correct_answer": "3",
        "explanation_hi": "उत्तराखण्ड में हिमालय की तीन मुख्य श्रेणियाँ हैं — वृहत् (महा) हिमालय, मध्य (लघु) हिमालय तथा बाह्य (शिवालिक) हिमालय।",
        "explanation_en": "Uttarakhand has three major Himalayan ranges — Greater Himalayas, Lesser (Middle) Himalayas, and Outer (Shivalik) Himalayas."
    },
    {
        "unit": 2, "chapter": "नदियाँ / Rivers",
        "text_hi": "गंगा नदी का उद्गम स्थल कौन सा है?",
        "text_en": "What is the source of the Ganga River?",
        "options": ["गंगोत्री (गोमुख) / Gangotri (Gaumukh)",
                    "यमुनोत्री / Yamunotri",
                    "केदारनाथ / Kedarnath",
                    "बद्रीनाथ / Badrinath"],
        "correct_answer": "गंगोत्री (गोमुख) / Gangotri (Gaumukh)",
        "explanation_hi": "गंगा नदी गंगोत्री हिमनद के गोमुख से निकलती है। इसे भागीरथी के नाम से भी जाना जाता है।",
        "explanation_en": "The Ganga originates from Gaumukh glacier at Gangotri, and is known as Bhagirathi in its upper course."
    },
    {
        "unit": 2, "chapter": "नदियाँ / Rivers",
        "text_hi": "अलकनन्दा और भागीरथी का संगम कहाँ होता है?",
        "text_en": "Where do Alaknanda and Bhagirathi rivers meet?",
        "options": ["देवप्रयाग / Devprayag",
                    "रुद्रप्रयाग / Rudraprayag",
                    "कर्णप्रयाग / Karnaprayag",
                    "विष्णुप्रयाग / Vishnuprayag"],
        "correct_answer": "देवप्रयाग / Devprayag",
        "explanation_hi": "देवप्रयाग में अलकनन्दा और भागीरथी का संगम होता है, और यहाँ से नदी 'गंगा' कहलाती है।",
        "explanation_en": "Alaknanda and Bhagirathi meet at Devprayag, after which the river is called Ganga."
    },
    {
        "unit": 2, "chapter": "नदियाँ / Rivers",
        "text_hi": "पंचप्रयाग में कौन से पाँच संगम शामिल हैं?",
        "text_en": "Which five confluences are part of Panchprayag?",
        "options": [
            "विष्णुप्रयाग, नन्दप्रयाग, कर्णप्रयाग, रुद्रप्रयाग, देवप्रयाग",
            "हरिद्वार, ऋषिकेश, श्रीनगर, देवप्रयाग, रुद्रप्रयाग",
            "विष्णुप्रयाग, सोनप्रयाग, त्रिवेणी, रुद्रप्रयाग, देवप्रयाग",
            "केशवप्रयाग, नन्दप्रयाग, कर्णप्रयाग, रुद्रप्रयाग, देवप्रयाग"
        ],
        "correct_answer": "विष्णुप्रयाग, नन्दप्रयाग, कर्णप्रयाग, रुद्रप्रयाग, देवप्रयाग",
        "explanation_hi": "गढ़वाल में अलकनन्दा नदी पर पाँच संगम हैं: विष्णुप्रयाग (धौलीगंगा), नन्दप्रयाग (नन्दाकिनी), कर्णप्रयाग (पिण्डर), रुद्रप्रयाग (मन्दाकिनी) और देवप्रयाग (भागीरथी)।",
        "explanation_en": "The five Prayags on Alaknanda: Vishnuprayag (Dhauliganga), Nandprayag (Nandakini), Karnaprayag (Pindar), Rudraprayag (Mandakini) and Devprayag (Bhagirathi)."
    },
    {
        "unit": 2, "chapter": "नदियाँ / Rivers",
        "text_hi": "यमुना नदी का उद्गम स्थल कहाँ है?",
        "text_en": "Where is the source of the Yamuna River?",
        "options": ["यमुनोत्री / Yamunotri",
                    "बंदरपूँछ / Bandarpoonch",
                    "मसूरी / Mussoorie",
                    "चकराता / Chakrata"],
        "correct_answer": "यमुनोत्री / Yamunotri",
        "explanation_hi": "यमुना नदी का उद्गम उत्तरकाशी जिले में यमुनोत्री हिमनद से होता है।",
        "explanation_en": "Yamuna originates from Yamunotri glacier in Uttarkashi district."
    },
    {
        "unit": 2, "chapter": "हिमनद / Glaciers",
        "text_hi": "उत्तराखण्ड का सबसे बड़ा हिमनद कौन सा है?",
        "text_en": "Which is the largest glacier in Uttarakhand?",
        "options": ["गंगोत्री हिमनद / Gangotri Glacier",
                    "मिलम हिमनद / Milam Glacier",
                    "पिण्डारी हिमनद / Pindari Glacier",
                    "खतलिंग हिमनद / Khatling Glacier"],
        "correct_answer": "गंगोत्री हिमनद / Gangotri Glacier",
        "explanation_hi": "गंगोत्री हिमनद उत्तराखण्ड का सबसे बड़ा हिमनद है जिसकी लम्बाई लगभग 30 किमी है।",
        "explanation_en": "Gangotri Glacier is the largest glacier in Uttarakhand, about 30 km long."
    },
    {
        "unit": 2, "chapter": "झीलें / Lakes",
        "text_hi": "नैनीताल में झील का निर्माण किस भूवैज्ञानिक प्रक्रिया से हुआ?",
        "text_en": "Naini Lake in Nainital was formed by which geological process?",
        "options": ["भूस्खलन से / Landslide",
                    "हिमनद क्षरण से / Glacial erosion",
                    "ज्वालामुखी से / Volcanic activity",
                    "नदी बाढ़ से / River flooding"],
        "correct_answer": "भूस्खलन से / Landslide",
        "explanation_hi": "नैनीताल की झील का निर्माण भूस्खलन से नाले के अवरुद्ध होने के कारण हुआ था।",
        "explanation_en": "Naini Lake was formed by a landslide that blocked the drainage of the area."
    },
    {
        "unit": 2, "chapter": "जलवायु / Climate",
        "text_hi": "उत्तराखण्ड में सर्वाधिक वर्षा किस क्षेत्र में होती है?",
        "text_en": "Which region of Uttarakhand receives the highest rainfall?",
        "options": ["नैनीताल के निकट के क्षेत्र / Areas near Nainital",
                    "देहरादून घाटी / Dehradun valley",
                    "चमोली जनपद / Chamoli district",
                    "पिथौरागढ़ / Pithoragarh"],
        "correct_answer": "नैनीताल के निकट के क्षेत्र / Areas near Nainital",
        "explanation_hi": "नैनीताल और उसके आसपास के क्षेत्र (खुर्पाताल) में राज्य की सर्वाधिक वर्षा होती है।",
        "explanation_en": "The Nainital region (Khurpatal) receives the highest rainfall in Uttarakhand."
    },
    {
        "unit": 2, "chapter": "भूगोल / Geography",
        "text_hi": "उत्तराखण्ड में 'दून' से क्या अभिप्राय है?",
        "text_en": "What does 'Doon' mean in context of Uttarakhand?",
        "options": ["हिमालय और शिवालिक के बीच की घाटी / Valley between Himalayas and Shivalik",
                    "ऊँची पहाड़ी चोटी / High mountain peak",
                    "नदी का मुहाना / River mouth",
                    "वन क्षेत्र / Forest area"],
        "correct_answer": "हिमालय और शिवालिक के बीच की घाटी / Valley between Himalayas and Shivalik",
        "explanation_hi": "'दून' शिवालिक श्रेणी और मध्य हिमालय के बीच स्थित अनुदैर्ध्य घाटियाँ हैं। देहरादून, कोटद्वार-लैंसडाउन दून आदि प्रमुख हैं।",
        "explanation_en": "'Doon' refers to longitudinal valleys between the Shivalik and the Middle Himalayas. Dehradun is the most notable Doon valley."
    },

    # ══════════════════════════════════════════════════════════════════
    # UNIT 3 — इतिहास (History)
    # ══════════════════════════════════════════════════════════════════

    {
        "unit": 3, "chapter": "प्राचीन इतिहास / Ancient History",
        "text_hi": "उत्तराखण्ड का प्राचीन नाम क्या था?",
        "text_en": "What was the ancient name of Uttarakhand?",
        "options": ["केदारखण्ड और मानसखण्ड / Kedarakhand and Manaskhanda",
                    "उत्तरांचल और गढ़वाल / Uttaranchal and Garhwal",
                    "हिमाचल और देवखण्ड / Himachal and Devkhand",
                    "आर्यावर्त और कुरुक्षेत्र / Aryavarta and Kurukshetra"],
        "correct_answer": "केदारखण्ड और मानसखण्ड / Kedarakhand and Manaskhanda",
        "explanation_hi": "गढ़वाल क्षेत्र को प्राचीन काल में 'केदारखण्ड' और कुमाऊँ को 'मानसखण्ड' कहा जाता था।",
        "explanation_en": "In ancient times Garhwal was called 'Kedarakhand' and Kumaon was called 'Manaskhanda'."
    },
    {
        "unit": 3, "chapter": "कत्यूरी वंश / Katyuri Dynasty",
        "text_hi": "कत्यूरी वंश की राजधानी कहाँ थी?",
        "text_en": "Where was the capital of the Katyuri dynasty?",
        "options": ["कार्तिकेयपुर / Kartikeyapur",
                    "अल्मोड़ा / Almora",
                    "चम्पावत / Champawat",
                    "श्रीनगर / Srinagar"],
        "correct_answer": "कार्तिकेयपुर / Kartikeyapur",
        "explanation_hi": "कत्यूरी शासकों की राजधानी कार्तिकेयपुर थी, जो वर्तमान बागेश्वर जिले के निकट है।",
        "explanation_en": "The Katyuri rulers had their capital at Kartikeyapur, near present-day Baijnath in Bageshwar district."
    },
    {
        "unit": 3, "chapter": "चन्द वंश / Chand Dynasty",
        "text_hi": "कुमाऊँ में चन्द वंश की स्थापना किसने की थी?",
        "text_en": "Who founded the Chand dynasty in Kumaon?",
        "options": ["सोम चन्द / Som Chand",
                    "रुद्र चन्द / Rudra Chand",
                    "कल्याण चन्द / Kalyan Chand",
                    "भीष्म चन्द / Bhishma Chand"],
        "correct_answer": "सोम चन्द / Som Chand",
        "explanation_hi": "सोम चन्द ने 700 ई. के लगभग चम्पावत में चन्द वंश की स्थापना की थी।",
        "explanation_en": "Som Chand founded the Chand dynasty around 700 AD at Champawat."
    },
    {
        "unit": 3, "chapter": "पवार वंश / Pawar Dynasty",
        "text_hi": "गढ़वाल में पवार वंश को एकीकृत करने वाला शासक कौन था?",
        "text_en": "Which ruler unified Garhwal under the Pawar (Shah) dynasty?",
        "options": ["अजयपाल / Ajaypaal",
                    "प्रद्युम्न शाह / Pradyumna Shah",
                    "मानशाह / Manshah",
                    "लखनपाल / Lakhanpaal"],
        "correct_answer": "अजयपाल / Ajaypaal",
        "explanation_hi": "अजयपाल ने 52 गढ़ों को जीतकर गढ़वाल राज्य की स्थापना की और इन्हें 'गढ़पाल' की उपाधि मिली।",
        "explanation_en": "Ajaypaal conquered 52 forts and unified Garhwal, earning the title 'Gadhpaal'."
    },
    {
        "unit": 3, "chapter": "गोरखा आक्रमण / Gurkha Invasion",
        "text_hi": "गोरखाओं ने उत्तराखण्ड पर किस वर्ष आधिपत्य स्थापित किया?",
        "text_en": "In which year did the Gurkhas establish control over Uttarakhand?",
        "options": ["1815", "1803", "1791", "1820"],
        "correct_answer": "1803",
        "explanation_hi": "गोरखाओं ने 1803 में गढ़वाल और 1791 में कुमाऊँ पर अधिकार कर लिया था।",
        "explanation_en": "The Gurkhas captured Garhwal in 1803 and Kumaon in 1791."
    },
    {
        "unit": 3, "chapter": "ब्रिटिश शासन / British Rule",
        "text_hi": "उत्तराखण्ड में ब्रिटिश शासन किस संधि के बाद स्थापित हुआ?",
        "text_en": "After which treaty was British rule established in Uttarakhand?",
        "options": ["सुगौली संधि 1815 / Treaty of Sugauli 1815",
                    "इलाहाबाद संधि 1765 / Treaty of Allahabad 1765",
                    "लाहौर संधि 1846 / Treaty of Lahore 1846",
                    "सेरिंगपट्टम संधि 1799 / Treaty of Seringapatam 1799"],
        "correct_answer": "सुगौली संधि 1815 / Treaty of Sugauli 1815",
        "explanation_hi": "1815 की सुगौली संधि के बाद गोरखा शक्ति समाप्त हुई और उत्तराखण्ड ब्रिटिश नियंत्रण में आया।",
        "explanation_en": "After the Treaty of Sugauli 1815, Gurkha power ended and Uttarakhand came under British control."
    },
    {
        "unit": 3, "chapter": "स्वतंत्रता संग्राम / Freedom Movement",
        "text_hi": "'कुली बेगार' आन्दोलन किस वर्ष हुआ था?",
        "text_en": "In which year was the 'Kuli Begar' movement held?",
        "options": ["1921", "1915", "1930", "1942"],
        "correct_answer": "1921",
        "explanation_hi": "13-14 जनवरी 1921 को बागेश्वर में उत्तरायणी के अवसर पर बेगार रजिस्टरों को सरयू में प्रवाहित किया गया।",
        "explanation_en": "On 13-14 January 1921 at Bageshwar during Uttarayani, Begar registers were thrown into the Saryu river."
    },
    {
        "unit": 3, "chapter": "स्वतंत्रता संग्राम / Freedom Movement",
        "text_hi": "'कुमाऊँ केसरी' के नाम से किसे जाना जाता है?",
        "text_en": "Who is known as 'Kumaon Kesari' (Lion of Kumaon)?",
        "options": ["बद्रीदत्त पाण्डेय / Badri Dutt Pandey",
                    "हरगोविन्द पंत / Hargovind Pant",
                    "गोविन्द बल्लभ पंत / Govind Ballabh Pant",
                    "श्रीदेव सुमन / Sridev Suman"],
        "correct_answer": "बद्रीदत्त पाण्डेय / Badri Dutt Pandey",
        "explanation_hi": "बद्रीदत्त पाण्डेय को उनके राष्ट्रीय जागरण के कार्यों के कारण 'कुमाऊँ केसरी' कहा जाता है।",
        "explanation_en": "Badri Dutt Pandey is called 'Kumaon Kesari' for his contribution to the freedom movement."
    },
    {
        "unit": 3, "chapter": "स्वतंत्रता संग्राम / Freedom Movement",
        "text_hi": "पेशावर काण्ड के नायक चन्द्रसिंह गढ़वाली का सम्बन्ध किस जिले से था?",
        "text_en": "Veer Chandra Singh Garhwali of the Peshawar Kand was from which district?",
        "options": ["पौड़ी गढ़वाल / Pauri Garhwal",
                    "चमोली / Chamoli",
                    "टिहरी / Tehri",
                    "उत्तरकाशी / Uttarkashi"],
        "correct_answer": "पौड़ी गढ़वाल / Pauri Garhwal",
        "explanation_hi": "वीर चन्द्रसिंह गढ़वाली पौड़ी जिले के 'मासू' गाँव के निवासी थे।",
        "explanation_en": "Veer Chandra Singh Garhwali was from 'Masu' village in Pauri Garhwal district."
    },
    {
        "unit": 3, "chapter": "स्वतंत्रता संग्राम / Freedom Movement",
        "text_hi": "टिहरी राजशाही के विरुद्ध शहीद होने वाले श्रीदेव सुमन की मृत्यु कब हुई?",
        "text_en": "When did Sridev Suman die while fighting against the Tehri monarchy?",
        "options": ["25 जुलाई 1944 / 25 July 1944",
                    "15 अगस्त 1944 / 15 August 1944",
                    "30 जनवरी 1943 / 30 January 1943",
                    "10 मई 1945 / 10 May 1945"],
        "correct_answer": "25 जुलाई 1944 / 25 July 1944",
        "explanation_hi": "श्रीदेव सुमन ने 84 दिन की भूख हड़ताल के बाद 25 जुलाई 1944 को शहादत प्राप्त की।",
        "explanation_en": "Sridev Suman attained martyrdom on 25 July 1944 after an 84-day hunger strike."
    },

    # ══════════════════════════════════════════════════════════════════
    # UNIT 4 — कृषि, वन, खनिज, उद्योग (Agriculture, Forest, Minerals, Industry)
    # ══════════════════════════════════════════════════════════════════

    {
        "unit": 4, "chapter": "कृषि / Agriculture",
        "text_hi": "उत्तराखण्ड में 'सीढ़ीदार खेती' को क्या कहते हैं?",
        "text_en": "What is terrace farming called in Uttarakhand?",
        "options": ["खिल / Khil", "सेरा / Sera", "नाली / Nali", "उड़ार / Udar"],
        "correct_answer": "सेरा / Sera",
        "explanation_hi": "उत्तराखण्ड में पहाड़ी ढलानों पर सीढ़ीदार खेती को 'सेरा' कहा जाता है।",
        "explanation_en": "Terrace farming on mountain slopes in Uttarakhand is called 'Sera'."
    },
    {
        "unit": 4, "chapter": "कृषि / Agriculture",
        "text_hi": "उत्तराखण्ड की प्रमुख खाद्य फसल कौन सी है?",
        "text_en": "What is the main food crop of Uttarakhand?",
        "options": ["गेहूँ और धान / Wheat and Paddy",
                    "ज्वार और बाजरा / Jowar and Bajra",
                    "मक्का और दालें / Maize and Pulses",
                    "आलू और टमाटर / Potato and Tomato"],
        "correct_answer": "गेहूँ और धान / Wheat and Paddy",
        "explanation_hi": "उत्तराखण्ड की मुख्य खाद्य फसलें गेहूँ और धान हैं। मण्डुआ (Mandua) भी पारम्परिक अनाज है।",
        "explanation_en": "Wheat and Paddy are the main food crops of Uttarakhand. Mandua (finger millet) is also a traditional grain."
    },
    {
        "unit": 4, "chapter": "वन / Forests",
        "text_hi": "उत्तराखण्ड के कुल भूभाग का कितना प्रतिशत वनों से आच्छादित है?",
        "text_en": "What percentage of Uttarakhand's total area is covered by forests?",
        "options": ["लगभग 71% / About 71%",
                    "लगभग 55% / About 55%",
                    "लगभग 45% / About 45%",
                    "लगभग 82% / About 82%"],
        "correct_answer": "लगभग 71% / About 71%",
        "explanation_hi": "उत्तराखण्ड का लगभग 71% भूभाग वनों से आच्छादित है, जो देश में सर्वाधिक में से एक है।",
        "explanation_en": "About 71% of Uttarakhand's area is covered by forests, one of the highest proportions in India."
    },
    {
        "unit": 4, "chapter": "वन / Forests",
        "text_hi": "चिपको आन्दोलन की शुरुआत किस स्थान से हुई थी?",
        "text_en": "Where did the Chipko Movement originate?",
        "options": ["रैणी गाँव, चमोली / Raini village, Chamoli",
                    "टिहरी / Tehri",
                    "देहरादून / Dehradun",
                    "नैनीताल / Nainital"],
        "correct_answer": "रैणी गाँव, चमोली / Raini village, Chamoli",
        "explanation_hi": "1974 में गौरा देवी के नेतृत्व में चमोली जिले के रैणी गाँव से चिपको आन्दोलन शुरू हुआ था।",
        "explanation_en": "In 1974, Gaura Devi led women of Raini village in Chamoli to hug trees — beginning the Chipko Movement."
    },
    {
        "unit": 4, "chapter": "खनिज / Minerals",
        "text_hi": "उत्तराखण्ड में कौन सा खनिज सर्वाधिक मात्रा में पाया जाता है?",
        "text_en": "Which mineral is found in the largest quantity in Uttarakhand?",
        "options": ["चूना पत्थर / Limestone",
                    "सोना / Gold",
                    "ताँबा / Copper",
                    "कोयला / Coal"],
        "correct_answer": "चूना पत्थर / Limestone",
        "explanation_hi": "उत्तराखण्ड में चूना पत्थर प्रमुख खनिज है। सिम्ली (देहरादून), सिताड़गंज आदि में इसके भण्डार हैं।",
        "explanation_en": "Limestone is the most abundant mineral in Uttarakhand, found in Simli (Dehradun), Sitarganj, etc."
    },
    {
        "unit": 4, "chapter": "उद्योग / Industries",
        "text_hi": "उत्तराखण्ड का सबसे बड़ा औद्योगिक क्षेत्र कहाँ है?",
        "text_en": "Where is the largest industrial area of Uttarakhand?",
        "options": ["सिडकुल, हरिद्वार / SIDCUL, Haridwar",
                    "पंतनगर / Pantnagar",
                    "रुड़की / Roorkee",
                    "काशीपुर / Kashipur"],
        "correct_answer": "सिडकुल, हरिद्वार / SIDCUL, Haridwar",
        "explanation_hi": "हरिद्वार में SIDCUL (State Infrastructure and Industrial Development Corporation of Uttarakhand) उत्तराखण्ड का सबसे बड़ा औद्योगिक क्षेत्र है।",
        "explanation_en": "SIDCUL Haridwar is Uttarakhand's largest industrial estate."
    },
    {
        "unit": 4, "chapter": "ऊर्जा / Energy",
        "text_hi": "उत्तराखण्ड की सबसे बड़ी जलविद्युत परियोजना कौन सी है?",
        "text_en": "Which is the largest hydroelectric project in Uttarakhand?",
        "options": ["टिहरी जलविद्युत परियोजना / Tehri Hydro Power Project",
                    "विष्णुगाड़ / Vishnugad",
                    "रामगंगा / Ramganga",
                    "कोटेश्वर / Koteshwar"],
        "correct_answer": "टिहरी जलविद्युत परियोजना / Tehri Hydro Power Project",
        "explanation_hi": "टिहरी बाँध परियोजना (2400 MW) उत्तराखण्ड की सबसे बड़ी जलविद्युत परियोजना है। यह एशिया का सबसे ऊँचा बाँध है।",
        "explanation_en": "Tehri Dam Project (2400 MW) is Uttarakhand's largest hydro project and Asia's tallest dam."
    },

    # ══════════════════════════════════════════════════════════════════
    # UNIT 5 — संस्कृति, साहित्य, कला (Culture, Literature, Art)
    # ══════════════════════════════════════════════════════════════════

    {
        "unit": 5, "chapter": "लोकनृत्य / Folk Dances",
        "text_hi": "गढ़वाल का प्रसिद्ध लोकनृत्य कौन सा है?",
        "text_en": "What is the famous folk dance of Garhwal?",
        "options": ["लांगविर / Langvir", "छपेली / Chhapeli", "झोड़ा / Jhoda", "छोलिया / Chholia"],
        "correct_answer": "लांगविर / Langvir",
        "explanation_hi": "लांगविर और छपेली गढ़वाल के प्रमुख लोकनृत्य हैं। लांगविर एकल एक्रोबैटिक नृत्य है।",
        "explanation_en": "Langvir and Chhapeli are major folk dances of Garhwal. Langvir is a solo acrobatic dance."
    },
    {
        "unit": 5, "chapter": "लोकनृत्य / Folk Dances",
        "text_hi": "कुमाऊँ का प्रसिद्ध लोकनृत्य कौन सा है?",
        "text_en": "What is the famous folk dance of Kumaon?",
        "options": ["झोड़ा / Jhoda और छोलिया / Chholia",
                    "रासलीला / Raslila",
                    "कजरी / Kajri",
                    "घुमरा / Ghumra"],
        "correct_answer": "झोड़ा / Jhoda और छोलिया / Chholia",
        "explanation_hi": "झोड़ा और छोलिया कुमाऊँ के प्रमुख लोकनृत्य हैं। छोलिया योद्धाओं का नृत्य है।",
        "explanation_en": "Jhoda and Chholia are major folk dances of Kumaon. Chholia is a warrior dance."
    },
    {
        "unit": 5, "chapter": "लोकगीत / Folk Songs",
        "text_hi": "उत्तराखण्ड का सर्वाधिक लोकप्रिय लोकगीत कौन सा है?",
        "text_en": "Which is the most popular folk song form of Uttarakhand?",
        "options": ["न्यौली / Nyauli",
                    "भजन / Bhajan",
                    "ग़ज़ल / Ghazal",
                    "दादरा / Dadra"],
        "correct_answer": "न्यौली / Nyauli",
        "explanation_hi": "न्यौली उत्तराखण्ड का एक विरह-प्रधान लोकगीत है जो पहाड़ की महिलाओं द्वारा गाया जाता है।",
        "explanation_en": "Nyauli is a popular love and separation folk song form sung by women in the mountains of Uttarakhand."
    },
    {
        "unit": 5, "chapter": "मेले / Fairs",
        "text_hi": "उत्तराखण्ड का सबसे बड़ा पशु मेला कौन सा है?",
        "text_en": "Which is the largest cattle fair of Uttarakhand?",
        "options": ["देवीधुरा / Devidhura",
                    "गौचर / Gauchar",
                    "कुम्भ / Kumbh",
                    "नन्दा देवी / Nanda Devi"],
        "correct_answer": "गौचर / Gauchar",
        "explanation_hi": "चमोली जिले के गौचर में प्रतिवर्ष नवम्बर में उत्तराखण्ड का सबसे बड़ा पशु मेला लगता है।",
        "explanation_en": "The largest cattle fair of Uttarakhand is held at Gauchar in Chamoli district every November."
    },
    {
        "unit": 5, "chapter": "मेले / Fairs",
        "text_hi": "'बग्वाल' मेला किस स्थान पर आयोजित होता है?",
        "text_en": "'Bagwal' fair (stone-pelting festival) is held at which place?",
        "options": ["देवीधुरा, चम्पावत / Devidhura, Champawat",
                    "बागेश्वर / Bageshwar",
                    "अल्मोड़ा / Almora",
                    "पिथौरागढ़ / Pithoragarh"],
        "correct_answer": "देवीधुरा, चम्पावत / Devidhura, Champawat",
        "explanation_hi": "बग्वाल मेला (पत्थर युद्ध) चम्पावत जिले के देवीधुरा में प्रतिवर्ष रक्षाबन्धन पर आयोजित होता है।",
        "explanation_en": "Bagwal (stone-pelting) fair is held annually on Raksha Bandhan at Devidhura, Champawat."
    },
    {
        "unit": 5, "chapter": "साहित्य / Literature",
        "text_hi": "'गढ़वाल का शेक्सपियर' किसे कहा जाता है?",
        "text_en": "Who is called the 'Shakespeare of Garhwal'?",
        "options": ["लोकरत्न पंत 'गुमानी' / Lokratan Pant Gumani",
                    "गिरीश तिवारी 'गिर्दा' / Girish Tiwari Girda",
                    "विशम्भरदत्त सकलानी / Vishambhardatt Saklani",
                    "सुमित्रानंदन पंत / Sumitranandan Pant"],
        "correct_answer": "लोकरत्न पंत 'गुमानी' / Lokratan Pant Gumani",
        "explanation_hi": "19वीं सदी के कवि लोकरत्न पंत 'गुमानी' को कुमाऊँनी साहित्य का पितामह माना जाता है।",
        "explanation_en": "Lokratan Pant 'Gumani' (19th century) is considered the father of Kumaoni literature."
    },
    {
        "unit": 5, "chapter": "साहित्य / Literature",
        "text_hi": "सुमित्रानंदन पंत का जन्म उत्तराखण्ड के किस स्थान पर हुआ था?",
        "text_en": "Sumitranandan Pant was born at which place in Uttarakhand?",
        "options": ["कौसानी / Kausani",
                    "अल्मोड़ा / Almora",
                    "देहरादून / Dehradun",
                    "रानीखेत / Ranikhet"],
        "correct_answer": "कौसानी / Kausani",
        "explanation_hi": "हिन्दी के प्रकृति-कवि सुमित्रानंदन पंत का जन्म 1900 में बागेश्वर जिले के कौसानी में हुआ था।",
        "explanation_en": "Hindi nature poet Sumitranandan Pant was born in 1900 at Kausani in Bageshwar district."
    },
    {
        "unit": 5, "chapter": "कला / Art",
        "text_hi": "'ऐपण' क्या है?",
        "text_en": "What is 'Aipan'?",
        "options": ["कुमाऊँनी लोक चित्रकला / Kumaoni folk art",
                    "गढ़वाली लोकनृत्य / Garhwali folk dance",
                    "एक प्रकार का आभूषण / A type of ornament",
                    "पारम्परिक वाद्ययंत्र / Traditional musical instrument"],
        "correct_answer": "कुमाऊँनी लोक चित्रकला / Kumaoni folk art",
        "explanation_hi": "'ऐपण' कुमाऊँ की पारम्परिक लोक-चित्रकला है जो धार्मिक अवसरों पर भूमि व दीवारों पर बनाई जाती है।",
        "explanation_en": "'Aipan' is a traditional Kumaoni folk art painted on floors and walls during religious occasions."
    },

    # ══════════════════════════════════════════════════════════════════
    # UNIT 6 — शिक्षा, स्वास्थ्य, प्रशासन (Education, Health, Administration)
    # ══════════════════════════════════════════════════════════════════

    {
        "unit": 6, "chapter": "शिक्षा / Education",
        "text_hi": "उत्तराखण्ड का पहला विश्वविद्यालय कौन सा था?",
        "text_en": "Which was the first university of Uttarakhand?",
        "options": ["कुमाऊँ विश्वविद्यालय, नैनीताल / Kumaon University, Nainital",
                    "गढ़वाल विश्वविद्यालय, श्रीनगर / Garhwal University, Srinagar",
                    "देहरादून विश्वविद्यालय / Dehradun University",
                    "पंतनगर विश्वविद्यालय / Pantnagar University"],
        "correct_answer": "कुमाऊँ विश्वविद्यालय, नैनीताल / Kumaon University, Nainital",
        "explanation_hi": "1973 में स्थापित कुमाऊँ विश्वविद्यालय उत्तराखण्ड का पहला विश्वविद्यालय था।",
        "explanation_en": "Kumaon University established in 1973 was the first university of Uttarakhand."
    },
    {
        "unit": 6, "chapter": "शिक्षा / Education",
        "text_hi": "IIT Roorkee (रुड़की) की स्थापना किस वर्ष हुई थी?",
        "text_en": "In which year was IIT Roorkee established?",
        "options": ["1847", "1949", "1905", "1960"],
        "correct_answer": "1847",
        "explanation_hi": "रुड़की में थॉमसन कॉलेज ऑफ सिविल इंजीनियरिंग 1847 में स्थापित हुई, जो बाद में IIT रुड़की बनी — यह एशिया का पहला तकनीकी संस्थान था।",
        "explanation_en": "Thomason College of Civil Engineering was established at Roorkee in 1847, later becoming IIT Roorkee — Asia's first technical institute."
    },
    {
        "unit": 6, "chapter": "प्रशासन / Administration",
        "text_hi": "उत्तराखण्ड के प्रथम राज्यपाल कौन थे?",
        "text_en": "Who was the first Governor of Uttarakhand?",
        "options": ["सुरजीत सिंह बरनाला / Surjit Singh Barnala",
                    "सुदर्शन अग्रवाल / Sudarshan Agarwal",
                    "अज़ीज़ क़ुरैशी / Aziz Qureshi",
                    "बी.एल. जोशी / B.L. Joshi"],
        "correct_answer": "सुरजीत सिंह बरनाला / Surjit Singh Barnala",
        "explanation_hi": "सुरजीत सिंह बरनाला उत्तराखण्ड के प्रथम राज्यपाल थे (2000-2003)।",
        "explanation_en": "Surjit Singh Barnala was the first Governor of Uttarakhand (2000-2003)."
    },
    {
        "unit": 6, "chapter": "प्रशासन / Administration",
        "text_hi": "उत्तराखण्ड के प्रथम मुख्यमंत्री कौन थे?",
        "text_en": "Who was the first Chief Minister of Uttarakhand?",
        "options": ["नित्यानन्द स्वामी / Nityanand Swami",
                    "भगत सिंह कोश्यारी / Bhagat Singh Koshyari",
                    "एन. डी. तिवारी / N. D. Tiwari",
                    "बी. सी. खण्डूड़ी / B. C. Khanduri"],
        "correct_answer": "नित्यानन्द स्वामी / Nityanand Swami",
        "explanation_hi": "9 नवम्बर 2000 को नित्यानन्द स्वामी उत्तराखण्ड के प्रथम मुख्यमंत्री बने थे।",
        "explanation_en": "Nityanand Swami became the first Chief Minister of Uttarakhand on 9 November 2000."
    },
    {
        "unit": 6, "chapter": "प्रशासन / Administration",
        "text_hi": "उत्तराखण्ड उच्च न्यायालय कहाँ स्थित है?",
        "text_en": "Where is the Uttarakhand High Court located?",
        "options": ["नैनीताल / Nainital",
                    "देहरादून / Dehradun",
                    "हरिद्वार / Haridwar",
                    "पौड़ी / Pauri"],
        "correct_answer": "नैनीताल / Nainital",
        "explanation_hi": "उत्तराखण्ड का उच्च न्यायालय नैनीताल में स्थित है।",
        "explanation_en": "The High Court of Uttarakhand is located in Nainital."
    },
    {
        "unit": 6, "chapter": "राज्य गठन / State Formation",
        "text_hi": "उत्तराखण्ड का नाम 'उत्तरांचल' से 'उत्तराखण्ड' कब किया गया?",
        "text_en": "When was Uttarakhand renamed from 'Uttaranchal' to 'Uttarakhand'?",
        "options": ["1 जनवरी 2007 / 1 January 2007",
                    "9 नवम्बर 2006 / 9 November 2006",
                    "15 अगस्त 2008 / 15 August 2008",
                    "26 जनवरी 2010 / 26 January 2010"],
        "correct_answer": "1 जनवरी 2007 / 1 January 2007",
        "explanation_hi": "उत्तरांचल का नाम बदलकर उत्तराखण्ड 1 जनवरी 2007 को किया गया।",
        "explanation_en": "Uttaranchal was renamed Uttarakhand on 1 January 2007."
    },
    {
        "unit": 6, "chapter": "पर्यटन / Tourism",
        "text_hi": "उत्तराखण्ड में 'चार धाम यात्रा' में कौन से धाम शामिल हैं?",
        "text_en": "Which Dhams are included in Uttarakhand's 'Char Dham Yatra'?",
        "options": [
            "बदरीनाथ, केदारनाथ, गंगोत्री, यमुनोत्री",
            "बदरीनाथ, द्वारका, पुरी, रामेश्वरम",
            "केदारनाथ, तुंगनाथ, रुद्रनाथ, मध्यमहेश्वर",
            "ऋषिकेश, हरिद्वार, बदरीनाथ, केदारनाथ"
        ],
        "correct_answer": "बदरीनाथ, केदारनाथ, गंगोत्री, यमुनोत्री",
        "explanation_hi": "उत्तराखण्ड के 'छोटे चार धाम' बदरीनाथ, केदारनाथ, गंगोत्री और यमुनोत्री हैं।",
        "explanation_en": "Uttarakhand's 'Chhota Char Dham' includes Badrinath, Kedarnath, Gangotri, and Yamunotri."
    },
    {
        "unit": 6, "chapter": "पर्यटन / Tourism",
        "text_hi": "'पंच केदार' में कौन से तीर्थ शामिल हैं?",
        "text_en": "Which shrines are part of 'Panch Kedar'?",
        "options": [
            "केदारनाथ, तुंगनाथ, रुद्रनाथ, मध्यमहेश्वर, कल्पेश्वर",
            "केदारनाथ, बदरीनाथ, गंगोत्री, यमुनोत्री, हेमकुण्ड",
            "तुंगनाथ, चोपता, देवरियाताल, उखीमठ, गुप्तकाशी",
            "केदारनाथ, त्रियुगीनारायण, गुप्तकाशी, रुद्रनाथ, कल्पेश्वर"
        ],
        "correct_answer": "केदारनाथ, तुंगनाथ, रुद्रनाथ, मध्यमहेश्वर, कल्पेश्वर",
        "explanation_hi": "पंच केदार में पाँच शिव तीर्थ हैं — केदारनाथ, तुंगनाथ, रुद्रनाथ, मध्यमहेश्वर और कल्पेश्वर।",
        "explanation_en": "Panch Kedar consists of five Shiva shrines — Kedarnath, Tungnath, Rudranath, Madhyamaheshwar, and Kalpeshwar."
    },

    # ══════════════════════════════════════════════════════════════════
    # UNIT 7 — जनजातियाँ, विविध (Tribes, Miscellaneous)
    # ══════════════════════════════════════════════════════════════════

    {
        "unit": 7, "chapter": "जनजातियाँ / Tribes",
        "text_hi": "उत्तराखण्ड की प्रमुख जनजातियाँ कौन सी हैं?",
        "text_en": "What are the major tribes of Uttarakhand?",
        "options": [
            "थारू, बुक्सा, जौनसारी, भोटिया, राजी / Tharu, Buksa, Jaunsari, Bhotiya, Raji",
            "गद्दी, कोली, मीणा, भील",
            "नागा, बोडो, कार्बी, मिज़ो",
            "संथाल, मुण्डा, हो, ओराँव"
        ],
        "correct_answer": "थारू, बुक्सा, जौनसारी, भोटिया, राजी / Tharu, Buksa, Jaunsari, Bhotiya, Raji",
        "explanation_hi": "उत्तराखण्ड में पाँच अनुसूचित जनजातियाँ हैं — थारू, बुक्सा, जौनसारी, भोटिया और राजी (वनरावत)।",
        "explanation_en": "Uttarakhand has five Scheduled Tribes — Tharu, Buksa, Jaunsari, Bhotiya, and Raji (Vanraut)."
    },
    {
        "unit": 7, "chapter": "जनजातियाँ / Tribes",
        "text_hi": "'राजी' जनजाति को किस अन्य नाम से जाना जाता है?",
        "text_en": "By what other name is the 'Raji' tribe known?",
        "options": ["वनरावत / Vanraut",
                    "बनजारा / Banjara",
                    "खस / Khas",
                    "कोल / Kol"],
        "correct_answer": "वनरावत / Vanraut",
        "explanation_hi": "राजी जनजाति को 'वनरावत' भी कहते हैं। ये पिथौरागढ़ जिले के जंगलों में निवास करती है।",
        "explanation_en": "The Raji tribe is also called 'Vanraut'. They inhabit the forests of Pithoragarh district."
    },
    {
        "unit": 7, "chapter": "जनजातियाँ / Tribes",
        "text_hi": "'जौनसारी' जनजाति मुख्यतः किस क्षेत्र में निवास करती है?",
        "text_en": "The 'Jaunsari' tribe mainly inhabits which region?",
        "options": ["जौनसार-बावर क्षेत्र, देहरादून / Jaunsar-Bawar, Dehradun",
                    "नैनीताल / Nainital",
                    "पिथौरागढ़ / Pithoragarh",
                    "चमोली / Chamoli"],
        "correct_answer": "जौनसार-बावर क्षेत्र, देहरादून / Jaunsar-Bawar, Dehradun",
        "explanation_hi": "जौनसारी जनजाति देहरादून जिले के जौनसार-बावर क्षेत्र में निवास करती है।",
        "explanation_en": "The Jaunsari tribe inhabits the Jaunsar-Bawar region of Dehradun district."
    },
    {
        "unit": 7, "chapter": "जनजातियाँ / Tribes",
        "text_hi": "'भोटिया' जनजाति की मुख्य आर्थिक गतिविधि क्या है?",
        "text_en": "What is the main economic activity of the 'Bhotiya' tribe?",
        "options": ["ऊन व्यापार और पशुपालन / Wool trade and animal husbandry",
                    "मत्स्य पालन / Fishing",
                    "कृषि / Agriculture",
                    "खनन / Mining"],
        "correct_answer": "ऊन व्यापार और पशुपालन / Wool trade and animal husbandry",
        "explanation_hi": "भोटिया जनजाति परम्परागत रूप से तिब्बत के साथ ऊन और बोरा व्यापार तथा पशुपालन करती थी।",
        "explanation_en": "Bhotiya tribe traditionally engaged in wool trade with Tibet and animal husbandry."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "उत्तराखण्ड में लोकसभा की कितनी सीटें हैं?",
        "text_en": "How many Lok Sabha seats does Uttarakhand have?",
        "options": ["5", "7", "3", "4"],
        "correct_answer": "5",
        "explanation_hi": "उत्तराखण्ड में लोकसभा की 5 सीटें हैं — हरिद्वार, गढ़वाल, टिहरी, अल्मोड़ा और नैनीताल-ऊधमसिंहनगर।",
        "explanation_en": "Uttarakhand has 5 Lok Sabha seats — Haridwar, Garhwal, Tehri, Almora, and Nainital-Udham Singh Nagar."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "उत्तराखण्ड की साक्षरता दर (2011) कितनी थी?",
        "text_en": "What was the literacy rate of Uttarakhand as per Census 2011?",
        "options": ["78.82%", "70.10%", "85.43%", "68.25%"],
        "correct_answer": "78.82%",
        "explanation_hi": "2011 की जनगणना के अनुसार उत्तराखण्ड की साक्षरता दर 78.82% थी।",
        "explanation_en": "As per Census 2011, Uttarakhand's literacy rate was 78.82%."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "उत्तराखण्ड का सर्वाधिक जनसंख्या वाला जिला कौन सा है?",
        "text_en": "Which is the most populous district of Uttarakhand?",
        "options": ["हरिद्वार / Haridwar",
                    "देहरादून / Dehradun",
                    "नैनीताल / Nainital",
                    "ऊधमसिंहनगर / Udham Singh Nagar"],
        "correct_answer": "हरिद्वार / Haridwar",
        "explanation_hi": "2011 की जनगणना के अनुसार हरिद्वार उत्तराखण्ड का सर्वाधिक जनसंख्या वाला जिला है।",
        "explanation_en": "As per Census 2011, Haridwar is the most populous district of Uttarakhand."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "उत्तराखण्ड का सबसे कम जनसंख्या वाला जिला कौन सा है?",
        "text_en": "Which is the least populous district of Uttarakhand?",
        "options": ["रुद्रप्रयाग / Rudraprayag",
                    "चम्पावत / Champawat",
                    "बागेश्वर / Bageshwar",
                    "उत्तरकाशी / Uttarkashi"],
        "correct_answer": "रुद्रप्रयाग / Rudraprayag",
        "explanation_hi": "2011 की जनगणना के अनुसार रुद्रप्रयाग उत्तराखण्ड का न्यूनतम जनसंख्या वाला जिला है।",
        "explanation_en": "As per Census 2011, Rudraprayag is the least populous district of Uttarakhand."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "उत्तराखण्ड का सर्वाधिक क्षेत्रफल वाला जिला कौन सा है?",
        "text_en": "Which is the largest district of Uttarakhand by area?",
        "options": ["चमोली / Chamoli",
                    "उत्तरकाशी / Uttarkashi",
                    "पिथौरागढ़ / Pithoragarh",
                    "पौड़ी / Pauri"],
        "correct_answer": "चमोली / Chamoli",
        "explanation_hi": "चमोली जिला (8,030 वर्ग किमी) उत्तराखण्ड का सबसे बड़ा जिला है।",
        "explanation_en": "Chamoli district (8,030 sq km) is the largest district of Uttarakhand by area."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "उत्तराखण्ड का सबसे छोटा जिला (क्षेत्रफल में) कौन सा है?",
        "text_en": "Which is the smallest district of Uttarakhand by area?",
        "options": ["चम्पावत / Champawat",
                    "रुद्रप्रयाग / Rudraprayag",
                    "बागेश्वर / Bageshwar",
                    "हरिद्वार / Haridwar"],
        "correct_answer": "चम्पावत / Champawat",
        "explanation_hi": "चम्पावत (1,766 वर्ग किमी) उत्तराखण्ड का क्षेत्रफल की दृष्टि से सबसे छोटा जिला है।",
        "explanation_en": "Champawat (1,766 sq km) is the smallest district of Uttarakhand by area."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "नन्दा देवी राष्ट्रीय उद्यान को यूनेस्को विश्व धरोहर स्थल का दर्जा कब मिला?",
        "text_en": "When was Nanda Devi National Park declared a UNESCO World Heritage Site?",
        "options": ["1988", "1995", "2001", "2005"],
        "correct_answer": "1988",
        "explanation_hi": "नन्दा देवी राष्ट्रीय उद्यान को 1988 में यूनेस्को विश्व धरोहर स्थल घोषित किया गया। फूलों की घाटी 2005 में शामिल हुई।",
        "explanation_en": "Nanda Devi National Park was declared UNESCO World Heritage Site in 1988. Valley of Flowers was added in 2005."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "जिम कॉर्बेट राष्ट्रीय उद्यान किस जिले में स्थित है?",
        "text_en": "Jim Corbett National Park is located in which district?",
        "options": ["नैनीताल / Nainital",
                    "रामनगर / Ramnagar",
                    "पौड़ी / Pauri",
                    "अल्मोड़ा / Almora"],
        "correct_answer": "नैनीताल / Nainital",
        "explanation_hi": "जिम कॉर्बेट राष्ट्रीय उद्यान नैनीताल जिले के रामनगर में स्थित है। यह भारत का पहला राष्ट्रीय उद्यान (1936) है।",
        "explanation_en": "Jim Corbett National Park is in Ramnagar, Nainital district. It is India's first national park (1936)."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "उत्तराखण्ड में 'स्काउटिंग' की शुरुआत किस नाम से की गई थी?",
        "text_en": "Under which scheme was 'Scouting' first started in Uttarakhand?",
        "options": ["गर्ल गाइड्स / Girl Guides",
                    "होम गार्ड / Home Guard",
                    "सेना भर्ती / Army Recruitment",
                    "एनसीसी / NCC"],
        "correct_answer": "गर्ल गाइड्स / Girl Guides",
        "explanation_hi": "उत्तराखण्ड में स्काउटिंग की शुरुआत गर्ल गाइड्स के रूप में हुई थी।",
        "explanation_en": "Scouting was first started in Uttarakhand under the Girl Guides scheme."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "उत्तराखण्ड में 'नन्दा राज जात यात्रा' कितने वर्षों में एक बार आयोजित होती है?",
        "text_en": "How often is the 'Nanda Raj Jat Yatra' held in Uttarakhand?",
        "options": ["12 वर्ष / 12 years",
                    "6 वर्ष / 6 years",
                    "3 वर्ष / 3 years",
                    "हर वर्ष / Every year"],
        "correct_answer": "12 वर्ष / 12 years",
        "explanation_hi": "नन्दा राज जात यात्रा प्रत्येक 12 वर्षों में एक बार आयोजित होती है। यह विश्व की सबसे लम्बी पैदल धार्मिक यात्रा मानी जाती है।",
        "explanation_en": "Nanda Raj Jat Yatra is held once every 12 years. It is considered the world's longest religious trek."
    },
    {
        "unit": 7, "chapter": "विविध / Miscellaneous",
        "text_hi": "उत्तराखण्ड की अर्थव्यवस्था का प्रमुख आधार क्या है?",
        "text_en": "What is the primary base of Uttarakhand's economy?",
        "options": ["कृषि और पर्यटन / Agriculture and Tourism",
                    "खनन और उद्योग / Mining and Industry",
                    "IT उद्योग / IT Industry",
                    "मत्स्य पालन / Fisheries"],
        "correct_answer": "कृषि और पर्यटन / Agriculture and Tourism",
        "explanation_hi": "उत्तराखण्ड की अर्थव्यवस्था मुख्यतः कृषि, पर्यटन और जलविद्युत पर निर्भर है।",
        "explanation_en": "Uttarakhand's economy primarily depends on agriculture, tourism, and hydropower."
    },
]
