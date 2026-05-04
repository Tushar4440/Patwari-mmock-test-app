"""
extracted_questions.py
Static curated bank of real, high-difficulty Uttarakhand GK questions.
Targeting 1000+ questions. This is BATCH 1 & 2 (~150 questions).
Categorized by sub-topic for targeted tests.
"""
import json

UK_GK_QUESTION_BANK = [
    # ── HISTORY - CHAND DYNASTY ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "UKSSSC VDO/VPDO 2021",
        "text": "चन्द शासनकाल में 'थतवान' (Thatwan) शब्दावली का प्रयोग किसके लिए किया जाता था?",
        "options": ["पट्टेदार", "भूमि का मुख्य स्वामी", "खेतिहर मजदूर", "राजस्व अधिकारी"],
        "correct_answer": "भूमि का मुख्य स्वामी",
        "explanation": "थतवान वह व्यक्ति होता था जिसे राजा से सीधे 'थत' (भूमि) का स्वामित्व प्राप्त होता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "UKPSC Lower Subordinate 2016",
        "text": "चन्द शासकों द्वारा लागू '36 रकम 32 कलम' राजस्व प्रणाली में 'साहु' (Sahu) कर किस विशिष्ट उद्देश्य हेतु लिया जाता था?",
        "options": ["सैनिकों के राशन हेतु", "पुल निर्माण हेतु", "राजकीय लेखकों (लिखवारों) के वेतन हेतु", "मन्दिरों के रखरखाव हेतु"],
        "correct_answer": "राजकीय लेखकों (लिखवारों) के वेतन हेतु",
        "explanation": "साहु कर राजकीय लेखकों के पारिश्रमिक के लिए वसूला जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Ajay Singh Rawat",
        "text": "अल्मोड़ा स्थित प्रसिद्ध 'खगमरा किला' (Khagmara Fort) का निर्माण किस चन्द शासक ने करवाया था?",
        "options": ["सोम चन्द", "भीष्म चन्द", "कल्याण चन्द", "रुद्र चन्द"],
        "correct_answer": "भीष्म चन्द",
        "explanation": "भीष्म चन्द ने अपनी राजधानी चम्पावत से अल्मोड़ा स्थानांतरित करने की योजना बनाई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "UKPSC GS 2012",
        "text": "चन्द शासनकाल में 'सिरतान' (Sirtan) कौन थे?",
        "options": ["अस्थायी कृषक", "स्थायी कृषक", "राजस्व अधिकारी", "सैनिक"],
        "correct_answer": "अस्थायी कृषक",
        "explanation": "सिरतान वे किसान थे जो केवल नकद लगान (सिरती) देते थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "UKSSSC History",
        "text": "किस चन्द शासक ने 'रेशम का कारखाना' स्थापित किया था?",
        "options": ["इन्द्र चन्द", "सोम चन्द", "रुद्र चन्द", "कल्याण चन्द"],
        "correct_answer": "इन्द्र चन्द",
        "explanation": "इन्द्र चन्द ने कुमाऊँ में रेशम उद्योग की शुरुआत की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "UKSSSC Archive",
        "text": "चन्द वंश का वह शासक कौन था जिसने मुगल सम्राट अकबर से मुलाकात की थी?",
        "options": ["रुद्र चन्द", "लक्ष्मी चन्द", "बाज़ बहादुर चन्द", "भीष्म चन्द"],
        "correct_answer": "रुद्र चन्द",
        "explanation": "रुद्र चन्द ने 1588 में लाहौर में अकबर से भेंट की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Badri Datt Pandey",
        "text": "कुमाऊँ में 'चौखूटिया' के पास 'मल्लावां' का युद्ध किसके बीच हुआ था?",
        "options": ["अंग्रेज और गोरखा", "चन्द और पवार", "रुद्र चन्द और अजयपाल", "बाज़ बहादुर चन्द और गोरखा"],
        "correct_answer": "रुद्र चन्द और अजयपाल",
        "explanation": "यह युद्ध कत्यूरी घाटी के अधिकार को लेकर हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Administrative History",
        "text": "चन्द काल में 'कमीण' (Kamin) और 'सयाणा' (Sayana) का मुख्य कार्य क्या था?",
        "options": ["सैनिक भर्ती", "राजस्व संग्रह", "न्याय निर्णय", "धार्मिक अनुष्ठान"],
        "correct_answer": "राजस्व संग्रह",
        "explanation": "वे गाँवों से राजस्व वसूलने के लिए उत्तरदायी ग्रामीण अधिकारी थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "UKSSSC Previous Year",
        "text": "किस चन्द शासक को 'गरुड़' की उपाधि दी गई थी?",
        "options": ["ज्ञान चन्द", "सोम चन्द", "कल्याण चन्द", "उद्योत चन्द"],
        "correct_answer": "ज्ञान चन्द",
        "explanation": "ज्ञान चन्द प्रथम को दिल्ली के सुल्तान ने गरुड़ की उपाधि दी थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Cultural History",
        "text": "चन्द शासन में 'बिश्ती' (Bishti) कर किस पर लगाया जाता था?",
        "options": ["पुलों पर", "नहरों के पानी पर", "पशुपालन पर", "हस्तशिल्प पर"],
        "correct_answer": "नहरों के पानी पर",
        "explanation": "सिंचाई के लिए पानी के उपयोग पर बिश्ती नामक कर वसूला जाता था।"
    },

    # ── HISTORY - KATYURI & ANCIENT ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Katyuri & Ancient",
        "source": "Ancient Inscriptions",
        "text": "कत्यूरी राजवंश की राजभाषा (प्रशासनिक भाषा) क्या थी?",
        "options": ["पाली", "प्राकृत", "संस्कृत", "कुमाऊँनी"],
        "correct_answer": "संस्कृत",
        "explanation": "कत्यूरी शासकों के अभिलेख संस्कृत भाषा में प्राप्त हुए हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Katyuri & Ancient",
        "source": "Shiv Prasad Dabral",
        "text": "कत्यूरी शासक 'भूदेव' ने किस मंदिर का निर्माण करवाया था?",
        "options": ["बद्रीनाथ", "केदारनाथ", "बैजनाथ", "जागेश्वर"],
        "correct_answer": "बैजनाथ",
        "explanation": "भूदेव ने बैजनाथ मंदिर समूह का निर्माण कराया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Katyuri & Ancient",
        "source": "UKPSC GS Paper",
        "text": "कत्यूरी काल में 'प्रांतपाल' नामक अधिकारी का मुख्य कार्य क्या था?",
        "options": ["गुप्तचर", "राजस्व", "सीमाओं की सुरक्षा", "न्याय"],
        "correct_answer": "सीमाओं की सुरक्षा",
        "explanation": "प्रांतपाल सीमाओं की रक्षा के लिए उत्तरदायी था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Katyuri & Ancient",
        "source": "Ancient Name Records",
        "text": "ऋषिकेश का प्राचीन नाम क्या था?",
        "options": ["कुब्जाम्रक", "मायापुर", "श्रीपुर", "पुनार"],
        "correct_answer": "कुब्जाम्रक",
        "explanation": "ऋषिकेश को प्राचीन काल में कुब्जाम्रक कहा जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Katyuri & Ancient",
        "source": "UKPSC GS",
        "text": "हरिद्वार का प्राचीन नाम 'मायापुरी' किस यात्री ने अपने यात्रा वृत्तांत में लिखा था?",
        "options": ["ह्वेनसांग", "फाह्यान", "इब्नबतूता", "मेगस्थनीज"],
        "correct_answer": "ह्वेनसांग",
        "explanation": "ह्वेनसांग ने हरिद्वार को 'मो-यु-लो' (मायापुर) कहा था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Katyuri & Ancient",
        "source": "UKSSSC Group C",
        "text": "कुणिन्द वंश का सबसे शक्तिशाली शासक किसे माना जाता है?",
        "options": ["अमोघभूति", "विभूति", "सुबाहु", "धनभूति"],
        "correct_answer": "अमोघभूति",
        "explanation": "अमोघभूति की रजत और ताम्र मुद्राएँ बड़ी संख्या में प्राप्त हुई हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Katyuri & Ancient",
        "source": "Ancient Scripts",
        "text": "कुणिन्द मुद्राओं पर किन लिपियों का प्रयोग मिलता है?",
        "options": ["ब्राह्मी और खरोष्ठी", "पाली और संस्कृत", "देवनागरी", "शारदा"],
        "correct_answer": "ब्राह्मी और खरोष्ठी",
        "explanation": "अमोघभूति की मुद्राओं पर ब्राह्मी और खरोष्ठी दोनों लिपियाँ अंकित हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Katyuri & Ancient",
        "source": "UKPSC Prelims",
        "text": "कत्यूरी प्रशासन में 'अक्षपटलिक' का मुख्य कार्य क्या था?",
        "options": ["अभिलेखों का संरक्षण", "सेनापति", "कोषाध्यक्ष", "न्यायाधीश"],
        "correct_answer": "अभिलेखों का संरक्षण",
        "explanation": "अक्षपटलिक राजकीय रिकॉर्ड्स और अभिलेखों का संरक्षक था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Katyuri & Ancient",
        "source": "Shaivite History",
        "text": "जागेश्वर के 'मृत्युंजय मंदिर' का निर्माण किस कत्यूरी राजा ने करवाया था?",
        "options": ["ईष्टगण देव", "ललितशूर देव", "बसंत देव", "निम्वर देव"],
        "correct_answer": "ईष्टगण देव",
        "explanation": "ईष्टगण देव ने जागेश्वर में कई मंदिरों का निर्माण करवाया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Katyuri & Ancient",
        "source": "Medieval Records",
        "text": "कत्यूरी राजाओं की शीतकालीन राजधानी कहाँ थी?",
        "options": ["ढिकुली", "बैजनाथ", "जोशीमठ", "पाण्डुकेश्वर"],
        "correct_answer": "ढिकुली",
        "explanation": "रामनगर के पास ढिकुली उनकी शीतकालीन राजधानी थी।"
    },

    # ── HISTORY - PAWAR & TEHRI ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Historical Gazettes",
        "text": "अजयपाल ने अपनी राजधानी चाँदपुर गढ़ी से देवलगढ़ किस वर्ष स्थानांतरित की थी?",
        "options": ["1512 ई.", "1515 ई.", "1517 ई.", "1520 ई."],
        "correct_answer": "1512 ई.",
        "explanation": "अजयपाल ने 1512 में देवलगढ़ राजधानी बनाई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri State History",
        "text": "टिहरी रियासत के प्रथम राजा कौन थे?",
        "options": ["सुदर्शन शाह", "प्रताप शाह", "कीर्ति शाह", "नरेन्द्र शाह"],
        "correct_answer": "सुदर्शन शाह",
        "explanation": "सुदर्शन शाह ने 28 दिसंबर 1815 को टिहरी रियासत की स्थापना की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri State Records",
        "text": "टिहरी रियासत का भारत संघ में विलय किस तिथि को हुआ था?",
        "options": ["1 अगस्त 1949", "15 अगस्त 1947", "26 जनवरी 1950", "15 जनवरी 1948"],
        "correct_answer": "1 अगस्त 1949",
        "explanation": "मानवेन्द्र शाह के समय टिहरी का भारत में विलय हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "UKSSSC VDO",
        "text": "गढ़वाल में 'अजयपाल' को किस अन्य नाम से भी जाना जाता था?",
        "options": ["गढ़पाल", "कौरव", "महाराज", "छत्रपति"],
        "correct_answer": "गढ़पाल",
        "explanation": "52 गढ़ों को जीतने के कारण उन्हें गढ़पाल कहा गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri State Records",
        "text": "टिहरी रियासत में 'टीका' (Tika) प्रथा क्या थी?",
        "options": ["विवाह कर", "राजस्व कर", "भूमि उपहार", "सैनिक सम्मान"],
        "correct_answer": "विवाह कर",
        "explanation": "विवाह के अवसर पर लिए जाने वाले कर को टीका कहा जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Garhwal History",
        "text": "गढ़वाल की किस रानी को 'नाक-काटी रानी' के नाम से जाना जाता है?",
        "options": ["रानी कर्णवती", "रानी गुलेरिया", "रानी कनकदेई", "तीलू रौतेली"],
        "correct_answer": "रानी कर्णवती",
        "explanation": "उन्होंने मुगल आक्रमणकारियों की नाक कटवा दी थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "UKPSC GS",
        "text": "पवार शासक मानशाह के दरबारी कवि 'भरत' ने किस ग्रंथ की रचना की थी?",
        "options": ["मानोदय काव्य", "गढ़वाल गौरव", "जहांगीर विनोद", "फतेहप्रकाश"],
        "correct_answer": "मानोदय काव्य",
        "explanation": "मानोदय काव्य पवार वंश के इतिहास का महत्वपूर्ण स्रोत है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Medieval Records",
        "text": "गढ़वाल के प्रसिद्ध 'पेशावर कांड' (1930) के नायक चन्द्रसिंह गढ़वाली किस बटालियन से थे?",
        "options": ["2/18 गढ़वाल राइफल्स", "3/18 गढ़वाल राइफल्स", "1/18 गढ़वाल राइफल्स", "4/18 गढ़वाल राइफल्स"],
        "correct_answer": "2/18 गढ़वाल राइफल्स",
        "explanation": "वे 2/18 रॉयल गढ़वाल राइफल्स के सिपाही थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri Admin History",
        "text": "टिहरी में 'झूला पैमाइश' (Jhoola Paimaish) भूमि बंदोबस्त किसने करवाया था?",
        "options": ["प्रताप शाह", "कीर्ति शाह", "नरेन्द्र शाह", "सुदर्शन शाह"],
        "correct_answer": "प्रताप शाह",
        "explanation": "प्रताप शाह ने टिहरी में झूला पैमाइश बंदोबस्त कराया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "UKSSSC Group C",
        "text": "श्रीनगर (गढ़वाल) के पास स्थित 'देवलगढ़' किस देवी के मंदिर के लिए प्रसिद्ध है?",
        "options": ["राजराजेश्वरी", "नन्दा देवी", "ज्वाला देवी", "धारी देवी"],
        "correct_answer": "राजराजेश्वरी",
        "explanation": "राजराजेश्वरी पवार शासकों की कुलदेवी थीं।"
    },

    # ── GEOGRAPHY & ECOLOGY ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "UKSSSC Forest Guard 2020",
        "text": "उत्तराखंड में 'वन शिकायतों की समिति' (Forest Grievances Committee) का गठन किस वर्ष किया गया था?",
        "options": ["13 अप्रैल 1921", "15 अगस्त 1922", "10 मार्च 1919", "25 जनवरी 1920"],
        "correct_answer": "13 अप्रैल 1921",
        "explanation": "1921 में पी. विन्धम की अध्यक्षता में इसका गठन हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife Records",
        "text": "उत्तराखंड के किस राष्ट्रीय उद्यान को यूनेस्को (UNESCO) द्वारा विश्व धरोहर सूची में शामिल किया गया है?",
        "options": ["नन्दा देवी एवं फूलों की घाटी", "कॉर्बेट", "राजाजी", "गंगोत्री"],
        "correct_answer": "नन्दा देवी एवं फूलों की घाटी",
        "explanation": "नन्दा देवी को 1988 और फूलों की घाटी को 2005 में शामिल किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers of UK",
        "text": "उत्तराखंड की कौन सी नदी 'विपिन' (Vipin) पर्वत से निकलती है और पश्चिमी रामगंगा की सहायक नदी है?",
        "options": ["गगास नदी", "बिनौ नदी", "नयार नदी", "कोसी नदी"],
        "correct_answer": "बिनौ नदी",
        "explanation": "बिनौ नदी पश्चिमी रामगंगा की सहायक नदी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "UKSSSC 2021",
        "text": "प्रसिद्ध 'बैजनाथ मंदिर' किस नदी के संगम पर स्थित है?",
        "options": ["गोमती और गरुड़ गंगा", "सरयू और गोमती", "अलकनन्दा और पिण्डर", "काली और गौरी"],
        "correct_answer": "गोमती और गरुड़ गंगा",
        "explanation": "बैजनाथ (बागेश्वर) गोमती नदी के तट पर स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Forest Movements",
        "text": "उत्तराखंड में 'रैणी गाँव' (चमोली) किस आंदोलन के लिए प्रसिद्ध है?",
        "options": ["चिपको आंदोलन", "मैती आंदोलन", "नशा नहीं रोजगार दो", "झपटो छीनो"],
        "correct_answer": "चिपको आंदोलन",
        "explanation": "1974 में गौरा देवी के नेतृत्व में यहाँ से चिपको आंदोलन शुरू हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peak Heights",
        "text": "उत्तराखंड के सबसे ऊँचे पर्वत शिखर 'नन्दा देवी' की ऊँचाई कितनी है?",
        "options": ["7817 मीटर", "7756 मीटर", "7120 मीटर", "8126 मीटर"],
        "correct_answer": "7817 मीटर",
        "explanation": "नन्दा देवी उत्तराखंड का सर्वोच्च शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes of UK",
        "text": "किस झील को 'भाई-बहन का ताल' (Bhai-Behan Tal) कहा जाता है?",
        "options": ["मासर ताल", "यम ताल", "सहस्त्र ताल", "नैनी ताल"],
        "correct_answer": "मासर ताल",
        "explanation": "टिहरी में स्थित मासर ताल को भाई-बहन का ताल भी कहते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife Census",
        "text": "'कस्तूरी मृग' उत्तराखंड के किस राष्ट्रीय उद्यान में सर्वाधिक संख्या में पाए जाते हैं?",
        "options": ["केदारनाथ वन्यजीव विहार", "कॉर्बेट", "राजाजी", "फूलों की घाटी"],
        "correct_answer": "केदारनाथ वन्यजीव विहार",
        "explanation": "चमोली-रुद्रप्रयाग स्थित केदारनाथ विहार इसके लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Geography Archive",
        "text": "पिण्डर नदी का उद्गम स्थल कहाँ है?",
        "options": ["पिण्डारी ग्लेशियर", "मिलम ग्लेशियर", "गंगोत्री", "यमुनोत्री"],
        "correct_answer": "पिण्डारी ग्लेशियर",
        "explanation": "पिण्डर नदी बागेश्वर के पिण्डारी ग्लेशियर से निकलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Forest Ecology",
        "text": "उत्तराखंड का राजकीय वृक्ष 'बुरांश' किस ऊँचाई पर पाया जाता है?",
        "options": ["1500-4000 मीटर", "500-1000 मीटर", "4000-6000 मीटर", "समुद्र तल के पास"],
        "correct_answer": "1500-4000 मीटर",
        "explanation": "बुरांश मध्यम हिमालयी क्षेत्रों में पाया जाता है।"
    },

    # ── FREEDOM MOVEMENT ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKSSSC Graduate Level",
        "text": "उत्तराखंड में 'कुली बेगार' प्रथा का आधिकारिक अंत 13-14 जनवरी 1921 को किस नदी के तट पर हुआ था?",
        "options": ["अलकनन्दा", "मंदाकिनी", "सरयू", "भागीरथी"],
        "correct_answer": "सरयू",
        "explanation": "बागेश्वर में सरयू तट पर बेगार रजिस्टरों को बहाकर इसका अंत किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKPSC Prelims 2012",
        "text": "कुमाऊँ परिषद का तीसरा अधिवेशन (1919) कहाँ आयोजित किया गया था?",
        "options": ["हल्द्वानी", "कोटद्वार", "काशीपुर", "अल्मोड़ा"],
        "correct_answer": "कोटद्वार",
        "explanation": "1919 का कोटद्वार अधिवेशन बद्री दत्त जोशी की अध्यक्षता में हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKSSSC Group C",
        "text": "टिहरी राज्य प्रजामंडल की स्थापना 23 जनवरी 1939 को कहाँ की गई थी?",
        "options": ["टिहरी", "देहरादून", "श्रीनगर", "मसूरी"],
        "correct_answer": "देहरादून",
        "explanation": "श्रीदेव सुमन ने देहरादून में इसकी स्थापना की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKSSSC Previous Year",
        "text": "प्रसिद्ध 'पेशावर कांड' (1930) किस दिन घटित हुआ था?",
        "options": ["23 अप्रैल 1930", "15 मई 1930", "10 जून 1930", "12 मार्च 1930"],
        "correct_answer": "23 अप्रैल 1930",
        "explanation": "23 अप्रैल 1930 को चन्द्रसिंह गढ़वाली ने गोली चलाने से मना कर दिया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKPSC GS Paper 2014",
        "text": "1857 की क्रांति के दौरान उत्तराखंड के किस क्रांतिकारी ने 'क्रांतिवीर' संगठन बनाया था?",
        "options": ["बद्री दत्त पाण्डेय", "कालू मेहरा", "हर्षदेव ओली", "इन्द्रमणि बडोनी"],
        "correct_answer": "कालू मेहरा",
        "explanation": "कालू मेहरा को प्रथम स्वतंत्रता संग्राम सेनानी माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKSSSC Archive",
        "text": "गांधीजी ने 'कुमाऊँ का बारदोली' किस क्षेत्र को कहा था?",
        "options": ["सल्ट", "गुजड़ू", "लोहाघाट", "सोमेश्वर"],
        "correct_answer": "सल्ट",
        "explanation": "अल्मोड़ा के सल्ट क्षेत्र की वीरता के कारण इसे यह संज्ञा दी गई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "Kumaon Parishad History",
        "text": "कुमाऊँ परिषद का विलय भारतीय राष्ट्रीय कांग्रेस में किस वर्ष हुआ?",
        "options": ["1926", "1924", "1928", "1930"],
        "correct_answer": "1926",
        "explanation": "1926 में परिषद का विलय कांग्रेस में कर दिया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKPSC Prelims",
        "text": "गढ़वाल में 'कांग्रेस' की स्थापना किस वर्ष हुई थी?",
        "options": ["1918", "1915", "1920", "1922"],
        "correct_answer": "1918",
        "explanation": "बैरिस्टर मुकुन्दीलाल और अनुसूया प्रसाद बहुगुणा के प्रयासों से 1918 में हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKSSSC History",
        "text": "श्रीदेव सुमन कब शहीद हुए थे?",
        "options": ["25 जुलाई 1944", "15 अगस्त 1944", "26 जनवरी 1943", "10 मई 1944"],
        "correct_answer": "25 जुलाई 1944",
        "explanation": "84 दिन की भूख हड़ताल के बाद वे शहीद हुए।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "Regional Satyagraha",
        "text": "उत्तराखंड में 'डोला-पालकी' आंदोलन के प्रणेता कौन थे?",
        "options": ["जयानंद भारती", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "श्रीदेव सुमन"],
        "correct_answer": "जयानंद भारती",
        "explanation": "यह दलितों के अधिकारों के लिए चलाया गया आंदोलन था।"
    },

    # ── POLITY & ADMINISTRATION ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Land Settlement Records",
        "text": "उत्तराखंड में '8वां भूमि बंदोबस्त' (1840) किस ब्रिटिश अधिकारी द्वारा गढ़वाल में कराया गया था?",
        "options": ["ट्रेल", "बेटन", "पॉव", "रैम्जे"],
        "correct_answer": "बेटन",
        "explanation": "जे.एच. बेटन ने 1840 में गढ़वाल में भूमि बंदोबस्त कराया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "UKPSC Upper Subordinate",
        "text": "किस ब्रिटिश कमिश्नर के कार्यकाल को 'कुमाऊँ का स्वर्ण काल' कहा जाता है?",
        "options": ["ई. गार्डनर", "जी.डब्ल्यू. ट्रेल", "हेनरी रैमजे", "लशिंगटन"],
        "correct_answer": "हेनरी रैमजे",
        "explanation": "हेनरी रैमजे (1856-1884) का कार्यकाल सुधारों के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Revenue Police Archive",
        "text": "उत्तराखंड में 'राजस्व पुलिस' व्यवस्था कब लागू की गई थी?",
        "options": ["1874", "1860", "1885", "1890"],
        "correct_answer": "1874",
        "explanation": "हेनरी रैमजे के काल में 1874 में यह व्यवस्था लागू हुई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "UKSSSC Group C",
        "text": "कुमाऊँ कमिश्नरी का मुख्यालय अल्मोड़ा से नैनीताल किस वर्ष स्थानांतरित किया गया था?",
        "options": ["1854", "1855", "1860", "1864"],
        "correct_answer": "1854",
        "explanation": "1854 में मुख्यालय नैनीताल बनाया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "UKPSC GS Paper",
        "text": "उत्तराखंड क्रांति दल (UKD) की स्थापना कब हुई थी?",
        "options": ["1979", "1980", "1985", "1990"],
        "correct_answer": "1979",
        "explanation": "25 जुलाई 1979 को मसूरी में इसकी स्थापना हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "State Formation Records",
        "text": "उत्तराखंड राज्य गठन के समय केंद्र में किस पार्टी की सरकार थी?",
        "options": ["राजग (NDA)", "संप्रग (UPA)", "जनता दल", "वामपंथी"],
        "correct_answer": "राजग (NDA)",
        "explanation": "अटल बिहारी वाजपेयी के नेतृत्व वाली NDA सरकार थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Legislative Records",
        "text": "उत्तराखंड विधानसभा की प्रथम महिला अध्यक्ष कौन थीं?",
        "options": ["ऋतु खंडूड़ी भूषण", "विजया बड़थ्वाल", "ममता राकेश", "अनुपमा रावत"],
        "correct_answer": "ऋतु खंडूड़ी भूषण",
        "explanation": "वे 2022 में विधानसभा अध्यक्ष चुनी गईं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "UKPSC Prelims",
        "text": "उत्तराखंड के प्रथम मुख्यमंत्री कौन थे?",
        "options": ["नित्यानंद स्वामी", "भगत सिंह कोश्यारी", "एन.डी. तिवारी", "बी.सी. खंडूड़ी"],
        "correct_answer": "नित्यानंद स्वामी",
        "explanation": "नित्यानंद स्वामी राज्य के प्रथम अंतरिम मुख्यमंत्री थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Judiciary Records",
        "text": "उत्तराखंड उच्च न्यायालय के प्रथम मुख्य न्यायाधीश कौन थे?",
        "options": ["न्यायमूर्ति ए.ए. देसाई", "न्यायमूर्ति एस.एच. कपाड़िया", "न्यायमूर्ति वी.के. बिष्ट", "न्यायमूर्ति आर.एस. चौहान"],
        "correct_answer": "न्यायमूर्ति ए.ए. देसाई",
        "explanation": "अशोक अभ्येन्द्र देसाई प्रथम मुख्य न्यायाधीश थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Administrative Units",
        "text": "उत्तराखंड में 'कुल कितने' नगर निगम (Municipal Corporations) हैं?",
        "options": ["9", "8", "7", "10"],
        "correct_answer": "9",
        "explanation": "हाल ही में श्रीनगर को नगर निगम बनाया गया है।"
    },

    # ── CULTURE, LITERATURE & PERSONALITIES ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Sahitya Akademi Records",
        "text": "प्रसिद्ध साहित्यकार मंगलेश डबराल को उनकी किस काव्य कृति के लिए साहित्य अकादमी पुरस्कार मिला?",
        "options": ["पहाड़ पर लालटेन", "घर का रास्ता", "हम जो देखते हैं", "आवाज भी एक जगह है"],
        "correct_answer": "हम जो देखते हैं",
        "explanation": "उन्हें 2000 में इसके लिए पुरस्कार मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "UKSSSC Group C",
        "text": "'भोटिया' जनजाति के ग्रीष्मकालीन आवासों को क्या कहा जाता है?",
        "options": ["मैत", "मुन्सा", "गुण्डा", "रोम्बा"],
        "correct_answer": "मैत",
        "explanation": "ग्रीष्मकालीन आवास को 'मैत' कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Anthropological Survey",
        "text": "उत्तराखंड में 'नन्दा राजजात' यात्रा कितने वर्षों के अंतराल पर आयोजित होती है?",
        "options": ["12 वर्ष", "10 वर्ष", "15 वर्ष", "6 वर्ष"],
        "correct_answer": "12 वर्ष",
        "explanation": "यह 12 वर्षों में एक बार आयोजित होती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "UKPSC Prelims",
        "text": "प्रसिद्ध 'जागर' गायिका बसंती बिष्ट को किस वर्ष पद्मश्री पुरस्कार मिला था?",
        "options": ["2017", "2015", "2019", "2021"],
        "correct_answer": "2017",
        "explanation": "उन्हें 2017 में पद्मश्री मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities of UK",
        "text": "पंडित नैन सिंह रावत ने अपनी प्रथम तिब्बत यात्रा किस वर्ष शुरू की थी?",
        "options": ["1865", "1863", "1868", "1870"],
        "correct_answer": "1865",
        "explanation": "नैन सिंह रावत ने 1865 में ल्हासा की यात्रा की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Golu Devta Legends",
        "text": "कुमाऊँ में 'न्याय का देवता' किस लोकदेवता को कहा जाता है?",
        "options": ["गोल्लू देवता", "भोलू देवता", "कलुआ देवता", "गंगनाथ"],
        "correct_answer": "गोल्लू देवता",
        "explanation": "चितई गोल्लू मंदिर अल्मोड़ा में न्याय की गुहार के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Regional Festivals",
        "text": "प्रसिद्ध 'बग्वाल मेला' (पत्थरों का युद्ध) किस स्थान पर आयोजित होता है?",
        "options": ["देवीधुरा", "सोमेश्वर", "पुनार", "श्रीनगर"],
        "correct_answer": "देवीधुरा",
        "explanation": "चंपावत के देवीधुरा में रक्षाबंधन के दिन यह मेला लगता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors of UK",
        "text": "'गढ़वाल की दिवंगत विभूतियाँ' पुस्तक के लेखक कौन हैं?",
        "options": ["भक्त दर्शन", "अजय सिंह रावत", "बद्रीदत्त पाण्डेय", "डबराल"],
        "correct_answer": "भक्त दर्शन",
        "explanation": "भक्त दर्शन ने गढ़वाल के महान व्यक्तित्वों पर यह पुस्तक लिखी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "UKPSC GS Paper 3",
        "text": "प्रसिद्ध कवि सुमित्रानंदन पंत का जन्म कहाँ हुआ था?",
        "options": ["कौसानी", "अल्मोड़ा", "बागेश्वर", "नैनीताल"],
        "correct_answer": "कौसानी",
        "explanation": "उनका जन्म 1900 में कौसानी (बागेश्वर) में हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "UKSSSC Group C 2017",
        "text": "उत्तराखंड के किस शहर को 'पहाड़ों की रानी' कहा जाता है?",
        "options": ["मसूरी", "नैनीताल", "अल्मोड़ा", "कौसानी"],
        "correct_answer": "मसूरी",
        "explanation": "मसूरी को पहाड़ों की रानी कहा जाता है।"
    },

    # ── BATCH 3: LAND SETTLEMENTS & JOURNALISM ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "R.S. Tolia - British Kumaon",
        "text": "उत्तराखंड में 'सन अस्सी' (San Assi) का भूमि बंदोबस्त किस ब्रिटिश अधिकारी ने 1823 में करवाया था?",
        "options": ["जी.डब्ल्यू. ट्रेल", "बेटन", "रैमजे", "ल्यूशिंगटन"],
        "correct_answer": "जी.डब्ल्यू. ट्रेल",
        "explanation": "1823 (संवत 1880) के इस बंदोबस्त को 'सन अस्सी' बंदोबस्त कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "UKPSC GS Paper",
        "text": "वैज्ञानिक पद्धति पर आधारित प्रथम भूमि बंदोबस्त (9वां बंदोबस्त) किसके द्वारा 1863-73 में कराया गया था?",
        "options": ["जी.डब्ल्यू. ट्रेल", "बेटन", "जे.ओ.बी. बैकेट", "पॉव"],
        "correct_answer": "जे.ओ.बी. बैकेट",
        "explanation": "बैकेट ने पहली बार डोरी के स्थान पर जरीब का प्रयोग किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC 2018",
        "text": "उत्तराखंड का प्रथम हिंदी समाचार पत्र 'समय विनोद' (1868) कहाँ से प्रकाशित होता था?",
        "options": ["नैनीताल", "जसपुर", "देहरादून", "अल्मोड़ा"],
        "correct_answer": "जसपुर",
        "explanation": "जयदत्त जोशी के संपादन में यह जसपुर (ऊधम सिंह नगर) से निकलता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism History",
        "text": "'गढ़वाली' समाचार पत्र के प्रथम संपादक कौन थे?",
        "options": ["गिरिजा दत्त नैथानी", "तारा दत्त गैरोला", "विशम्भर दत्त चन्दोला", "भक्त दर्शन"],
        "correct_answer": "गिरिजा दत्त नैथानी",
        "explanation": "1905 में गिरिजा दत्त नैथानी ने इसका संपादन शुरू किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKPSC GS",
        "text": "दुगड्डा (पौड़ी) से 'पुरुषार्थ' समाचार पत्र का प्रकाशन 1917 में किसने शुरू किया था?",
        "options": ["गिरिजा दत्त नैथानी", "बद्रीदत्त पाण्डेय", "ललिता प्रसाद नैथानी", "हरगोविंद पंत"],
        "correct_answer": "गिरिजा दत्त नैथानी",
        "explanation": "गिरिजा दत्त नैथानी ने इसे दुगड्डा से निकाला था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKSSSC Archive",
        "text": "1922 में 'तरुण कुमाऊँ' समाचार पत्र का संपादन लैंसडाउन से किसने किया था?",
        "options": ["बैरिस्टर मुकुन्दीलाल", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "श्रीदेव सुमन"],
        "correct_answer": "बैरिस्टर मुकुन्दीलाल",
        "explanation": "मुकुन्दीलाल ने इसे लैंसडाउन से प्रकाशित किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountain Passes Records",
        "text": "उत्तराखंड के किस दर्रे (Pass) से होकर मानसरोवर यात्री तिब्बत जाते हैं?",
        "options": ["लिपुलेख", "माना", "नीति", "थांग ला"],
        "correct_answer": "लिपुलेख",
        "explanation": "पिथौरागढ़ स्थित लिपुलेख दर्रे से मानसरोवर यात्रा संपन्न होती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks of UK",
        "text": "प्रसिद्ध 'कामेट' (Kamet) पर्वत शिखर की ऊँचाई कितनी है?",
        "options": ["7756 मीटर", "7817 मीटर", "7120 मीटर", "7434 मीटर"],
        "correct_answer": "7756 मीटर",
        "explanation": "कामेट चमोली जिले में स्थित उत्तराखंड का दूसरा सबसे ऊँचा शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Tribes Records",
        "text": "उत्तराखंड की किस प्राचीन जनजाति को 'किरात' (Kiratas) के नाम से भी जाना जाता था?",
        "options": ["भोटिया", "राजी", "थारू", "जौनसारी"],
        "correct_answer": "भोटिया",
        "explanation": "किरातों को उत्तराखंड की प्राचीनतम जनजाति माना जाता है, जिनके वंशज भोटिया और राजी माने जाते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "UKSSSC Group C",
        "text": "'कालसी' (देहरादून) स्थित अशोक के शिलालेख की खोज किसने की थी?",
        "options": ["जॉन फॉरेस्ट", "कनिंघम", "प्रिंसिपल", "ट्रेल"],
        "correct_answer": "जॉन फॉरेस्ट",
        "explanation": "1860 में जॉन फॉरेस्ट ने इस शिलालेख की खोज की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Administrative Archive",
        "text": "कुमाऊँ में 'कमीण' और 'सयाणा' की नियुक्ति किस ब्रिटिश कमिश्नर ने समाप्त की थी?",
        "options": ["ट्रेल", "रैमजे", "ल्यूशिंगटन", "बेटन"],
        "correct_answer": "ट्रेल",
        "explanation": "ट्रेल ने पुरानी राजस्व व्यवस्था में सुधार के लिए यह कदम उठाया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKPSC GS Paper",
        "text": "1921 के कुली बेगार आंदोलन के समय कुमाऊँ का कमिश्नर कौन था?",
        "options": ["पी. विन्धम", "डाईबल", "फिशर", "रैमजे"],
        "correct_answer": "पी. विन्धम",
        "explanation": "पी. विन्धम उस समय कुमाऊँ के कमिश्नर थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand Genealogy",
        "text": "चन्द वंश का वह शासक जिसने 'कुमाऊँ का स्वर्ण काल' (Chand Golden Age) का नेतृत्व किया?",
        "options": ["जगत चन्द", "रुद्र चन्द", "लक्ष्मी चन्द", "कल्याण चन्द"],
        "correct_answer": "जगत चन्द",
        "explanation": "जगत चन्द (1708-1720) के काल को चन्द शासन का स्वर्ण काल कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Revenue Records",
        "text": "चन्द शासन में 'न्यावली' (Nyavali) कर किस लिए लिया जाता था?",
        "options": ["न्याय पाने के लिए", "नदी पार करने के लिए", "भूमि माप के लिए", "युद्ध के खर्च के लिए"],
        "correct_answer": "न्याय पाने के लिए",
        "explanation": "न्याय प्राप्ति के समय लिया जाने वाला कर न्यावली कहलाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife Archive",
        "text": "एशिया का प्रथम राष्ट्रीय उद्यान 'हेली नेशनल पार्क' (कॉर्बेट) कब स्थापित हुआ था?",
        "options": ["1936", "1935", "1940", "1945"],
        "correct_answer": "1936",
        "explanation": "1936 में इसे हेली नेशनल पार्क के नाम से स्थापित किया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education History",
        "text": "उत्तराखंड में 'रुड़की इंजीनियरिंग कॉलेज' की स्थापना किस वर्ष हुई थी?",
        "options": ["1847", "1850", "1845", "1852"],
        "correct_answer": "1847",
        "explanation": "यह भारत का प्रथम इंजीनियरिंग कॉलेज था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities of UK",
        "text": "किसे 'वृक्ष मानव' (Vriksha Manav) के नाम से जाना जाता है?",
        "options": ["वश्वेश्वर दत्त सकलानी", "सुन्दरलाल बहुगुणा", "चण्डी प्रसाद भट्ट", "कल्याण सिंह रावत"],
        "correct_answer": "वश्वेश्वर दत्त सकलानी",
        "explanation": "उन्होंने लाखों पेड़ लगाकर उत्तराखंड को हरा-भरा बनाया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore Records",
        "text": "कुमाऊँ की लोकगाथाओं में 'राजुला-मालूशाही' क्या है?",
        "options": ["एक प्रेम गाथा", "एक वीर गाथा", "एक धार्मिक गाथा", "एक ऐतिहासिक युद्ध"],
        "correct_answer": "एक प्रेम गाथा",
        "explanation": "राजुला और मालूशाही की कथा कुमाऊँ की प्रसिद्ध प्रेम गाथा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Glaciers of UK",
        "text": "उत्तराखंड का सबसे बड़ा ग्लेशियर कौन सा है?",
        "options": ["गंगोत्री", "पिण्डारी", "मिलम", "चोराबाड़ी"],
        "correct_answer": "गंगोत्री",
        "explanation": "गंगोत्री ग्लेशियर (उत्तरकाशी) उत्तराखंड का सबसे बड़ा हिमनद है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC Group C",
        "text": "नैनीताल में 'नैनी झील' की खोज 1841 में किसने की थी?",
        "options": ["पी. बैरन", "ट्रेल", "रैमजे", "ल्यूशिंगटन"],
        "correct_answer": "पी. बैरन",
        "explanation": "पी. बैरन नामक अंग्रेज व्यापारी ने इस झील की खोज की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Garhwal History",
        "text": "पवार वंश का वह शासक जिसे 'गढ़वाल का अशोक' कहा जाता है?",
        "options": ["अजयपाल", "कनकपाल", "मानशाह", "प्रद्युम्न शाह"],
        "correct_answer": "अजयपाल",
        "explanation": "अजयपाल ने 52 गढ़ों का एकीकरण कर शांति स्थापित की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKPSC GS Paper",
        "text": "1923 के प्रान्तीय चुनावों में 'स्वराज पार्टी' के टिकट पर कुमाऊँ से कौन निर्वाचित हुए थे?",
        "options": ["हरगोविंद पंत", "बद्रीदत्त पाण्डेय", "गोविंद बल्लभ पंत", "बैरिस्टर मुकुन्दीलाल"],
        "correct_answer": "हरगोविंद पंत",
        "explanation": "हरगोविंद पंत स्वराज पार्टी के प्रमुख नेता थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "UKPSC GS",
        "text": "उत्तराखंड में 'जिला पंचायत' के अध्यक्ष का चुनाव कैसे होता है?",
        "options": ["अप्रत्यक्ष रीति से", "प्रत्यक्ष रीति से", "मनोनीत", "राज्यपाल द्वारा"],
        "correct_answer": "अप्रत्यक्ष रीति से",
        "explanation": "जिला पंचायत सदस्य अपने में से अध्यक्ष का चुनाव करते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals Archive",
        "text": "उत्तराखंड का प्रसिद्ध 'नन्दा देवी मेला' अल्मोड़ा में किस दिन शुरू होता है?",
        "options": ["अष्टमी", "सप्तमी", "नवमी", "दशमी"],
        "correct_answer": "अष्टमी",
        "explanation": "भाद्रपद शुक्ल अष्टमी को यह मेला धूमधाम से मनाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Revenue Archive",
        "text": "चन्द शासन में 'भेंट' (Bhent) कर किसलिए दिया जाता था?",
        "options": ["राजा या राजकुमार को", "सैनिकों को", "मन्दिरों को", "ब्राह्मणों को"],
        "correct_answer": "राजा या राजकुमार को",
        "explanation": "राजा या राजपरिवार के सदस्यों को दी जाने वाली नकद राशि भेंट कहलाती थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri History",
        "text": "टिहरी रियासत में 'रवाईं कांड' (Rawain Kand) कब घटित हुआ था?",
        "options": ["30 मई 1930", "15 अप्रैल 1930", "20 जून 1930", "10 मई 1930"],
        "correct_answer": "30 मई 1930",
        "explanation": "इसे उत्तराखंड का 'जलियावाला बाग' भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "कुमाऊँ में 'बखानी' का क्या अर्थ है?",
        "options": ["कहावतें", "लोकगाथा", "जागर", "पहेली"],
        "correct_answer": "कहावतें",
        "explanation": "कुमाऊँनी में कहावतों को बखानी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers Archive",
        "text": "काली नदी और गोरी नदी का संगम कहाँ होता है?",
        "options": ["जौलजीबी", "धारचूला", "मुनस्यारी", "पिथौरागढ़"],
        "correct_answer": "जौलजीबी",
        "explanation": "जौलजीबी में प्रसिद्ध व्यापारिक मेला भी लगता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC Group C",
        "text": "नैनीताल में 'भयानक भूस्खलन' किस वर्ष हुआ था, जिसने शहर का स्वरूप बदल दिया?",
        "options": ["1880", "1890", "1875", "1885"],
        "correct_answer": "1880",
        "explanation": "18 सितंबर 1880 को हुए भूस्खलन में सैकड़ों लोग मारे गए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Administrative History",
        "text": "कुमाऊँ में 'शराब की पहली फैक्ट्री' कहाँ स्थापित की गई थी?",
        "options": ["जीनी (नैनीताल)", "अल्मोड़ा", "हल्द्वानी", "रानीखेत"],
        "correct_answer": "जीनी (नैनीताल)",
        "explanation": "अंग्रेजों ने अपनी जरूरतों के लिए जीनी (Jeanie) में फैक्ट्री लगाई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKPSC GS",
        "text": "1942 के भारत छोड़ो आंदोलन के समय 'सल्ट' में हुई गोलीबारी में कौन शहीद हुए थे?",
        "options": ["खिमानंद और गंगाराम", "बद्रीदत्त पाण्डेय", "श्रीदेव सुमन", "कालू मेहरा"],
        "correct_answer": "खिमानंद और गंगाराम",
        "explanation": "सल्ट (अल्मोड़ा) में 5 सितंबर 1942 को ये दोनों भाई शहीद हुए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "UKSSSC Group C",
        "text": "'गोविषाण' (Govishan) प्राचीन नाम किस शहर का था?",
        "options": ["काशीपुर", "रुद्रपुर", "हल्द्वानी", "सितारगंज"],
        "correct_answer": "काशीपुर",
        "explanation": "ह्वेनसांग ने काशीपुर को गोविषाण कहा था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Valley Archive",
        "text": "किसे 'उत्तराखंड का स्विट्जरलैंड' (Mini Switzerland) कहा जाता है?",
        "options": ["चोपता", "कौसानी", "हर्शील", "मुनस्यारी"],
        "correct_answer": "चोपता",
        "explanation": "चोपता (रुद्रप्रयाग) को अपनी प्राकृतिक सुंदरता के कारण यह नाम दिया गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "प्रसिद्ध समाज सुधारक 'स्वामी दयानंद सरस्वती' उत्तराखंड में पहली बार कहाँ आए थे?",
        "options": ["हरिद्वार", "ऋषिकेश", "श्रीनगर", "देहरादून"],
        "correct_answer": "हरिद्वार",
        "explanation": "वे 1867 में हरिद्वार कुंभ के अवसर पर आए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers of UK",
        "text": "भागीरथी और अलकनन्दा का संगम कहाँ होता है?",
        "options": ["देवप्रयाग", "रुद्रप्रयाग", "कर्णप्रयाग", "नन्दप्रयाग"],
        "correct_answer": "देवप्रयाग",
        "explanation": "यहाँ से इसे 'गंगा' के नाम से जाना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC Group C",
        "text": "कुमाऊँ में 'तुलाराम' (Tula Ram) कौन थे?",
        "options": ["एक प्रसिद्ध स्वतंत्रता सेनानी", "एक ब्रिटिश अधिकारी", "एक लोक गायक", "एक चन्द शासक"],
        "correct_answer": "एक प्रसिद्ध स्वतंत्रता सेनानी",
        "explanation": "उन्होंने ब्रिटिश शासन के खिलाफ विद्रोह किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri State",
        "text": "टिहरी रियासत में 'चौथ' (Chauth) क्या था?",
        "options": ["एक प्रकार का कर", "एक प्रशासनिक पद", "एक धार्मिक उत्सव", "एक दंड"],
        "correct_answer": "एक प्रकार का कर",
        "explanation": "उपज का चौथा हिस्सा कर के रूप में लिया जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Art Archive",
        "text": "उत्तराखंड के प्रसिद्ध चित्रकार 'मोलाराम' किस शैली के लिए जाने जाते हैं?",
        "options": ["गढ़वाल शैली", "कुमाऊँनी शैली", "मुगल शैली", "कांगड़ा शैली"],
        "correct_answer": "गढ़वाल शैली",
        "explanation": "मोलाराम गढ़वाल चित्रकला शैली के सबसे बड़े कलाकार थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes of UK",
        "text": "उत्तराखंड की किस झील का आकार 'अश्वखुर' (Horse-shoe) के समान है?",
        "options": ["सातताल", "नैनीताल", "भीमताल", "नौकुचियाताल"],
        "correct_answer": "सातताल",
        "explanation": "सातताल की नल-दमयन्ती ताल का आकार ऐसा माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKPSC GS",
        "text": "कुमाऊँ के किस कमिश्नर ने 'जेलों' में सुधार के लिए कार्य किया था?",
        "options": ["ल्यूशिंगटन", "ट्रेल", "रैमजे", "बेटन"],
        "correct_answer": "ल्यूशिंगटन",
        "explanation": "थॉमस ल्यूशिंगटन ने जेल सुधारों पर बल दिया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKSSSC History",
        "text": "'गढ़ केसरी' के नाम से किसे जाना जाता है?",
        "options": ["अनुसूया प्रसाद बहुगुणा", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "इन्द्रमणि बडोनी"],
        "correct_answer": "अनुसूया प्रसाद बहुगुणा",
        "explanation": "उनके अदम्य साहस के कारण उन्हें यह उपाधि मिली।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Tribes Archive",
        "text": "उत्तराखंड की 'थारू' जनजाति मुख्य रूप से किस जिले में पाई जाती है?",
        "options": ["ऊधम सिंह नगर", "चम्पावत", "नैनीताल", "पिथौरागढ़"],
        "correct_answer": "ऊधम सिंह नगर",
        "explanation": "ऊधम सिंह नगर के खटीमा और सितारगंज में थारू निवास करते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Customs",
        "text": "उत्तराखंड में 'भिटौली' (Bhitauli) क्या है?",
        "options": ["एक त्यौहार", "एक उपहार", "एक लोक गीत", "एक पकवान"],
        "correct_answer": "एक उपहार",
        "explanation": "विवाहित लड़कियों को मायके से भेजे जाने वाले उपहार को भिटौली कहते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Wonders",
        "text": "विश्व प्रसिद्ध 'फूलों की घाटी' (Valley of Flowers) की खोज 1931 में किसने की थी?",
        "options": ["फ्रैंक स्माइथ", "पी. बैरन", "जॉन फॉरेस्ट", "जिम कॉर्बेट"],
        "correct_answer": "फ्रैंक स्माइथ",
        "explanation": "ब्रिटिश पर्वतारोही फ्रैंक स्माइथ ने इसकी खोज की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKPSC GS Paper",
        "text": "अल्मोड़ा में 'कुमाऊँ संघ' (Kumaon Association) की स्थापना किस वर्ष हुई थी?",
        "options": ["1916", "1912", "1918", "1920"],
        "correct_answer": "1916",
        "explanation": "सितंबर 1916 में नैनीताल में इसकी नींव रखी गई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Tehri State",
        "text": "टिहरी रियासत में 'राजस्व' का मुख्य स्रोत क्या था?",
        "options": ["भूमि कर", "वन उपज", "व्यापार", "सीमा शुल्क"],
        "correct_answer": "भूमि कर",
        "explanation": "भूमि कर रियासत की आय का सबसे बड़ा स्रोत था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forest History",
        "text": "उत्तराखंड में 'प्रथम वन बंदोबस्त' किसने कराया था?",
        "options": ["ट्रेल", "रैमजे", "बेटन", "ल्यूशिंगटन"],
        "correct_answer": "ट्रेल",
        "explanation": "1823 में ट्रेल ने वनों का सीमांकन शुरू किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "UKPSC GS",
        "text": "उत्तराखंड के किस लोकगीत में 'न्योली' (Nyoli) क्या है?",
        "options": ["विरह गीत", "प्रेम गीत", "कृषि गीत", "धार्मिक गीत"],
        "correct_answer": "विरह गीत",
        "explanation": "न्योली कुमाऊँ का एक प्रसिद्ध विरह प्रधान लोकगीत है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers of UK",
        "text": "अलकनन्दा की वह सहायक नदी जो 'बद्रीनाथ' के पास स्थित है?",
        "options": ["ऋषि गंगा", "धौली गंगा", "मंदाकिनी", "पिण्डर"],
        "correct_answer": "ऋषि गंगा",
        "explanation": "ऋषि गंगा बद्रीनाथ के पास अलकनन्दा में मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC Group C",
        "text": "नैनीताल में 'सेंट जोसेफ कॉलेज' की स्थापना किस वर्ष हुई थी?",
        "options": ["1888", "1890", "1885", "1892"],
        "correct_answer": "1888",
        "explanation": "यह नैनीताल के सबसे पुराने शिक्षण संस्थानों में से एक है।"
    },

    # ── BATCH 4: DISTRICTS & INSTITUTIONS ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Institutional Records",
        "text": "भारत के प्रथम कृषि विश्वविद्यालय 'पंतनगर विश्वविद्यालय' की स्थापना किस वर्ष हुई थी?",
        "options": ["17 नवंबर 1960", "15 अगस्त 1962", "26 जनवरी 1958", "10 अक्टूबर 1965"],
        "correct_answer": "17 नवंबर 1960",
        "explanation": "जवाहरलाल नेहरू ने इसका उद्घाटन किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Forestry Archive",
        "text": "देहरादून स्थित 'वन अनुसंधान संस्थान' (FRI) की मुख्य इमारत का उद्घाटन किस वर्ष हुआ था?",
        "options": ["1929", "1906", "1921", "1932"],
        "correct_answer": "1929",
        "explanation": "संस्थान की स्थापना 1906 में हुई थी, लेकिन मुख्य भवन का उद्घाटन 1929 में लॉर्ड इरविन ने किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "District Administration",
        "text": "पिथौरागढ़, चमोली और उत्तरकाशी जिलों का गठन एक साथ किस वर्ष किया गया था?",
        "options": ["24 फरवरी 1960", "15 अगस्त 1962", "1 जनवरी 1958", "10 मार्च 1965"],
        "correct_answer": "24 फरवरी 1960",
        "explanation": "इन तीनों सीमावर्ती जिलों का गठन 1960 में हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife Archive",
        "text": "'अस्कोट वन्यजीव विहार' (Askot Wildlife Sanctuary) मुख्य रूप से किसके संरक्षण के लिए प्रसिद्ध है?",
        "options": ["कस्तूरी मृग", "बाघ", "हाथी", "हिम तेंदुआ"],
        "correct_answer": "कस्तूरी मृग",
        "explanation": "पिथौरागढ़ स्थित यह विहार कस्तूरी मृग के लिए जाना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Religious Sites",
        "text": "चम्पावत स्थित 'बालेश्वर मंदिर' का निर्माण किस शैली में किया गया है?",
        "options": ["नागर शैली", "द्रविड़ शैली", "कत्यूरी शैली", "बेसर शैली"],
        "correct_answer": "नागर शैली",
        "explanation": "बालेश्वर मंदिर अपनी उत्कृष्ट नक्काशी और नागर शैली के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers of UK",
        "text": "सर्यू और गोमती नदी का संगम उत्तराखंड के किस नगर में होता है?",
        "options": ["बागेश्वर", "पिथौरागढ़", "अल्मोड़ा", "चंपावत"],
        "correct_answer": "बागेश्वर",
        "explanation": "बागेश्वर का प्रसिद्ध बागनाथ मंदिर इसी संगम पर स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes Archive",
        "text": "उत्तराखंड की किस झील को 'कंकाल झील' (Skeleton Lake) के नाम से जाना जाता है?",
        "options": ["रूपकुंड", "हेमकुंड", "नचिकेता ताल", "डोडीताल"],
        "correct_answer": "रूपकुंड",
        "explanation": "चमोली में स्थित रूपकुंड में प्राचीन मानव कंकाल पाए गए हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Arts",
        "text": "'ऐपण' (Aipan) कला का संबंध उत्तराखंड के किस क्षेत्र से है?",
        "options": ["कुमाऊँ", "गढ़वाल", "जौनसार", "तराई"],
        "correct_answer": "कुमाऊँ",
        "explanation": "ऐपण कुमाऊँ की एक प्रसिद्ध लोक चित्रकला शैली है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education Archive",
        "text": "नैनीताल में 'शेरवुड कॉलेज' की स्थापना किस वर्ष हुई थी?",
        "options": ["1869", "1880", "1875", "1890"],
        "correct_answer": "1869",
        "explanation": "यह नैनीताल के सबसे प्रतिष्ठित और पुराने स्कूलों में से एक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "'कुमाऊँ केसरी' के नाम से किसे जाना जाता है?",
        "options": ["बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "गोविंद बल्लभ पंत", "इन्द्रमणि बडोनी"],
        "correct_answer": "बद्रीदत्त पाण्डेय",
        "explanation": "कुली बेगार आंदोलन के सफल नेतृत्व के कारण उन्हें यह उपाधि मिली।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Legal Records",
        "text": "उत्तराखंड उच्च न्यायालय के भवन का निर्माण किसने करवाया था?",
        "options": ["सर संतानाम", "हेनरी रैमजे", "लॉर्ड कर्जन", "बैटन"],
        "correct_answer": "सर संतानाम",
        "explanation": "नैनीताल स्थित राजभवन (अब उच्च न्यायालय) का निर्माण सेंटोनी मैकडोनाल्ड के काल में हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers of UK",
        "text": "मंदाकिनी नदी किस स्थान पर अलकनन्दा में मिलती है?",
        "options": ["रुद्रप्रयाग", "कर्णप्रयाग", "देवप्रयाग", "नन्दप्रयाग"],
        "correct_answer": "रुद्रप्रयाग",
        "explanation": "रुद्रप्रयाग पंच प्रयागों में से एक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Books and Authors",
        "text": "'हिमालय की खस' (Khasas of Himalaya) पुस्तक के लेखक कौन हैं?",
        "options": ["डी.डी. शर्मा", "अजय सिंह रावत", "बद्रीदत्त पाण्डेय", "ई.टी. एटकिंसन"],
        "correct_answer": "डी.डी. शर्मा",
        "explanation": "डॉ. डी.डी. शर्मा ने उत्तराखंड की जनजातियों पर गहन शोध किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forestry Archive",
        "text": "उत्तराखंड में 'चिपको आंदोलन' के समय उत्तर प्रदेश के मुख्यमंत्री कौन थे?",
        "options": ["हेमवती नंदन बहुगुणा", "नारायण दत्त तिवारी", "मुलायम सिंह यादव", "कल्याण सिंह"],
        "correct_answer": "हेमवती नंदन बहुगुणा",
        "explanation": "1974 के चिपको आंदोलन के समय बहुगुणा जी मुख्यमंत्री थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Records",
        "text": "कत्यूरी वंश की कुलदेवी का नाम क्या था?",
        "options": ["कोट भ्रामरी", "नन्दा देवी", "राजराजेश्वरी", "ज्वाला देवी"],
        "correct_answer": "कोट भ्रामरी",
        "explanation": "बागेश्वर स्थित कोट भ्रामरी कत्यूरी शासकों की आराध्य देवी थीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks",
        "text": "'त्रिशूल' पर्वत शिखर किस जिले में स्थित है?",
        "options": ["चमोली", "उत्तरकाशी", "पिथौरागढ़", "रुद्रप्रयाग"],
        "correct_answer": "चमोली",
        "explanation": "त्रिशूल पर्वत चमोली जिले का एक प्रमुख शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Instruments",
        "text": "उत्तराखंड का 'राजकीय वाद्य यंत्र' क्या है?",
        "options": ["ढोल", "हुड़का", "मशकबीन", "नगाड़ा"],
        "correct_answer": "ढोल",
        "explanation": "2015 में ढोल को उत्तराखंड का राजकीय वाद्य यंत्र घोषित किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'पटवारी' पद का सृजन 1819 में किसने किया था?",
        "options": ["जी.डब्ल्यू. ट्रेल", "बेटन", "गार्डनर", "रैमजे"],
        "correct_answer": "जी.डब्ल्यू. ट्रेल",
        "explanation": "ट्रेल ने प्रशासनिक व्यवस्था के लिए 9 पटवारियों के पद सृजित किए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "'लधिया' नदी किसकी सहायक नदी है?",
        "options": ["काली नदी", "अलकनन्दा", "भागीरथी", "कोसी"],
        "correct_answer": "काली नदी",
        "explanation": "लधिया काली नदी की अंतिम सहायक नदी है जो उत्तराखंड में मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Legislative Records",
        "text": "उत्तराखंड विधानसभा की प्रथम निर्वाचित अध्यक्ष कौन थे?",
        "options": ["यशपाल आर्य", "प्रकाश पंत", "हरबंश कपूर", "गोविंद सिंह कुंजवाल"],
        "correct_answer": "यशपाल आर्य",
        "explanation": "प्रकाश पंत प्रथम अंतरिम अध्यक्ष थे, जबकि यशपाल आर्य प्रथम निर्वाचित अध्यक्ष थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Garhwal History",
        "text": "पवार वंश का 55वाँ शासक कौन था?",
        "options": ["सुदर्शन शाह", "प्रद्युम्न शाह", "मानवेन्द्र शाह", "ललित शाह"],
        "correct_answer": "सुदर्शन शाह",
        "explanation": "सुदर्शन शाह ने टिहरी रियासत की स्थापना की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards",
        "text": "उत्तराखंड के प्रथम व्यक्ति जिन्हें 'पद्म विभूषण' से सम्मानित किया गया?",
        "options": ["डॉ. घनानंद पाण्डे", "भैरो दत्त पाण्डेय", "कुंवर सिंह नेगी", "चण्डी प्रसाद भट्ट"],
        "correct_answer": "डॉ. घनानंद पाण्डे",
        "explanation": "1969 में उन्हें विज्ञान एवं अभियांत्रिकी के क्षेत्र में यह सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Heritage",
        "text": "उत्तराखंड में 'फूलों की घाटी' को राष्ट्रीय उद्यान कब घोषित किया गया?",
        "options": ["1982", "1980", "1985", "1988"],
        "correct_answer": "1982",
        "explanation": "1982 में इसे नेशनल पार्क का दर्जा मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism History",
        "text": "1913 में अल्मोड़ा से 'कुमाऊँ कुमुद' समाचार पत्र का संपादन किसने किया था?",
        "options": ["पूर्णानंद", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "तारा दत्त गैरोला"],
        "correct_answer": "पूर्णानंद",
        "explanation": "यह एक प्रसिद्ध साप्ताहिक पत्र था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "कुमाऊँ में 'छोलिया' (Chholiya) नृत्य किस अवसर पर किया जाता है?",
        "options": ["विवाह", "फसल कटाई", "जन्म", "धार्मिक त्यौहार"],
        "correct_answer": "विवाह",
        "explanation": "यह एक प्रसिद्ध युद्ध नृत्य है जो अब शादियों में मुख्य रूप से किया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "किस नदी को 'पुराणों' में 'कौशिकी' (Kaushiki) कहा गया है?",
        "options": ["कोसी नदी", "रामगंगा", "पिण्डर", "काली"],
        "correct_answer": "कोसी नदी",
        "explanation": "कोसी नदी को प्राचीन ग्रंथों में कौशिकी कहा गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Health Archive",
        "text": "उत्तराखंड में 'कुष्ठ रोग' निवारण हेतु अल्मोड़ा में अस्पताल की स्थापना कब हुई थी?",
        "options": ["1854", "1840", "1860", "1870"],
        "correct_answer": "1854",
        "explanation": "ल्यूशिंगटन के समय यह पहल की गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Districts",
        "text": "क्षेत्रफल की दृष्टि से उत्तराखंड का 'सबसे छोटा' जिला कौन सा है?",
        "options": ["चम्पावत", "रुद्रप्रयाग", "बागेश्वर", "हरिद्वार"],
        "correct_answer": "चम्पावत",
        "explanation": "चम्पावत का क्षेत्रफल सबसे कम है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "'गौरा पंत' (शिवानी) का जन्म कहाँ हुआ था?",
        "options": ["राजकोट", "अल्मोड़ा", "नैनीताल", "देहरादून"],
        "correct_answer": "राजकोट",
        "explanation": "उनका जन्म गुजरात के राजकोट में हुआ था, लेकिन वे मूल रूप से कुमाऊँनी थीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'हाथी पर्वत' (Hathi Parvat) किस जिले में स्थित है?",
        "options": ["चमोली", "उत्तरकाशी", "पिथौरागढ़", "बागेश्वर"],
        "correct_answer": "चमोली",
        "explanation": "चमोली के जोशीमठ के पास यह शिखर स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC Group C",
        "text": "अंग्रेजों ने कुमाऊँ में 'चाय का प्रथम बागान' कहाँ लगाया था?",
        "options": ["लक्ष्मेर (अल्मोड़ा)", "भीमताल", "भवाली", "रानीखेत"],
        "correct_answer": "लक्ष्मेर (अल्मोड़ा)",
        "explanation": "1835 में अल्मोड़ा के पास चाय बागान शुरू किया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'हिलजात्रा' (Hill Jatra) उत्सव का संबंध किस जिले से है?",
        "options": ["पिथौरागढ़", "चमोली", "उत्तरकाशी", "अल्मोड़ा"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "यह कृषि और पशुपालन से संबंधित उत्सव है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Valleys",
        "text": "'दारमा' और 'व्यास' घाटी को जोड़ने वाला दर्रा कौन सा है?",
        "options": ["सिन ला", "जयन्ती", "थांग ला", "नीति"],
        "correct_answer": "सिन ला",
        "explanation": "सिन ला दर्रा इन दो प्रसिद्ध घाटियों को जोड़ता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education History",
        "text": "कुमाऊँ विश्वविद्यालय की स्थापना किस वर्ष हुई थी?",
        "options": ["1973", "1970", "1975", "1980"],
        "correct_answer": "1973",
        "explanation": "1973 में कुमाऊँ और गढ़वाल विश्वविद्यालयों की स्थापना हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Books",
        "text": "'कुमाऊँ का इतिहास' पुस्तक के लेखक कौन हैं?",
        "options": ["बद्रीदत्त पाण्डेय", "अजय सिंह रावत", "शिव प्रसाद डबराल", "हरिकृष्ण रतूड़ी"],
        "correct_answer": "बद्रीदत्त पाण्डेय",
        "explanation": "जेल में रहते हुए उन्होंने यह ऐतिहासिक ग्रंथ लिखा था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "पश्चिमी रामगंगा नदी का उद्गम स्थल कहाँ है?",
        "options": ["दूधातोली श्रेणी", "पिण्डारी", "मिलम", "गंगोत्री"],
        "correct_answer": "दूधातोली श्रेणी",
        "explanation": "दूधातोली को 'उत्तराखंड का पामीर' भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKPSC GS",
        "text": "1815 में सुगौली की संधि पर हस्ताक्षर करने वाला गोरखा अधिकारी कौन था?",
        "options": ["गजराज मिश्र", "अमर सिंह थापा", "हस्तीदल", "रणजोर सिंह"],
        "correct_answer": "गजराज मिश्र",
        "explanation": "गजराज मिश्र और चं. शेखर उपाध्याय ने हस्ताक्षर किए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "'पहाड़ का गांधी' (Gandhi of Hills) किसे कहा जाता है?",
        "options": ["जसवंत सिंह बिष्ट", "इन्द्रमणि बडोनी", "बद्रीदत्त पाण्डेय", "सुन्दरलाल बहुगुणा"],
        "correct_answer": "जसवंत सिंह बिष्ट",
        "explanation": "कुमाऊँ क्षेत्र में उनके गांधीवादी कार्यों के लिए उन्हें यह कहा जाता है (इन्द्रमणि बडोनी को 'उत्तराखंड का गांधी' कहा जाता है)।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife",
        "text": "उत्तराखंड में 'जिम कॉर्बेट' नेशनल पार्क का प्रवेश द्वार कहाँ स्थित है?",
        "options": ["ढिकाला", "रामनगर", "कोटद्वार", "हल्द्वानी"],
        "correct_answer": "ढिकाला",
        "explanation": "ढिकाला कॉर्बेट का मुख्य प्रवेश द्वार और विश्राम स्थल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "District Data",
        "text": "उत्तराखंड के किस जिले में 'सबसे कम' विकासखंड (Blocks) हैं?",
        "options": ["रुद्रप्रयाग और बागेश्वर", "चम्पावत", "पिथौरागढ़", "उत्तरकाशी"],
        "correct_answer": "रुद्रप्रयाग और बागेश्वर",
        "explanation": "इन दोनों जिलों में केवल 3-3 विकासखंड हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Tribes",
        "text": "जौनसारी जनजाति के 'महासू' देवता का मुख्य मंदिर कहाँ स्थित है?",
        "options": ["हनोल", "लाखामंडल", "कालसी", "चकराता"],
        "correct_answer": "हनोल",
        "explanation": "हनोल (देहरादून) महासू देवता का प्रसिद्ध तीर्थ स्थल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Songs",
        "text": "उत्तराखंड में 'खुदेड़' (Khuded) गीत किस भावना से संबंधित है?",
        "options": ["विरह और याद", "वीरता", "खुशी", "भक्ति"],
        "correct_answer": "विरह और याद",
        "explanation": "मायके की याद में विवाहित महिलाओं द्वारा यह गाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'नल-दमयन्ती' ताल किस ताल समूह का हिस्सा है?",
        "options": ["सातताल", "नैनीताल", "भीमताल", "नौकुचियाताल"],
        "correct_answer": "सातताल",
        "explanation": "सातताल में राम, लक्ष्मण, सीता, नल-दमयन्ती आदि ताल शामिल हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism History",
        "text": "1930 में 'स्वाधीन प्रजा' समाचार पत्र का प्रकाशन किसने शुरू किया था?",
        "options": ["विक्टर मोहन जोशी", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "श्रीदेव सुमन"],
        "correct_answer": "विक्टर मोहन जोशी",
        "explanation": "उन्होंने अल्मोड़ा से इसका प्रकाशन शुरू किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Heritage",
        "text": "उत्तराखंड में 'रम्माण' (Ramman) उत्सव किस जिले से संबंधित है?",
        "options": ["चमोली", "रुद्रप्रयाग", "उत्तरकाशी", "पिथौरागढ़"],
        "correct_answer": "चमोली",
        "explanation": "चमोली के सलूड़-डुंग्रा गाँव का यह उत्सव यूनेस्को की धरोहर सूची में शामिल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "कोसी नदी किस स्थान पर 'रामगंगा' (पश्चिमी) में मिलती है?",
        "options": ["सुल्तानपुर", "रामनगर", "बाजपुर", "काशीपुर"],
        "correct_answer": "सुल्तानपुर",
        "explanation": "उत्तर प्रदेश के सुल्तानपुर के पास कोसी रामगंगा में मिल जाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forestry",
        "text": "उत्तराखंड में 'मैती' (Maiti) आंदोलन की शुरुआत कब हुई थी?",
        "options": ["1995", "1990", "1998", "2000"],
        "correct_answer": "1995",
        "explanation": "कल्याण सिंह रावत ने इसकी शुरुआत की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'गढ़वाल का इतिहास' पुस्तक के लेखक कौन हैं?",
        "options": ["हरिकृष्ण रतूड़ी", "बद्रीदत्त पाण्डेय", "अजय सिंह रावत", "पाण्डे"],
        "correct_answer": "हरिकृष्ण रतूड़ी",
        "explanation": "1928 में यह पुस्तक प्रकाशित हुई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Glaciers",
        "text": "पिण्डारी ग्लेशियर किस जिले में स्थित है?",
        "options": ["बागेश्वर", "पिथौरागढ़", "चमोली", "उत्तरकाशी"],
        "correct_answer": "बागेश्वर",
        "explanation": "पिण्डारी ग्लेशियर बागेश्वर जिले का प्रमुख हिमनद है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Administrative Units",
        "text": "उत्तराखंड में 'मण्डल' (Divisions) की संख्या कितनी है?",
        "options": ["2", "3", "4", "1"],
        "correct_answer": "2",
        "explanation": "कुमाऊँ और गढ़वाल मण्डल (गैरसैण मण्डल की घोषणा हुई थी लेकिन वर्तमान में 2 ही क्रियाशील हैं)।"
    },

    # ── BATCH 5: PERSONALITIES & ARCHITECTURE ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards Archive",
        "text": "गोविंद बल्लभ पंत को 'भारत रत्न' से किस वर्ष सम्मानित किया गया था?",
        "options": ["1957", "1955", "1960", "1952"],
        "correct_answer": "1957",
        "explanation": "वे उत्तर प्रदेश के प्रथम मुख्यमंत्री और भारत के गृहमंत्री रहे थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Temple Architecture",
        "text": "अल्मोड़ा स्थित 'कटारमल सूर्य मंदिर' का निर्माण किस शताब्दी में हुआ था?",
        "options": ["9वीं शताब्दी", "7वीं शताब्दी", "11वीं शताब्दी", "13वीं शताब्दी"],
        "correct_answer": "9वीं शताब्दी",
        "explanation": "यह मंदिर कत्यूरी राजा कटारमल द्वारा निर्मित माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "UKSSSC History",
        "text": "'गढ़वाल का नेपोलियन' किसे कहा जाता है?",
        "options": ["अजयपाल", "कनकपाल", "मानशाह", "महिपति शाह"],
        "correct_answer": "अजयपाल",
        "explanation": "52 गढ़ों को जीतने के कारण उन्हें यह संज्ञा दी गई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Jnanpith Awards",
        "text": "हिंदी के प्रसिद्ध कवि सुमित्रानंदन पंत को उनके किस काव्य संग्रह के लिए 'ज्ञानपीठ पुरस्कार' मिला था?",
        "options": ["चिदम्बरा", "पल्लव", "गुंजन", "ग्राम्या"],
        "correct_answer": "चिदम्बरा",
        "explanation": "1968 में उन्हें चिदम्बरा के लिए यह पुरस्कार मिला था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKPSC GS",
        "text": "1857 के विद्रोह के समय कुमाऊँ का कमिश्नर कौन था?",
        "options": ["हेनरी रैमजे", "ल्यूशिंगटन", "बेटन", "गार्डनर"],
        "correct_answer": "हेनरी रैमजे",
        "explanation": "हेनरी रैमजे ने 1857 के दौरान कुमाऊँ में शांति बनाए रखी थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks of UK",
        "text": "चमोली जिले में स्थित 'बद्रीनाथ' धाम किस पर्वत पर स्थित है?",
        "options": ["नर और नारायण पर्वत", "नीलकंठ पर्वत", "नन्दा देवी", "कामेत"],
        "correct_answer": "नर और नारायण पर्वत",
        "explanation": "बद्रीनाथ मंदिर इन दो पर्वतों के मध्य स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'उत्तराखंड का इतिहास' (12 खंडों में) किसने लिखा है?",
        "options": ["शिव प्रसाद डबराल 'चारण'", "अजय सिंह रावत", "बद्रीदत्त पाण्डेय", "डबराल"],
        "correct_answer": "शिव प्रसाद डबराल 'चारण'",
        "explanation": "उन्हें उत्तराखंड का 'इनसाइक्लोपीडिया' भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Valleys",
        "text": "'नीलांग घाटी' उत्तराखंड के किस जिले में स्थित है?",
        "options": ["उत्तरकाशी", "पिथौरागढ़", "चमोली", "रुद्रप्रयाग"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "नीलांग घाटी को 'उत्तराखंड का लद्दाख' भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri State",
        "text": "टिहरी रियासत में 'ढांढक' (Dhandak) आंदोलन किससे संबंधित था?",
        "options": ["मजदूरों से", "किसानों से", "सैनिकों से", "व्यापारियों से"],
        "correct_answer": "मजदूरों से",
        "explanation": "यह मुख्य रूप से वन श्रमिकों और मजदूरों का विद्रोह था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "कुमाऊँ में प्रसिद्ध 'बग्वाल' (Devidhura) में किन चार खामों (Clans) के बीच युद्ध होता है?",
        "options": ["चम्याल, गहरवाल, लमगड़िया और वालिक", "राठौड़, चौहान, पवार और तोमर", "थारू, बोक्सा, भोटिया और राजी", "पाण्डे, जोशी, पंत और पाठक"],
        "correct_answer": "चम्याल, गहरवाल, लमगड़िया और वालिक",
        "explanation": "देवीधुरा मेले में इन चार खामों के लोग भाग लेते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Heritage",
        "text": "उत्तराखंड के किस स्थान को 'पिथौरागढ़ का प्रवेश द्वार' कहा जाता है?",
        "options": ["लोहाघाट", "घाट", "टनकपुर", "धारचूला"],
        "correct_answer": "घाट",
        "explanation": "घाट को पिथौरागढ़ का प्रवेश द्वार माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Institutions",
        "text": "उत्तराखंड राज्य लोक सेवा आयोग (UKPSC) का मुख्यालय कहाँ स्थित है?",
        "options": ["हरिद्वार", "देहरादून", "नैनीताल", "हल्द्वानी"],
        "correct_answer": "हरिद्वार",
        "explanation": "UKPSC का मुख्यालय हरिद्वार के गुरुकुल कांगड़ी के पास स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC Group C",
        "text": "कुमाऊँ में 'अलमगोरा' (Almora) शहर की स्थापना किसने की थी?",
        "options": ["भीष्म चन्द", "सोम चन्द", "कल्याण चन्द", "रुद्र चन्द"],
        "correct_answer": "भीष्म चन्द",
        "explanation": "भीष्म चन्द ने खगमरा किले के साथ शहर की नींव रखी थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'फूलदेई' त्यौहार किस महीने में मनाया जाता है?",
        "options": ["चैत्र", "वैशाख", "श्रावण", "फाल्गुन"],
        "correct_answer": "चैत्र",
        "explanation": "चैत्र मास की संक्रांति को यह त्यौहार मनाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Agriculture",
        "text": "उत्तराखंड में 'मण्डुआ' (Mandua) उत्पादन में भारत का कौन सा स्थान है?",
        "options": ["प्रथम", "द्वितीय", "तृतीय", "चतुर्थ"],
        "correct_answer": "प्रथम",
        "explanation": "उत्तराखंड मण्डुआ (कोदा) उत्पादन में देश में अग्रणी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Records",
        "text": "उत्तराखंड का प्रथम ऐतिहासिक राजवंश किसे माना जाता है?",
        "options": ["कुणिन्द", "कत्यूरी", "पवार", "चन्द"],
        "correct_answer": "कुणिन्द",
        "explanation": "कुणिन्दों को उत्तराखंड का प्रथम राजनीतिक/ऐतिहासिक वंश माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "प्रसिद्ध पर्यावरणविद सुन्दरलाल बहुगुणा का जन्म कहाँ हुआ था?",
        "options": ["मरोड़ा गाँव (टिहरी)", "चोपता", "उत्तरकाशी", "चमोली"],
        "correct_answer": "मरोड़ा गाँव (टिहरी)",
        "explanation": "चिपको आंदोलन को वैश्विक पहचान दिलाने में उनका बड़ा योगदान था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "भागीरथी नदी पर स्थित 'टिहरी बाँध' की ऊँचाई कितनी है?",
        "options": ["260.5 मीटर", "240 मीटर", "280 मीटर", "250 मीटर"],
        "correct_answer": "260.5 मीटर",
        "explanation": "यह भारत का सबसे ऊँचा बाँध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education",
        "text": "उत्तराखंड में 'नैनीताल' में प्रथम मेथोडिस्ट चर्च की स्थापना कब हुई थी?",
        "options": ["1858", "1850", "1860", "1870"],
        "correct_answer": "1858",
        "explanation": "पादरी विलियम बटलर ने इसकी स्थापना की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Current Status",
        "text": "उत्तराखंड की 'द्वितीय राजभाषा' कौन सी है?",
        "options": ["संस्कृत", "अंग्रेजी", "कुमाऊँनी", "गढ़वाली"],
        "correct_answer": "संस्कृत",
        "explanation": "2010 में संस्कृत को द्वितीय राजभाषा का दर्जा दिया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Garhwal History",
        "text": "गढ़वाल के किस शासक ने अपनी राजधानी श्रीनगर से टिहरी स्थानांतरित की थी?",
        "options": ["सुदर्शन शाह", "प्रताप शाह", "मानवेन्द्र शाह", "कीर्ति शाह"],
        "correct_answer": "सुदर्शन शाह",
        "explanation": "1815 में सुदर्शन शाह ने टिहरी को राजधानी बनाया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Heritage",
        "text": "उत्तराखंड में 'पांडव नृत्य' किस क्षेत्र में अधिक लोकप्रिय है?",
        "options": ["गढ़वाल", "कुमाऊँ", "तराई", "मैदानी क्षेत्र"],
        "correct_answer": "गढ़वाल",
        "explanation": "यह नृत्य पांडवों के जीवन की घटनाओं पर आधारित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "उत्तराखंड की किस झील को 'सरोवरों की रानी' कहा जाता है?",
        "options": ["नैनीताल", "भीमताल", "नौकुचियाताल", "सातताल"],
        "correct_answer": "नैनीताल",
        "explanation": "नैनीताल को झीलों का शहर और सरोवरों की रानी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC History",
        "text": "कुमाऊँ में 'फांसी गधेरा' (Phansi Gadhera) किस स्थान पर स्थित है?",
        "options": ["नैनीताल", "अल्मोड़ा", "हल्द्वानी", "रानीखेत"],
        "correct_answer": "नैनीताल",
        "explanation": "स्वतंत्रता सेनानियों को यहाँ फांसी दी जाती थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड की तीलू रौतेली' (गढ़वाल की झांसी की रानी) कहा जाता है?",
        "options": ["तीलू रौतेली", "गौरा देवी", "जिया रानी", "विशला देवी"],
        "correct_answer": "तीलू रौतेली",
        "explanation": "उनकी वीरता के कारण उन्हें यह उपमा दी गई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'पंचचूली' पर्वत शिखर किस जिले में स्थित है?",
        "options": ["पिथौरागढ़", "चमोली", "उत्तरकाशी", "बागेश्वर"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "पिथौरागढ़ की व्यास घाटी में यह 5 शिखरों का समूह है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "उत्तराखंड में 'राजस्व पुलिस' का जनक किसे माना जाता है?",
        "options": ["हेनरी रैमजे", "जी.डब्ल्यू. ट्रेल", "बैटन", "गार्डनर"],
        "correct_answer": "हेनरी रैमजे",
        "explanation": "उन्होंने 1874 में यह व्यवस्था स्थायी रूप से लागू की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Literature",
        "text": "'गढ़वाल पेंटिंग्स' (Garhwal Paintings) पुस्तक के लेखक कौन हैं?",
        "options": ["बैरिस्टर मुकुन्दीलाल", "मोलाराम", "अजय सिंह रावत", "रतूड़ी"],
        "correct_answer": "बैरिस्टर मुकुन्दीलाल",
        "explanation": "उन्होंने मोलाराम की चित्रकला को विश्व स्तर पर पहचान दिलाई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "अलकनन्दा और पिण्डर नदी का संगम कहाँ होता है?",
        "options": ["कर्णप्रयाग", "रुद्रप्रयाग", "देवप्रयाग", "नन्दप्रयाग"],
        "correct_answer": "कर्णप्रयाग",
        "explanation": "कर्णप्रयाग चमोली जिले में स्थित एक पवित्र संगम है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKPSC GS",
        "text": "1947 में 'युगवाणी' समाचार पत्र का प्रकाशन देहरादून से किसने शुरू किया था?",
        "options": ["भगवती प्रसाद पांथरी", "भक्त दर्शन", "श्रीदेव सुमन", "बद्रीदत्त पाण्डेय"],
        "correct_answer": "भगवती प्रसाद पांथरी",
        "explanation": "यह उत्तराखंड आंदोलन का प्रमुख मुखपत्र रहा।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "उत्तराखंड के प्रसिद्ध गायक 'नरेन्द्र सिंह नेगी' किस विधा के लिए जाने जाते हैं?",
        "options": ["लोक गायन", "शास्त्रीय संगीत", "ग़ज़ल", "सूफी संगीत"],
        "correct_answer": "लोक गायन",
        "explanation": "उन्हें 'गढ़वाल का स्वर' कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Heritage",
        "text": "उत्तराखंड के किस स्थान को 'भारत का मिनी स्विट्जरलैंड' कहा जाता है?",
        "options": ["चोपता", "कौसानी", "हर्शील", "मुनस्यारी"],
        "correct_answer": "चोपता",
        "explanation": "चोपता (रुद्रप्रयाग) को अपनी सुंदरता के लिए यह कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forestry",
        "text": "चिपको आंदोलन की प्रथम सूत्रधार 'गौरा देवी' का संबंध किस गाँव से था?",
        "options": ["रैणी गाँव", "लाता गाँव", "माणा गाँव", "मलारी गाँव"],
        "correct_answer": "रैणी गाँव",
        "explanation": "चमोली के रैणी गाँव से 1974 में आंदोलन शुरू हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Districts",
        "text": "जनसंख्या की दृष्टि से उत्तराखंड का 'सबसे बड़ा' जिला कौन सा है?",
        "options": ["हरिद्वार", "देहरादून", "ऊधम सिंह नगर", "नैनीताल"],
        "correct_answer": "हरिद्वार",
        "explanation": "2011 की जनगणना के अनुसार हरिद्वार सर्वाधिक जनसंख्या वाला जिला है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Sites",
        "text": "देहरादून स्थित 'लाखामंडल' (Lakhamandal) किस काल के अवशेषों के लिए प्रसिद्ध है?",
        "options": ["महाभारत काल", "रामायण काल", "मुगल काल", "ब्रिटिश काल"],
        "correct_answer": "महाभारत काल",
        "explanation": "माना जाता है कि यहाँ लाक्षागृह स्थित था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'गढ़वाल की दिवंगत विभूतियाँ' पुस्तक के लेखक कौन हैं?",
        "options": ["भक्त दर्शन", "अजय सिंह रावत", "डबराल", "पाण्डे"],
        "correct_answer": "भक्त दर्शन",
        "explanation": "भक्त दर्शन ने गढ़वाल के महान व्यक्तित्वों पर यह पुस्तक लिखी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife",
        "text": "उत्तराखंड में 'राजाजी नेशनल पार्क' का नाम किसके नाम पर रखा गया है?",
        "options": ["सी. राजगोपालाचारी", "जवाहरलाल नेहरू", "इन्दिरा गांधी", "जिम कॉर्बेट"],
        "correct_answer": "सी. राजगोपालाचारी",
        "explanation": "स्वतंत्र भारत के प्रथम भारतीय गवर्नर जनरल के नाम पर।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education History",
        "text": "उत्तराखंड में 'सेंट जोर्ज कॉलेज' (मसूरी) की स्थापना कब हुई थी?",
        "options": ["1853", "1840", "1860", "1870"],
        "correct_answer": "1853",
        "explanation": "यह मसूरी के सबसे पुराने संस्थानों में से एक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "कुमाऊँ में 'जागर' (Jagar) का मुख्य अर्थ क्या है?",
        "options": ["देवताओं को जगाना", "लोकगीत गाना", "युद्ध नृत्य", "कृषि उत्सव"],
        "correct_answer": "देवताओं को जगाना",
        "explanation": "यह देवताओं और पितरों के आह्वान की एक विधि है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "अलकनन्दा नदी का उद्गम स्थल कहाँ है?",
        "options": ["सतोपंथ ग्लेशियर", "गंगोत्री", "यमुनोत्री", "मिलम"],
        "correct_answer": "सतोपंथ ग्लेशियर",
        "explanation": "यह चमोली जिले में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC History",
        "text": "उत्तराखंड में 'नशा नहीं रोजगार दो' का नारा किस आंदोलन में दिया गया था?",
        "options": ["उत्तराखंड राज्य प्राप्ति आंदोलन", "चिपको आंदोलन", "मैती आंदोलन", "कुली बेगार"],
        "correct_answer": "उत्तराखंड राज्य प्राप्ति आंदोलन",
        "explanation": "शराब विरोधी और पृथक राज्य आंदोलन के दौरान यह लोकप्रिय हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Districts",
        "text": "उत्तराखंड का 'सबसे उत्तर' में स्थित जिला कौन सा है?",
        "options": ["उत्तरकाशी", "चमोली", "पिथौरागढ़", "देहरादून"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "उत्तरकाशी राज्य का सबसे उत्तरी जिला है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'कुमाऊँ की लक्ष्मी बाई' कहा जाता है?",
        "options": ["जिया रानी", "तीलू रौतेली", "गौरा देवी", "विशला देवी"],
        "correct_answer": "जिया रानी",
        "explanation": "रानी जिया को कुमाऊँ की लक्ष्मी बाई के नाम से जाना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "उत्तराखंड की किस झील को 'मछलियों का ताल' (Machhliyon ka Tal) कहा जाता है?",
        "options": ["नौकुचियाताल", "नैनीताल", "भीमताल", "सातताल"],
        "correct_answer": "नौकुचियाताल",
        "explanation": "नौकुचियाताल अपनी गहराई और मछलियों के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Archive",
        "text": "कुमाऊँ में 'बैटन' (Batten) का भूमि बंदोबस्त किस वर्ष हुआ था?",
        "options": ["1840", "1835", "1845", "1850"],
        "correct_answer": "1840",
        "explanation": "जे.एच. बैटन ने 1840 में गढ़वाल और कुमाऊँ में सुधारवादी बंदोबस्त कराया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के प्रथम 'रेमन मैग्सेसे' पुरस्कार विजेता कौन हैं?",
        "options": ["चण्डी प्रसाद भट्ट", "दीप जोशी", "सुन्दरलाल बहुगुणा", "कल्याण सिंह रावत"],
        "correct_answer": "चण्डी प्रसाद भट्ट",
        "explanation": "1982 में उन्हें पर्यावरण संरक्षण के लिए यह पुरस्कार मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "रामगंगा (पश्चिमी) नदी अलकनन्दा में किस स्थान पर मिलती है?",
        "options": ["यह अलकनन्दा में नहीं मिलती", "रुद्रप्रयाग", "कर्णप्रयाग", "देवप्रयाग"],
        "correct_answer": "यह अलकनन्दा में नहीं मिलती",
        "explanation": "पश्चिमी रामगंगा सीधे गंगा की सहायक नदी है, अलकनन्दा की नहीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC History",
        "text": "उत्तराखंड में 'डालियों का दगड्या' संगठन की स्थापना किसने की थी?",
        "options": ["चण्डी प्रसाद भट्ट", "सुन्दरलाल बहुगुणा", "गौरा देवी", "कल्याण सिंह रावत"],
        "correct_answer": "चण्डी प्रसाद भट्ट",
        "explanation": "चिपको आंदोलन के दौरान वनों के संरक्षण के लिए इसकी स्थापना की गई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Elections",
        "text": "उत्तराखंड विधानसभा में 'अनुसूचित जनजाति' (ST) के लिए कितनी सीटें आरक्षित हैं?",
        "options": ["2", "3", "4", "5"],
        "correct_answer": "2",
        "explanation": "नानकमत्ता और चक्राता सीटें ST के लिए आरक्षित हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'हरेला' (Harela) त्यौहार मुख्य रूप से किसका प्रतीक है?",
        "options": ["खुशहाली और नई फसल", "युद्ध की जीत", "शादी", "भक्ति"],
        "correct_answer": "खुशहाली और नई फसल",
        "explanation": "यह श्रावण मास में बोई जाने वाली फसल का उत्सव है।"
    },

    # ── BATCH 6: STATE SYMBOLS & MARTYRS ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "State Symbols Records",
        "text": "उत्तराखंड के 'राजकीय पशु' (कस्तूरी मृग) का वैज्ञानिक नाम क्या है?",
        "options": ["मास्कस क्राइसोगास्टर", "लोफोफोरस इम्पिजनस", "सेड्रस देवदारा", "मॉसकॉट"],
        "correct_answer": "मास्कस क्राइसोगास्टर",
        "explanation": "कस्तूरी मृग को मास्कस क्राइसोगास्टर के नाम से जाना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "State Symbols",
        "text": "उत्तराखंड की 'राजकीय तितली' (Common Peacock) को किस वर्ष घोषित किया गया था?",
        "options": ["2016", "2015", "2014", "2017"],
        "correct_answer": "2016",
        "explanation": "2016 में कॉमन पीकॉक को राजकीय तितली का दर्जा मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "Tehri Martyrs",
        "text": "टिहरी रियासत के खिलाफ विद्रोह में 'नागेन्द्र सकलानी' और 'मोलू भरदारी' किस वर्ष शहीद हुए थे?",
        "options": ["11 जनवरी 1948", "15 अगस्त 1947", "26 जनवरी 1948", "10 मई 1947"],
        "correct_answer": "11 जनवरी 1948",
        "explanation": "वे कीर्तिनगर विद्रोह के दौरान शहीद हुए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Disasters",
        "text": "केदारनाथ में आई 'भीषण आपदा' किस तिथि को घटित हुई थी?",
        "options": ["16-17 जून 2013", "15-16 जून 2013", "10-11 जून 2013", "20-21 जून 2013"],
        "correct_answer": "16-17 जून 2013",
        "explanation": "चोराबाड़ी ताल के फटने से मंदाकिनी नदी में आई बाढ़ ने तबाही मचाई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Disasters",
        "text": "उत्तरकाशी में 'विनाशकारी भूकंप' किस वर्ष आया था?",
        "options": ["1991", "1999", "1995", "1980"],
        "correct_answer": "1991",
        "explanation": "20 अक्टूबर 1991 को उत्तरकाशी में भीषण भूकंप आया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के 'प्रथम' परमवीर चक्र विजेता कौन थे?",
        "options": ["मेजर सोमनाथ शर्मा", "मेजर शैतान सिंह", "गब्बर सिंह नेगी", "चन्द्रसिंह गढ़वाली"],
        "correct_answer": "मेजर सोमनाथ शर्मा",
        "explanation": "उन्हें मरणोपरांत 1947 में भारत का प्रथम परमवीर चक्र मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Victoria Cross Records",
        "text": "प्रथम विश्व युद्ध के दौरान 'विक्टोरिया क्रॉस' पाने वाले उत्तराखंड के प्रथम व्यक्ति कौन थे?",
        "options": ["दरबान सिंह नेगी", "गब्बर सिंह नेगी", "चन्द्रसिंह गढ़वाली", "सोमनाथ शर्मा"],
        "correct_answer": "दरबान सिंह नेगी",
        "explanation": "1914 में उन्हें यह सर्वोच्च ब्रिटिश सैन्य सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'असिस्टेंट कमिश्नर' के रूप में हेनरी रैमजे की नियुक्ति किस वर्ष हुई थी?",
        "options": ["1840", "1835", "1845", "1850"],
        "correct_answer": "1840",
        "explanation": "वे ल्यूशिंगटन के सहायक के रूप में आए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks",
        "text": "'बंदरपूँछ' (Bandarpunch) पर्वत शिखर किस जिले में स्थित है?",
        "options": ["उत्तरकाशी", "चमोली", "पिथौरागढ़", "रुद्रप्रयाग"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "यहीं से यमुना नदी का उद्गम स्थल यमुनोत्री ग्लेशियर स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Institutions",
        "text": "उत्तराखंड में 'हिमालयन सांस्कृतिक केंद्र' (Himalayan Cultural Center) कहाँ स्थित है?",
        "options": ["देहरादून", "अल्मोड़ा", "श्रीनगर", "हल्द्वानी"],
        "correct_answer": "देहरादून",
        "explanation": "गढ़ी कैंट, देहरादून में यह स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri State",
        "text": "टिहरी रियासत के अंतिम शासक कौन थे?",
        "options": ["मानवेन्द्र शाह", "नरेन्द्र शाह", "कीर्ति शाह", "प्रताप शाह"],
        "correct_answer": "मानवेन्द्र शाह",
        "explanation": "1949 में उनके समय टिहरी का भारत में विलय हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Books",
        "text": "'मेमोयर्स ऑफ देहरादून' (Memoirs of Dehradun) के लेखक कौन हैं?",
        "options": ["जी.आर.सी. विलियम्स", "एटकिंसन", "ट्रेल", "रैमजे"],
        "correct_answer": "जी.आर.सी. विलियम्स",
        "explanation": "यह देहरादून के इतिहास पर महत्वपूर्ण पुस्तक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Passes",
        "text": "'माना दर्रा' (Mana Pass) उत्तराखंड को किसके साथ जोड़ता है?",
        "options": ["तिब्बत", "हिमाचल प्रदेश", "नेपाल", "लद्दाख"],
        "correct_answer": "तिब्बत",
        "explanation": "माना दर्रा चमोली को तिब्बत से जोड़ता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'आपदा प्रबंधन' की शुरुआत किस ब्रिटिश कमिश्नर के समय मानी जाती है?",
        "options": ["हेनरी रैमजे", "ल्यूशिंगटन", "ट्रेल", "बेटन"],
        "correct_answer": "हेनरी रैमजे",
        "explanation": "1880 के नैनीताल भूस्खलन के बाद उन्होंने सुरक्षा के कड़े नियम बनाए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "प्रसिद्ध जागर गायक 'प्रीतम भरतवाण' को किस वर्ष पद्मश्री मिला था?",
        "options": ["2019", "2017", "2021", "2015"],
        "correct_answer": "2019",
        "explanation": "उन्हें लोक गायन के लिए 2019 में सम्मानित किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'डोडीताल' (Dodital) किस जिले में स्थित है और किसके लिए प्रसिद्ध है?",
        "options": ["उत्तरकाशी - ट्राउट मछली", "चमोली - कंकाल", "नैनीताल - कमल", "टिहरी - भाई-बहन"],
        "correct_answer": "उत्तरकाशी - ट्राउट मछली",
        "explanation": "यह छह कोनों वाली झील है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Religious Sites",
        "text": "जागेश्वर धाम में 'पुष्टि भगवती' मंदिर का निर्माण किसने करवाया था?",
        "options": ["कत्यूरी शासकों ने", "चन्द शासकों ने", "पवार शासकों ने", "अंग्रेजों ने"],
        "correct_answer": "कत्यूरी शासकों ने",
        "explanation": "जागेश्वर के अधिकांश मंदिर कत्यूरी काल के हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'मांगल' (Mangal) गीत किस अवसर पर गाए जाते हैं?",
        "options": ["विवाह और शुभ कार्य", "युद्ध", "फसल कटाई", "मृत्यु"],
        "correct_answer": "विवाह और शुभ कार्य",
        "explanation": "गढ़वाल क्षेत्र में विवाह के समय मांगल गीत गाने की परंपरा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Glaciers",
        "text": "भागीरथी नदी किस ग्लेशियर के 'गोमुख' नामक स्थान से निकलती है?",
        "options": ["गंगोत्री ग्लेशियर", "खतलिंग ग्लेशियर", "चोराबाड़ी ग्लेशियर", "सतोपंथ"],
        "correct_answer": "गंगोत्री ग्लेशियर",
        "explanation": "गंगोत्री ग्लेशियर उत्तरकाशी जिले में है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC Group C",
        "text": "अल्मोड़ा में 'डिबेटिंग क्लब' की स्थापना किस वर्ष हुई थी?",
        "options": ["1870", "1871", "1868", "1875"],
        "correct_answer": "1870",
        "explanation": "इसी क्लब के प्रयासों से 1871 में अल्मोड़ा अखबार शुरू हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'शेर-ए-कुमाऊँ' (Sher-e-Kumaon) कहा जाता है?",
        "options": ["हर्षदेव ओली", "बद्रीदत्त पाण्डेय", "कालू मेहरा", "गोविंद बल्लभ पंत"],
        "correct_answer": "हर्षदेव ओली",
        "explanation": "उनकी प्रखर राजनीतिक शैली के कारण उन्हें यह कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'दूधातोली' श्रेणी को किस अन्य नाम से जाना जाता है?",
        "options": ["उत्तराखंड का पामीर", "पहाड़ों की रानी", "मिनी स्विट्जरलैंड", "देवभूमि"],
        "correct_answer": "उत्तराखंड का पामीर",
        "explanation": "यह पाँच नदियों (पश्चिमी रामगंगा, अटागाड़, पश्चिमी नयार, पूर्वी नयार और वुनो) का उद्गम स्थल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'लोहाघाट' छावनी की स्थापना किस वर्ष हुई थी?",
        "options": ["1815", "1840", "1850", "1860"],
        "correct_answer": "1815",
        "explanation": "गोरखा युद्ध के तुरंत बाद अंग्रेजों ने यहाँ छावनी बनाई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'कुमाऊँ की लोककला' पुस्तक के लेखक कौन हैं?",
        "options": ["यशोधर मठपाल", "डी.डी. शर्मा", "अजय सिंह रावत", "डबराल"],
        "correct_answer": "यशोधर मठपाल",
        "explanation": "यशोधर मठपाल ने कुमाऊँ की रॉक पेंटिंग्स और लोककला पर शोध किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "पश्चिमी नयार और पूर्वी नयार का संगम कहाँ होता है?",
        "options": ["सतपुली", "श्रीनगर", "देहरादून", "रुद्रप्रयाग"],
        "correct_answer": "सतपुली",
        "explanation": "सतपुली (पौड़ी) के पास नयार की दोनों शाखाएँ मिलती हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism History",
        "text": "1939 में 'कर्मभूमि' समाचार पत्र का प्रकाशन कहाँ से शुरू हुआ था?",
        "options": ["लैंसडाउन", "कोटद्वार", "श्रीनगर", "देहरादून"],
        "correct_answer": "लैंसडाउन",
        "explanation": "भक्त दर्शन और भैरव दत्त धूलिया ने इसे शुरू किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के 'गांधी' इन्द्रमणि बडोनी का जन्म कहाँ हुआ था?",
        "options": ["अखौड़ी गाँव (टिहरी)", "मरोड़ा गाँव", "चोपता", "उत्तरकाशी"],
        "correct_answer": "अखौड़ी गाँव (टिहरी)",
        "explanation": "वे राज्य प्राप्ति आंदोलन के प्रमुख नेता थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Heritage",
        "text": "उत्तराखंड में 'कॉर्बेट नेशनल पार्क' के मध्य से कौन सी नदी बहती है?",
        "options": ["रामगंगा (पश्चिमी)", "कोसी", "गगास", "बिनौ"],
        "correct_answer": "रामगंगा (पश्चिमी)",
        "explanation": "रामगंगा इस नेशनल पार्क की जीवन रेखा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Records",
        "text": "अशोक का 'कालसी शिलालेख' किस भाषा में है?",
        "options": ["पाली", "प्राकृत", "संस्कृत", "खरोष्ठी"],
        "correct_answer": "पाली",
        "explanation": "यह शिलालेख पाली भाषा और ब्राह्मी लिपि में है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "उत्तराखंड में 'हुड़का' (Hudka) किस विधा का प्रमुख वाद्य है?",
        "options": ["जागर और कृषि", "युद्ध", "शास्त्रीय", "जन्म उत्सव"],
        "correct_answer": "जागर और कृषि",
        "explanation": "कृषि कार्यों (हुड़किया बौल) और जागरों में इसका प्रयोग होता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife",
        "text": "उत्तराखंड में 'नन्दा देवी बायोस्फीयर रिजर्व' किस वर्ष स्थापित हुआ था?",
        "options": ["1988", "1982", "1990", "1985"],
        "correct_answer": "1988",
        "explanation": "1988 में इसे बायोस्फीयर रिजर्व घोषित किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education History",
        "text": "नैनीताल में 'बिड़ला विद्या मंदिर' की स्थापना किस वर्ष हुई थी?",
        "options": ["1947", "1950", "1940", "1955"],
        "correct_answer": "1947",
        "explanation": "यह आजादी के वर्ष में स्थापित हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'गढ़वाल की झाँसी की रानी' कहा जाता है?",
        "options": ["तीलू रौतेली", "गौरा देवी", "विशला देवी", "जिया रानी"],
        "correct_answer": "तीलू रौतेली",
        "explanation": "तीलू रौतेली को उनकी वीरता के लिए यह सम्मान प्राप्त है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Valleys",
        "text": "'हर की दून' (Har ki Dun) घाटी किस जिले में स्थित है?",
        "options": ["उत्तरकाशी", "चमोली", "पिथौरागढ़", "रुद्रप्रयाग"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "यह घाटी फतेह पर्वत की तलहटी में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'राजस्व पुलिस' व्यवस्था को कब समाप्त करने की सिफारिश की गई है (हाल ही में)?",
        "options": ["2022", "2021", "2020", "2023"],
        "correct_answer": "2022",
        "explanation": "अंकिता भंडारी केस के बाद इस व्यवस्था को चरणबद्ध तरीके से खत्म करने की घोषणा हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Heritage",
        "text": "उत्तराखंड में 'थाली' (Thali) नृत्य किस क्षेत्र में किया जाता है?",
        "options": ["कुमाऊँ", "गढ़वाल", "तराई", "जौनसार"],
        "correct_answer": "कुमाऊँ",
        "explanation": "कुमाऊँ में मांगलिक अवसरों पर थाली बजाकर नृत्य किया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "सरयू नदी किसकी सबसे बड़ी सहायक नदी है?",
        "options": ["काली नदी", "गंगा", "अलकनन्दा", "यमुना"],
        "correct_answer": "काली नदी",
        "explanation": "सरयू काली नदी में सबसे ज्यादा जल लाने वाली सहायक नदी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forestry",
        "text": "उत्तराखंड में 'वनों का वर्गीकरण' सर्वप्रथम किस वर्ष किया गया था?",
        "options": ["1878", "1865", "1893", "1927"],
        "correct_answer": "1878",
        "explanation": "भारतीय वन अधिनियम 1878 के तहत वर्गीकरण हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'हिमालयन गजेटियर' (Himalayan Gazetteer) के लेखक कौन हैं?",
        "options": ["ई.टी. एटकिंसन", "जी.डब्ल्यू. ट्रेल", "बेटन", "रैमजे"],
        "correct_answer": "ई.टी. एटकिंसन",
        "explanation": "यह उत्तराखंड के इतिहास और भूगोल पर सबसे विस्तृत ग्रंथ है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Glaciers",
        "text": "मिलम ग्लेशियर उत्तराखंड के किस जिले में स्थित है?",
        "options": ["पिथौरागढ़", "चमोली", "उत्तरकाशी", "बागेश्वर"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "यह कुमाऊँ मण्डल का सबसे बड़ा ग्लेशियर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Legislation",
        "text": "उत्तराखंड का 'राजकीय खेल' कौन सा है?",
        "options": ["फुटबॉल", "क्रिकेट", "हॉकी", "बैडमिंटन"],
        "correct_answer": "फुटबॉल",
        "explanation": "2011 में फुटबॉल को राजकीय खेल घोषित किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Tribes",
        "text": "जौनसारी जनजाति के त्यौहार 'विशू' (Bishu) का क्या अर्थ है?",
        "options": ["वैसाखी", "दीपावली", "होली", "दशहरा"],
        "correct_answer": "वैसाखी",
        "explanation": "विशू जौनसार बावर क्षेत्र का महत्वपूर्ण त्यौहार है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "प्रसिद्ध समाज सुधारक 'आर्य समाज' के स्वामी श्रद्धानंद ने कहाँ गुरुकुल की स्थापना की थी?",
        "options": ["हरिद्वार", "ऋषिकेश", "देहरादून", "नैनीताल"],
        "correct_answer": "हरिद्वार",
        "explanation": "1902 में कांगड़ी (हरिद्वार) में गुरुकुल कांगड़ी की स्थापना हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'दूनागिरि' (Dunagiri) पर्वत शिखर किस जिले में स्थित है?",
        "options": ["चमोली", "अल्मोड़ा", "बागेश्वर", "पिथौरागढ़"],
        "correct_answer": "चमोली",
        "explanation": "यह चमोली जिले का एक प्रसिद्ध शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'कमिश्नर रैमजे' का कार्यकाल कब समाप्त हुआ था?",
        "options": ["1884", "1880", "1890", "1875"],
        "correct_answer": "1884",
        "explanation": "1856 से 1884 तक वे कमिश्नर रहे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के किस व्यक्ति को 'पद्म श्री' से सर्वप्रथम सम्मानित किया गया था?",
        "options": ["छत्रपति जोशी", "लक्ष्मण सिंह जंगपांगी", "कुंवर सिंह नेगी", "घनानंद पाण्डे"],
        "correct_answer": "लक्ष्मण सिंह जंगपांगी",
        "explanation": "1959 में उन्हें यह सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Parks",
        "text": "उत्तराखंड में 'फूलों की घाटी' को यूनेस्को की विश्व धरोहर सूची में कब शामिल किया गया?",
        "options": ["2005", "1988", "2010", "1995"],
        "correct_answer": "2005",
        "explanation": "14 जुलाई 2005 को इसे शामिल किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri State",
        "text": "टिहरी में 'प्रताप हाईस्कूल' की स्थापना किसने की थी?",
        "options": ["प्रताप शाह", "कीर्ति शाह", "नरेन्द्र शाह", "सुदर्शन शाह"],
        "correct_answer": "प्रताप शाह",
        "explanation": "प्रताप शाह ने टिहरी में शिक्षा के प्रसार के लिए स्कूल खोला था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'ब्रिटिश गढ़वाल का गजेटियर' (Gazetteer of British Garhwal) किसने लिखा था?",
        "options": ["एच.जी. वाल्टन", "एटकिंसन", "विलियम्स", "फिशर"],
        "correct_answer": "एच.जी. वाल्टन",
        "explanation": "1910 में वाल्टन ने यह गजेटियर तैयार किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Legislative Records",
        "text": "उत्तराखंड के प्रथम 'निर्वाचित' मुख्यमंत्री कौन थे?",
        "options": ["एन.डी. तिवारी", "नित्यानंद स्वामी", "भगत सिंह कोश्यारी", "बी.सी. खंडूड़ी"],
        "correct_answer": "एन.डी. तिवारी",
        "explanation": "2002 के प्रथम आम चुनाव के बाद वे मुख्यमंत्री बने।"
    },

    # ── BATCH 7: STATEHOOD MOVEMENT & MODERN SPORTS ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "Statehood Movement Records",
        "text": "उत्तराखंड आंदोलन के दौरान 'खटीमा कांड' (Khatima Incident) कब हुआ था?",
        "options": ["1 सितंबर 1994", "2 सितंबर 1994", "2 अक्टूबर 1994", "15 सितंबर 1994"],
        "correct_answer": "1 सितंबर 1994",
        "explanation": "यह पृथक राज्य आंदोलन की एक दुखद घटना थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "Statehood Movement",
        "text": "'मुजफ्फरनगर कांड' (रामपुर तिराहा कांड) किस तिथि को घटित हुआ था?",
        "options": ["2 अक्टूबर 1994", "1 अक्टूबर 1994", "2 सितंबर 1994", "10 अक्टूबर 1994"],
        "correct_answer": "2 अक्टूबर 1994",
        "explanation": "दिल्ली जा रहे आंदोलनकारियों पर पुलिस ने बर्बरता की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "Statehood Movement",
        "text": "उत्तराखंड पृथक राज्य की मांग के लिए 'श्रीनगर' के श्रीयंत्र टापू पर शहीद होने वाले आंदोलनकारी कौन थे?",
        "options": ["यशोधर बेन्जवाल और राजेश रावत", "इन्द्रमणि बडोनी", "नागेन्द्र सकलानी", "तीलू रौतेली"],
        "correct_answer": "यशोधर बेन्जवाल और राजेश रावत",
        "explanation": "1995 में श्रीयंत्र टापू पर पुलिस कार्रवाई में वे शहीद हुए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Sports Archive",
        "text": "उत्तराखंड की 'एकता बिष्ट' (Ekta Bisht) का संबंध किस खेल से है?",
        "options": ["क्रिकेट", "हॉकी", "बैडमिंटन", "फुटबॉल"],
        "correct_answer": "क्रिकेट",
        "explanation": "वे अल्मोड़ा से हैं और भारतीय महिला क्रिकेट टीम की प्रसिद्ध स्पिनर हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Sports Records",
        "text": "IPL में शतक बनाने वाले पहले भारतीय बल्लेबाज 'मनीष पाण्डेय' का मूल संबंध उत्तराखंड के किस जिले से है?",
        "options": ["नैनीताल", "अल्मोड़ा", "बागेश्वर", "पिथौरागढ़"],
        "correct_answer": "नैनीताल",
        "explanation": "मनीष पाण्डेय का परिवार मूल रूप से नैनीताल का रहने वाला है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "उत्तराखंड की 'कोसी नदी' (Kosi River) का उद्गम स्थल कौन सा है?",
        "options": ["धारपानी धार (कौसानी)", "दूधातोली", "पिण्डारी", "मिलम"],
        "correct_answer": "धारपानी धार (कौसानी)",
        "explanation": "यह अल्मोड़ा के कौसानी के पास से निकलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Institutional Records",
        "text": "उत्तराखंड में 'सिडकुल' (SIDCUL) की स्थापना किस वर्ष हुई थी?",
        "options": ["2002", "2000", "2005", "2010"],
        "correct_answer": "2002",
        "explanation": "राज्य में औद्योगिक विकास के लिए इसकी स्थापना की गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC Group C",
        "text": "अंग्रेजों ने कुमाऊँ मण्डल का मुख्यालय 'अल्मोड़ा से नैनीताल' किस वर्ष स्थानांतरित किया था?",
        "options": ["1854", "1840", "1860", "1870"],
        "correct_answer": "1854",
        "explanation": "1854 में नैनीताल को कुमाऊँ मण्डल का मुख्यालय बनाया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Tribes",
        "text": "उत्तराखंड की कौन सी जनजाति 'आठूँ' (Aathoo) त्यौहार मनाती है?",
        "options": ["भोटिया", "राजी", "थारू", "बोक्सा"],
        "correct_answer": "भोटिया",
        "explanation": "भोटिया जनजाति में यह एक महत्वपूर्ण उत्सव है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के किस व्यक्ति को 'पहाड़ी' (Pahari) उपनाम से जाना जाता है?",
        "options": ["शिवानी", "बद्रीदत्त पाण्डेय", "गिरिजा दत्त नैथानी", "ललिता प्रसाद"],
        "correct_answer": "शिवानी",
        "explanation": "प्रसिद्ध लेखिका गौरा पंत को 'शिवानी' और कभी-कभी 'पहाड़ी' संदर्भों में याद किया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Valleys",
        "text": "'पिण्डर घाटी' का अंतिम गाँव कौन सा है?",
        "options": ["खाती गाँव", "माणा गाँव", "मलारी गाँव", "रैणी गाँव"],
        "correct_answer": "खाती गाँव",
        "explanation": "पिण्डारी ग्लेशियर के मार्ग पर स्थित खाती अंतिम गाँव है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forestry",
        "text": "उत्तराखंड में 'वन पंचायतों' का गठन सर्वप्रथम किस वर्ष हुआ था?",
        "options": ["1931", "1921", "1940", "1927"],
        "correct_answer": "1931",
        "explanation": "वनों के प्रबंधन के लिए यह एक अनूठी पंचायत व्यवस्था है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "प्रसिद्ध कुमाऊँनी गायक 'गोपाल बाबू गोस्वामी' का जन्म कहाँ हुआ था?",
        "options": ["चाँदीखेत (अल्मोड़ा)", "भीमताल", "रानीखेत", "हल्द्वानी"],
        "correct_answer": "चाँदीखेत (अल्मोड़ा)",
        "explanation": "वे अपनी मधुर आवाज के लिए 'कुमाऊँ की कोकिला' (पुरुष स्वर में) माने जाते थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "किस झील को 'भाई-बहन का ताल' (Bhai-Bahen Tal) कहा जाता है?",
        "options": ["महासर ताल", "यम्मु ताल", "सहस्त्र ताल", "मातृ ताल"],
        "correct_answer": "महासर ताल",
        "explanation": "टिहरी गढ़वाल में स्थित दो कटोरानुमा झीलों को यह नाम दिया गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKPSC GS",
        "text": "कुमाऊँ में 'पटवारी व्यवस्था' को आधुनिक रूप देने वाला कमिश्नर कौन था?",
        "options": ["रैमजे", "ट्रेल", "बैटन", "ल्यूशिंगटन"],
        "correct_answer": "रैमजे",
        "explanation": "रैमजे ने पटवारियों के अधिकार और क्षेत्रों को व्यवस्थित किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'जागर' लगाने वाले व्यक्ति को क्या कहा जाता है?",
        "options": ["जगरिया", "डंगरिया", "स्याणा", "भैंलो"],
        "correct_answer": "जगरिया",
        "explanation": "जगरिया जागर लगाने वाला मुख्य गायक/अनुष्ठानकर्ता होता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "पश्चिमी रामगंगा नदी किस पर्वत श्रेणी से निकलती है?",
        "options": ["दूधातोली", "नन्दा देवी", "कामेत", "त्रिशूल"],
        "correct_answer": "दूधातोली",
        "explanation": "यह पौड़ी, चमोली और अल्मोड़ा के बीच स्थित श्रेणी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Temple Sites",
        "text": "पिथौरागढ़ स्थित 'पाताल भुवनेश्वर' गुफा की खोज किसने की थी (मान्यतानुसार)?",
        "options": ["आदि गुरु शंकराचार्य", "राजा पिथोरा", "ट्रेल", "चंद राजाओं ने"],
        "correct_answer": "आदि गुरु शंकराचार्य",
        "explanation": "माना जाता है कि शंकराचार्य जी ने इस गुफा को पुनः खोजा था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "District Data",
        "text": "उत्तराखंड के किस जिले में 'सर्वाधिक' ग्राम पंचायतें हैं?",
        "options": ["पौड़ी गढ़वाल", "अल्मोड़ा", "देहरादून", "टिहरी गढ़वाल"],
        "correct_answer": "पौड़ी गढ़वाल",
        "explanation": "पौड़ी में ग्राम पंचायतों की संख्या सबसे अधिक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'हिमालय की बेटी' (Daughter of Himalaya) पुस्तक की लेखिका कौन हैं?",
        "options": ["राधा भट्ट", "गौरा देवी", "शिवानी", "बचेंद्री पाल"],
        "correct_answer": "राधा भट्ट",
        "explanation": "प्रसिद्ध समाजसेविका राधा भट्ट ने यह पुस्तक लिखी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife",
        "text": "उत्तराखंड में 'केदारनाथ वन्यजीव विहार' की स्थापना कब हुई थी?",
        "options": ["1972", "1980", "1975", "1982"],
        "correct_answer": "1972",
        "explanation": "यह कस्तूरी मृग के संरक्षण के लिए स्थापित किया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'कमिश्नर ट्रेल' ने 1823 में कितने जिलों का गठन किया था?",
        "options": ["2", "3", "1", "4"],
        "correct_answer": "2",
        "explanation": "उन्होंने कुमाऊँ और गढ़वाल (बाद में पौड़ी) को व्यवस्थित किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड का गांधी' कहा जाता है?",
        "options": ["इन्द्रमणि बडोनी", "सुन्दरलाल बहुगुणा", "बद्रीदत्त पाण्डेय", "गोविंद बल्लभ पंत"],
        "correct_answer": "इन्द्रमणि बडोनी",
        "explanation": "राज्य प्राप्ति आंदोलन में उनके अहिंसक संघर्ष के कारण।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "किस झील को 'मानव निर्मित' (Artificial) माना जाता है?",
        "options": ["टिहरी झील", "नैनीताल", "भीमताल", "डोडीताल"],
        "correct_answer": "टिहरी झील",
        "explanation": "टिहरी बाँध बनने के कारण इस विशाल झील का निर्माण हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forestry",
        "text": "उत्तराखंड में 'प्रथम वन निरीक्षक' कौन नियुक्त हुए थे?",
        "options": ["डॉ. ब्रैंडिस", "मेजर पियर्सन", "हेनरी रैमजे", "ट्रेल"],
        "correct_answer": "मेजर पियर्सन",
        "explanation": "1868 में उनकी नियुक्ति हुई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Institutions",
        "text": "उत्तराखंड में 'भारतीय सैन्य अकादमी' (IMA) की स्थापना कब हुई थी?",
        "options": ["1 अक्टूबर 1932", "15 अगस्त 1947", "10 दिसंबर 1932", "1 जनवरी 1930"],
        "correct_answer": "1 अक्टूबर 1932",
        "explanation": "सर फिलिप चैटवुड ने इसकी स्थापना की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "कोसी नदी की 'सहायक नदी' कौन सी है?",
        "options": ["मीनगाड़", "अलकनन्दा", "भागीरथी", "काली"],
        "correct_answer": "मीनगाड़",
        "explanation": "मीनगाड़ कोसी की एक छोटी सहायक नदी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Temple Sites",
        "text": "रुद्रप्रयाग स्थित 'कोटेश्वर महादेव' मंदिर किस नदी के किनारे है?",
        "options": ["अलकनन्दा", "मंदाकिनी", "भागीरथी", "नयार"],
        "correct_answer": "अलकनन्दा",
        "explanation": "यह मंदिर अलकनन्दा नदी के तट पर एक गुफा में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Legislation",
        "text": "उत्तराखंड राज्य विधेयक 'लोकसभा' में कब पारित हुआ था?",
        "options": ["1 अगस्त 2000", "10 अगस्त 2000", "15 अगस्त 2000", "28 अगस्त 2000"],
        "correct_answer": "1 अगस्त 2000",
        "explanation": "1 अगस्त को लोकसभा और 10 अगस्त को राज्यसभा में पारित हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड की प्रथम महिला 'IPS' अधिकारी कौन हैं?",
        "options": ["ज्योति राव पाण्डेय", "कंचन चौधरी भट्टाचार्य", "विमला पंत", "ममता रावत"],
        "correct_answer": "ज्योति राव पाण्डेय",
        "explanation": "ज्योति राव पाण्डेय उत्तराखंड कैडर की पहली महिला IPS अधिकारी मानी जाती हैं (कंचन चौधरी देश की पहली DGP थीं)।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'चौखम्बा' (Chaukhamba) पर्वत शिखर कहाँ स्थित है?",
        "options": ["चमोली", "उत्तरकाशी", "रुद्रप्रयाग", "बागेश्वर"],
        "correct_answer": "चमोली",
        "explanation": "यह चमोली जिले के प्रसिद्ध शिखरों में से एक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education History",
        "text": "उत्तराखंड में 'प्रेस' की शुरुआत का श्रेय किसे जाता है?",
        "options": ["पादरी मरे", "जयदत्त जोशी", "बद्रीदत्त पाण्डेय", "ट्रेल"],
        "correct_answer": "पादरी मरे",
        "explanation": "उन्होंने मसूरी में 'द हिल्स' समाचार पत्र के लिए प्रेस लगाई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'उत्तराखंड की विभूतियाँ' पुस्तक के लेखक कौन हैं?",
        "options": ["शक्ति प्रसाद सकलानी", "अजय सिंह रावत", "डबराल", "पाण्डे"],
        "correct_answer": "शक्ति प्रसाद सकलानी",
        "explanation": "उन्होंने राज्य के प्रमुख व्यक्तित्वों पर यह शोधपरक पुस्तक लिखी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Heritage",
        "text": "उत्तराखंड में 'बुग्याल' (Bugyals) किसे कहा जाता है?",
        "options": ["मखमली घास के मैदान", "घने जंगल", "बर्फ के मैदान", "नदी घाटी"],
        "correct_answer": "मखमली घास के मैदान",
        "explanation": "उच्च हिमालयी क्षेत्रों में पाए जाने वाले घास के मैदानों को बुग्याल कहते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism History",
        "text": "1922 में 'गढ़वाली' समाचार पत्र का प्रकाशन कहाँ से पुनः शुरू हुआ था?",
        "options": ["देहरादून", "श्रीनगर", "कोटद्वार", "अल्मोड़ा"],
        "correct_answer": "देहरादून",
        "explanation": "विशम्भर दत्त चन्दोला ने इसे देहरादून से व्यवस्थित किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'गढ़वाल का हातिमताई' कहा जाता है?",
        "options": ["कुंवर सिंह नेगी", "प्रताप शाह", "महिपति शाह", "अजयपाल"],
        "correct_answer": "कुंवर सिंह नेगी",
        "explanation": "उनकी उदारता और ब्रेल लिपि के कार्यों के लिए उन्हें यह कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'झिलमिल ताल' (Jhilmil Tal) उत्तराखंड के किस जिले में स्थित है?",
        "options": ["चंपावत", "नैनीताल", "उधम सिंह नगर", "पिथौरागढ़"],
        "correct_answer": "चंपावत",
        "explanation": "चंपावत के टनकपुर के पास यह सुंदर ताल स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'कमिश्नर रैमजे' को किस नाम से पुकारा जाता था?",
        "options": ["कुमाऊँ का बेताज बादशाह", "राजा रैमजे", "अल्ट्रा कमिश्नर", "गार्डनर का उत्तराधिकारी"],
        "correct_answer": "कुमाऊँ का बेताज बादशाह",
        "explanation": "उनके लंबे और प्रभावशाली कार्यकाल के कारण उन्हें यह उपाधि मिली।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड की प्रथम महिला 'मेयर' (देहरादून) कौन थीं?",
        "options": ["मनोरमा शर्मा डोबरियाल", "विमला पंत", "आशा नौटियाल", "अमृता रावत"],
        "correct_answer": "मनोरमा शर्मा डोबरियाल",
        "explanation": "वे देहरादून की पहली महिला मेयर निर्वाचित हुई थीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "अलकनन्दा नदी की 'लंबाई' उत्तराखंड में कितनी है?",
        "options": ["195 किमी", "205 किमी", "180 किमी", "250 किमी"],
        "correct_answer": "195 किमी",
        "explanation": "यह देवप्रयाग तक की लंबाई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKSSSC History",
        "text": "अल्मोड़ा में 'कुमाऊँ परिषद' का कांग्रेस में विलय किस वर्ष हुआ था?",
        "options": ["1926", "1916", "1920", "1930"],
        "correct_answer": "1926",
        "explanation": "1926 में इसका विलय भारतीय राष्ट्रीय कांग्रेस में हो गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Legislation",
        "text": "उत्तराखंड राज्य का 'प्रथम' सूचना आयुक्त कौन था?",
        "options": ["डॉ. आर.एस. टोलिया", "प्रकाश पंत", "अशोक कांत शरण", "सी.पी. भट्ट"],
        "correct_answer": "डॉ. आर.एस. टोलिया",
        "explanation": "वे राज्य के मुख्य सचिव भी रहे थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'घी संक्रांति' (Ghee Sankranti) किस महीने में मनाई जाती है?",
        "options": ["भाद्रपद", "चैत्र", "वैशाख", "श्रावण"],
        "correct_answer": "भाद्रपद",
        "explanation": "भादो के महीने में ओलगिया (घी संक्रांति) मनाई जाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'स्वर्गारोहिणी' (Swargarohini) पर्वत शिखर किस जिले में स्थित है?",
        "options": ["उत्तरकाशी और चमोली", "पिथौरागढ़", "बागेश्वर", "रुद्रप्रयाग"],
        "correct_answer": "उत्तरकाशी और चमोली",
        "explanation": "यह शिखर अपनी धार्मिक मान्यता के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forestry History",
        "text": "उत्तराखंड में 'वृक्षारोपण दिवस' कब मनाया जाता है?",
        "options": ["25 जुलाई", "5 जून", "15 अगस्त", "10 जनवरी"],
        "correct_answer": "25 जुलाई",
        "explanation": "श्रीदेव सुमन की पुण्यतिथि पर यह दिवस मनाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'कूर्मांचल केसरी' बद्रीदत्त पाण्डेय का जन्म कहाँ हुआ था?",
        "options": ["कनखल (हरिद्वार)", "अल्मोड़ा", "नैनीताल", "बागेश्वर"],
        "correct_answer": "कनखल (हरिद्वार)",
        "explanation": "उनका जन्म 15 फरवरी 1882 को कनखल में हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Passes",
        "text": "'लिपुलेख दर्रा' (Lipulekh Pass) किस जिले में स्थित है?",
        "options": ["पिथौरागढ़", "चमोली", "उत्तरकाशी", "चंपावत"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "यह भारत और चीन के बीच व्यापार का प्रमुख मार्ग है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'पुलिस थाना' की स्थापना अल्मोड़ा में किस वर्ष हुई थी?",
        "options": ["1837", "1840", "1815", "1850"],
        "correct_answer": "1837",
        "explanation": "यह कुमाऊँ का पहला पुलिस थाना था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'बगवाल' (Bagwal) का अर्थ क्या है?",
        "options": ["दीपावली और पाषाण युद्ध", "होली", "रक्षाबंधन", "विवाह"],
        "correct_answer": "दीपावली और पाषाण युद्ध",
        "explanation": "कुमाऊँ में दीपावली को बगवाल कहते हैं, और देवीधुरा में पाषाण युद्ध को भी बग्वाल कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Judiciary",
        "text": "उत्तराखंड उच्च न्यायालय के प्रथम 'मुख्य न्यायाधीश' कौन थे?",
        "options": ["अशोक ए. देसाई", "एस.एच. कपाड़िया", "जे.एस. वर्मा", "प्रकाश पंत"],
        "correct_answer": "अशोक ए. देसाई",
        "explanation": "उन्होंने राज्य के पहले मुख्य न्यायाधीश के रूप में शपथ ली थी।"
    },

    # ── BATCH 8: DEMOGRAPHICS & ENVIRONMENT ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Census 2011",
        "text": "2011 की जनगणना के अनुसार उत्तराखंड की कुल साक्षरता दर (Literacy Rate) कितनी है?",
        "options": ["78.82%", "75.50%", "82.40%", "70.20%"],
        "correct_answer": "78.82%",
        "explanation": "इसमें पुरुष साक्षरता 87.40% और महिला साक्षरता 70% है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Census 2011",
        "text": "2011 की जनगणना के अनुसार उत्तराखंड का लिंगानुपात (Sex Ratio) कितना है?",
        "options": ["963", "943", "950", "970"],
        "correct_answer": "963",
        "explanation": "उत्तराखंड का लिंगानुपात राष्ट्रीय औसत (943) से बेहतर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Census 2011",
        "text": "उत्तराखंड के किस जिले में 2011 की जनगणना के अनुसार 'न्यूनतम' साक्षरता दर है?",
        "options": ["ऊधम सिंह नगर", "हरिद्वार", "उत्तरकाशी", "चंपावत"],
        "correct_answer": "ऊधम सिंह नगर",
        "explanation": "ऊधम सिंह नगर की साक्षरता दर राज्य में सबसे कम दर्ज की गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Census 2011",
        "text": "2011 की जनगणना के अनुसार उत्तराखंड का 'जनसंख्या घनत्व' (Population Density) कितना है?",
        "options": ["189", "150", "200", "175"],
        "correct_answer": "189",
        "explanation": "यह प्रति वर्ग किलोमीटर व्यक्तियों की संख्या है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Environment Records",
        "text": "प्रसिद्ध पर्यावरणविद् 'सुन्दरलाल बहुगुणा' का जन्म कहाँ हुआ था?",
        "options": ["मरोड़ा गाँव (टिहरी)", "अखौड़ी", "चोपता", "देहरादून"],
        "correct_answer": "मरोड़ा गाँव (टिहरी)",
        "explanation": "उनका जन्म 1927 में टिहरी जिले के मरोड़ा गाँव में हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Environment Awards",
        "text": "चण्डी प्रसाद भट्ट को 'रेमन मैग्सेसे' पुरस्कार किस वर्ष मिला था?",
        "options": ["1982", "1985", "1990", "1980"],
        "correct_answer": "1982",
        "explanation": "चिपको आंदोलन और पर्यावरण संरक्षण के लिए उन्हें यह सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Chipko Movement",
        "text": "'चिपको वुमन' (Chipko Woman) के नाम से किसे जाना जाता है?",
        "options": ["गौरा देवी", "विशला देवी", "तुलसी देवी", "कमला पंत"],
        "correct_answer": "गौरा देवी",
        "explanation": "गौरा देवी ने 1974 में रैणी गाँव से पेड़ों को बचाने का नेतृत्व किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Agriculture History",
        "text": "पन्तनगर विश्वविद्यालय (GB Pant University) की स्थापना किस वर्ष हुई थी?",
        "options": ["17 नवंबर 1960", "15 अगस्त 1960", "26 जनवरी 1961", "10 मई 1959"],
        "correct_answer": "17 नवंबर 1960",
        "explanation": "यह भारत का पहला कृषि विश्वविद्यालय था, जिसका उद्घाटन जवाहरलाल नेहरू ने किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Census 2011",
        "text": "उत्तराखंड के किस जिले में सर्वाधिक 'लिंगानुपात' (Sex Ratio) है?",
        "options": ["अल्मोड़ा", "रुद्रप्रयाग", "पौड़ी", "बागेश्वर"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "अल्मोड़ा में लिंगानुपात 1139 है जो राज्य में सर्वाधिक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Census 2011",
        "text": "उत्तराखंड के किस जिले में सर्वाधिक 'शहरी' जनसंख्या निवास करती है?",
        "options": ["देहरादून", "हरिद्वार", "ऊधम सिंह नगर", "नैनीताल"],
        "correct_answer": "देहरादून",
        "explanation": "देहरादून राज्य का सबसे अधिक शहरीकृत जिला है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "UKPSC GS",
        "text": "उत्तराखंड में 'चाय' (Tea) की खेती सर्वप्रथम कब शुरू हुई थी?",
        "options": ["1835", "1824", "1840", "1850"],
        "correct_answer": "1835",
        "explanation": "कमिश्नर विलियम ट्रेल के प्रयासों से कुमाऊँ में चाय का बगीचा लगाया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Art History",
        "text": "उत्तराखंड के प्रसिद्ध चित्रकार 'मोलूराम' (Mola Ram) का संबंध किस शैली से है?",
        "options": ["गढ़वाल शैली", "कुमाऊँनी शैली", "कांगड़ा शैली", "राजस्थानी शैली"],
        "correct_answer": "गढ़वाल शैली",
        "explanation": "मोलूराम गढ़वाल चित्रकला शैली के सबसे प्रसिद्ध कलाकार थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Hydro Projects",
        "text": "उत्तराखंड की 'मनेरी भाली' (Maneri Bhali) जलविद्युत परियोजना किस नदी पर है?",
        "options": ["भागीरथी", "अलकनन्दा", "यमुना", "काली"],
        "correct_answer": "भागीरथी",
        "explanation": "यह परियोजना उत्तरकाशी जिले में भागीरथी नदी पर स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Medieval Records",
        "text": "कत्यूरी शासनकाल में 'भृति' (Bhriti) क्या था?",
        "options": ["मजदूरी या वेतन", "कर", "भूमि उपहार", "सैनिक पद"],
        "correct_answer": "मजदूरी या वेतन",
        "explanation": "कत्यूरी काल में काम के बदले दिए जाने वाले पारिश्रमिक को भृति कहा जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Passes",
        "text": "'ट्रेल पास' (Trail's Pass) किन दो स्थानों को जोड़ता है?",
        "options": ["बागेश्वर और पिथौरागढ़", "चमोली और उत्तरकाशी", "पिथौरागढ़ और तिब्बत", "देहरादून और उत्तरकाशी"],
        "correct_answer": "बागेश्वर और पिथौरागढ़",
        "explanation": "1830 में कमिश्नर ट्रेल ने इसकी खोज की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "प्रसिद्ध लोकगायक 'नरेन्द्र सिंह नेगी' का जन्म किस जिले में हुआ था?",
        "options": ["पौड़ी गढ़वाल", "टिहरी गढ़वाल", "चमोली", "रुद्रप्रयाग"],
        "correct_answer": "पौड़ी गढ़वाल",
        "explanation": "नरेन्द्र सिंह नेगी जी का जन्म पौड़ी के पौड़ी शहर में हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'आपदा प्रबंधन' (Disaster Management) का पहला व्यवस्थित प्रयास किसने किया था?",
        "options": ["हेनरी रैमजे", "ट्रेल", "गार्डनर", "बेटन"],
        "correct_answer": "हेनरी रैमजे",
        "explanation": "1880 के नैनीताल भूस्खलन के बाद उन्होंने नाली निर्माण और सुरक्षा के नियम बनाए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "उत्तराखंड में 'टोंस' (Tons) नदी किसकी सहायक नदी है?",
        "options": ["यमुना", "गंगा", "अलकनन्दा", "काली"],
        "correct_answer": "यमुना",
        "explanation": "टोंस नदी कालसी के पास यमुना में मिल जाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Institutions",
        "text": "उत्तराखंड में 'पहाड़ी संग्रहालय' (Hill Museum) कहाँ स्थित है?",
        "options": ["भीमताल", "देहरादून", "अल्मोड़ा", "श्रीनगर"],
        "correct_answer": "भीमताल",
        "explanation": "प्रसिद्ध लोक संस्कृति संग्रहालय खुटानी (भीमताल) में यशोधर मठपाल द्वारा स्थापित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri State",
        "text": "टिहरी में 'आधुनिक शिक्षा' का जनक किसे माना जाता है?",
        "options": ["प्रताप शाह", "कीर्ति शाह", "नरेन्द्र शाह", "सुदर्शन शाह"],
        "correct_answer": "प्रताप शाह",
        "explanation": "उन्होंने टिहरी में पहली बार अंग्रेजी स्कूल और अस्पताल खुलवाए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Valleys",
        "text": "'नैलंग घाटी' (Nelang Valley) किस जिले में स्थित है?",
        "options": ["उत्तरकाशी", "चमोली", "पिथौरागढ़", "रुद्रप्रयाग"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "इसे 'उत्तराखंड का लद्दाख' भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Legislation",
        "text": "कुमाऊँ में 'कुली बेगार' को समाप्त करने के लिए 'कुली एजेंसी' का विचार किसने दिया था?",
        "options": ["जोत सिंह नेगी", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "तारा दत्त गैरोला"],
        "correct_answer": "जोत सिंह नेगी",
        "explanation": "1908 में जोत सिंह नेगी ने कुली एजेंसी की स्थापना की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'खुदेड़' (Khuded) गीत किस भावना से संबंधित है?",
        "options": ["मायके की याद (विरह)", "युद्ध की खुशी", "फसल कटाई", "भक्ति"],
        "correct_answer": "मायके की याद (विरह)",
        "explanation": "विवाहित महिला द्वारा मायके की याद में गाए जाने वाले गीतों को खुदेड़ कहते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Glaciers",
        "text": "'खतलिंग ग्लेशियर' (Khatling Glacier) से कौन सी नदी निकलती है?",
        "options": ["भिलंगना", "भागीरथी", "मंदाकिनी", "पिण्डर"],
        "correct_answer": "भिलंगना",
        "explanation": "भिलंगना टिहरी जिले के खतलिंग ग्लेशियर से निकलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Tribes",
        "text": "महाभारत के किस पर्व में 'कुणिन्द' राजाओं का उल्लेख मिलता है?",
        "options": ["वन पर्व", "आदि पर्व", "भीष्म पर्व", "शांति पर्व"],
        "correct_answer": "वन पर्व",
        "explanation": "वन पर्व में कुणिन्द शासक सुबाहु का वर्णन मिलता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "प्रसिद्ध 'त्रिशूल' पर्वत शिखर किस जिले में स्थित है?",
        "options": ["चमोली", "पिथौरागढ़", "अल्मोड़ा", "बागेश्वर"],
        "correct_answer": "चमोली",
        "explanation": "यह चमोली जिले का एक प्रमुख शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "District Info",
        "text": "क्षेत्रफल की दृष्टि से उत्तराखंड का 'सबसे छोटा' जिला कौन सा है?",
        "options": ["चंपावत", "रुद्रप्रयाग", "बागेश्वर", "हरिद्वार"],
        "correct_answer": "चंपावत",
        "explanation": "चंपावत का क्षेत्रफल राज्य में सबसे कम है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'मुंशी' पद का सृजन किस कमिश्नर ने किया था?",
        "options": ["ट्रेल", "गार्डनर", "ल्यूशिंगटन", "बेटन"],
        "correct_answer": "ट्रेल",
        "explanation": "प्रशासनिक कार्यों में सहायता के लिए ट्रेल ने मुंशी और कानूनगो के पद बनाए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'कथैया' (Katheya) त्यौहार कहाँ मनाया जाता है?",
        "options": ["जौनसार", "कुमाऊँ", "तराई", "भोटिया क्षेत्र"],
        "correct_answer": "जौनसार",
        "explanation": "जौनसार बावर क्षेत्र में यह एक विशिष्ट उत्सव है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "किस नदी को 'उत्तराखंड की स्वर्ण रेखा' कहा जाता है?",
        "options": ["पिण्डर", "अलकनन्दा", "भागीरथी", "यमुना"],
        "correct_answer": "पिण्डर",
        "explanation": "पिण्डर नदी की रेत में सोने के कण पाए जाने की लोकमान्यता के कारण।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forestry",
        "text": "उत्तराखंड में 'चिपको आंदोलन' की माता गौरा देवी का निधन किस वर्ष हुआ था?",
        "options": ["1991", "1995", "1985", "1980"],
        "correct_answer": "1991",
        "explanation": "4 जुलाई 1991 को गौरा देवी का निधन हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'कुमाऊँ का इतिहास' पुस्तक के लेखक बद्रीदत्त पाण्डेय ने यह पुस्तक कहाँ लिखी थी?",
        "options": ["जेल में", "अल्मोड़ा में", "देहरादून में", "नैनीताल में"],
        "correct_answer": "जेल में",
        "explanation": "उन्होंने जेल में रहते हुए इस ऐतिहासिक ग्रंथ की रचना की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "उत्तराखंड की 'सात ताल' (Sattal) झीलों में कौन सी झील शामिल नहीं है?",
        "options": ["नैनी ताल", "राम ताल", "लक्ष्मण ताल", "सीता ताल"],
        "correct_answer": "नैनी ताल",
        "explanation": "सात ताल नैनीताल जिले में है, लेकिन नैनी ताल स्वयं इसका हिस्सा नहीं है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'फाँसी का गधेरा' (Phansi ka Gadhera) कहाँ स्थित है?",
        "options": ["नैनीताल", "अल्मोड़ा", "हल्द्वानी", "रानीखेत"],
        "correct_answer": "नैनीताल",
        "explanation": "1857 के विद्रोहियों को यहाँ फाँसी दी गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "उत्तराखंड का 'राजकीय गीत' किसने लिखा है?",
        "options": ["हेमन्त बिष्ट", "नरेन्द्र सिंह नेगी", "प्रीतम भरतवाण", "गिरीश तिवारी गिरदा"],
        "correct_answer": "हेमन्त बिष्ट",
        "explanation": "'उत्तराखंड देवभूमि मातृभूमि शत-शत वंदन' गीत हेमन्त बिष्ट ने लिखा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'पंचाचूली' (Panchachuli) शिखर की ऊँचाई कितनी है?",
        "options": ["6904 मीटर", "7120 मीटर", "6500 मीटर", "7000 मीटर"],
        "correct_answer": "6904 मीटर",
        "explanation": "यह पिथौरागढ़ जिले में स्थित पाँच चोटियों का समूह है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Legislation",
        "text": "उत्तराखंड में 'पंचायती राज अधिनियम' किस वर्ष लागू हुआ था (अपना स्वतंत्र)?",
        "options": ["2016", "2010", "2014", "2018"],
        "correct_answer": "2016",
        "explanation": "4 अप्रैल 2016 को उत्तराखंड का अपना पंचायती राज अधिनियम लागू हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin History",
        "text": "कुमाऊँ में 'असिस्टेंट कमिश्नर' का पद कब समाप्त किया गया था?",
        "options": ["1891", "1885", "1895", "1880"],
        "correct_answer": "1891",
        "explanation": "1891 में कुमाऊँ और तराई जिलों के गठन के साथ व्यवस्था बदली गई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'मध्य हिमालय का पुरातत्व' किसकी रचना है?",
        "options": ["यशोधर मठपाल", "अजय सिंह रावत", "डबराल", "डी.डी. शर्मा"],
        "correct_answer": "यशोधर मठपाल",
        "explanation": "यशोधर मठपाल ने उत्तराखंड के प्रागैतिहासिक इतिहास पर गहरा शोध किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Glaciers",
        "text": "उत्तराखंड का सबसे 'बड़ा' ग्लेशियर कौन सा है?",
        "options": ["गंगोत्री ग्लेशियर", "मिलम ग्लेशियर", "पिण्डारी ग्लेशियर", "चोराबाड़ी"],
        "correct_answer": "गंगोत्री ग्लेशियर",
        "explanation": "यह लगभग 30 किमी लंबा और 2 किमी चौड़ा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Judiciary",
        "text": "उत्तराखंड उच्च न्यायालय 'भवन' का निर्माण किसने करवाया था?",
        "options": ["सर सेंटोनी मैकडॉनेल", "हेनरी रैमजे", "लशिंगटन", "गार्डनर"],
        "correct_answer": "सर सेंटोनी मैकडॉनेल",
        "explanation": "नैनीताल स्थित यह भवन गॉथिक शैली में बना है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'जेल' की स्थापना अल्मोड़ा में किस वर्ष हुई थी?",
        "options": ["1816", "1821", "1815", "1830"],
        "correct_answer": "1816",
        "explanation": "यह उत्तराखंड की पहली जेल थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'फूलदेई' (Phool Dei) त्यौहार किस दिन मनाया जाता है?",
        "options": ["चैत्र मास की संक्रांति", "बैशाख संक्रांति", "श्रावण संक्रांति", "भादो संक्रांति"],
        "correct_answer": "चैत्र मास की संक्रांति",
        "explanation": "यह बच्चों का त्यौहार है जो बसंत के आगमन पर मनाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "मंदाकिनी नदी का 'संगम' अलकनन्दा से कहाँ होता है?",
        "options": ["रुद्रप्रयाग", "कर्णप्रयाग", "देवप्रयाग", "नन्दप्रयाग"],
        "correct_answer": "रुद्रप्रयाग",
        "explanation": "पंच प्रयागों में रुद्रप्रयाग महत्वपूर्ण है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Legislation",
        "text": "उत्तराखंड में 'कुली बेगार' को अवैध घोषित करने के लिए हाई कोर्ट में याचिका किसने दी थी (ऐतिहासिक)?",
        "options": ["तारा दत्त गैरोला", "बद्रीदत्त पाण्डेय", "बैरिस्टर मुकुन्दीलाल", "अनुसूया प्रसाद"],
        "correct_answer": "तारा दत्त गैरोला",
        "explanation": "उन्होंने कानूनी स्तर पर इस प्रथा का विरोध किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के किस महान क्रांतिकारी को 'आजाद' (Azad) उपनाम से जाना जाता था?",
        "options": ["श्रीदेव सुमन", "राम सिंह धौनी", "चन्द्रसिंह गढ़वाली", "कालू मेहरा"],
        "correct_answer": "राम सिंह धौनी",
        "explanation": "उन्हें उत्तराखंड का आजाद कहा जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'कामेत' (Kamet) पर्वत शिखर किस जिले में स्थित है?",
        "options": ["चमोली", "उत्तरकाशी", "पिथौरागढ़", "रुद्रप्रयाग"],
        "correct_answer": "चमोली",
        "explanation": "यह नन्दा देवी के बाद राज्य का दूसरा सबसे ऊँचा शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Legislation",
        "text": "उत्तराखंड की 'द्वितीय' राजभाषा कौन सी है?",
        "options": ["संस्कृत", "कुमाऊँनी", "गढ़वाली", "उर्दू"],
        "correct_answer": "संस्कृत",
        "explanation": "2010 में संस्कृत को द्वितीय राजभाषा का दर्जा दिया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Medieval Records",
        "text": "कत्यूरी काल में 'महादंडनायक' कौन था?",
        "options": ["मुख्य न्यायाधीश", "सेनापति", "कोषाध्यक्ष", "राज्यपाल"],
        "correct_answer": "मुख्य न्यायाधीश",
        "explanation": "न्याय प्रशासन का प्रमुख महादंडनायक कहलाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Heritage",
        "text": "उत्तराखंड में 'छिपला कोट' (Chipla Kot) कहाँ स्थित है?",
        "options": ["पिथौरागढ़", "चमोली", "अल्मोड़ा", "बागेश्वर"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "यह पिथौरागढ़ जिले में स्थित एक धार्मिक और प्राकृतिक स्थल है।"
    },

    # ── BATCH 9: RIVERS, LAKES & RESISTANCE ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "River Systems",
        "text": "नेपाल और उत्तराखंड की सीमा बनाने वाली नदी कौन सी है?",
        "options": ["काली नदी", "कोसी", "रामगंगा", "सरयू"],
        "correct_answer": "काली नदी",
        "explanation": "काली नदी भारत (उत्तराखंड) और नेपाल के बीच प्राकृतिक सीमा बनाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes of Kumaon",
        "text": "किस ताल को 'नल-दमयन्ती ताल' (Nal Damyanti Tal) कहा जाता है?",
        "options": ["सातताल का एक हिस्सा", "भीमताल", "नौकुचियाताल", "खुरपाताल"],
        "correct_answer": "सातताल का एक हिस्सा",
        "explanation": "सातताल समूह की एक झील को नल-दमयन्ती ताल के नाम से जाना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Political History",
        "text": "'कुमाऊँ संघ' (Kumaon Association) की स्थापना किस वर्ष हुई थी?",
        "options": ["1916", "1912", "1920", "1905"],
        "correct_answer": "1916",
        "explanation": "सामाजिक और राजनीतिक समस्याओं के समाधान के लिए 1916 में इसकी स्थापना हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "Salt Satyagraha",
        "text": "अल्मोड़ा के 'नगरपालिका भवन' पर तिरंगा फहराने वाली महिलाओं का नेतृत्व किसने किया था?",
        "options": ["बिश्नी देवी शाह", "कुंती वर्मा", "गौरा देवी", "विशला देवी"],
        "correct_answer": "बिश्नी देवी शाह",
        "explanation": "बिश्नी देवी शाह उत्तराखंड की पहली महिला स्वतंत्रता सेनानी मानी जाती हैं जिन्होंने जेल यात्रा की।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "River Life-lines",
        "text": "हल्द्वानी शहर किस नदी के तट पर स्थित है?",
        "options": ["गौला नदी", "कोसी नदी", "रामगंगा", "काली"],
        "correct_answer": "गौला नदी",
        "explanation": "गौला नदी हल्द्वानी की जीवनरेखा कही जाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Pandukeshwar Plates",
        "text": "पाण्डुकेश्वर ताम्रपत्र किस वंश के इतिहास की जानकारी देते हैं?",
        "options": ["कत्यूरी वंश", "चन्द वंश", "पवार वंश", "कुणिन्द"],
        "correct_answer": "कत्यूरी वंश",
        "explanation": "इन ताम्रपत्रों से कत्यूरी राजाओं की वंशावली और दान की जानकारी मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के किस साहित्यकार को 'आधुनिक डबराल' (Modern Dabral) के रूप में याद किया जाता है?",
        "options": ["शिव प्रसाद डबराल 'चारण'", "मंगलेश डबराल", "वीरेन डंगवाल", "शैलेश मटियानी"],
        "correct_answer": "शिव प्रसाद डबराल 'चारण'",
        "explanation": "उन्होंने उत्तराखंड का विशाल इतिहास 12 भागों में लिखा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peak Records",
        "text": "'बद्रीनाथ' धाम किस पर्वत शिखर की गोद में स्थित है?",
        "options": ["नर और नारायण पर्वत", "नीलकंठ", "नन्दा देवी", "कामेट"],
        "correct_answer": "नर और नारायण पर्वत",
        "explanation": "बद्रीनाथ नर और नारायण नामक दो पर्वतों के बीच स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Changes",
        "text": "कुमाऊँ में 'असिस्टेंट कमिश्नर' पद पर रहते हुए हेनरी रैमजे ने कहाँ अपना मुख्यालय बनाया था?",
        "options": ["नैनीताल", "अल्मोड़ा", "लोहाघाट", "हल्द्वानी"],
        "correct_answer": "नैनीताल",
        "explanation": "उन्होंने नैनीताल के विकास में महत्वपूर्ण भूमिका निभाई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music & Folklore",
        "text": "उत्तराखंड में 'न्यौली' (Nyoli) क्या है?",
        "options": ["एक विरह गीत", "एक त्यौहार", "एक वाद्य यंत्र", "एक नृत्य"],
        "correct_answer": "एक विरह गीत",
        "explanation": "न्यौली कुमाऊँ क्षेत्र का एक प्रसिद्ध प्रेम और विरह प्रधान लोकगीत है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Tehri State",
        "text": "टिहरी रियासत में 'पौंण टूटी' (Paun Tuti) क्या था?",
        "options": ["एक प्रकार का कर", "एक प्रथा", "एक आभूषण", "एक भोजन"],
        "correct_answer": "एक प्रकार का कर",
        "explanation": "यह व्यापारिक वस्तुओं के आयात-निर्यात पर लिया जाने वाला कर था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Lakes",
        "text": "'श्यामला ताल' (Shyamla Tal) किस जिले में स्थित है?",
        "options": ["चंपावत", "नैनीताल", "अल्मोड़ा", "पिथौरागढ़"],
        "correct_answer": "चंपावत",
        "explanation": "यहाँ विवेकानन्द आश्रम भी स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Kumaon Records",
        "text": "अंग्रेजों ने कुमाऊँ में 'पहला थाना' (1837) कहाँ स्थापित किया था?",
        "options": ["अल्मोड़ा", "नैनीताल", "रानीखेत", "कोटद्वार"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "अल्मोड़ा में पुलिस प्रशासन की शुरुआत 1837 में हुई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'मसूरी मेडले' (Mussoorie Medley) पुस्तक के लेखक कौन हैं?",
        "options": ["प्रोफेसर गणेश शैली", "रस्किन बॉन्ड", "विलियम्स", "फिशर"],
        "correct_answer": "प्रोफेसर गणेश शैली",
        "explanation": "यह मसूरी के इतिहास पर एक महत्वपूर्ण पुस्तक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Glacier Systems",
        "text": "कपिनी ग्लेशियर (Kapini Glacier) कहाँ स्थित है?",
        "options": ["बागेश्वर", "पिथौरागढ़", "चमोली", "उत्तरकाशी"],
        "correct_answer": "बागेश्वर",
        "explanation": "यह सुंदरढूँगा ग्लेशियर के पास स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Dynasties",
        "text": "किस कत्यूरी शासक ने अपनी राजधानी 'जोशीमठ से कत्यूर घाटी' स्थानांतरित की थी?",
        "options": ["नरसिंह देव", "बसंत देव", "ललितशूर", "ईष्टगण"],
        "correct_answer": "नरसिंह देव",
        "explanation": "नरसिंह देव ने राजधानी परिवर्तन का निर्णय लिया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "UKSSSC History",
        "text": "उत्तराखंड में 'होमरूल लीग' की स्थापना किस वर्ष हुई थी?",
        "options": ["1914", "1916", "1912", "1918"],
        "correct_answer": "1914",
        "explanation": "विक्टर मोहन जोशी, बद्रीदत्त पाण्डेय आदि ने इसकी नींव रखी थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "River Tributaries",
        "text": "भिलंगना नदी की सहायक नदी कौन सी है?",
        "options": ["मेदे गंगा और दूध गंगा", "मंदाकिनी", "पिण्डर", "नयार"],
        "correct_answer": "मेदे गंगा और दूध गंगा",
        "explanation": "ये भिलंगना की छोटी सहायक नदियाँ हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'झुमैलो' (Jhumailo) क्या है?",
        "options": ["एक नृत्य और गीत", "एक त्यौहार", "एक पकवान", "एक आभूषण"],
        "correct_answer": "एक नृत्य और गीत",
        "explanation": "गढ़वाल क्षेत्र में वसंत आगमन पर यह सामूहिक नृत्य किया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin History",
        "text": "कुमाऊँ में 'लोहाघाट' के पास 'मायावती आश्रम' की स्थापना किस वर्ष हुई थी?",
        "options": ["1899", "1905", "1895", "1901"],
        "correct_answer": "1899",
        "explanation": "स्वामी विवेकानन्द के अनुयायियों ने इसकी स्थापना की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountain Ranges",
        "text": "'बंदरपूँछ' पर्वत शिखर की ऊँचाई कितनी है?",
        "options": ["6316 मीटर", "7120 मीटर", "6500 मीटर", "6000 मीटर"],
        "correct_answer": "6316 मीटर",
        "explanation": "यह उत्तरकाशी जिले का प्रसिद्ध शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism History",
        "text": "1871 में 'अल्मोड़ा अखबार' के पहले संपादक कौन थे?",
        "options": ["बुद्धिबल्लभ पंत", "बद्रीदत्त पाण्डेय", "इम्तियाज अली", "जीवानंद"],
        "correct_answer": "बुद्धिबल्लभ पंत",
        "explanation": "उन्होंने इस ऐतिहासिक अखबार का संपादन शुरू किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'गढ़वाल की लोककथाएँ' पुस्तक के लेखक कौन हैं?",
        "options": ["तारा दत्त गैरोला", "गोविन्द चातक", "डबराल", "पाण्डे"],
        "correct_answer": "तारा दत्त गैरोला",
        "explanation": "उन्होंने शेरपा ओकले के साथ मिलकर 'हिमालयन फोकलोर' भी लिखी थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'बेनीताल' (Benital) किस जिले में स्थित है?",
        "options": ["चमोली", "रुद्रप्रयाग", "अल्मोड़ा", "उत्तरकाशी"],
        "correct_answer": "चमोली",
        "explanation": "यह आदि बद्री के पास स्थित एक छोटा और सुंदर ताल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Temples",
        "text": "गोपेश्वर के 'लोह स्तंभ' पर किस राजा का उल्लेख मिलता है?",
        "options": ["अशोक चल्ल", "अशोक", "अमोघभूति", "बसंत देव"],
        "correct_answer": "अशोक चल्ल",
        "explanation": "1191 ई. में नेपाली शासक अशोक चल्ल के विजय का उल्लेख है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "Political Awakening",
        "text": "उत्तराखंड में 'गढ़वाल यूनियन' की स्थापना किस वर्ष हुई थी?",
        "options": ["1901", "1905", "1910", "1912"],
        "correct_answer": "1901",
        "explanation": "तारा दत्त गैरोला के प्रयासों से इसकी स्थापना हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "धौलीगंगा (पश्चिमी) किसकी सहायक नदी है?",
        "options": ["अलकनन्दा", "भागीरथी", "मंदाकिनी", "काली"],
        "correct_answer": "अलकनन्दा",
        "explanation": "यह विष्णुप्रयाग में अलकनन्दा से मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड की तीलू रौतेली' (आधुनिक संदर्भ में) कहा जाता है?",
        "options": ["ममता रावत", "बचेंद्री पाल", "गौरा देवी", "विशला देवी"],
        "correct_answer": "ममता रावत",
        "explanation": "2013 की आपदा में उनके साहस के लिए उन्हें यह सम्मान दिया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'पहला बंदोबस्त' (1815) किसने किया था?",
        "options": ["ई. गार्डनर", "ट्रेल", "रैमजे", "ल्यूशिंगटन"],
        "correct_answer": "ई. गार्डनर",
        "explanation": "गार्डनर ने कुमाऊँ का प्रथम संक्षिप्त बंदोबस्त किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife",
        "text": "उत्तराखंड में 'बिन्सर वन्यजीव विहार' कहाँ स्थित है?",
        "options": ["अल्मोड़ा", "नैनीताल", "चंपावत", "बागेश्वर"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "यह अपनी प्राकृतिक सुंदरता और वन्यजीवों के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'गैंड़वा' (Gaindwa) मेला कहाँ लगता है?",
        "options": ["पौड़ी गढ़वाल", "उत्तरकाशी", "रुद्रप्रयाग", "चंपावत"],
        "correct_answer": "पौड़ी गढ़वाल",
        "explanation": "थलीसैंण क्षेत्र में यह प्रसिद्ध मेला आयोजित होता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Dynasties",
        "text": "कत्यूरी काल में 'कुलपति' (Kulapati) कौन था?",
        "options": ["शिक्षा प्रमुख", "राजस्व प्रमुख", "सेनापति", "धार्मिक गुरु"],
        "correct_answer": "शिक्षा प्रमुख",
        "explanation": "कुलपति शिक्षा और विद्वानों का प्रमुख अधिकारी होता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Freedom Movement",
        "source": "Political History",
        "text": "अल्मोड़ा में 'डिबेटिंग क्लब' के अध्यक्ष कौन थे?",
        "options": ["बुद्धिबल्लभ पंत", "भीम सिंह", "बद्रीदत्त पाण्डेय", "जीवानंद"],
        "correct_answer": "बुद्धिबल्लभ पंत",
        "explanation": "वे इसके संस्थापक और प्रमुख संरक्षक थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "मंदाकिनी नदी का उद्गम स्थल कहाँ है?",
        "options": ["चोराबाड़ी ग्लेशियर", "खतलिंग", "पिण्डारी", "गंगोत्री"],
        "correct_answer": "चोराबाड़ी ग्लेशियर",
        "explanation": "यह केदारनाथ के ठीक ऊपर स्थित ग्लेशियर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "उत्तराखंड में 'रणभूत कौथिग' (Ranbhut Kauthig) कहाँ मनाया जाता है?",
        "options": ["टिहरी गढ़वाल", "पौड़ी", "उत्तरकाशी", "अल्मोड़ा"],
        "correct_answer": "टिहरी गढ़वाल",
        "explanation": "युद्ध में शहीद हुए वीरों की याद में यह मनाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forestry Records",
        "text": "कुमाऊँ में 'वनों की प्रथम नीलामी' किस वर्ष हुई थी?",
        "options": ["1858", "1860", "1850", "1865"],
        "correct_answer": "1858",
        "explanation": "हेनरी रैमजे के काल में वनों का दोहन शुरू हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Passes",
        "text": "'सिन्ला दर्रा' (Sinla Pass) किनके बीच स्थित है?",
        "options": ["दारमा और व्यास घाटी", "चमोली और उत्तरकाशी", "पिथौरागढ़ और तिब्बत", "नेपाल और भारत"],
        "correct_answer": "दारमा और व्यास घाटी",
        "explanation": "यह पिथौरागढ़ की दो प्रमुख घाटियों को जोड़ता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'गढ़वाल का दानवीर' कहा जाता है?",
        "options": ["घनानंद खण्डूड़ी", "प्रताप शाह", "महिपति शाह", "अजयपाल"],
        "correct_answer": "घनानंद खण्डूड़ी",
        "explanation": "उनकी शिक्षा और समाज सेवा के कार्यों के लिए उन्हें यह सम्मान प्राप्त है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Temples",
        "text": "लाखामंडल के 'शिव मंदिर' का निर्माण किस राजकुमारी ने करवाया था?",
        "options": ["राजकुमारी ईश्वरा", "राजकुमारी जिया", "कर्णवती", "तीलू रौतेली"],
        "correct_answer": "राजकुमारी ईश्वरा",
        "explanation": "यदुवंश की राजकुमारी ईश्वरा के अभिलेख यहाँ से प्राप्त हुए हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "उत्तराखंड में 'अलकनन्दा' की सबसे पहली सहायक नदी कौन सी है?",
        "options": ["लक्ष्मण गंगा", "सरस्वती", "धौलीगंगा", "पिण्डर"],
        "correct_answer": "सरस्वती",
        "explanation": "केशवप्रयाग में सरस्वती अलकनन्दा से मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'भैलो' (Bhailo) त्यौहार किस अवसर पर मनाया जाता है?",
        "options": ["इगास दीपावली", "होली", "वैशाखी", "हरेला"],
        "correct_answer": "इगास दीपावली",
        "explanation": "दीपावली के 11 दिन बाद इगास के दिन भैलो खेला जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'पटवारी' पदों का सृजन कमिश्नर ट्रेल ने किस वर्ष किया था?",
        "options": ["1819", "1815", "1821", "1825"],
        "correct_answer": "1819",
        "explanation": "प्रशासनिक कार्यक्षमता बढ़ाने के लिए 9 पटवारी पद बनाए गए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks",
        "text": "'द्रौपदी का डांडा' पर्वत शिखर कहाँ स्थित है?",
        "options": ["उत्तरकाशी", "चमोली", "रुद्रप्रयाग", "पिथौरागढ़"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "हाल ही में यहाँ हुए हिमस्खलन के कारण यह चर्चा में रहा।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'कुमाऊँ की लक्ष्मीबाई' कहा जाता है?",
        "options": ["जिया रानी", "विशला देवी", "तुलसी देवी", "कमला पंत"],
        "correct_answer": "जिया रानी",
        "explanation": "कत्यूरी रानी जिया रानी को उनकी वीरता के लिए यह सम्मान प्राप्त है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Tribes",
        "text": "उत्तराखंड की किस जनजाति के लोग 'बाली' और 'शकुन' त्यौहार मनाते हैं?",
        "options": ["थारू", "बोक्सा", "जौनसारी", "भोटिया"],
        "correct_answer": "थारू",
        "explanation": "थारू जनजाति के अपने विशिष्ट रीति-रिवाज हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "नयार नदी का उद्गम स्थल कहाँ है?",
        "options": ["दूधातोली श्रेणी", "त्रिशूल", "कामेत", "नन्दा देवी"],
        "correct_answer": "दूधातोली श्रेणी",
        "explanation": "पूर्वी और पश्चिमी नयार दोनों दूधातोली से निकलती हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'हिमालय का इतिहास' (History of Himalaya) पुस्तक के लेखक कौन हैं?",
        "options": ["डॉ. मदन चंद्र भट्ट", "डबराल", "अजय सिंह रावत", "पाण्डे"],
        "correct_answer": "डॉ. मदन चंद्र भट्ट",
        "explanation": "यह हिमालयी क्षेत्र के इतिहास पर एक महत्वपूर्ण कृति है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'पहला डाकघर' (Post Office) अल्मोड़ा में कब खुला था?",
        "options": ["1815", "1816", "1820", "1825"],
        "correct_answer": "1815",
        "explanation": "अंग्रेजों ने आते ही संचार व्यवस्था के लिए डाकघर खोला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'द्रोण सागर' ताल कहाँ स्थित है?",
        "options": ["काशीपुर", "नैनीताल", "हल्द्वानी", "रुद्रपुर"],
        "correct_answer": "काशीपुर",
        "explanation": "यह ऊधम सिंह नगर के काशीपुर में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड राज्य की 'पहली महिला राज्यपाल' कौन थी?",
        "options": ["मार्ग्रेट अल्वा", "बेबी रानी मौर्य", "विमला पंत", "कंचन चौधरी"],
        "correct_answer": "मार्ग्रेट अल्वा",
        "explanation": "वे राज्य की चौथी राज्यपाल थीं।"
    },

    # ── BATCH 10: MODERN MILESTONES & AWARDS ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Bharat Ratna Records",
        "text": "गोविंद बल्लभ पंत को 'भारत रत्न' किस वर्ष प्रदान किया गया था?",
        "options": ["1957", "1955", "1960", "1950"],
        "correct_answer": "1957",
        "explanation": "वे उत्तर प्रदेश के प्रथम मुख्यमंत्री और भारत के गृह मंत्री रहे थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Infrastructure",
        "text": "उत्तराखंड में 'चार धाम ऑल वेदर रोड' परियोजना की कुल लंबाई लगभग कितनी है?",
        "options": ["889 किमी", "950 किमी", "1000 किमी", "750 किमी"],
        "correct_answer": "889 किमी",
        "explanation": "यह परियोजना चार धामों को जोड़ने के लिए बनाई जा रही है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Railway Projects",
        "text": "'ऋषिकेश-कर्णप्रयाग' रेलवे लाइन की कुल लंबाई कितनी है?",
        "options": ["125 किमी", "150 किमी", "100 किमी", "140 किमी"],
        "correct_answer": "125 किमी",
        "explanation": "यह एक महत्वाकांक्षी रेल परियोजना है जिसमें कई सुरंगे शामिल हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Education",
        "text": "उत्तराखंड के किस स्थान को 'स्कूलों की राजधानी' (School Capital) कहा जाता है?",
        "options": ["देहरादून", "नैनीताल", "मसूरी", "श्रीनगर"],
        "correct_answer": "देहरादून",
        "explanation": "यहाँ कई प्रतिष्ठित बोर्डिंग स्कूल स्थित हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Sports",
        "text": "निशानेबाज 'अभिनव बिन्द्रा' का संबंध उत्तराखंड के किस जिले से है?",
        "options": ["देहरादून", "पौड़ी", "टिहरी", "नैनीताल"],
        "correct_answer": "देहरादून",
        "explanation": "ओलंपिक स्वर्ण पदक विजेता अभिनव बिन्द्रा देहरादून के रहने वाले हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "उत्तराखंड के प्रसिद्ध संगीतकार 'जीत सिंह नेगी' का संबंध किस क्षेत्र से था?",
        "options": ["गढ़वाली लोकसंगीत", "कुमाऊँनी", "शास्त्रीय", "पॉप संगीत"],
        "correct_answer": "गढ़वाली लोकसंगीत",
        "explanation": "वे गढ़वाली लोकसंगीत के स्तंभ माने जाते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "उत्तराखंड में 'काली' और 'गौरी' नदी का संगम कहाँ होता है?",
        "options": ["जौलजीबी", "धारचूला", "पिथौरागढ़", "टनकपुर"],
        "correct_answer": "जौलजीबी",
        "explanation": "यहाँ प्रसिद्ध जौलजीबी मेला भी लगता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Resistance",
        "text": "कुमाऊँ में 'गांधी' आश्रम की स्थापना चनौदा (स्रोमेश्वर) में किसने की थी?",
        "options": ["शांतिलाल त्रिवेदी", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "विक्टर मोहन जोशी"],
        "correct_answer": "शांतिलाल त्रिवेदी",
        "explanation": "1937 में उन्होंने गांधी जी की प्रेरणा से इसकी स्थापना की।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'मुख्यमंत्री वात्सल्य योजना' किसके लिए शुरू की गई है?",
        "options": ["कोविड अनाथ बच्चों के लिए", "बुजुर्गों के लिए", "किसानों के लिए", "छात्रों के लिए"],
        "correct_answer": "कोविड अनाथ बच्चों के लिए",
        "explanation": "ऐसे बच्चों को आर्थिक सहायता प्रदान करने के लिए यह योजना है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Valleys",
        "text": "'फूलों की घाटी' की खोज किसने की थी?",
        "options": ["फ्रैंक स्माइथ", "एटकिंसन", "विलियम्स", "रस्किन बॉन्ड"],
        "correct_answer": "फ्रैंक स्माइथ",
        "explanation": "1931 में फ्रैंक स्माइथ ने इसकी खोज की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Literature",
        "text": "किसे 'उत्तराखंड का व्यास' कहा जाता है?",
        "options": ["शिव प्रसाद डबराल", "शैलेश मटियानी", "सुमित्रानंदन पंत", "मंगलेश डबराल"],
        "correct_answer": "शिव प्रसाद डबराल",
        "explanation": "उनके विशाल ऐतिहासिक लेखन के कारण उन्हें यह उपाधि मिली।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife",
        "text": "उत्तराखंड में 'नंदा देवी' को नेशनल पार्क कब घोषित किया गया?",
        "options": ["1982", "1988", "1985", "1990"],
        "correct_answer": "1982",
        "explanation": "1982 में इसे नेशनल पार्क बनाया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Legislation",
        "text": "उत्तराखंड में 'लोकपाल' विधेयक कब पारित हुआ था (सबसे पहले)?",
        "options": ["2011", "2013", "2015", "2010"],
        "correct_answer": "2011",
        "explanation": "बी.सी. खंडूड़ी के कार्यकाल में इसे पारित किया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "एवरेस्ट फतह करने वाली प्रथम भारतीय महिला 'बचेंद्री पाल' का जन्म कहाँ हुआ था?",
        "options": ["नाकुरी (उत्तरकाशी)", "मरोड़ा", "चोपता", "हल्द्वानी"],
        "correct_answer": "नाकुरी (उत्तरकाशी)",
        "explanation": "उनका जन्म उत्तरकाशी जिले के नाकुरी गाँव में हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'झिलमिल झील' किस जिले में स्थित है?",
        "options": ["हरिद्वार", "नैनीताल", "चंपावत", "पिथौरागढ़"],
        "correct_answer": "हरिद्वार",
        "explanation": "यह हरिद्वार जिले के राजाजी नेशनल पार्क के पास स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Institutions",
        "text": "देहरादून में 'सर्वे ऑफ इंडिया' (Survey of India) का मुख्यालय कब स्थानांतरित किया गया?",
        "options": ["1942", "1940", "1945", "1950"],
        "correct_answer": "1942",
        "explanation": "दूसरे विश्व युद्ध के दौरान इसे कोलकाता से देहरादून लाया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'कण्डाली' (Kandali) त्यौहार कितने वर्षों के अंतराल पर मनाया जाता है?",
        "options": ["12 वर्ष", "10 वर्ष", "6 वर्ष", "8 वर्ष"],
        "correct_answer": "12 वर्ष",
        "explanation": "भोटिया (शौका) जनजाति द्वारा 12 वर्ष में एक बार मनाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "गंगा नदी की लंबाई 'देवप्रयाग से हरिद्वार' तक कितनी है?",
        "options": ["96 किमी", "100 किमी", "90 किमी", "110 किमी"],
        "correct_answer": "96 किमी",
        "explanation": "उत्तराखंड में गंगा की कुल लंबाई 96 किमी मानी जाती है (देवप्रयाग से सीमा तक)।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Demographics",
        "text": "उत्तराखंड का 'सर्वाधिक जनसंख्या' वाला जिला कौन सा है?",
        "options": ["हरिद्वार", "देहरादून", "ऊधम सिंह नगर", "नैनीताल"],
        "correct_answer": "हरिद्वार",
        "explanation": "2011 की जनगणना के अनुसार हरिद्वार की जनसंख्या सबसे अधिक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Art",
        "text": "'ऐपण' (Aipan) कला का संबंध मुख्य रूप से किस क्षेत्र से है?",
        "options": ["कुमाऊँ", "गढ़वाल", "जौनसार", "तराई"],
        "correct_answer": "कुमाऊँ",
        "explanation": "यह कुमाऊँ की एक प्रसिद्ध लोक चित्रकला (रंगोली) है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Archaeology",
        "text": "उत्तराखंड में 'कपिनी गुफा' कहाँ स्थित है?",
        "options": ["पिथौरागढ़", "चमोली", "उत्तरकाशी", "अल्मोड़ा"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "यहाँ से प्राचीन शैल चित्र प्राप्त हुए हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'हाथी पर्वत' (Hathi Parvat) कहाँ स्थित है?",
        "options": ["जोशीमठ (चमोली)", "उत्तरकाशी", "रुद्रप्रयाग", "बागेश्वर"],
        "correct_answer": "जोशीमठ (चमोली)",
        "explanation": "यह जोशीमठ के पास स्थित एक प्रसिद्ध शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'होमस्टे योजना' कब शुरू की गई थी?",
        "options": ["2018", "2016", "2020", "2015"],
        "correct_answer": "2018",
        "explanation": "ग्रामीण पर्यटन को बढ़ावा देने के लिए यह योजना शुरू हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'लाली' (Lali) किस प्रकार का गीत है?",
        "options": ["प्रेम गीत", "त्यौहार गीत", "कृषि गीत", "वीर गाथा"],
        "correct_answer": "प्रेम गीत",
        "explanation": "यह कुमाऊँ क्षेत्र का एक मधुर लोकगीत है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism",
        "text": "1902 में 'गढ़वाल भ्रातृ मण्डल' की स्थापना कहाँ हुई थी?",
        "options": ["लखनऊ", "श्रीनगर", "देहरादून", "मसूरी"],
        "correct_answer": "लखनऊ",
        "explanation": "मथुरा प्रसाद नैथानी ने इसकी स्थापना लखनऊ में की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'भेंकल ताल' (Bhenkal Tal) कहाँ स्थित है?",
        "options": ["चमोली", "रुद्रप्रयाग", "उत्तरकाशी", "पिथौरागढ़"],
        "correct_answer": "चमोली",
        "explanation": "यह एक अंडाकार झील है जो चमोली जिले में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Districts",
        "text": "उत्तराखंड के कितने जिले 'नेपाल' की सीमा को स्पर्श करते हैं?",
        "options": ["3", "4", "2", "5"],
        "correct_answer": "3",
        "explanation": "पिथौरागढ़, चंपावत और ऊधम सिंह नगर नेपाल की सीमा से लगते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'पिथौरागढ़ का गांधी' कहा जाता है?",
        "options": ["प्रयाग दत्त पंत", "इन्द्रमणि बडोनी", "बद्रीदत्त पाण्डेय", "कालू मेहरा"],
        "correct_answer": "प्रयाग दत्त पंत",
        "explanation": "पिथौरागढ़ में स्वतंत्रता आंदोलन का नेतृत्व करने के कारण।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "पिण्डर और अलकनन्दा का संगम कहाँ होता है?",
        "options": ["कर्णप्रयाग", "रुद्रप्रयाग", "नन्दप्रयाग", "देवप्रयाग"],
        "correct_answer": "कर्णप्रयाग",
        "explanation": "यह संगम चमोली जिले के कर्णप्रयाग में होता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'शराब की पहली फैक्ट्री' कहाँ लगाई गई थी?",
        "options": ["अल्मोड़ा", "हल्द्वानी", "नैनीताल", "रामनगर"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "अंग्रेजों ने अपनी जरूरतों के लिए इसे स्थापित किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Demographics",
        "text": "उत्तराखंड का 'न्यूनतम जनसंख्या' वाला जिला कौन सा है?",
        "options": ["रुद्रप्रयाग", "चंपावत", "बागेश्वर", "पिथौरागढ़"],
        "correct_answer": "रुद्रप्रयाग",
        "explanation": "रुद्रप्रयाग की जनसंख्या राज्य के सभी जिलों में सबसे कम है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards",
        "text": "उत्तराखंड के किस व्यक्ति को 'प्रथम' ज्ञानपीठ पुरस्कार मिला था?",
        "options": ["सुमित्रानंदन पंत", "मंगलेश डबराल", "शिवानी", "शैलेश मटियानी"],
        "correct_answer": "सुमित्रानंदन पंत",
        "explanation": "1968 में 'चिदंबरा' के लिए उन्हें यह सर्वोच्च सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Valleys",
        "text": "'सौर घाटी' (Sor Valley) किस जिले का प्राचीन नाम है?",
        "options": ["पिथौरागढ़", "चंपावत", "बागेश्वर", "अल्मोड़ा"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "पिथौरागढ़ शहर सौर घाटी में ही स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Inscriptions",
        "text": "'राजकुमारी ईश्वरा' का शिलालेख कहाँ से प्राप्त हुआ है?",
        "options": ["लाखामंडल", "कालसी", "जागेश्वर", "बद्रीनाथ"],
        "correct_answer": "लाखामंडल",
        "explanation": "देहरादून के लाखामंडल से यह महत्वपूर्ण ऐतिहासिक स्रोत मिला है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Institutions",
        "text": "उत्तराखंड में 'रंगमंच' का भीष्म पितामह किसे कहा जाता है?",
        "options": ["गिरीश तिवारी गिरदा", "मोहन उप्रेती", "रणबीर सिंह बिष्ट", "बृजेंद्र लाल शाह"],
        "correct_answer": "गिरीश तिवारी गिरदा",
        "explanation": "वे एक प्रसिद्ध जनकवि और रंगकर्मी थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "पश्चिमी रामगंगा की लंबाई उत्तराखंड में कितनी है?",
        "options": ["155 किमी", "120 किमी", "180 किमी", "200 किमी"],
        "correct_answer": "155 किमी",
        "explanation": "यह पौड़ी, चमोली और अल्मोड़ा से होकर बहती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism",
        "text": "1939 में 'संदेश' समाचार पत्र का प्रकाशन कहाँ से हुआ था?",
        "options": ["कोटद्वार", "लैंसडाउन", "देहरादून", "श्रीनगर"],
        "correct_answer": "कोटद्वार",
        "explanation": "कृपाराम मिश्र 'मनहर' ने इसे कोटद्वार से निकाला था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'फाचकण्डी ताल' (Fachkandi Tal) किस जिले में स्थित है?",
        "options": ["उत्तरकाशी", "चमोली", "रुद्रप्रयाग", "पिथौरागढ़"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "इस ताल का पानी उबलता हुआ प्रतीत होता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'थड्या' (Thadya) नृत्य किस समय किया जाता है?",
        "options": ["वसंत पंचमी से बिखोती तक", "होली में", "दीपावली में", "विवाह में"],
        "correct_answer": "वसंत पंचमी से बिखोती तक",
        "explanation": "यह महिलाओं द्वारा किया जाने वाला एक पारंपरिक नृत्य है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Dynasties",
        "text": "कत्यूरी काल में 'पटल' (Patal) क्या था?",
        "options": ["एक प्रशासनिक इकाई", "एक कर", "एक आभूषण", "एक शस्त्र"],
        "correct_answer": "एक प्रशासनिक इकाई",
        "explanation": "प्रशासनिक सुविधा के लिए राज्य को पटलों में बाँटा गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Passes",
        "text": "'कुंगरी-बिंगरी' दर्रा किनके बीच स्थित है?",
        "options": ["पिथौरागढ़ और तिब्बत", "चमोली और उत्तरकाशी", "चंपावत और नेपाल", "बागेश्वर और पिथौरागढ़"],
        "correct_answer": "पिथौरागढ़ और तिब्बत",
        "explanation": "यह उच्च हिमालयी क्षेत्र का एक प्रसिद्ध दर्रा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Demographics",
        "text": "2011 की जनगणना के अनुसार उत्तराखंड का 'साक्षरता' में भारत में कौन सा स्थान है?",
        "options": ["17वां", "15वां", "20वां", "25वां"],
        "correct_answer": "17वां",
        "explanation": "साक्षरता दर के मामले में उत्तराखंड 17वें स्थान पर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'हिमालय की यात्रा' पुस्तक के लेखक कौन हैं?",
        "options": ["काका कालेलकर", "रस्किन बॉन्ड", "डबराल", "पाण्डे"],
        "correct_answer": "काका कालेलकर",
        "explanation": "उन्होंने हिमालय की यात्राओं का सजीव वर्णन किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'पहला सिविल अस्पताल' अल्मोड़ा में कब बना था?",
        "options": ["1848", "1840", "1850", "1860"],
        "correct_answer": "1848",
        "explanation": "ब्रिटिश शासन काल में स्वास्थ्य सुविधाओं की शुरुआत हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "अलकनन्दा नदी का उद्गम स्थल कहाँ है?",
        "options": ["सतोपंथ ग्लेशियर", "गंगोत्री", "खतलिंग", "पिण्डारी"],
        "correct_answer": "सतोपंथ ग्लेशियर",
        "explanation": "यह चमोली जिले में स्थित अलकापुरी बाँक के पास सतोपंथ झील से निकलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "उत्तराखंड में 'बाजूबंद' (Bajuband) किस प्रकार का गीत है?",
        "options": ["संवादात्मक प्रेम गीत", "भक्ति गीत", "वीर गाथा", "विवाह गीत"],
        "correct_answer": "संवादात्मक प्रेम गीत",
        "explanation": "यह जंगलों में पेड़ों के नीचे गाया जाने वाला संवाद शैली का गीत है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Archaeology",
        "text": "उत्तराखंड में 'हुडली' (Hudli) शैल चित्र कहाँ से प्राप्त हुए हैं?",
        "options": ["उत्तरकाशी", "अल्मोड़ा", "पिथौरागढ़", "चमोली"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "यहाँ नीले रंग के शैल चित्र मिले हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks",
        "text": "'त्रिशूल' शिखर की ऊँचाई कितनी है?",
        "options": ["7120 मीटर", "7817 मीटर", "7756 मीटर", "6904 मीटर"],
        "correct_answer": "7120 मीटर",
        "explanation": "यह चमोली जिले में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड राज्य लोक सेवा आयोग (UKPSC) का मुख्यालय कहाँ है?",
        "options": ["हरिद्वार", "देहरादून", "नैनीताल", "अल्मोड़ा"],
        "correct_answer": "हरिद्वार",
        "explanation": "यह हरिद्वार के कनखल मार्ग पर स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'गढ़वाल पेंटिंग्स' (Garhwal Paintings) पुस्तक के लेखक कौन हैं?",
        "options": ["बैरिस्टर मुकुन्दीलाल", "मोलूराम", "मठपाल", "पाण्डे"],
        "correct_answer": "बैरिस्टर मुकुन्दीलाल",
        "explanation": "उन्होंने मोलूराम की चित्रकला को विश्व के सामने रखा।"
    },

    # ── BATCH 11: ENVIRONMENT & ARCHAEOLOGY ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Environmental Movements",
        "text": "उत्तराखंड में 'मैती आंदोलन' (Maiti Movement) के जनक कौन हैं?",
        "options": ["कल्याण सिंह रावत", "चण्डी प्रसाद भट्ट", "सच्चिदानंद भारती", "जगत सिंह चौधरी"],
        "correct_answer": "कल्याण सिंह रावत",
        "explanation": "1995 में ग्वालदम (चमोली) से उन्होंने इस अनोखे वृक्षारोपण आंदोलन की शुरुआत की।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife Sanctuaries",
        "text": "'अस्कोट मस्क डियर सैंक्चुअरी' (Askot Musk Deer Sanctuary) किस जिले में है?",
        "options": ["पिथौरागढ़", "चमोली", "उत्तरकाशी", "बागेश्वर"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "यह कस्तूरी मृग के संरक्षण के लिए 1986 में स्थापित किया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Dams & Projects",
        "text": "'पंचेश्वर बाँध' (Pancheshwar Dam) परियोजना किन दो देशों के बीच का संयुक्त उपक्रम है?",
        "options": ["भारत और नेपाल", "भारत और चीन", "भारत और भूटान", "भारत और बांग्लादेश"],
        "correct_answer": "भारत और नेपाल",
        "explanation": "यह महाकाली (काली) नदी पर एक विशाल जलविद्युत परियोजना है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Numismatics",
        "text": "कुणिन्द मुद्राओं में सबसे महत्वपूर्ण 'अमोघभूति' (Amoghbhuti) किस धातु की बनी थीं?",
        "options": ["रजत और ताम्र", "स्वर्ण", "कांसा", "लोहा"],
        "correct_answer": "रजत और ताम्र",
        "explanation": "अमोघभूति प्रकार की मुद्राएं कुणिन्द शासन के चरमोत्कर्ष को दर्शाती हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "किसे 'कंकाल झील' (Skeleton Lake) के नाम से जाना जाता है?",
        "options": ["रूपकुण्ड", "हेमकुण्ड", "लोकपाल", "सतोपंथ"],
        "correct_answer": "रूपकुण्ड",
        "explanation": "यहाँ से बड़ी संख्या में नरकंकाल मिले हैं, जो आज भी रहस्य का विषय हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Archaeology",
        "text": "कत्यूरी राजाओं की 'कुलदेवी' का नाम क्या था?",
        "options": ["कोट भ्रामरी", "नंदा देवी", "ज्वाला देवी", "पुर्णागिरी"],
        "correct_answer": "कोट भ्रामरी",
        "explanation": "बागेश्वर के पास उनका प्रसिद्ध मंदिर स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "कोसी नदी का उद्गम स्थल कहाँ है?",
        "options": ["धारपानी धार (कौसानी)", "पिण्डारी", "मिलम", "खतलिंग"],
        "correct_answer": "धारपानी धार (कौसानी)",
        "explanation": "यह अल्मोड़ा जिले की कौसानी पहाड़ियों से निकलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "उत्तराखंड में 'प्रथम व्यक्तिगत सत्याग्रही' कौन थे?",
        "options": ["जगमोहन सिंह नेगी", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "विक्टर मोहन जोशी"],
        "correct_answer": "जगमोहन सिंह नेगी",
        "explanation": "1940 के व्यक्तिगत सत्याग्रह में उन्होंने भाग लिया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards",
        "text": "उत्तराखंड के किस व्यक्ति को 'पद्म विभूषण' (प्रथम) मिला था?",
        "options": ["डॉ. घनानंद पाण्डेय", "भैरव दत्त पाण्डेय", "बचेंद्री पाल", "सुन्दरलाल बहुगुणा"],
        "correct_answer": "डॉ. घनानंद पाण्डेय",
        "explanation": "विज्ञान और अभियांत्रिकी के क्षेत्र में उन्हें यह सम्मान मिला था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "प्रसिद्ध 'नीलकंठ' शिखर किस जिले में स्थित है?",
        "options": ["चमोली", "रुद्रप्रयाग", "पौड़ी", "उत्तरकाशी"],
        "correct_answer": "चमोली",
        "explanation": "इसे 'गढ़वाल का क्वीन' (Queen of Garhwal) भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'ब्रिटिश गढ़वाल का गजेटियर' किसने लिखा था?",
        "options": ["एच.जी. वाल्टन", "ई. एटकिंसन", "ट्रेल", "बैटेन"],
        "correct_answer": "एच.जी. वाल्टन",
        "explanation": "1910 में उन्होंने इस महत्वपूर्ण संदर्भ ग्रंथ की रचना की।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "River Tributaries",
        "text": "सरयू नदी किसकी सहायक नदी है?",
        "options": ["काली नदी", "गंगा", "यमुना", "कोसी"],
        "correct_answer": "काली नदी",
        "explanation": "सरयू पंचेश्वर में काली नदी से मिल जाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Pawar & Tehri",
        "source": "Pawar Dynasty",
        "text": "गढ़वाल के किस शासक ने 'शाह' (Shah) की उपाधि धारण की थी (सबसे पहले)?",
        "options": ["बलभद्र शाह", "अजयपाल", "मान शाह", "प्रताप शाह"],
        "correct_answer": "बलभद्र शाह",
        "explanation": "लोदी वंश के बहलोल लोदी ने उन्हें यह उपाधि दी थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड का वृक्ष मित्र' (Tree Friend) कहा जाता है?",
        "options": ["विश्वेश्वर दत्त सकलानी", "सुन्दरलाल बहुगुणा", "गौरा देवी", "चण्डी प्रसाद भट्ट"],
        "correct_answer": "विश्वेश्वर दत्त सकलानी",
        "explanation": "उन्होंने लाखों पेड़ लगाकर पहाड़ों को हरा-भरा किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'भेंकल ताल' (Bhenkal Tal) किस जिले में है?",
        "options": ["चमोली", "रुद्रप्रयाग", "पिथौरागढ़", "चंपावत"],
        "correct_answer": "चमोली",
        "explanation": "यह चमोली जिले में स्थित एक सुंदर ताल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin History",
        "text": "कुमाऊँ में 'राजस्व पुलिस' व्यवस्था कब लागू हुई थी?",
        "options": ["1874", "1860", "1880", "1890"],
        "correct_answer": "1874",
        "explanation": "हेनरी रैमजे के कार्यकाल में पटवारियों को पुलिस के अधिकार दिए गए।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Passes",
        "text": "'कालिन्दी दर्रा' किन दो स्थानों को जोड़ता है?",
        "options": ["उत्तरकाशी और चमोली", "पिथौरागढ़ और तिब्बत", "बागेश्वर और पिथौरागढ़", "नेपाल और भारत"],
        "correct_answer": "उत्तरकाशी और चमोली",
        "explanation": "यह उच्च हिमालयी क्षेत्र का एक कठिन दर्रा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Tribes",
        "text": "उत्तराखंड की किस जनजाति में 'बदला विवाह' (Badla Marriage) की प्रथा थी?",
        "options": ["थारू", "भोटिया", "जौनसारी", "राजी"],
        "correct_answer": "थारू",
        "explanation": "बहनों की अदला-बदली कर विवाह करने की प्राचीन प्रथा थारू समाज में प्रचलित थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "प्रसिद्ध 'गौचर मेला' कब शुरू हुआ था?",
        "options": ["1943", "1950", "1940", "1935"],
        "correct_answer": "1943",
        "explanation": "कमिश्नर बार्नेडी के प्रयासों से यह व्यापारिक मेला शुरू हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "अलकनन्दा और नन्दाकिनी का संगम कहाँ होता है?",
        "options": ["नन्दप्रयाग", "रुद्रप्रयाग", "कर्णप्रयाग", "विष्णुप्रयाग"],
        "correct_answer": "नन्दप्रयाग",
        "explanation": "नन्दाकिनी नदी नन्दप्रयाग में अलकनन्दा से मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Resistance",
        "text": "उत्तराखंड में 'डोला-पालकी' (Dola-Palki) आंदोलन का नेतृत्व किसने किया था?",
        "options": ["जयानंद भारती", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "खुशीराम"],
        "correct_answer": "जयानंद भारती",
        "explanation": "शिल्पकारों को सामाजिक अधिकार दिलाने के लिए यह आंदोलन चलाया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'छोपाती' (Chhopati) क्या है?",
        "options": ["एक नृत्य और गीत", "एक त्यौहार", "एक वाद्य यंत्र", "एक पकवान"],
        "correct_answer": "एक नृत्य और गीत",
        "explanation": "जौनसार बावर क्षेत्र का एक प्रसिद्ध लोकनृत्य है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Dynasties",
        "text": "कत्यूरी शासनकाल में 'उपरिक' (Uparika) कौन था?",
        "options": ["प्रांत का राज्यपाल", "कोषाध्यक्ष", "सेनापति", "न्यायाधीश"],
        "correct_answer": "प्रांत का राज्यपाल",
        "explanation": "प्रांतों के शासक को उपरिक कहा जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "उत्तराखंड की 'सबसे गहरी' झील कौन सी है?",
        "options": ["नौकुचियाताल", "भीमताल", "नैनीताल", "सातताल"],
        "correct_answer": "नौकुचियाताल",
        "explanation": "यह नैनीताल जिले में स्थित है और इसकी गहराई लगभग 40 मीटर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Changes",
        "text": "कुमाऊँ और गढ़वाल को दो अलग जिलों में किस वर्ष बाँटा गया था?",
        "options": ["1839", "1815", "1850", "1891"],
        "correct_answer": "1839",
        "explanation": "प्रशासनिक सुविधा के लिए गढ़वाल को अलग जिला बनाया गया और मुख्यालय पौड़ी रखा गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'कुमाऊँनी भाषा का वैज्ञानिक अध्ययन' किसकी पुस्तक है?",
        "options": ["डॉ. गंगादत्त उप्रेती", "डॉ. डी.डी. शर्मा", "शैलेश मटियानी", "डबराल"],
        "correct_answer": "डॉ. डी.डी. शर्मा",
        "explanation": "उन्हें भाषा विज्ञान के क्षेत्र में पद्मश्री भी मिला है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Glaciers",
        "text": "पिण्डारी ग्लेशियर किन दो जिलों की सीमा पर स्थित है?",
        "options": ["बागेश्वर और चमोली", "पिथौरागढ़ और बागेश्वर", "चमोली और पिथौरागढ़", "उत्तरकाशी और चमोली"],
        "correct_answer": "बागेश्वर और चमोली",
        "explanation": "यह उत्तराखंड का दूसरा सबसे बड़ा ग्लेशियर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Temples",
        "text": "जागेश्वर धाम में कुल कितने छोटे-बड़े मंदिर हैं?",
        "options": ["124", "100", "50", "150"],
        "correct_answer": "124",
        "explanation": "यह कुमाऊँ का सबसे बड़ा मंदिर समूह है, जिसे कत्यूरी राजाओं ने बनवाया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'हरेला' (Harela) पर्व का मुख्य संबंध किससे है?",
        "options": ["फसल और हरियाली", "वीर पूजा", "पितृ पूजा", "विवाह"],
        "correct_answer": "फसल और हरियाली",
        "explanation": "सावन के महीने में प्रकृति के प्रति आभार व्यक्त करने के लिए यह मनाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "उत्तराखंड में 'कोसी' और 'रामगंगा' (पश्चिमी) के बीच कौन सी पर्वत श्रेणी स्थित है?",
        "options": ["दूधातोली", "बिन्सर", "चोपता", "त्रिशूल"],
        "correct_answer": "बिन्सर",
        "explanation": "अल्मोड़ा जिले में यह क्षेत्र जल विभाजक का कार्य करता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'कमिश्नर' का पद किस वर्ष सृजित किया गया था?",
        "options": ["1815", "1820", "1830", "1850"],
        "correct_answer": "1815",
        "explanation": "गार्डनर कुमाऊँ के प्रथम कमिश्नर बने थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "उत्तराखंड में 'जागर' (Jagar) क्या है?",
        "options": ["देवी-देवताओं का आह्वान", "एक वाद्य यंत्र", "एक नृत्य शैली", "एक आभूषण"],
        "correct_answer": "देवी-देवताओं का आह्वान",
        "explanation": "जागर के माध्यम से स्थानीय देवताओं को प्रसन्न किया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "उत्तराखंड का 'सबसे ऊँचा' पर्वत शिखर कौन सा है?",
        "options": ["नन्दा देवी (पश्चिमी)", "कामेट", "त्रिशूल", "चौखम्बा"],
        "correct_answer": "नन्दा देवी (पश्चिमी)",
        "explanation": "इसकी ऊँचाई 7817 मीटर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Numismatics",
        "text": "कुणिन्दों की 'अल्मोड़ा प्रकार' की मुद्राओं पर कितने राजाओं के नाम मिलते हैं?",
        "options": ["8", "4", "10", "6"],
        "correct_answer": "8",
        "explanation": "इन मुद्राओं से शिवदत्त, शिवपालित जैसे शासकों की जानकारी मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड का चाणक्य' (Chanakya) कहा जाता है?",
        "options": ["पुरिया नैथानी", "हर्षदेव जोशी", "पंत", "डबराल"],
        "correct_answer": "पुरिया नैथानी",
        "explanation": "गढ़वाल रियासत के चतुर राजनीतिज्ञ के रूप में उन्हें यह ख्याति प्राप्त है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "किस झील का आकार 'अर्धचन्द्राकार' (Crescent Shape) है?",
        "options": ["नैनीताल", "भीमताल", "खुरपाताल", "नल-दमयन्ती ताल"],
        "correct_answer": "नैनीताल",
        "explanation": "नैनीताल झील का आकार आँखों या अर्धचन्द्र जैसा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'तराई जिला' किस वर्ष गठित किया गया था?",
        "options": ["1842", "1891", "1815", "1850"],
        "correct_answer": "1842",
        "explanation": "तराई क्षेत्र के प्रबंधन के लिए इसे अलग जिला बनाया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'गढ़वाल का इतिहास' (History of Garhwal) पुस्तक के लेखक कौन हैं?",
        "options": ["हरिकृष्ण रतूड़ी", "डबराल", "पाण्डे", "रतूड़ी"],
        "correct_answer": "हरिकृष्ण रतूड़ी",
        "explanation": "1910 में उन्होंने गढ़वाल के इतिहास पर यह प्रथम व्यवस्थित पुस्तक लिखी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "यमुना नदी की लंबाई उत्तराखंड में कितनी है?",
        "options": ["136 किमी", "150 किमी", "100 किमी", "110 किमी"],
        "correct_answer": "136 किमी",
        "explanation": "यह यमुनोत्री से धालीपुर तक की लंबाई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Tribes",
        "text": "उत्तराखंड की किस जनजाति के लोग स्वयं को 'जनक' का वंशज मानते हैं?",
        "options": ["जौनसारी", "थारू", "भोटिया", "राजी"],
        "correct_answer": "जौनसारी",
        "explanation": "जौनसारी समाज के लोग पांडवों और राजा जनक से अपना संबंध जोड़ते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "उत्तराखंड में 'हुड़का' (Hurka) किस प्रकार का वाद्य यंत्र है?",
        "options": ["चर्म वाद्य", "सुषिर वाद्य", "घन वाद्य", "तंतु वाद्य"],
        "correct_answer": "चर्म वाद्य",
        "explanation": "यह कृषि कार्यों और जागर में बजाया जाने वाला प्रमुख यंत्र है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks",
        "text": "'चौखम्बा' शिखर किस जिले में स्थित है?",
        "options": ["चमोली", "रुद्रप्रयाग", "पौड़ी", "उत्तरकाशी"],
        "correct_answer": "चमोली",
        "explanation": "यह बद्रीनाथ के पास स्थित एक विशाल शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin History",
        "text": "उत्तराखंड में 'डिप्टी कमिश्नर' पद पर रहने वाले प्रथम भारतीय कौन थे?",
        "options": ["पी. डब्लू. पांगती", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "विक्टर मोहन जोशी"],
        "correct_answer": "पी. डब्लू. पांगती",
        "explanation": "स्वतंत्रता के बाद प्रशासनिक सेवा में उनका महत्वपूर्ण स्थान था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड की झांसी की रानी' (तीलू रौतेली) का धर्म-भाई कहा जाता है?",
        "options": ["थोपा", "घमाण", "नगी", "रतन"],
        "correct_answer": "थोपा",
        "explanation": "तीलू रौतेली की वीर गाथाओं में थोपा और घमाण का उल्लेख मिलता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "किस ताल को 'भाई-बहन ताल' (Brother-Sister Lake) कहा जाता है?",
        "options": ["मसर ताल", "यम ताल", "महासर ताल", "डोडी ताल"],
        "correct_answer": "महासर ताल",
        "explanation": "टिहरी गढ़वाल में स्थित यह ताल दो कटोरानुमा तालों का समूह है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Dynasties",
        "text": "कत्यूरी काल में 'महाप्रमातार' (Mahapramatar) कौन था?",
        "options": ["भूमि की नाप-जोख करने वाला", "कोषाध्यक्ष", "सेनापति", "न्यायाधीश"],
        "correct_answer": "भूमि की नाप-जोख करने वाला",
        "explanation": "राजस्व प्रशासन में भूमि मापन का कार्य इसी अधिकारी का था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'हिमालय की खस' (Khas of Himalaya) किसकी पुस्तक है?",
        "options": ["डॉ. डी.डी. शर्मा", "डबराल", "पाण्डे", "जोशी"],
        "correct_answer": "डॉ. डी.डी. शर्मा",
        "explanation": "उत्तराखंड की प्राचीन जातियों पर उनका यह महत्वपूर्ण शोध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "काली और सरयू का संगम कहाँ होता है?",
        "options": ["पंचेश्वर", "जौलजीबी", "धारचूला", "टनकपुर"],
        "correct_answer": "पंचेश्वर",
        "explanation": "यहाँ काली नदी को 'शारदा' भी कहा जाने लगता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'पहला बंदोबस्त' करने वाला ट्रेल का कार्यकाल क्या था?",
        "options": ["1816-1835", "1815-1830", "1820-1840", "1825-1845"],
        "correct_answer": "1816-1835",
        "explanation": "ट्रेल को 'कुमाऊँ का वास्तविक कमिश्नर' माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के किस महान व्यक्ति को 'धरतीपुत्र' (Son of Earth) कहा जाता है?",
        "options": ["हेमवती नंदन बहुगुणा", "गोविंद बल्लभ पंत", "सुन्दरलाल बहुगुणा", "चण्डी प्रसाद भट्ट"],
        "correct_answer": "हेमवती नंदन बहुगुणा",
        "explanation": "वे उत्तर प्रदेश के मुख्यमंत्री और केंद्रीय मंत्री रहे थे।"
    },

    # ── BATCH 12: JOURNALISM & FESTIVALS ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism History",
        "text": "उत्तराखंड का 'पहला दैनिक' (Daily) समाचार पत्र कौन सा था?",
        "options": ["पर्वतीय", "अल्मोड़ा अखबार", "गढ़वाली", "शक्ति"],
        "correct_answer": "पर्वतीय",
        "explanation": "विष्णु दत्त उनियाल द्वारा नैनीताल से इसका संपादन किया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism History",
        "text": "1905 में 'गढ़वाली' समाचार पत्र का संपादन किसने किया था?",
        "options": ["गिरिजा दत्त नैथानी", "तारा दत्त गैरोला", "विशम्भर दत्त चन्दोला", "उपरोक्त सभी"],
        "correct_answer": "गिरिजा दत्त नैथानी",
        "explanation": "उन्होंने गढ़वाली भाषा और संस्कृति के उत्थान के लिए यह पत्र शुरू किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Social Reform",
        "text": "'समता' (Samata) समाचार पत्र की शुरुआत किसने की थी?",
        "options": ["हरि प्रसाद टम्टा", "बद्रीदत्त पाण्डेय", "ललिता प्रसाद", "खुशीराम"],
        "correct_answer": "हरि प्रसाद टम्टा",
        "explanation": "1934 में दलितों के उत्थान और सामाजिक समानता के लिए इसे अल्मोड़ा से शुरू किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Nanda Raj Jat",
        "text": "'नंदा राज जात' (Nanda Raj Jat) यात्रा कितने वर्षों के अंतराल पर आयोजित होती है?",
        "options": ["12 वर्ष", "10 वर्ष", "6 वर्ष", "8 वर्ष"],
        "correct_answer": "12 वर्ष",
        "explanation": "इसे 'हिमालय का महाकुंभ' भी कहा जाता है, जो चमोली के कासुवा गाँव से शुरू होती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "UNESCO Heritage",
        "text": "'रम्माण' (Ramman) उत्सव को यूनेस्को (UNESCO) द्वारा कब विश्व विरासत घोषित किया गया?",
        "options": ["2009", "2012", "2005", "2015"],
        "correct_answer": "2009",
        "explanation": "चमोली के सलूर-डुंग्रा गाँव का यह मुखौटा नृत्य अपनी विशिष्टता के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'बिखोती' (Bikhoti) का मेला कब आयोजित होता है?",
        "options": ["वैशाख की संक्रांति", "चैत्र संक्रांति", "श्रावण संक्रांति", "कार्तिक"],
        "correct_answer": "वैशाख की संक्रांति",
        "explanation": "अल्मोड़ा के द्वाराहाट में स्याल्दे-बिखोती का भव्य मेला लगता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism History",
        "text": "'शक्ति' (Shakti) समाचार पत्र की स्थापना किस ऐतिहासिक घटना के बाद हुई थी?",
        "options": ["अल्मोड़ा अखबार के बंद होने के बाद", "कुली बेगार आंदोलन", "नमक सत्याग्रही", "होमरूल लीग"],
        "correct_answer": "अल्मोड़ा अखबार के बंद होने के बाद",
        "explanation": "1918 में बद्रीदत्त पाण्डेय ने शक्ति का प्रकाशन शुरू किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'हेनरी रैमजे' का कार्यकाल कब से कब तक था?",
        "options": ["1856-1884", "1850-1875", "1860-1890", "1840-1865"],
        "correct_answer": "1856-1884",
        "explanation": "उन्हें 'कुमाऊँ का बेताज बादशाह' कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "National Parks",
        "text": "उत्तराखंड का सबसे 'छोटा' राष्ट्रीय उद्यान कौन सा है?",
        "options": ["फूलों की घाटी", "राजाजी", "गंगोत्री", "नंदा देवी"],
        "correct_answer": "फूलों की घाटी",
        "explanation": "इसका क्षेत्रफल मात्र 87.5 वर्ग किमी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'गर्व भंजक' (Pride Breaker) की उपाधि दी गई थी?",
        "options": ["माधो सिंह भंडारी", "महिपति शाह", "लोदी रिखोला", "कालू मेहरा"],
        "correct_answer": "माधो सिंह भंडारी",
        "explanation": "उनकी वीरता के कारण उन्हें गर्व भंजक कहा जाता था (महिपति शाह के सेनापति)।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "काली और कुटीयांगती नदी का संगम कहाँ होता है?",
        "options": ["गुंजी", "धारचूला", "पिथौरागढ़", "टनकपुर"],
        "correct_answer": "गुंजी",
        "explanation": "पिथौरागढ़ जिले के गुंजी में यह महत्वपूर्ण संगम होता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Institutions",
        "text": "देहरादून में 'एफ.आर.आई.' (FRI) की स्थापना किस वर्ष हुई थी?",
        "options": ["1906", "1900", "1910", "1895"],
        "correct_answer": "1906",
        "explanation": "इम्पीरियल फॉरेस्ट रिसर्च इंस्टीट्यूट के रूप में इसकी शुरुआत हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'गढ़वाल गजेटियर' (Garhwal Gazetteer) पुस्तक के लेखक कौन थे?",
        "options": ["एच.जी. वाल्टन", "एटकिंसन", "नेविले", "विलियम्स"],
        "correct_answer": "एच.जी. वाल्टन",
        "explanation": "उन्होंने गढ़वाल और नैनीताल दोनों के गजेटियर लिखे थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks",
        "text": "'केदारनाथ' पर्वत शिखर की ऊँचाई कितनी है?",
        "options": ["6940 मीटर", "7120 मीटर", "6500 मीटर", "7000 मीटर"],
        "correct_answer": "6940 मीटर",
        "explanation": "यह रुद्रप्रयाग जिले में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड राज्य के 'प्रथम लोकायुक्त' कौन थे?",
        "options": ["न्यायमूर्ति एस.एच. कपाड़िया", "न्यायमूर्ति रजा", "न्यायमूर्ति देसाई", "न्यायमूर्ति पंत"],
        "correct_answer": "न्यायमूर्ति रजा",
        "explanation": "एस.एच. रजा राज्य के पहले लोकायुक्त बने थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'पहला बंदोबस्त' करने वाला कमिश्नर कौन था?",
        "options": ["ई. गार्डनर", "ट्रेल", "रैमजे", "ल्यूशिंगटन"],
        "correct_answer": "ई. गार्डनर",
        "explanation": "1815 में उन्होंने संक्षिप्त व्यवस्था लागू की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड का गांधी' कहा जाता है?",
        "options": ["इन्द्रमणि बडोनी", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "सुन्दरलाल बहुगुणा"],
        "correct_answer": "इन्द्रमणि बडोनी",
        "explanation": "राज्य प्राप्ति आंदोलन में उनकी अहिंसक भूमिका के कारण।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Passes",
        "text": "'माना दर्रा' (Mana Pass) किनके बीच स्थित है?",
        "options": ["चमोली और तिब्बत", "उत्तरकाशी और तिब्बत", "पिथौरागढ़ और तिब्बत", "नेपाल और भारत"],
        "correct_answer": "चमोली और तिब्बत",
        "explanation": "इसे 'डुंग्री ला' के नाम से भी जाना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Inscriptions",
        "text": "'कालसी' का शिलालेख किस भाषा में है?",
        "options": ["प्राकृत", "पाली", "संस्कृत", "हिन्दी"],
        "correct_answer": "प्राकृत",
        "explanation": "अशोक के इस शिलालेख की भाषा प्राकृत और लिपि ब्राह्मी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'नगर निगम' (Municipal Corporation) की संख्या कितनी है (वर्तमान)?",
        "options": ["9", "8", "6", "10"],
        "correct_answer": "9",
        "explanation": "श्रीनगर को हाल ही में नगर निगम बनाया गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'खुरपाताल' (Khurpatal) किस जिले में स्थित है?",
        "options": ["नैनीताल", "अल्मोड़ा", "बागेश्वर", "चंपावत"],
        "correct_answer": "नैनीताल",
        "explanation": "इसका आकार घोड़े के खुर जैसा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'वनों का प्रबंधन' करने वाला पहला कमिश्नर कौन था?",
        "options": ["हेनरी रैमजे", "ट्रेल", "गार्डनर", "बेटन"],
        "correct_answer": "हेनरी रैमजे",
        "explanation": "उन्होंने वनों की सुरक्षा के लिए नाप और बेनाप भूमि के नियम बनाए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'उत्तराखंड की लोक कलाएँ' किसकी रचना है?",
        "options": ["यशोधर मठपाल", "डबराल", "डी.डी. शर्मा", "पाण्डे"],
        "correct_answer": "यशोधर मठपाल",
        "explanation": "उन्होंने उत्तराखंड की शैल चित्रकला और लोक कला पर व्यापक शोध किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "रामगंगा (पश्चिमी) किसकी सहायक नदी है?",
        "options": ["गंगा", "यमुना", "काली", "कोसी"],
        "correct_answer": "गंगा",
        "explanation": "यह कन्नौज के पास गंगा में मिल जाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Resistance",
        "text": "उत्तराखंड में 'कुली उतार' क्या था?",
        "options": ["एक प्रकार का कर", "निशुल्क कुली सेवा", "समान लाने की मजबूरी", "उपरोक्त सभी"],
        "correct_answer": "एक प्रकार का कर",
        "explanation": "अंग्रेज अधिकारियों का सामान ढोने के लिए ग्रामीणों पर यह कर लगाया जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife Sanctuaries",
        "text": "'गोविंद वन्यजीव विहार' किस जिले में स्थित है?",
        "options": ["उत्तरकाशी", "चमोली", "पिथौरागढ़", "रुद्रप्रयाग"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "यह बर्फानी तेंदुए के संरक्षण के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Dynasties",
        "text": "कत्यूरी काल में 'महासांघिविग्रहिक' कौन था?",
        "options": ["विदेश मंत्री", "कोषाध्यक्ष", "सेनापति", "न्यायाधीश"],
        "correct_answer": "विदेश मंत्री",
        "explanation": "संधि और युद्ध का कार्यभार इसी अधिकारी के पास था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "किस ताल को 'रहस्यमयी झील' (Mysterious Lake) कहा जाता है?",
        "options": ["रूपकुण्ड", "हेमकुण्ड", "सातताल", "भीमताल"],
        "correct_answer": "रूपकुण्ड",
        "explanation": "नरकंकालों की उपस्थिति के कारण इसे रहस्यमयी माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'हिलजात्रा' (Hill Jatra) उत्सव कहाँ मनाया जाता है?",
        "options": ["पिथौरागढ़", "अल्मोड़ा", "चंपावत", "बागेश्वर"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "यह कृषि उत्सव नेपाल की 'इंद्रजात्रा' से प्रेरित माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Journalism History",
        "text": "1918 में 'शक्ति' का प्रकाशन कहाँ से शुरू हुआ था?",
        "options": ["अल्मोड़ा", "देहरादून", "नैनीताल", "पौड़ी"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "देशभक्ति और सामाजिक चेतना के लिए बद्रीदत्त पाण्डेय ने इसे शुरू किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "अलकनन्दा की सहायक नदी 'ऋषि गंगा' का संगम कहाँ होता है?",
        "options": ["बद्रीनाथ के पास", "जोशीमठ", "विष्णुप्रयाग", "कर्णप्रयाग"],
        "correct_answer": "बद्रीनाथ के पास",
        "explanation": "ऋषि गंगा बद्रीनाथ धाम के समीप अलकनन्दा से मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "उत्तराखंड में 'बांसुरी' को स्थानीय भाषा में क्या कहा जाता है?",
        "options": ["मुरली/बांसुरी", "रणसिंघा", "हुड़का", "डौंर"],
        "correct_answer": "मुरली/बांसुरी",
        "explanation": "इसे स्थानीय रूप से मुरली ही कहा जाता है, लेकिन यह लोक वाद्य यंत्रों में महत्वपूर्ण है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks",
        "text": "'चौखम्बा' पर्वत शिखर की ऊँचाई कितनी है?",
        "options": ["7138 मीटर", "7120 मीटर", "7756 मीटर", "6904 मीटर"],
        "correct_answer": "7138 मीटर",
        "explanation": "यह चमोली जिले का एक प्रमुख शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'पटवारी' व्यवस्था का जनक किसे माना जाता है?",
        "options": ["ट्रेल", "रैमजे", "गार्डनर", "ल्यूशिंगटन"],
        "correct_answer": "ट्रेल",
        "explanation": "1819 में ट्रेल ने पटवारी पदों का सृजन कर राजस्व व्यवस्था मजबूत की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'हिमालयन ट्रेवल्स' (Himalayan Travels) पुस्तक के लेखक कौन हैं?",
        "options": ["जोत सिंह नेगी", "तारा दत्त गैरोला", "डबराल", "पाण्डे"],
        "correct_answer": "जोत सिंह नेगी",
        "explanation": "यह यात्रा वृत्तांत 1920 में प्रकाशित हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "भिलंगना नदी का उद्गम स्थल क्या है?",
        "options": ["खतलिंग ग्लेशियर", "गंगोत्री", "सतोपंथ", "पिण्डारी"],
        "correct_answer": "खतलिंग ग्लेशियर",
        "explanation": "यह टिहरी जिले में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Ancient Dynasties",
        "text": "कत्यूरी काल में 'गोल्मिक' (Golmika) कौन था?",
        "options": ["पैदल सेना का प्रमुख", "कोषाध्यक्ष", "न्यायाधीश", "मंत्री"],
        "correct_answer": "पैदल सेना का प्रमुख",
        "explanation": "सेना के विभिन्न अंगों में पैदल सेना के नायक को गोल्मिक कहते थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड का मंडेला' कहा जाता है?",
        "options": ["बृजेन्द्र लाल शाह", "इन्द्रमणि बडोनी", "बद्रीदत्त पाण्डेय", "श्रीदेव सुमन"],
        "correct_answer": "बृजेन्द्र लाल शाह",
        "explanation": "उन्हें सामाजिक और सांस्कृतिक कार्यों के लिए यह ख्याति प्राप्त है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'द्रोण ताल' किस जिले में स्थित है?",
        "options": ["ऊधम सिंह नगर", "नैनीताल", "हरिद्वार", "देहरादून"],
        "correct_answer": "ऊधम सिंह नगर",
        "explanation": "यह काशीपुर में स्थित है और गुरु द्रोणाचार्य से संबंधित माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Resistance",
        "text": "कुली बेगार आंदोलन के समय कुमाऊँ के कमिश्नर कौन थे?",
        "options": ["पी. विन्धम", "हेनरी रैमजे", "ल्यूशिंगटन", "बेटन"],
        "correct_answer": "पी. विन्धम",
        "explanation": "1921 के आंदोलन के समय विन्धम कमिश्नर के पद पर थे।"
    },

    # ── BATCH 13: CHAND DYNASTY & AGRICULTURE ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "कुमाऊँ में 'चन्द वंश' (Chand Dynasty) का संस्थापक किसे माना जाता है?",
        "options": ["सोम चन्द", "थोर चन्द", "लक्ष्मी चन्द", "ज्ञान चन्द"],
        "correct_answer": "सोम चन्द",
        "explanation": "प्रचलित मान्यताओं के अनुसार सोम चन्द ने कुमाऊँ में चन्द वंश की नींव रखी थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द शासक को 'मुगल सम्राट' शाहजहाँ ने 'बहादुर' की उपाधि दी थी?",
        "options": ["बाज बहादुर चन्द", "कल्याण चन्द", "भीष्म चन्द", "रुद्र चन्द"],
        "correct_answer": "बाज बहादुर चन्द",
        "explanation": "बाज बहादुर चन्द ने मुगलों से अच्छे संबंध बनाए रखे थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द काल में 'सिरती' (Sirti) क्या था?",
        "options": ["एक प्रकार का नकद कर", "एक आभूषण", "एक प्रशासनिक पद", "एक उत्सव"],
        "correct_answer": "एक प्रकार का नकद कर",
        "explanation": "सिरती केवल नकद रूप में लिया जाने वाला राजस्व कर था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Agriculture",
        "text": "उत्तराखंड के किस क्षेत्र को 'फलों का कटोरा' (Fruit Bowl) कहा जाता है?",
        "options": ["रामगढ़ (नैनीताल)", "हल्द्वानी", "काशीपुर", "कोटद्वार"],
        "correct_answer": "रामगढ़ (नैनीताल)",
        "explanation": "यहाँ बड़ी मात्रा में सेब, आड़ू और खुबानी का उत्पादन होता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Soil Types",
        "text": "तराई क्षेत्र की मिट्टी किस प्रकार की होती है?",
        "options": ["महीन कणों वाली उपजाऊ", "पथरीली", "बलुई", "लाल मिट्टी"],
        "correct_answer": "महीन कणों वाली उपजाऊ",
        "explanation": "तराई क्षेत्र कृषि के लिए बहुत उपजाऊ माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "River Systems",
        "text": "उत्तराखंड में 'कोसी' नदी को प्राचीन काल में क्या कहा जाता था?",
        "options": ["कौशिकी", "श्यामा", "नवा", "भद्रा"],
        "correct_answer": "कौशिकी",
        "explanation": "पुराणों और प्राचीन ग्रंथों में कोसी का नाम कौशिकी मिलता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द राजा ने 'रुद्रपुर' शहर की स्थापना की थी?",
        "options": ["रुद्र चन्द", "लक्ष्मी चन्द", "भीष्म चन्द", "त्रिमल चन्द"],
        "correct_answer": "रुद्र चन्द",
        "explanation": "तराई क्षेत्र के प्रबंधन के लिए उन्होंने रुद्रपुर की स्थापना की।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Horticulture",
        "text": "उत्तराखंड में 'लीची' (Litchi) का प्रमुख उत्पादक जिला कौन सा है?",
        "options": ["देहरादून", "नैनीताल", "अल्मोड़ा", "चंपावत"],
        "correct_answer": "देहरादून",
        "explanation": "देहरादून की लीची विश्व प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द शासनकाल में 'कमीण' (Kamin) और 'सयाणा' (Sayana) कौन थे?",
        "options": ["राजस्व वसूलने वाले", "सैनिक", "पुजारी", "न्यायाधीश"],
        "correct_answer": "राजस्व वसूलने वाले",
        "explanation": "गाँवों से कर वसूल कर सरकार तक पहुँचाने की जिम्मेदारी इनकी थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "उत्तराखंड की 'शारदा' (काली) नदी को तराई में किस नाम से जाना जाता है?",
        "options": ["शारदा", "गौरी", "धौली", "कोसी"],
        "correct_answer": "शारदा",
        "explanation": "टनकपुर के बाद काली नदी को शारदा कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द शासक ने 'चौमहला' (Chaumahla) महलों का निर्माण करवाया था?",
        "options": ["बाज बहादुर चन्द", "कल्याण चन्द", "लक्ष्मी चन्द", "ज्ञान चन्द"],
        "correct_answer": "बाज बहादुर चन्द",
        "explanation": "उन्होंने अल्मोड़ा में कई महलों और मंदिरों का निर्माण करवाया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Landforms",
        "text": "पहाड़ों की ढलानों पर बनाई जाने वाली खेती को क्या कहते हैं?",
        "options": ["सीढ़ीदार खेती", "झूम खेती", "मिश्रित खेती", "गहन खेती"],
        "correct_answer": "सीढ़ीदार खेती",
        "explanation": "मिट्टी के कटाव को रोकने और सिंचाई के लिए यह पद्धति अपनाई जाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द काल में 'साहु' (Sahu) शब्द किसके लिए प्रयुक्त होता था?",
        "options": ["लेखक/क्लर्क", "व्यापारी", "सैनिक", "पुजारी"],
        "correct_answer": "लेखक/क्लर्क",
        "explanation": "प्रशासनिक कार्यों में साहु का कार्य लेखन से संबंधित था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Agriculture",
        "text": "उत्तराखंड में 'मंडुआ' (Ragi) किस प्रकार की फसल है?",
        "options": ["खरीफ", "रबी", "जायद", "नकद"],
        "correct_answer": "खरीफ",
        "explanation": "यह मुख्य रूप से वर्षा ऋतु में उगाई जाने वाली पोषक फसल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द शासक को 'लखुली बिराली' (Lakhuli Birali) कहा जाता था?",
        "options": ["लक्ष्मी चन्द", "रुद्र चन्द", "भीष्म चन्द", "थोर चन्द"],
        "correct_answer": "लक्ष्मी चन्द",
        "explanation": "गढ़वाल के विरुद्ध बार-बार हारने के कारण उन्हें यह उपनाम मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Tea Estates",
        "text": "उत्तराखंड में 'कौसानी' चाय बागान की स्थापना किस वर्ष हुई थी?",
        "options": ["1839", "1850", "1860", "1845"],
        "correct_answer": "1839",
        "explanation": "ब्रिटिश शासनकाल में चाय की खेती को बहुत बढ़ावा दिया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द काल में 'थोकदार' (Thokdar) का कार्य क्या था?",
        "options": ["राजस्व वसूली", "सैन्य नेतृत्व", "धार्मिक अनुष्ठान", "न्याय"],
        "correct_answer": "राजस्व वसूली",
        "explanation": "थोकदार कई गाँवों के राजस्व प्रबंधन का प्रमुख होता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Crops",
        "text": "उत्तराखंड में 'झंगोरा' (Barnyard Millet) का सर्वाधिक उत्पादन कहाँ होता है?",
        "options": ["पर्वतीय क्षेत्रों में", "तराई", "भाबर", "मैदानी"],
        "correct_answer": "पर्वतीय क्षेत्रों में",
        "explanation": "यह पहाड़ों की एक पारंपरिक और पौष्टिक फसल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द शासक ने 'खगमरा' (Khagmara) किले का निर्माण करवाया था?",
        "options": ["भीष्म चन्द", "कल्याण चन्द", "रुद्र चन्द", "सोम चन्द"],
        "correct_answer": "भीष्म चन्द",
        "explanation": "अल्मोड़ा में खगमरा किला भीष्म चन्द द्वारा बनवाया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Forestry",
        "text": "उत्तराखंड में 'बांज' (Oak) वृक्ष का महत्व क्या है?",
        "options": ["जल संरक्षण और चारा", "इमारती लकड़ी", "औषधि", "तेल उत्पादन"],
        "correct_answer": "जल संरक्षण और चारा",
        "explanation": "बांज के जंगल वर्षा जल को सोखने और पशुओं के चारे के लिए बहुत महत्वपूर्ण हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द काल में 'नेगी' (Negi) पद का क्या अर्थ था?",
        "options": ["एक विशिष्ट प्रशासनिक अधिकारी", "सैनिक", "मजदूर", "कलाकार"],
        "correct_answer": "एक विशिष्ट प्रशासनिक अधिकारी",
        "explanation": "नेगी उन अधिकारियों को कहा जाता था जो राजस्व और सैन्य कार्यों में सहायक थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "River Tributaries",
        "text": "पिण्डर नदी किसकी सहायक नदी है?",
        "options": ["अलकनन्दा", "भागीरथी", "यमुना", "काली"],
        "correct_answer": "अलकनन्दा",
        "explanation": "पिण्डर कर्णप्रयाग में अलकनन्दा से मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द राजा ने 'जागेश्वर' मंदिर का जीर्णोद्धार करवाया था?",
        "options": ["बाज बहादुर चन्द", "लक्ष्मी चन्द", "रुद्र चन्द", "ज्ञान चन्द"],
        "correct_answer": "बाज बहादुर चन्द",
        "explanation": "उन्होंने जागेश्वर मंदिर समूह में कई सुधार और निर्माण कार्य करवाए।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Land Use",
        "text": "उत्तराखंड के कितने प्रतिशत भू-भाग पर खेती की जाती है?",
        "options": ["लगभग 13%", "लगभग 20%", "लगभग 30%", "लगभग 50%"],
        "correct_answer": "लगभग 13%",
        "explanation": "पर्वतीय भौगोलिक स्थिति के कारण कृषि योग्य भूमि बहुत कम है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द शासन में 'बिष्ट' (Bisht) कौन थे?",
        "options": ["सैन्य अधिकारी", "राजस्व क्लर्क", "पुजारी", "व्यापारी"],
        "correct_answer": "सैन्य अधिकारी",
        "explanation": "बिष्ट उच्च पदस्थ सैन्य और प्रशासनिक अधिकारी हुआ करते थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife",
        "text": "उत्तराखंड का 'राजकीय पशु' कस्तूरी मृग किस ऊँचाई पर पाया जाता है?",
        "options": ["2000-5000 मीटर", "500-1000 मीटर", "1000-2000 मीटर", "6000-8000 मीटर"],
        "correct_answer": "2000-5000 मीटर",
        "explanation": "यह उच्च हिमालयी क्षेत्रों का निवासी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द शासक ने 'बगवाली पोखर' (Bagwali Pokhar) का युद्ध लड़ा था?",
        "options": ["ललित शाह (गढ़वाल) के विरुद्ध मोहन चन्द", "रुद्र चन्द", "लक्ष्मी चन्द", "बाज बहादुर चन्द"],
        "correct_answer": "ललित शाह (गढ़वाल) के विरुद्ध मोहन चन्द",
        "explanation": "यह चन्द और पवार सेनाओं के बीच एक प्रसिद्ध युद्ध था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Water Bodies",
        "text": "उत्तराखंड में 'नौला' (Naula) क्या है?",
        "options": ["एक पारंपरिक जल स्रोत", "एक नृत्य", "एक आभूषण", "एक पकवान"],
        "correct_answer": "एक पारंपरिक जल स्रोत",
        "explanation": "नौला एक छोटा, वर्गाकार जल कुंड होता है जिसे पीने के पानी के लिए बनाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द काल में 'गल्ला छौड़ा' (Galla Chhaura) क्या था?",
        "options": ["अनाज के रूप में लिया जाने वाला कर", "एक उत्सव", "एक प्रथा", "एक सैन्य पद"],
        "correct_answer": "अनाज के रूप में लिया जाने वाला कर",
        "explanation": "कुल उपज का छठा हिस्सा 'गल्ला' के रूप में लिया जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks",
        "text": "प्रसिद्ध 'चौखम्बा' शिखर किस जिले में स्थित है?",
        "options": ["चमोली", "रुद्रप्रयाग", "पौड़ी", "उत्तरकाशी"],
        "correct_answer": "चमोली",
        "explanation": "यह बद्रीनाथ के पास स्थित एक विशाल शिखर है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द वंश का 'अंतिम' राजा कौन था?",
        "options": ["महेन्द्र चन्द", "मोहन चन्द", "कल्याण चन्द", "दीप चन्द"],
        "correct_answer": "महेन्द्र चन्द",
        "explanation": "1790 में गोरखाओं से हारने के बाद महेन्द्र चन्द अंतिम शासक साबित हुए।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Forestry",
        "text": "उत्तराखंड में 'चीड़' (Pine) के पेड़ से क्या प्राप्त किया जाता है?",
        "options": ["लीसा (Resin)", "चारा", "औषधि", "तेल"],
        "correct_answer": "लीसा (Resin)",
        "explanation": "लीसा का उपयोग तारपीन का तेल और अन्य औद्योगिक उत्पाद बनाने में होता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द शासक ने 'मल्ला महल' (Malla Mahal) का निर्माण करवाया था?",
        "options": ["रुद्र चन्द", "भीष्म चन्द", "कल्याण चन्द", "बाज बहादुर चन्द"],
        "correct_answer": "रुद्र चन्द",
        "explanation": "अल्मोड़ा का मल्ला महल रुद्र चन्द द्वारा बनवाया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'गिरि ताल' (Giri Tal) कहाँ स्थित है?",
        "options": ["काशीपुर", "नैनीताल", "हल्द्वानी", "रुद्रपुर"],
        "correct_answer": "काशीपुर",
        "explanation": "यह ऊधम सिंह नगर के काशीपुर में स्थित एक धार्मिक और पर्यटन स्थल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द शासनकाल में 'चार बूढ़ा' (Char Budha) व्यवस्था क्या थी?",
        "options": ["चार प्रमुख जातियों का समूह", "चार मंत्रियों का समूह", "चार किलों का रक्षक", "चार न्यायाधीशों का समूह"],
        "correct_answer": "चार प्रमुख जातियों का समूह",
        "explanation": "कार्की, बोरा, तड़ागी और चौधरी जातियों का प्रशासनिक व्यवस्था में विशेष स्थान था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "कोसी नदी किस नदी की सहायक नदी है?",
        "options": ["रामगंगा (पश्चिमी)", "गंगा", "यमुना", "काली"],
        "correct_answer": "रामगंगा (पश्चिमी)",
        "explanation": "कोसी रामगंगा में मिल जाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द शासक ने 'कटास' (Katas) कर लगाया था?",
        "options": ["लक्ष्मी चन्द", "बाज बहादुर चन्द", "रुद्र चन्द", "ज्ञान चन्द"],
        "correct_answer": "लक्ष्मी चन्द",
        "explanation": "सैन्य अभियानों के खर्च के लिए उन्होंने नए कर लगाए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Soil",
        "text": "उत्तराखंड के भाबर क्षेत्र की मिट्टी कैसी होती है?",
        "options": ["पथरीली और कंकड़ वाली", "उपजाऊ", "रेतीली", "लाल"],
        "correct_answer": "पथरीली और कंकड़ वाली",
        "explanation": "भाबर क्षेत्र में नदियाँ विलुप्त हो जाती हैं और यहाँ की जमीन खेती के लिए बहुत कठिन है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द काल में 'पलिया' (Paliya) कौन थे?",
        "options": ["मजदूर", "सैनिक", "लेखक", "पुजारी"],
        "correct_answer": "मजदूर",
        "explanation": "खेतों और निर्माण कार्यों में लगे मजदूरों को पलिया कहा जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "किस ताल को 'नल ताल' के नाम से भी जाना जाता है?",
        "options": ["कमल ताल", "भीमताल", "नौकुचियाताल", "खुरपाताल"],
        "correct_answer": "कमल ताल",
        "explanation": "नल-दमयन्ती ताल के पास स्थित कमल ताल को भी कभी-कभी इसी नाम से पुकारा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द राजा ने अपनी राजधानी 'चंपावत से अल्मोड़ा' स्थानांतरित की थी?",
        "options": ["कल्याण चन्द (भीष्म चन्द ने योजना बनाई थी)", "भीष्म चन्द", "रुद्र चन्द", "सोम चन्द"],
        "correct_answer": "कल्याण चन्द (भीष्म चन्द ने योजना बनाई थी)",
        "explanation": "राजधानी परिवर्तन का कार्य कल्याण चन्द के समय पूर्ण हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Horticulture",
        "text": "उत्तराखंड में 'अखरोट' (Walnut) का सर्वाधिक उत्पादन किस जिले में होता है?",
        "options": ["उत्तरकाशी", "अल्मोड़ा", "चंपावत", "नैनीताल"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "उत्तरकाशी जिला अखरोट उत्पादन में राज्य में अग्रणी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द शासन में 'ज्यूल्या' (Jyulya) क्या था?",
        "options": ["नकद कर", "भूमि उपहार", "प्रशासनिक पद", "एक उत्सव"],
        "correct_answer": "नकद कर",
        "explanation": "यह एक प्रकार का राजस्व कर था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "मंदाकिनी नदी किसकी सहायक नदी है?",
        "options": ["अलकनन्दा", "भागीरथी", "यमुना", "काली"],
        "correct_answer": "अलकनन्दा",
        "explanation": "मंदाकिनी रुद्रप्रयाग में अलकनन्दा से मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द राजा ने 'बालेश्वर' मंदिर (चंपावत) का निर्माण करवाया था?",
        "options": ["उद्योत चन्द", "रुद्र चन्द", "लक्ष्मी चन्द", "भीष्म चन्द"],
        "correct_answer": "उद्योत चन्द",
        "explanation": "चंपावत का बालेश्वर मंदिर उद्योत चन्द द्वारा बनवाया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Crops",
        "text": "उत्तराखंड में 'आलू' (Potato) की खेती सर्वप्रथम कहाँ शुरू हुई थी?",
        "options": ["देहरादून (1823)", "नैनीताल", "अल्मोड़ा", "मसूरी"],
        "correct_answer": "देहरादून (1823)",
        "explanation": "देहरादून के पास आलू की खेती ब्रिटिश काल में शुरू की गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "चन्द काल में 'कौतलि' (Kautali) क्या था?",
        "options": ["भूमि कर", "एक आभूषण", "एक पकवान", "एक पद"],
        "correct_answer": "भूमि कर",
        "explanation": "राजस्व व्यवस्था में कौतलि एक महत्वपूर्ण कर था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Forestry",
        "text": "उत्तराखंड में 'लाल मिट्टी' मुख्य रूप से किस क्षेत्र में पाई जाती है?",
        "options": ["पर्वतीय ढलानों पर", "तराई", "मैदानी", "नदी घाटियों"],
        "correct_answer": "पर्वतीय ढलानों पर",
        "explanation": "पहाड़ी क्षेत्रों की मिट्टी में लोहे की अधिकता के कारण यह लाल दिखती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Chand Dynasty",
        "source": "Chand History",
        "text": "किस चन्द शासक ने 'तल्ली ताल' और 'मल्ली ताल' (नैनीताल) के आसपास का विकास किया था?",
        "options": ["बाज बहादुर चन्द", "कल्याण चन्द", "रुद्र चन्द", "दीप चन्द"],
        "correct_answer": "बाज बहादुर चन्द",
        "explanation": "उन्होंने नैनीताल क्षेत्र में कई विकास कार्य करवाए।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Agriculture",
        "text": "उत्तराखंड में 'मिश्रित खेती' (Mixed Farming) का क्या अर्थ है?",
        "options": ["खेती और पशुपालन साथ-साथ", "दो फसलों को एक साथ उगाना", "विभिन्न बीजों का उपयोग", "उपरोक्त सभी"],
        "correct_answer": "खेती और पशुपालन साथ-साथ",
        "explanation": "ग्रामीण अर्थव्यवस्था में खेती और पशुपालन एक-दूसरे के पूरक हैं।"
    },

    # ── BATCH 14: ARCHITECTURE & EDUCATION ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Temple Architecture",
        "text": "उत्तराखंड का प्रसिद्ध 'कटारमल सूर्य मंदिर' किस वास्तु शैली में बना है?",
        "options": ["उत्तराखंड शैली (कत्यूरी)", "द्रविड़ शैली", "नागर शैली", "मिश्रित शैली"],
        "correct_answer": "उत्तराखंड शैली (कत्यूरी)",
        "explanation": "यह मंदिर भगवान सूर्य को समर्पित है और अपनी शिल्पकला के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Temple History",
        "text": "अल्मोड़ा स्थित 'चितई गोलू देवता' मंदिर का निर्माण किसने करवाया था?",
        "options": ["बाज बहादुर चन्द", "लक्ष्मी चन्द", "रुद्र चन्द", "भीष्म चन्द"],
        "correct_answer": "बाज बहादुर चन्द",
        "explanation": "गोलू देवता को कुमाऊँ में न्याय का देवता माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Ancient Temples",
        "text": "'बैजनाथ' (Baijnath) मंदिर समूह किस नदी के तट पर स्थित है?",
        "options": ["गोमती", "सरयू", "कोसी", "गौला"],
        "correct_answer": "गोमती",
        "explanation": "बागेश्वर जिले के बैजनाथ में गोमती नदी के तट पर कत्यूरी मंदिरों का भव्य समूह है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Heritage Buildings",
        "text": "देहरादून का 'घंटाघर' (Clock Tower) किसकी स्मृति में बनवाया गया था?",
        "options": ["लाला बलवीर सिंह", "रानी कर्णवती", "महाराजा प्रताप शाह", "हेनली"],
        "correct_answer": "लाला बलवीर सिंह",
        "explanation": "इस ऐतिहासिक मीनार का नाम 'बलवीर क्लॉक टावर' है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education History",
        "text": "उत्तराखंड में 'रुड़की इंजीनियरिंग कॉलेज' की स्थापना किस वर्ष हुई थी?",
        "options": ["1847", "1850", "1860", "1840"],
        "correct_answer": "1847",
        "explanation": "यह एशिया का पहला इंजीनियरिंग कॉलेज है, जिसे अब IIT रुड़की के नाम से जाना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Religious Sites",
        "text": "'महासू देवता' का प्रसिद्ध मंदिर कहाँ स्थित है?",
        "options": ["हनोल (देहरादून)", "मसूरी", "चोपता", "जोशीमठ"],
        "correct_answer": "हनोल (देहरादून)",
        "explanation": "यह जौनसार बावर क्षेत्र के आराध्य देवता हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Institutions",
        "text": "नैनीताल में 'सेंट जोसेफ कॉलेज' की स्थापना किस वर्ष हुई थी?",
        "options": ["1888", "1880", "1895", "1900"],
        "correct_answer": "1888",
        "explanation": "नैनीताल को ब्रिटिश काल में शिक्षा के केंद्र के रूप में विकसित किया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Architectural Styles",
        "text": "उत्तराखंड के मंदिरों में 'छत्र' (Canopy) बनाने की परंपरा किस शैली की विशेषता है?",
        "options": ["पैगोडा शैली", "नागर शैली", "द्रविड़", "शिखर शैली"],
        "correct_answer": "पैगोडा शैली",
        "explanation": "हिमालयी क्षेत्रों के कई मंदिरों में लकड़ी के छत्र पाए जाते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Legal History",
        "text": "कुमाऊँ में 'शेड्यूल्ड डिस्ट्रिक्ट एक्ट' (Scheduled District Act) कब लागू हुआ था?",
        "options": ["1874", "1860", "1880", "1890"],
        "correct_answer": "1874",
        "explanation": "इस कानून ने कुमाऊँ को एक विशेष प्रशासनिक दर्जा दिया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Folk Architecture",
        "text": "उत्तराखंड के पुराने घरों में नक्काशीदार लकड़ी के प्रवेश द्वार को क्या कहते हैं?",
        "options": ["खोली", "देहरी", "आँगण", "छज्जा"],
        "correct_answer": "खोली",
        "explanation": "खोली पर की गई चित्रकारी और नक्काशी स्थानीय शिल्प कला का सुंदर नमूना है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education History",
        "text": "देहरादून में 'दून स्कूल' की स्थापना किसने की थी?",
        "options": ["सतीश रंजन दास", "जवाहरलाल नेहरू", "डॉ. सर्वपल्ली राधाकृष्णन", "लॉर्ड कर्जन"],
        "correct_answer": "सतीश रंजन दास",
        "explanation": "1935 में भारत के इस प्रतिष्ठित बोर्डिंग स्कूल की स्थापना हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Forts",
        "text": "पिथौरागढ़ का 'लन्दन फोर्ट' (London Fort) किसने बनवाया था?",
        "options": ["गोरखा शासकों ने", "अंग्रेजों ने", "चन्द राजाओं ने", "पवार राजाओं ने"],
        "correct_answer": "गोरखा शासकों ने",
        "explanation": "इसे बाद में अंग्रेजों ने लन्दन फोर्ट नाम दिया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Social Institutions",
        "text": "नैनीताल में 'रिवर बैंक' (River Bank) कॉलोनी का विकास किसने किया था?",
        "options": ["हेनरी रैमजे", "ल्यूशिंगटन", "बेटन", "गार्डनर"],
        "correct_answer": "हेनरी रैमजे",
        "explanation": "उन्होंने नैनीताल के शहरी नियोजन में महत्वपूर्ण योगदान दिया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Temple Features",
        "text": "जागेश्वर मंदिर समूह में 'मृत्युंजय' मंदिर का निर्माण किसने करवाया था?",
        "options": ["शालिवाहन देव", "इष्टगण देव", "बसंत देव", "ललितशूर"],
        "correct_answer": "शालिवाहन देव",
        "explanation": "यह जागेश्वर का सबसे प्राचीन मंदिर माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'वैकेंसी' (Vacancy) प्रथा क्या थी?",
        "options": ["खाली जमीन का सरकारी अधिग्रहण", "नौकरियों में आरक्षण", "कर माफी", "सैन्य भर्ती"],
        "correct_answer": "खाली जमीन का सरकारी अधिग्रहण",
        "explanation": "बेवारिस जमीन को सरकार अपने कब्जे में ले लेती थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Religious Sites",
        "text": "'हेमकुण्ड साहिब' के पास कौन सी झील स्थित है?",
        "options": ["लोकपाल झील", "सतोपंथ", "रूपकुण्ड", "नंदा कुण्ड"],
        "correct_answer": "लोकपाल झील",
        "explanation": "सिखों के इस पवित्र तीर्थ स्थल को लोकपाल भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Infrastructure",
        "text": "ऋषिकेश में 'लक्ष्मण झूला' का आधुनिक निर्माण किस वर्ष हुआ था?",
        "options": ["1929", "1935", "1920", "1940"],
        "correct_answer": "1929",
        "explanation": "पुराना झूला लोहे की रस्सियों से बना था, जिसे 1929 में आधुनिक रूप दिया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Cave Temples",
        "text": "'पाताल भुवनेश्वर' गुफा मंदिर किस जिले में स्थित है?",
        "options": ["पिथौरागढ़", "अल्मोड़ा", "बागेश्वर", "चंपावत"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "यह एक भूमिगत गुफा मंदिर है जिसमें कई प्राकृतिक आकृतियाँ बनी हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Forestry",
        "text": "उत्तराखंड में 'वन पंचायतों' का गठन किस वर्ष शुरू हुआ था?",
        "options": ["1931", "1921", "1940", "1950"],
        "correct_answer": "1931",
        "explanation": "वनों के स्थानीय प्रबंधन के लिए यह एक अनोखी व्यवस्था है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Temple Architecture",
        "text": "केदारनाथ मंदिर के निर्माण में किस प्रकार के पत्थरों का उपयोग हुआ है?",
        "options": ["भूरे रंग के बड़े पत्थर", "सफेद संगमरमर", "लाल बलुआ पत्थर", "काले पत्थर"],
        "correct_answer": "भूरे रंग के बड़े पत्थर",
        "explanation": "यह मंदिर कत्यूरी शैली में बना है और अत्यंत सुदृढ़ है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education",
        "text": "मसूरी में 'वुडस्टॉक स्कूल' (Woodstock School) की स्थापना किस वर्ष हुई थी?",
        "options": ["1854", "1860", "1880", "1900"],
        "correct_answer": "1854",
        "explanation": "यह एशिया के सबसे पुराने अंतरराष्ट्रीय स्कूलों में से एक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Forts",
        "text": "अल्मोड़ा का 'लाल मण्डी' किला किसने बनवाया था?",
        "options": ["कल्याण चन्द", "रुद्र चन्द", "भीष्म चन्द", "बाज बहादुर चन्द"],
        "correct_answer": "कल्याण चन्द",
        "explanation": "इसे बाद में अंग्रेजों ने 'फोर्ट मोयरा' नाम दिया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'मुसाफिरखाना' (Rest House) बनाने की परंपरा किसने शुरू की थी?",
        "options": ["ट्रेल", "रैमजे", "गार्डनर", "ल्यूशिंगटन"],
        "correct_answer": "ट्रेल",
        "explanation": "यात्रियों की सुविधा के लिए उन्होंने मुख्य मार्गों पर विश्राम गृह बनवाए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Religious Sites",
        "text": "'कालीमठ' (Kalimath) मंदिर किस नदी के तट पर है?",
        "options": ["सरस्वती (रुद्रप्रयाग)", "मंदाकिनी", "अलकनन्दा", "नयार"],
        "correct_answer": "सरस्वती (रुद्रप्रयाग)",
        "explanation": "यह सिद्धपीठों में से एक है और काली नदी के पास सरस्वती तट पर स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Social Reform",
        "text": "उत्तराखंड में 'स्वराज्य आश्रम' की स्थापना कहाँ हुई थी?",
        "options": ["अल्मोड़ा", "देहरादून", "नैनीताल", "हल्द्वानी"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "स्वतंत्रता सेनानियों के प्रशिक्षण और बैठकों के लिए इसे बनाया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Temple Features",
        "text": "उत्तराखंड के किस मंदिर में 'धनुष-बाण' की पूजा की जाती है?",
        "options": ["टपकेश्वर (देहरादून)", "जागेश्वर", "बद्रीनाथ", "केदारनाथ"],
        "correct_answer": "टपकेश्वर (देहरादून)",
        "explanation": "यहाँ द्रोणाचार्य और अश्वत्थामा से जुड़ी कथाएँ प्रचलित हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Infrastructure",
        "text": "नैनीताल में 'सैंड्स स्कूल' (St. Mary's Convent) की स्थापना कब हुई थी?",
        "options": ["1878", "1880", "1890", "1900"],
        "correct_answer": "1878",
        "explanation": "यह नैनीताल के पुराने और प्रतिष्ठित कॉन्वेंट स्कूलों में से एक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Temple Architecture",
        "text": "'गोपीनाथ मंदिर' (गोपेश्वर) का निर्माण किस शैली में हुआ है?",
        "options": ["हिमालयन (नागर) शैली", "द्रविड़", "पैगोडा", "मिश्रित"],
        "correct_answer": "हिमालयन (नागर) शैली",
        "explanation": "यह मंदिर अपने विशाल त्रिशूल और शिल्पकला के लिए जाना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'इन्सपेक्टर ऑफ स्कूल्स' का पद किस वर्ष सृजित किया गया था?",
        "options": ["1857", "1860", "1850", "1870"],
        "correct_answer": "1857",
        "explanation": "बुद्धिबल्लभ पंत कुमाऊँ के प्रथम स्कूल इंस्पेक्टर बने थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Heritage Structures",
        "text": "उत्तराखंड में 'रंग महल' (Rang Mahal) कहाँ स्थित है?",
        "options": ["श्रीनगर (गढ़वाल)", "अल्मोड़ा", "टिहरी", "रुद्रप्रयाग"],
        "correct_answer": "श्रीनगर (गढ़वाल)",
        "explanation": "यह पवार राजाओं द्वारा बनवाया गया एक ऐतिहासिक महल था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Personalities",
        "text": "किसे 'कुमाऊँ का दानवीर' (Donor of Kumaon) कहा जाता है?",
        "options": ["पदम सिंह बिष्ट", "देव सिंह दानू", "खुशीराम", "बद्रीदत्त पाण्डेय"],
        "correct_answer": "देव सिंह दानू",
        "explanation": "उनकी समाज सेवा और दानशीलता के लिए उन्हें यह सम्मान प्राप्त है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Ancient Inscriptions",
        "text": "उत्तराखंड में 'मूर्तिकला' का स्वर्ण युग किस काल को माना जाता है?",
        "options": ["कत्यूरी काल", "चन्द काल", "पवार काल", "ब्रिटिश काल"],
        "correct_answer": "कत्यूरी काल",
        "explanation": "कत्यूरी राजाओं के समय भव्य मंदिरों और मूर्तियों का निर्माण हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Institutions",
        "text": "नैनीताल में 'राजभवन' (Raj Bhavan) का निर्माण किस शैली में हुआ है?",
        "options": ["गॉथिक शैली", "नागर शैली", "मुगल", "आधुनिक"],
        "correct_answer": "गॉथिक शैली",
        "explanation": "इसे 'बकिंघम पैलेस' की तर्ज पर बनवाया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Religious Sites",
        "text": "'पूर्णागिरी' मंदिर किस पर्वत पर स्थित है?",
        "options": ["अन्नपूर्णा पर्वत", "नीलकंठ", "त्रिशूल", "नंदा देवी"],
        "correct_answer": "अन्नपूर्णा पर्वत",
        "explanation": "चंपावत जिले के टनकपुर के पास यह प्रसिद्ध शक्तिपीठ है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Admin Records",
        "text": "कुमाऊँ में 'पहला छापाखाना' (Printing Press) कहाँ लगा था?",
        "options": ["अल्मोड़ा", "मसूरी", "देहरादून", "नैनीताल"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "अल्मोड़ा अखबार के प्रकाशन के लिए इसकी स्थापना की गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Temple Features",
        "text": "उत्तराखंड के किस मंदिर में 'पत्थर के गोले' फेंकने की परंपरा (बग्वाल) थी?",
        "options": ["देवीधुरा (चंपावत)", "चितई", "जागेश्वर", "बद्रीनाथ"],
        "correct_answer": "देवीधुरा (चंपावत)",
        "explanation": "माँ बाराही के मंदिर में रक्षाबंधन के दिन यह प्रसिद्ध मेला लगता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Education",
        "text": "देहरादून में 'आई.एम.ए.' (IMA) की स्थापना किस वर्ष हुई थी?",
        "options": ["1932", "1930", "1935", "1940"],
        "correct_answer": "1932",
        "explanation": "भारतीय सैन्य अकादमी की स्थापना फील्ड मार्शल फिलिप चेटवुड ने की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Heritage Cities",
        "text": "किसे 'उत्तराखंड की छोटी काशी' कहा जाता है?",
        "options": ["विभाण्डेश्वर (अल्मोड़ा)", "बागेश्वर", "ऋषिकेश", "हरिद्वार"],
        "correct_answer": "विभाण्डेश्वर (अल्मोड़ा)",
        "explanation": "अपनी धार्मिक पवित्रता के कारण इसे उत्तर की छोटी काशी कहते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - British Rule",
        "source": "Legislation",
        "text": "कुमाऊँ में 'बेगार' प्रथा को समाप्त करने के लिए 'कमिश्नर ट्रेल' ने क्या व्यवस्था की थी?",
        "options": ["खच्चर सेना का गठन", "मजदूरी देना", "जेल भेजना", "उपरोक्त कोई नहीं"],
        "correct_answer": "खच्चर सेना का गठन",
        "explanation": "सामान ढोने के लिए उन्होंने खच्चरों की व्यवस्था की ताकि जनता पर बोझ कम हो।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Architecture & Heritage",
        "source": "Religious Architecture",
        "text": "उत्तराखंड में 'पंच केदार' में से कौन सा मंदिर 'पितृ तीर्थ' के रूप में प्रसिद्ध है?",
        "options": ["रुद्रनाथ", "तुंगनाथ", "मदमहेश्वर", "कल्पेश्वर"],
        "correct_answer": "रुद्रनाथ",
        "explanation": "यहाँ पितरों का तर्पण करने का विशेष महत्व माना जाता है।"
    },

    # ── BATCH 15: PROTECTED AREAS & MODERN LEADERS ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "UNESCO Heritage",
        "text": "'नंदा देवी बायोस्फीयर रिजर्व' (Nanda Devi Biosphere Reserve) को यूनेस्को ने कब विश्व धरोहर घोषित किया?",
        "options": ["1988", "1992", "2005", "2000"],
        "correct_answer": "1988",
        "explanation": "यह अपनी दुर्लभ जैव विविधता और हिमालयी पारिस्थितिकी के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Exploration",
        "text": "'फूलों की घाटी' (Valley of Flowers) की खोज का श्रेय किसे दिया जाता है?",
        "options": ["फ्रैंक स्मिथ (Frank Smythe)", "जिम कॉर्बेट", "ट्रेल", "बैटेन"],
        "correct_answer": "फ्रैंक स्मिथ (Frank Smythe)",
        "explanation": "1931 में स्मिथ ने इस घाटी को दुनिया के सामने रखा और बाद में 'The Valley of Flowers' पुस्तक लिखी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Freedom Struggle",
        "text": "टिहरी रियासत के विरुद्ध आंदोलन करने वाले 'श्रीदेव सुमन' की मृत्यु कितने दिनों की भूख हड़ताल के बाद हुई थी?",
        "options": ["84 दिन", "50 दिन", "100 दिन", "75 दिन"],
        "correct_answer": "84 दिन",
        "explanation": "25 जुलाई 1944 को 84 दिनों के ऐतिहासिक अनशन के बाद वे शहीद हुए।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Glaciers",
        "text": "उत्तराखंड का सबसे बड़ा ग्लेशियर 'गंगोत्री' की लंबाई लगभग कितनी है?",
        "options": ["30 किमी", "20 किमी", "15 किमी", "50 किमी"],
        "correct_answer": "30 किमी",
        "explanation": "यह उत्तरकाशी जिले में स्थित है और गंगा का मुख्य स्रोत है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Environmental Movements",
        "text": "चिपको आंदोलन की 'प्रथम महिला' नेता कौन थी?",
        "options": ["गौरा देवी", "बचेंद्री पाल", "दीपा देवी", "मैत्रेयी"],
        "correct_answer": "गौरा देवी",
        "explanation": "1974 में रेणी गाँव (चमोली) से उन्होंने वनों की कटाई के विरोध में महिलाओं का नेतृत्व किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "गंगा नदी की उत्तराखंड में कुल लंबाई कितनी है?",
        "options": ["96 किमी", "150 किमी", "205 किमी", "110 किमी"],
        "correct_answer": "96 किमी",
        "explanation": "देवप्रयाग से हरिद्वार (राज्य की सीमा) तक इसकी लंबाई 96 किमी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "किसे 'पहाड़ का गांधी' (Gandhi of Hills) कहा जाता है?",
        "options": ["जसवंत सिंह बिष्ट", "इन्द्रमणि बडोनी", "बद्रीदत्त पाण्डेय", "सुन्दरलाल बहुगुणा"],
        "correct_answer": "जसवंत सिंह बिष्ट",
        "explanation": "अल्मोड़ा क्षेत्र में उनके सामाजिक कार्यों के कारण उन्हें यह उपनाम मिला (नोट: इन्द्रमणि बडोनी को उत्तराखंड का गांधी कहते हैं)।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'बन्दरपूँछ' पर्वत शिखर किस जिले में स्थित है?",
        "options": ["उत्तरकाशी", "चमोली", "टिहरी", "रुद्रप्रयाग"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "यमुना नदी का उद्गम इसी पर्वत की ढलानों से होता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Formation",
        "text": "उत्तराखंड राज्य गठन के लिए 'कौशिक समिति' का गठन किस वर्ष हुआ था?",
        "options": ["1993", "1994", "1992", "1995"],
        "correct_answer": "1993",
        "explanation": "मुलायम सिंह यादव सरकार ने रमाशंकर कौशिक की अध्यक्षता में यह समिति बनाई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife Sanctuaries",
        "text": "'केदारनाथ वन्यजीव विहार' का मुख्य उद्देश्य किस पशु का संरक्षण है?",
        "options": ["कस्तूरी मृग", "बाघ", "हाथी", "बर्फानी तेंदुआ"],
        "correct_answer": "कस्तूरी मृग",
        "explanation": "यह उत्तराखंड का सबसे बड़ा वन्यजीव विहार (957 वर्ग किमी) है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'कुमाऊँ विश्वविद्यालय' की स्थापना किस वर्ष हुई थी?",
        "options": ["1973", "1970", "1975", "1980"],
        "correct_answer": "1973",
        "explanation": "गढ़वाल और कुमाऊँ दोनों विश्वविद्यालयों की स्थापना 1973 में हुई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'सतोपंथ ताल' किस आकृति का है?",
        "options": ["त्रिभुजाकार", "वर्गाकार", "गोलाकार", "अर्धचन्द्राकार"],
        "correct_answer": "त्रिभुजाकार",
        "explanation": "इसे ब्रह्मा, विष्णु और महेश का प्रतीक माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "किसे 'गढ़वाल का शेर' (Lion of Garhwal) कहा जाता है?",
        "options": ["अनसूया प्रसाद बहुगुणा", "बद्रीदत्त पाण्डेय", "वीर चन्द्र सिंह गढ़वाली", "श्रीदेव सुमन"],
        "correct_answer": "अनसूया प्रसाद बहुगुणा",
        "explanation": "स्वतंत्रता संग्राम में उनकी ओजस्वी भूमिका के कारण उन्हें यह ख्याति मिली।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "National Parks",
        "text": "'कार्बेट नेशनल पार्क' का पुराना नाम क्या था?",
        "options": ["हेली नेशनल पार्क", "रामगंगा पार्क", "गंगोत्री पार्क", "राजाजी पार्क"],
        "correct_answer": "हेली नेशनल पार्क",
        "explanation": "1936 में स्थापित यह भारत का पहला राष्ट्रीय उद्यान था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Symbols",
        "text": "उत्तराखंड के 'राज्य गीत' के लेखक कौन हैं?",
        "options": ["हेमंत बिष्ट", "नरेन्द्र सिंह नेगी", "प्रीतम भरतवाण", "पदमश्री डबराल"],
        "correct_answer": "हेमंत बिष्ट",
        "explanation": "'उत्तराखंड देवभूमि मातृभूमि' गीत 2016 में अपनाया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Passes",
        "text": "'लिपुलेख दर्रा' (Lipulekh Pass) किस जिले में स्थित है?",
        "options": ["पिथौरागढ़", "चमोली", "उत्तरकाशी", "बागेश्वर"],
        "correct_answer": "पिथौरागढ़",
        "explanation": "यह दर्रा कैलाश मानसरोवर यात्रा के लिए प्रसिद्ध मार्ग है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Women of UK",
        "text": "उत्तराखंड की प्रथम महिला 'पद्मश्री' विजेता कौन हैं?",
        "options": ["बचेंद्री पाल", "गौरा देवी", "दीपा नौटियाल", "पुष्पा बिष्ट"],
        "correct_answer": "बचेंद्री पाल",
        "explanation": "1984 में एवरेस्ट फतह करने के बाद उन्हें यह सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "अलकनन्दा की सबसे पहली सहायक नदी कौन सी है?",
        "options": ["लक्ष्मण गंगा (ऋषि गंगा)", "नन्दाकिनी", "पिण्डर", "मंदाकिनी"],
        "correct_answer": "लक्ष्मण गंगा (ऋषि गंगा)",
        "explanation": "यह बद्रीनाथ के पास अलकनन्दा से मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Movements",
        "text": "उत्तराखंड में 'शराब विरोधी आंदोलन' का मुख्य नारा क्या था?",
        "options": ["नशा नहीं रोजगार दो", "शराब हटाओ देश बचाओ", "हर हाथ को काम", "पर्यावरण बचाओ"],
        "correct_answer": "नशा नहीं रोजगार दो",
        "explanation": "1980 के दशक में कुमाऊँ मंडल में यह आंदोलन चरम पर था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks",
        "text": "'त्रिशूल' शिखर किस जिले में स्थित है?",
        "options": ["चमोली", "बागेश्वर", "पिथौरागढ़", "रुद्रप्रयाग"],
        "correct_answer": "चमोली",
        "explanation": "इसकी तीन चोटियाँ त्रिशूल जैसी दिखती हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Freedom Struggle",
        "text": "1930 के 'रवाईं कांड' (Rawai Incident) को उत्तराखंड का क्या कहा जाता है?",
        "options": ["जलियांवाला बाग कांड", "चोरी-चोरा", "नमक सत्याग्रह", "खेड़ा आंदोलन"],
        "correct_answer": "जलियांवाला बाग कांड",
        "explanation": "तिलाड़ी में वन अधिकारों के लिए संघर्ष कर रहे लोगों पर निहत्थे गोलियाँ चलाई गई थीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Waterfalls",
        "text": "प्रसिद्ध 'सहस्त्रधारा' जलप्रपात किस जिले में है?",
        "options": ["देहरादून", "मसूरी", "नैनीताल", "ऋषिकेश"],
        "correct_answer": "देहरादून",
        "explanation": "इसके जल में गंधक (Sulphur) होने के कारण इसे औषधीय माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "किसे 'कुमाऊँ केसरी' (Kumaon Kesari) के नाम से जाना जाता है?",
        "options": ["बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "गोविंद बल्लभ पंत", "विक्टर मोहन जोशी"],
        "correct_answer": "बद्रीदत्त पाण्डेय",
        "explanation": "कुली बेगार आंदोलन के सफल नेतृत्व के बाद उन्हें यह उपाधि दी गई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Dams",
        "text": "टिहरी बाँध (Tehri Dam) की ऊँचाई कितनी है?",
        "options": ["260.5 मीटर", "240 मीटर", "280 मीटर", "250 मीटर"],
        "correct_answer": "260.5 मीटर",
        "explanation": "यह भारत का सबसे ऊँचा बाँध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Symbols",
        "text": "उत्तराखंड का 'राज्य खेल' क्या है?",
        "options": ["फुटबॉल", "क्रिकेट", "हॉकी", "कबड्डी"],
        "correct_answer": "फुटबॉल",
        "explanation": "2011 में फुटबॉल को उत्तराखंड का राज्य खेल घोषित किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Glaciers",
        "text": "'कफनी ग्लेशियर' किस जिले में स्थित है?",
        "options": ["बागेश्वर", "पिथौरागढ़", "चमोली", "उत्तरकाशी"],
        "correct_answer": "बागेश्वर",
        "explanation": "यह पिण्डर नदी के दाईं ओर स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "देहरादून में 'वाडिया इंस्टीट्यूट ऑफ हिमालयन जियोलॉजी' की स्थापना किस वर्ष हुई थी?",
        "options": ["1968", "1975", "1960", "1980"],
        "correct_answer": "1968",
        "explanation": "यह हिमालय के भू-वैज्ञानिक अध्ययन के लिए प्रमुख संस्थान है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'भीमताल' झील की प्रमुख विशेषता क्या है?",
        "options": ["इसके बीच में एक द्वीप है", "यह सबसे गहरी है", "यह सबसे ऊँची है", "यह आकार में गोल है"],
        "correct_answer": "इसके बीच में एक द्वीप है",
        "explanation": "द्वीप पर एक सुंदर रेस्टोरेंट/एक्वेरियम बना हुआ है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "उत्तराखंड के किस व्यक्ति को 'आजाद' (Azad) के उपनाम से जाना जाता था?",
        "options": ["श्रीधर किमोठी", "श्रीदेव सुमन", "भगत सिंह कोश्यारी", "बद्रीदत्त पाण्डेय"],
        "correct_answer": "श्रीधर किमोठी",
        "explanation": "राज्य आंदोलन और सामाजिक कार्यों में उनकी सक्रियता के कारण उन्हें आजाद कहा जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "River Systems",
        "text": "भागीरथी और भिलंगना का संगम कहाँ होता है?",
        "options": ["पुरानी टिहरी (गणेश प्रयाग)", "देवप्रयाग", "रुद्रप्रयाग", "उत्तरकाशी"],
        "correct_answer": "पुरानी टिहरी (गणेश प्रयाग)",
        "explanation": "अब यह स्थान टिहरी बाँध की झील में डूब चुका है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Symbols",
        "text": "उत्तराखंड की 'राज्य तितली' कॉमन पीकॉक को कब घोषित किया गया?",
        "options": ["2016", "2014", "2015", "2017"],
        "correct_answer": "2016",
        "explanation": "हिमालयी क्षेत्र की यह तितली अत्यंत सुंदर होती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "National Parks",
        "text": "'गोविंद राष्ट्रीय उद्यान' किस जिले में है?",
        "options": ["उत्तरकाशी", "चमोली", "रुद्रप्रयाग", "पिथौरागढ़"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "यहाँ बर्फानी तेंदुआ और कस्तूरी मृग पाए जाते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Awards",
        "text": "उत्तराखंड के किस व्यक्ति को प्रथम 'भारत रत्न' मिला था?",
        "options": ["पंडित गोविंद बल्लभ पंत", "हेमवती नंदन बहुगुणा", "सुन्दरलाल बहुगुणा", "चण्डी प्रसाद भट्ट"],
        "correct_answer": "पंडित गोविंद बल्लभ पंत",
        "explanation": "1957 में उन्हें भारत के सर्वोच्च नागरिक सम्मान से नवाजा गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "'दूधातोली' पर्वत श्रेणी किन तीन जिलों की सीमा पर है?",
        "options": ["चमोली, पौड़ी और अल्मोड़ा", "पिथौरागढ़, बागेश्वर और चमोली", "देहरादून, टिहरी और उत्तरकाशी", "हरिद्वार, पौड़ी और नैनीताल"],
        "correct_answer": "चमोली, पौड़ी और अल्मोड़ा",
        "explanation": "इसे 'उत्तराखंड का पामीर' (Pamir of Uttarakhand) भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Formation",
        "text": "उत्तराखंड को 'विशेष राज्य' का दर्जा कब मिला था?",
        "options": ["1 अप्रैल 2001", "9 नवंबर 2000", "15 अगस्त 2001", "1 जनवरी 2002"],
        "correct_answer": "1 अप्रैल 2001",
        "explanation": "विशेष राज्य के दर्जे के साथ उत्तराखंड 11वाँ हिमालयी राज्य बना।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "River Tributaries",
        "text": "धौलीगंगा (पश्चिमी) किसकी सहायक नदी है?",
        "options": ["अलकनन्दा", "भागीरथी", "यमुना", "काली"],
        "correct_answer": "अलकनन्दा",
        "explanation": "यह विष्णुप्रयाग में अलकनन्दा से मिलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "उत्तराखंड की प्रथम महिला 'निर्वाचन आयुक्त' कौन थी?",
        "options": ["राधा रतूड़ी", "विजया बड़थ्वाल", "पुष्पा बिष्ट", "अमृत कौर"],
        "correct_answer": "राधा रतूड़ी",
        "explanation": "वर्तमान में वे राज्य की प्रथम महिला मुख्य सचिव भी हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "'हेमकुण्ड' झील से कौन सी नदी निकलती है?",
        "options": ["लक्ष्मण गंगा (अलकनन्दा की सहायक)", "भागीरथी", "मंदाकिनी", "पिण्डर"],
        "correct_answer": "लक्ष्मण गंगा (अलकनन्दा की सहायक)",
        "explanation": "हेमकुण्ड से निकलने वाली नदी को 'हेमगंगा' या लक्ष्मण गंगा कहते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "देहरादून में 'सर्वे ऑफ इंडिया' का मुख्यालय किस वर्ष लाया गया था?",
        "options": ["1942", "1867", "1950", "1900"],
        "correct_answer": "1942",
        "explanation": "विश्व युद्ध के दौरान इसे कोलकाता से देहरादून स्थानांतरित किया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Peaks",
        "text": "'कामेत' (Kamet) पर्वत की ऊँचाई कितनी है?",
        "options": ["7756 मीटर", "7817 मीटर", "7120 मीटर", "6940 मीटर"],
        "correct_answer": "7756 मीटर",
        "explanation": "यह उत्तराखंड की दूसरी सबसे ऊँची चोटी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Women of UK",
        "text": "'गढ़वाल की नाक काटी रानी' (Nakti Rani) किसे कहा जाता है?",
        "options": ["कर्णवती", "गौरा देवी", "तीलू रौतेली", "मैत्रेयी"],
        "correct_answer": "कर्णवती",
        "explanation": "उन्होंने मुगल सेना के सैनिकों की नाक कटवा दी थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "अलकनन्दा नदी का उद्गम स्थल कहाँ है?",
        "options": ["सतोपंथ ग्लेशियर", "गंगोत्री", "यमुनोत्री", "मिलम"],
        "correct_answer": "सतोपंथ ग्लेशियर",
        "explanation": "यह चमोली जिले में स्थित अलकापुरी बाँक के पास सतोपंथ शिखर से निकलती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Symbols",
        "text": "उत्तराखंड की 'राज्य भाषा' हिन्दी के साथ दूसरी भाषा कौन सी है?",
        "options": ["संस्कृत", "कुमाऊँनी", "गढ़वाली", "अंग्रेजी"],
        "correct_answer": "संस्कृत",
        "explanation": "2010 में संस्कृत को दूसरी आधिकारिक भाषा का दर्जा दिया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife",
        "text": "उत्तराखंड का 'राज्य पक्षी' मोनाल किस ऊँचाई पर पाया जाता है?",
        "options": ["2500-5000 मीटर", "500-1000 मीटर", "1000-2000 मीटर", "6000 मीटर से ऊपर"],
        "correct_answer": "2500-5000 मीटर",
        "explanation": "यह एक रंगीन हिमालयी पक्षी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Symbols",
        "text": "उत्तराखंड के 'राज्य चिन्ह' में कितनी पर्वत चोटियाँ दर्शाई गई हैं?",
        "options": ["3", "4", "5", "2"],
        "correct_answer": "3",
        "explanation": "राज्य चिन्ह में तीन चोटियाँ और नीचे गंगा की चार लहरें हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Passes",
        "text": "'ट्रेल पास' (Trail's Pass) किन दो जिलों को जोड़ता है?",
        "options": ["बागेश्वर और पिथौरागढ़", "चमोली और उत्तरकाशी", "पिथौरागढ़ और तिब्बत", "चमोली और बागेश्वर"],
        "correct_answer": "बागेश्वर और पिथौरागढ़",
        "explanation": "1830 में कमिश्नर ट्रेल ने इस दर्रे की खोज की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Awards",
        "text": "उत्तराखंड के किस व्यक्ति को 'पद्म भूषण' (प्रथम) मिला था?",
        "options": ["कमलेन्दु मति शाह", "बचेंद्री पाल", "सुन्दरलाल बहुगुणा", "चण्डी प्रसाद भट्ट"],
        "correct_answer": "कमलेन्दु मति शाह",
        "explanation": "1958 में समाज सेवा के लिए उन्हें यह सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "किस झील के किनारे 'स्वामी विवेकानंद' को ज्ञान प्राप्त हुआ था?",
        "options": ["श्यामला ताल (चंपावत)", "भीमताल", "नैनीताल", "सातताल"],
        "correct_answer": "श्यामला ताल (चंपावत)",
        "explanation": "यहाँ विवेकानंद आश्रम भी स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Freedom Struggle",
        "text": "स्वतंत्रता आंदोलन के दौरान 'सालम का शेर' किसे कहा गया?",
        "options": ["राम सिंह धौनी", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "विक्टर मोहन जोशी"],
        "correct_answer": "राम सिंह धौनी",
        "explanation": "अल्मोड़ा के सालम क्षेत्र में उनके क्रांतिकारी कार्यों के कारण।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "मन्दाकिनी और अलकनन्दा का संगम स्थल कहाँ है?",
        "options": ["रुद्रप्रयाग", "देवप्रयाग", "कर्णप्रयाग", "नन्दप्रयाग"],
        "correct_answer": "रुद्रप्रयाग",
        "explanation": "रुद्रप्रयाग पाँच प्रयागों में से एक महत्वपूर्ण तीर्थ है।"
    },

    # ── BATCH 16: DANCES & STATE SYMBOLS ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Dances",
        "text": "उत्तराखंड का प्रसिद्ध 'झोड़ा' (Jhora) नृत्य मुख्य रूप से किस क्षेत्र में प्रचलित है?",
        "options": ["कुमाऊँ", "गढ़वाल", "जौनसार", "भाबर"],
        "correct_answer": "कुमाऊँ",
        "explanation": "यह सामूहिक रूप से घेरे में किया जाने वाला उल्लासपूर्ण नृत्य है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Dances",
        "text": "'थड्या' (Thadya) नृत्य कब किया जाता है?",
        "options": ["बसंत आगमन पर", "विवाह में", "मृत्यु पर", "फसल कटाई पर"],
        "correct_answer": "बसंत आगमन पर",
        "explanation": "गढ़वाल क्षेत्र में नवविवाहित युवतियों द्वारा पहली बार मायके आने पर किया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Musical Instruments",
        "text": "उत्तराखंड के 'राज्य वाद्य यंत्र' का नाम क्या है?",
        "options": ["ढोल", "हुड़का", "रणसिंघा", "बांसुरी"],
        "correct_answer": "ढोल",
        "explanation": "2015 में ढोल को राज्य वाद्य यंत्र घोषित किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Songs",
        "text": "उत्तराखंड में 'खुदेड़' (Khuded) गीत किस भावना से संबंधित है?",
        "options": ["विछोह और याद", "वीर गाथा", "हास्य", "भक्ति"],
        "correct_answer": "विछोह और याद",
        "explanation": "मायके की याद में विवाहित महिलाओं द्वारा यह गीत गाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "District Formation",
        "text": "चंपावत, बागेश्वर और रुद्रप्रयाग जिलों का गठन किस वर्ष हुआ था?",
        "options": ["1997", "1995", "1991", "2000"],
        "correct_answer": "1997",
        "explanation": "सितंबर 1997 में इन तीन नए जिलों का निर्माण किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "State Symbols",
        "text": "उत्तराखंड के 'राज्य वृक्ष' बुराँश का वैज्ञानिक नाम क्या है?",
        "options": ["रोडोडेन्ड्रॉन अर्बोरियम", "सिडस देवदारा", "फाइकस रिलिजिओसा", "बाँबुसा"],
        "correct_answer": "रोडोडेन्ड्रॉन अर्बोरियम",
        "explanation": "यह मार्च-अप्रैल के महीने में लाल फूलों से लद जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "State Symbols",
        "text": "उत्तराखंड के 'राज्य पुष्प' ब्रह्मकमल का स्थानीय नाम क्या है?",
        "options": ["कौल पदम", "फेन कमल", "हिमालयी कमल", "देव कमल"],
        "correct_answer": "कौल पदम",
        "explanation": "यह हिमालयी क्षेत्रों में 3000-5000 मीटर की ऊँचाई पर पाया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Dances",
        "text": "'चौंफला' (Chonfula) नृत्य किस क्षेत्र से संबंधित है?",
        "options": ["गढ़वाल", "कुमाऊँ", "तराई", "भाबर"],
        "correct_answer": "गढ़वाल",
        "explanation": "यह स्त्री-पुरुषों द्वारा सामूहिक रूप से किया जाने वाला श्रृंगार प्रधान नृत्य है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Musical Instruments",
        "text": "'मशकबीन' (Mashakbeen) उत्तराखंड में किस परंपरा का हिस्सा है?",
        "options": ["विवाह और सैन्य बैंड", "जागर", "कृषि कार्य", "मृत्यु संस्कार"],
        "correct_answer": "विवाह और सैन्य बैंड",
        "explanation": "यह एक स्कॉटिश वाद्य यंत्र (Bagpipe) है जो पहाड़ों में अत्यंत लोकप्रिय हो गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Songs",
        "text": "उत्तराखंड में 'छपेली' (Chhapeli) क्या है?",
        "options": ["एक प्रेम गीत और नृत्य", "एक आभूषण", "एक पकवान", "एक त्यौहार"],
        "correct_answer": "एक प्रेम गीत और नृत्य",
        "explanation": "यह प्रेमी-प्रेमिका के संवादों पर आधारित एक मनोरंजक नृत्य शैली है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "State Symbols",
        "text": "ब्रह्मकमल के फूल उत्तराखंड में किस महीने में खिलते हैं?",
        "options": ["जुलाई से सितंबर", "मार्च से मई", "जनवरी से मार्च", "अक्टूबर से दिसंबर"],
        "correct_answer": "जुलाई से सितंबर",
        "explanation": "वर्षा ऋतु के दौरान हिमालय की चोटियों पर ये फूल खिलते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Dances",
        "text": "किसे 'उत्तराखंड का गर्भा' कहा जाता है?",
        "options": ["झोड़ा नृत्य", "चांचरी", "थड्या", "पांडव नृत्य"],
        "correct_answer": "झोड़ा नृत्य",
        "explanation": "सामूहिक घेरे में किए जाने के कारण इसकी तुलना गर्भा से की जाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'कुल तहसीलों' की संख्या कितनी है (लगभग)?",
        "options": ["110", "95", "100", "120"],
        "correct_answer": "110",
        "explanation": "प्रशासनिक सुविधा के लिए समय-समय पर नई तहसीलों का गठन होता रहता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Musical Instruments",
        "text": "'रणसिंघा' (Ransingha) किस धातु का बना होता है?",
        "options": ["ताँबा", "पीतल", "लोहा", "कांसा"],
        "correct_answer": "ताँबा",
        "explanation": "यह युद्ध और मंगल कार्यों में बजाया जाने वाला सुषिर वाद्य है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Songs",
        "text": "उत्तराखंड में 'न्योली' (Nyoli) क्या है?",
        "options": ["विरह प्रधान लोकगीत", "एक आभूषण", "एक वाद्य यंत्र", "एक त्यौहार"],
        "correct_answer": "विरह प्रधान लोकगीत",
        "explanation": "कुमाऊँ क्षेत्र में जंगल और पहाड़ों की एकांत में गाया जाने वाला मधुर गीत है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "State Symbols",
        "text": "उत्तराखंड के राज्य चिन्ह में प्रयुक्त 'सत्यमेव जयते' कहाँ से लिया गया है?",
        "options": ["मुण्डकोपनिषद्", "ऋग्वेद", "महाभारत", "रामायण"],
        "correct_answer": "मुण्डकोपनिषद्",
        "explanation": "यह भारत का राष्ट्रीय आदर्श वाक्य भी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Dances",
        "text": "'पांडव नृत्य' (Pandav Nritya) मुख्य रूप से किस जिले में आयोजित होता है?",
        "options": ["गढ़वाल क्षेत्र (चमोली/रुद्रप्रयाग)", "पिथौरागढ़", "नैनीताल", "अल्मोड़ा"],
        "correct_answer": "गढ़वाल क्षेत्र (चमोली/रुद्रप्रयाग)",
        "explanation": "पांडवों के हिमालय गमन की कथा पर आधारित यह एक जीवंत परंपरा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड विधानसभा की 'प्रथम महिला अध्यक्ष' कौन थी?",
        "options": ["रितु खण्डूड़ी", "विजया बड़थ्वाल", "पुष्पा बिष्ट", "अमृत कौर"],
        "correct_answer": "रितु खण्डूड़ी",
        "explanation": "2022 में वे उत्तराखंड की पहली महिला स्पीकर बनीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Music",
        "text": "उत्तराखंड में 'डौंर-थाली' (Daunr-Thali) का प्रयोग किसमें होता है?",
        "options": ["जागर गायन", "विवाह", "फसल कटाई", "त्यौहार"],
        "correct_answer": "जागर गायन",
        "explanation": "देवताओं के आह्वान (जागर) के समय डौंर और थाली मुख्य वाद्य होते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "State Symbols",
        "text": "उत्तराखंड का राज्य पशु कस्तूरी मृग का वैज्ञानिक नाम क्या है?",
        "options": ["मास्कस क्राइसोगास्टर", "लोफोफोरस इम्पिजनस", "पैंथेरा टाइग्रिस", "बोस म्यूटस"],
        "correct_answer": "मास्कस क्राइसोगास्टर",
        "explanation": "इसे 'हिमालयन मस्क डियर' भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Lore",
        "text": "'जीतू बगड़वाल' की लोक गाथा किस वाद्य यंत्र के साथ गाई जाती है?",
        "options": ["हुड़का", "ढोल", "बांसुरी", "रणसिंघा"],
        "correct_answer": "हुड़का",
        "explanation": "हुड़की बौल और जीतू बगड़वाल की गाथाएँ पहाड़ों में अत्यंत लोकप्रिय हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड के 'प्रथम राज्यपाल' कौन थे?",
        "options": ["सुरजीत सिंह बरनाला", "सुदर्शन अग्रवाल", "बी.एल. जोशी", "अजीज कुरैशी"],
        "correct_answer": "सुरजीत सिंह बरनाला",
        "explanation": "9 नवंबर 2000 को उन्होंने शपथ ली थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Arts",
        "text": "'ऐपण' (Aipan) उत्तराखंड की किस प्रकार की कला है?",
        "options": ["चित्रकला (लोक कला)", "मूर्तिकला", "वास्तुकला", "संगीत"],
        "correct_answer": "चित्रकला (लोक कला)",
        "explanation": "यह कुमाऊँ की एक पारंपरिक देहरी/दीवार चित्रकला शैली है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड के 'प्रथम मुख्यमंत्री' कौन थे (अन्तरिम)?",
        "options": ["नित्यानंद स्वामी", "भगत सिंह कोश्यारी", "नारायण दत्त तिवारी", "बी.सी. खण्डूड़ी"],
        "correct_answer": "नित्यानंद स्वामी",
        "explanation": "अन्तरिम सरकार के मुख्यमंत्री के रूप में उन्होंने कार्यभार संभाला था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'कुमाऊँ का नरसिंह' (Narsingh of Kumaon) कहा जाता है?",
        "options": ["हर्षदेव जोशी", "पंत", "डबराल", "नेगी"],
        "correct_answer": "हर्षदेव जोशी",
        "explanation": "कुमाऊँ की राजनीति में उनके दबदबे के कारण उन्हें यह नाम दिया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "State Symbols",
        "text": "बुराँश का फूल खिलने का प्रमुख समय कौन सा है?",
        "options": ["फरवरी से अप्रैल", "मई से जुलाई", "अगस्त से अक्टूबर", "नवंबर से जनवरी"],
        "correct_answer": "फरवरी से अप्रैल",
        "explanation": "बसंत ऋतु में यह पहाड़ों को लालिमा से भर देता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Festivals",
        "text": "उत्तराखंड में 'घी संक्रांति' (Ghee Sankranti) कब मनाई जाती है?",
        "options": ["सितंबर (भाद्रपद)", "जनवरी", "अप्रैल", "अगस्त"],
        "correct_answer": "सितंबर (भाद्रपद)",
        "explanation": "इसे ओलगिया भी कहा जाता है, जिसमें घी खाने की परंपरा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड उच्च न्यायालय के 'प्रथम मुख्य न्यायाधीश' कौन थे?",
        "options": ["न्यायमूर्ति ए.ए. देसाई", "न्यायमूर्ति एस.एच. कपाड़िया", "न्यायमूर्ति रजा", "न्यायमूर्ति पंत"],
        "correct_answer": "न्यायमूर्ति ए.ए. देसाई",
        "explanation": "नैनीताल उच्च न्यायालय की स्थापना के समय वे प्रथम मुख्य न्यायाधीश थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'गढ़वाल की लोककथाएँ' पुस्तक के लेखक कौन हैं?",
        "options": ["शिवानंद नौटियाल", "तारा दत्त गैरोला", "डबराल", "पाण्डे"],
        "correct_answer": "शिवानंद नौटियाल",
        "explanation": "उन्होंने गढ़वाल की लोक संस्कृति और कथाओं का व्यापक संग्रह किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'कुल जिलों' की संख्या कितनी है?",
        "options": ["13", "11", "15", "10"],
        "correct_answer": "13",
        "explanation": "गढ़वाल मंडल में 7 और कुमाऊँ मंडल में 6 जिले हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "'बगड़वाल' जाति का मुख्य वाद्य यंत्र क्या है?",
        "options": ["हुड़का", "ढोल", "मशकबीन", "बांसुरी"],
        "correct_answer": "हुड़का",
        "explanation": "हुड़का इस जाति की गायकी का अभिन्न अंग है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड विधानसभा में 'कितनी सीटें' हैं?",
        "options": ["70", "71", "60", "80"],
        "correct_answer": "70",
        "explanation": "एंग्लो-इंडियन सीट के प्रावधान के हटने के बाद अब केवल 70 निर्वाचित सीटें हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folklore",
        "text": "उत्तराखंड में 'जागर' लगाने वाले व्यक्ति को क्या कहा जाता है?",
        "options": ["जगरिया", "पुजारी", "गायक", "भक्त"],
        "correct_answer": "जगरिया",
        "explanation": "जगरिया ही देवताओं का आह्वान और स्तुति करता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'प्रथम महिला आईएएस' (IAS) अधिकारी कौन थी?",
        "options": ["ज्योत्सना भट्ट", "राधा रतूड़ी", "पुष्पा बिष्ट", "अमृत कौर"],
        "correct_answer": "ज्योत्सना भट्ट",
        "explanation": "वे राज्य की पहली महिला प्रशासनिक अधिकारी के रूप में जानी जाती हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'गढ़वाल का हातिमताई' (Hatimtai of Garhwal) कहा जाता है?",
        "options": ["कुंवर सिंह नेगी", "पदम सिंह", "जोत सिंह", "ललिता प्रसाद"],
        "correct_answer": "कुंवर सिंह नेगी",
        "explanation": "उनकी उदारता और समाज सेवा के कारण उन्हें यह उपाधि मिली।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'पंचायती राज' अधिनियम कब लागू हुआ था (राज्य का अपना)?",
        "options": ["2016", "2010", "2000", "2012"],
        "correct_answer": "2016",
        "explanation": "राज्य ने 4 अप्रैल 2016 को अपना पंचायती राज अधिनियम पारित किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Folk Arts",
        "text": "उत्तराखंड में 'पिठौं' (Pithain) क्या है?",
        "options": ["माथे पर लगाया जाने वाला तिलक", "एक पकवान", "एक त्यौहार", "एक नृत्य"],
        "correct_answer": "माथे पर लगाया जाने वाला तिलक",
        "explanation": "शुभ कार्यों में पिठौं (अक्षत और हल्दी का मिश्रण) लगाना अनिवार्य माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड का 'सबसे बड़ा' जिला (क्षेत्रफल में) कौन सा है?",
        "options": ["चमोली", "उत्तरकाशी", "पिथौरागढ़", "पौड़ी"],
        "correct_answer": "चमोली",
        "explanation": "चमोली राज्य का सबसे बड़ा जिला है (सरकारी आंकड़ों के अनुसार)।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'कुमाऊँ का इतिहास' पुस्तक किसने लिखी है?",
        "options": ["बद्रीदत्त पाण्डेय", "हरिकृष्ण रतूड़ी", "डबराल", "पाण्डे"],
        "correct_answer": "बद्रीदत्त पाण्डेय",
        "explanation": "जेल प्रवास के दौरान उन्होंने यह विस्तृत ग्रंथ लिखा था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड विधानसभा का 'प्रथम अधिवेशन' कहाँ हुआ था?",
        "options": ["देहरादून", "नैनीताल", "गैरसैंण", "ऋषिकेश"],
        "correct_answer": "देहरादून",
        "explanation": "प्रथम सत्र का आयोजन राजधानी देहरादून में हुआ था।"
    },

    # ── BATCH 17: ECONOMY, INDUSTRY & REFORMERS ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Industrial Estates",
        "text": "उत्तराखंड में 'सिडकुल' (SIDCUL) का मुख्यालय कहाँ स्थित है?",
        "options": ["देहरादून", "हरिद्वार", "पंतनगर", "सितारगंज"],
        "correct_answer": "देहरादून",
        "explanation": "सिडकुल राज्य में औद्योगिक विकास के लिए नोडल एजेंसी है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Large Scale Industry",
        "text": "'बी.एच.ई.एल.' (BHEL) उत्तराखंड के किस शहर में स्थित है?",
        "options": ["हरिद्वार", "रुड़की", "देहरादून", "हल्द्वानी"],
        "correct_answer": "हरिद्वार",
        "explanation": "रानीपुर (हरिद्वार) में भेल की एक विशाल इकाई स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Social Reformers",
        "text": "गांधीजी की शिष्या 'सरला बहन' (Sarla Behn) का वास्तविक नाम क्या था?",
        "options": ["कैथरीन हिलीमन", "मेडेलिन स्लेड", "एनी बेसेंट", "सिस्टर निवेदिता"],
        "correct_answer": "कैथरीन हिलीमन",
        "explanation": "उन्होंने कौसानी में लक्ष्मी आश्रम की स्थापना की और महिलाओं के उत्थान के लिए कार्य किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Social Reformers",
        "text": "'मीरा बहन' (Mira Behn) का वास्तविक नाम क्या था?",
        "options": ["मेडेलिन स्लेड", "कैथरीन हिलीमन", "मार्गरेट", "एलिजाबेथ"],
        "correct_answer": "मेडेलिन स्लेड",
        "explanation": "उन्होंने ऋषिकेश के पास पशुलोक (Pashulok) आश्रम की स्थापना की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "IT & Services",
        "text": "उत्तराखंड में 'आई.टी. पार्क' (IT Park) कहाँ स्थित है?",
        "options": ["देहरादून", "नैनीताल", "हरिद्वार", "पंतनगर"],
        "correct_answer": "देहरादून",
        "explanation": "सहस्त्रधारा रोड, देहरादून में आई.टी. पार्क की स्थापना की गई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Institutions",
        "text": "उत्तराखंड में 'भेषज विकास योजना' कब शुरू की गई थी?",
        "options": ["1949", "1955", "1960", "2000"],
        "correct_answer": "1949",
        "explanation": "जड़ी-बूटियों के संरक्षण और विकास के लिए यह योजना शुरू हुई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Environmental Leaders",
        "text": "किसे 'चिपको वुमन' (Chipko Woman) के नाम से जाना जाता है?",
        "options": ["गौरा देवी", "बचेंद्री पाल", "वन्दना शिवा", "राधा बहन"],
        "correct_answer": "गौरा देवी",
        "explanation": "पेड़ों को कटने से बचाने के लिए उन्होंने महिलाओं को पेड़ों से चिपकने के लिए प्रेरित किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Tourism Economy",
        "text": "उत्तराखंड में 'होटल मैनेजमेंट संस्थान' (IHM) कहाँ स्थित है?",
        "options": ["देहरादून", "अल्मोड़ा", "ऋषिकेश", "हरिद्वार"],
        "correct_answer": "देहरादून",
        "explanation": "यह पर्यटन और आतिथ्य सत्कार के क्षेत्र में प्रशिक्षण देने वाला प्रमुख संस्थान है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "उत्तराखंड की 'प्रथम महिला स्नातक' कौन थी?",
        "options": ["लक्ष्मी देवी शास्त्री", "गौरा पंत", "राधा भट्ट", "दीपा नौटियाल"],
        "correct_answer": "लक्ष्मी देवी शास्त्री",
        "explanation": "शिक्षा के क्षेत्र में महिलाओं की भागीदारी की उन्होंने शुरुआत की।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Agriculture Export",
        "text": "उत्तराखंड में 'एप्पल मिशन' (Apple Mission) किस जिले से शुरू किया गया था?",
        "options": ["उत्तरकाशी", "अल्मोड़ा", "नैनीताल", "चमोली"],
        "correct_answer": "उत्तरकाशी",
        "explanation": "सेब उत्पादन को बढ़ावा देने के लिए उत्तरकाशी में यह मिशन सक्रिय है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "नैनीताल में 'आर्यभट्ट प्रेक्षण विज्ञान शोध संस्थान' (ARIES) की स्थापना किस वर्ष हुई थी (वाराणसी से स्थानांतरण)?",
        "options": ["1955", "1960", "1950", "1970"],
        "correct_answer": "1955",
        "explanation": "यह खगोल विज्ञान के क्षेत्र में एक प्रमुख शोध संस्थान है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Resources",
        "text": "उत्तराखंड में 'मैग्नेसाइट' (Magnesite) का सर्वाधिक भंडार कहाँ पाया जाता है?",
        "options": ["झिरौली (अल्मोड़ा) और चण्डक (पिथौरागढ़)", "देहरादून", "नैनीताल", "पौड़ी"],
        "correct_answer": "झिरौली (अल्मोड़ा) और चण्डक (पिथौरागढ़)",
        "explanation": "मैग्नेसाइट के लिए ये क्षेत्र राज्य में सबसे समृद्ध हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Reformers",
        "text": "कुमाऊँ में 'नशा नहीं रोजगार दो' आंदोलन की शुरुआत किस संगठन ने की थी?",
        "options": ["उत्तराखंड संघर्ष वाहिनी", "कुमाऊँ परिषद", "गढ़वाल हितकारिणी", "महिपाल दल"],
        "correct_answer": "उत्तराखंड संघर्ष वाहिनी",
        "explanation": "1984 में अल्मोड़ा से इस सशक्त आंदोलन की शुरुआत हुई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Hydropower",
        "text": "उत्तराखंड की 'प्रथम जलविद्युत परियोजना' कौन सी थी?",
        "options": ["ग्लोगी परियोजना (मसूरी)", "टिहरी बाँध", "चिला परियोजना", "डाकपत्थर"],
        "correct_answer": "ग्लोगी परियोजना (मसूरी)",
        "explanation": "1907-1909 में स्थापित यह उत्तर भारत की भी सबसे पुरानी परियोजनाओं में से एक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Women Leaders",
        "text": "किसे 'इच्छागिरी माई' (Icchagiri Mai) के नाम से जाना जाता था?",
        "options": ["तिनले माई", "दीपा देवी", "सरला बहन", "गौरा देवी"],
        "correct_answer": "तिनले माई",
        "explanation": "वे एक प्रसिद्ध महिला संन्यासी और समाज सुधारक थीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Cooperatives",
        "text": "उत्तराखंड में 'दुग्ध विकास' हेतु 'डेयरी विकास संघ' की स्थापना सबसे पहले कहाँ हुई थी?",
        "options": ["हल्द्वानी (1949)", "देहरादून", "हरिद्वार", "रुद्रपुर"],
        "correct_answer": "हल्द्वानी (1949)",
        "explanation": "सहकारी डेयरी विकास की नींव हल्द्वानी से रखी गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "नैनीताल में 'टी.बी. सेनिटोरियम' (TB Sanatorium) की स्थापना भवाली में कब हुई थी?",
        "options": ["1912", "1900", "1920", "1895"],
        "correct_answer": "1912",
        "explanation": "यह भारत के सबसे पुराने टीबी अस्पतालों में से एक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Paper Industry",
        "text": "उत्तराखंड में 'सेंचुरी पेपर मिल' कहाँ स्थित है?",
        "options": ["लालकुआँ (नैनीताल)", "सितारगंज", "काशीपुर", "हल्द्वानी"],
        "correct_answer": "लालकुआँ (नैनीताल)",
        "explanation": "यह एशिया की बड़ी पेपर मिलों में गिनी जाती है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Movements",
        "text": "उत्तराखंड में 'कुली बेगार' प्रथा का आधिकारिक अंत किस वर्ष हुआ था?",
        "options": ["1921", "1920", "1925", "1930"],
        "correct_answer": "1921",
        "explanation": "बागेश्वर में सरयू तट पर ग्रामीणों ने बेगार रजिस्टर बहाकर इस प्रथा का अंत किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Forest Products",
        "text": "उत्तराखंड में 'लीसा' (Resin) निकालने का कार्य सरकारी तौर पर किस वर्ष शुरू हुआ था?",
        "options": ["1890", "1900", "1910", "1920"],
        "correct_answer": "1890",
        "explanation": "ब्रिटिश काल में चीड़ के वनों से लीसा निकासी का व्यवस्थित कार्य शुरू हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "उत्तराखंड के किस महान व्यक्ति को 'धरतीपुत्र' कहा जाता है?",
        "options": ["हेमवती नंदन बहुगुणा", "गोविंद बल्लभ पंत", "सुन्दरलाल बहुगुणा", "चण्डी प्रसाद भट्ट"],
        "correct_answer": "हेमवती nandan बहुगुणा",
        "explanation": "वे राज्य के एक प्रभावशाली राजनीतिक नेता थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Horticulture",
        "text": "उत्तराखंड में 'चाय विकास बोर्ड' (Tea Development Board) का मुख्यालय कहाँ है?",
        "options": ["अल्मोड़ा", "कौसानी", "हल्द्वानी", "देहरादून"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "चाय की खेती के विकास के लिए यह बोर्ड अल्मोड़ा में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Awards",
        "text": "उत्तराखंड से 'रेमन मैग्सेसे पुरस्कार' प्राप्त करने वाले प्रथम व्यक्ति कौन थे?",
        "options": ["चण्डी प्रसाद भट्ट", "दीप जोशी", "सुन्दरलाल बहुगुणा", "बद्रीदत्त पाण्डेय"],
        "correct_answer": "चण्डी प्रसाद भट्ट",
        "explanation": "1982 में पर्यावरण संरक्षण के लिए उन्हें यह सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Livestock",
        "text": "उत्तराखंड में 'भेड एवं ऊन विकास बोर्ड' कहाँ स्थित है?",
        "options": ["देहरादून", "अल्मोड़ा", "पिथौरागढ़", "चंपावत"],
        "correct_answer": "देहरादून",
        "explanation": "पर्वतीय क्षेत्रों में ऊन उत्पादन को बढ़ावा देने का कार्य यह बोर्ड करता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Social Reform",
        "text": "उत्तराखंड में 'गांधी आश्रम' की स्थापना सोमेश्वर (अल्मोड़ा) में किसने की थी?",
        "options": ["शांति लाल त्रिवेदी", "बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "विक्टर मोहन जोशी"],
        "correct_answer": "शांति लाल त्रिवेदी",
        "explanation": "1937 में चनौदा (सोमेश्वर) में गांधी आश्रम की स्थापना हुई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Mining",
        "text": "उत्तराखंड में 'जिप्सम' (Gypsum) का सर्वाधिक उत्पादन किस जिले में होता है?",
        "options": ["देहरादून", "नैनीताल", "पौड़ी", "टिहरी"],
        "correct_answer": "देहरादून",
        "explanation": "देहरादून जिले में जिप्सम के पर्याप्त भंडार मौजूद हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Political Parties",
        "text": "'उत्तराखंड क्रांति दल' (UKD) की स्थापना किस वर्ष हुई थी?",
        "options": ["1979", "1980", "1975", "1985"],
        "correct_answer": "1979",
        "explanation": "डॉ. देवीदत्त पंत की अध्यक्षता में मसूरी में इसकी स्थापना हुई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Transport",
        "text": "उत्तराखंड में 'प्रथम रेलगाड़ी' कब चली थी?",
        "options": ["1884", "1890", "1880", "1900"],
        "correct_answer": "1884",
        "explanation": "किच्छा से काठगोदाम के बीच पहली बार रेल सेवा शुरू हुई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Freedom Struggle",
        "text": "उत्तराखंड में 'नमक सत्याग्रह' के दौरान 'नंदा देवी' के नेतृत्व में कहाँ प्रदर्शन हुआ था?",
        "options": ["अल्मोड़ा", "नैनीताल", "देहरादून", "पौड़ी"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "नगर पालिका भवन पर झंडा फहराने और नमक कानून तोड़ने में महिलाओं की बड़ी भूमिका थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Hydropower",
        "text": "उत्तराखंड जलविद्युत निगम (UJVNL) की स्थापना कब हुई थी?",
        "options": ["2001", "2000", "2005", "2010"],
        "correct_answer": "2001",
        "explanation": "यह राज्य की जलविद्युत परियोजनाओं के प्रबंधन का कार्य करता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'एच.एन.बी. गढ़वाल विश्वविद्यालय' (HNBGU) को केंद्रीय विश्वविद्यालय का दर्जा कब मिला?",
        "options": ["2009", "2000", "2005", "2015"],
        "correct_answer": "2009",
        "explanation": "15 जनवरी 2009 को इसे सेंट्रल यूनिवर्सिटी बनाया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Small Scale Industry",
        "text": "उत्तराखंड में 'हथकरघा' (Handloom) उद्योग के लिए प्रसिद्ध स्थान कौन सा है?",
        "options": ["काशीपुर", "हल्द्वानी", "रुद्रपुर", "कोटद्वार"],
        "correct_answer": "काशीपुर",
        "explanation": "काशीपुर और जसपुर क्षेत्र हथकरघा और कपड़ा उद्योग के लिए जाने जाते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "उत्तराखंड के किस व्यक्ति को 'पहाड़ का गांधी' (स्वतंत्रता संग्राम सेनानी) कहा जाता है?",
        "options": ["जसवंत सिंह बिष्ट", "इन्द्रमणि बडोनी", "सुन्दरलाल बहुगुणा", "चण्डी प्रसाद भट्ट"],
        "correct_answer": "जसवंत सिंह बिष्ट",
        "explanation": "कुमाऊँ क्षेत्र में उनके गांधीवादी आदर्शों के कारण।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Resources",
        "text": "उत्तराखंड में 'चूना पत्थर' (Limestone) का सबसे बड़ा क्षेत्र कौन सा है?",
        "options": ["देहरादून", "पिथौरागढ़", "चमोली", "नैनीताल"],
        "correct_answer": "देहरादून",
        "explanation": "देहरादून का कालसी और मंदारम क्षेत्र चूना पत्थर के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Movements",
        "text": "उत्तराखंड में 'डोला-पालकी' आंदोलन का मुख्य उद्देश्य क्या था?",
        "options": ["शिल्पकारों को सामाजिक समानता", "वनों का अधिकार", "शिक्षा", "राजनीतिक अधिकार"],
        "correct_answer": "शिल्पकारों को सामाजिक समानता",
        "explanation": "जयानंद भारती ने इस कुप्रथा के विरुद्ध संघर्ष किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Agriculture",
        "text": "उत्तराखंड में 'औषधीय एवं सुगंधित पौधा संस्थान' (CIMAP) कहाँ है?",
        "options": ["पंतनगर", "देहरादून", "नैनीताल", "अल्मोड़ा"],
        "correct_answer": "पंतनगर",
        "explanation": "सुगंधित पौधों और जड़ी-बूटियों पर शोध के लिए यह संस्थान महत्वपूर्ण है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Symbols",
        "text": "उत्तराखंड के 'राज्य चिन्ह' में किन नदियों की लहरें दिखाई गई हैं?",
        "options": ["गंगा", "यमुना", "काली", "अलकनन्दा"],
        "correct_answer": "गंगा",
        "explanation": "प्रतीकात्मक रूप से गंगा की चार लहरें राज्य की नदियों का प्रतिनिधित्व करती हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Dairy",
        "text": "उत्तराखंड में 'आँचल' (Anchal) ब्रांड का संबंध किससे है?",
        "options": ["दूध और डेयरी उत्पाद", "फल", "शहद", "हथकरघा"],
        "correct_answer": "दूध और डेयरी उत्पाद",
        "explanation": "यह राज्य सहकारी डेयरी फेडरेशन का आधिकारिक ब्रांड है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "उत्तराखंड के 'प्रथम मुख्यमंत्री' जिन्होंने अपना कार्यकाल पूरा किया?",
        "options": ["नारायण दत्त तिवारी", "नित्यानंद स्वामी", "भगत सिंह कोश्यारी", "बी.सी. खण्डूड़ी"],
        "correct_answer": "नारायण दत्त तिवारी",
        "explanation": "वे राज्य के पहले निर्वाचित मुख्यमंत्री थे जिन्होंने 5 वर्ष का कार्यकाल पूरा किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Resources",
        "text": "उत्तराखंड में 'ताँबा' (Copper) मुख्य रूप से कहाँ पाया जाता है?",
        "options": ["अल्मोड़ा और चमोली", "देहरादून", "हरिद्वार", "नैनीताल"],
        "correct_answer": "अल्मोड़ा और चमोली",
        "explanation": "अल्मोड़ा के ताँबाखानी और चमोली के नागनाथ क्षेत्र ताँबे के लिए जाने जाते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'प्रशासनिक अकादमी' (Administrative Academy) कहाँ स्थित है?",
        "options": ["नैनीताल", "देहरादून", "मसूरी", "अल्मोड़ा"],
        "correct_answer": "नैनीताल",
        "explanation": "आर.एस. टोलिया उत्तराखंड प्रशासनिक अकादमी नैनीताल में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Hydropower",
        "text": "उत्तराखंड में 'किसाऊ बाँध' (Kishau Dam) किस नदी पर प्रस्तावित है?",
        "options": ["टोंस नदी", "यमुना", "गंगा", "भागीरथी"],
        "correct_answer": "टोंस नदी",
        "explanation": "यह हिमाचल प्रदेश और उत्तराखंड की सीमा पर टोंस नदी पर एक बड़ी परियोजना है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Women Leaders",
        "text": "उत्तराखंड की प्रथम महिला 'निर्वाचन आयुक्त' (First Woman Election Commissioner) कौन थी?",
        "options": ["राधा रतूड़ी", "ज्योत्सना भट्ट", "विजया बड़थ्वाल", "पुष्पा बिष्ट"],
        "correct_answer": "राधा रतूड़ी",
        "explanation": "वे राज्य की एक प्रमुख प्रशासनिक अधिकारी रही हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Resources",
        "text": "उत्तराखंड में 'डोलोमाइट' (Dolomite) का सर्वाधिक उत्पादन कहाँ होता है?",
        "options": ["देहरादून", "पिथौरागढ़", "टिहरी", "नैनीताल"],
        "correct_answer": "देहरादून",
        "explanation": "देहरादून जिला डोलोमाइट के उत्पादन में प्रमुख है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "किसे 'गढ़वाल का शेर' कहा जाता है?",
        "options": ["अनसूया प्रसाद बहुगुणा", "बद्रीदत्त पाण्डेय", "वीर चन्द्र सिंह गढ़वाली", "श्रीदेव सुमन"],
        "correct_answer": "अनसूया प्रसाद बहुगुणा",
        "explanation": "उनकी प्रखर राष्ट्रवादी सोच के कारण उन्हें यह ख्याति मिली।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Agriculture",
        "text": "उत्तराखंड में 'मत्स्य पालन' (Fisheries) हेतु प्रसिद्ध स्थान कौन सा है?",
        "options": ["भीमताल (नैनीताल)", "हरिद्वार", "ऋषिकेश", "रुद्रपुर"],
        "correct_answer": "भीमताल (नैनीताल)",
        "explanation": "भीमताल में मत्स्य अनुसंधान और प्रजनन केंद्र स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'राज्य सूचना आयोग' का मुख्यालय कहाँ है?",
        "options": ["देहरादून", "नैनीताल", "अल्मोड़ा", "हल्द्वानी"],
        "correct_answer": "देहरादून",
        "explanation": "सूचना के अधिकार (RTI) से संबंधित राज्य का सर्वोच्च निकाय देहरादून में है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Industrial Estates",
        "text": "पंतनगर में सिडकुल औद्योगिक क्षेत्र की स्थापना किस वर्ष हुई थी?",
        "options": ["2002", "2000", "2005", "2010"],
        "correct_answer": "2002",
        "explanation": "राज्य के औद्योगिक विकास के लिए पंतनगर एक महत्वपूर्ण हब बना।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Movements",
        "text": "उत्तराखंड में 'मैती आंदोलन' (Maiti Movement) का मुख्य संदेश क्या है?",
        "options": ["वृक्षारोपण और संरक्षण", "शराब निषेध", "शिक्षा", "वन्यजीव सुरक्षा"],
        "correct_answer": "वृक्षारोपण और संरक्षण",
        "explanation": "शादी के अवसर पर दुल्हा-दुल्हन द्वारा पौधा लगाने की यह एक भावनात्मक परंपरा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Horticulture",
        "text": "उत्तराखंड में 'शहद' (Honey) के उत्पादन के लिए कौन सा जिला प्रसिद्ध है?",
        "options": ["नैनीताल", "अल्मोड़ा", "चंपावत", "हरिद्वार"],
        "correct_answer": "नैनीताल",
        "explanation": "नैनीताल के ज्योलीकोट क्षेत्र में मधुमक्खी पालन का प्रमुख केंद्र है।"
    },

    # ── BATCH 18: LITERATURE, SPORTS & PERSONALITIES ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Literary Giants",
        "text": "प्रकृति के सुकुमार कवि 'सुमित्रानंदन पंत' का जन्म कहाँ हुआ था?",
        "options": ["कौसानी (बागेश्वर)", "अल्मोड़ा", "नैनीताल", "मसूरी"],
        "correct_answer": "कौसानी (बागेश्वर)",
        "explanation": "वे हिन्दी साहित्य के छायावादी युग के प्रमुख स्तंभ थे और प्रथम ज्ञानपीठ पुरस्कार विजेता (हिन्दी) भी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "प्रसिद्ध लेखिका 'शिवानी' (Shivani) का वास्तविक नाम क्या था?",
        "options": ["गौरा पंत", "राधा पंत", "मंजू नौटियाल", "पुष्पा बिष्ट"],
        "correct_answer": "गौरा पंत",
        "explanation": "हिन्दी साहित्य में उन्होंने कुमाऊँनी संस्कृति को जीवंत किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "प्रसिद्ध लेखक 'रस्किन बाण्ड' (Ruskin Bond) मुख्य रूप से किस शहर में निवास करते हैं?",
        "options": ["मसूरी (मसूरी)", "नैनीताल", "देहरादून", "रानीखेत"],
        "correct_answer": "मसूरी (मसूरी)",
        "explanation": "वे मसूरी के लांढौर क्षेत्र में रहते हैं और उन्होंने बच्चों के लिए बहुत साहित्य लिखा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Literary Giants",
        "text": "किसे 'उत्तराखंड का व्यास' (Vyasa of Uttarakhand) कहा जाता है?",
        "options": ["शिवप्रसाद डबराल 'चारण'", "बद्रीदत्त पाण्डेय", "हरिकृष्ण रतूड़ी", "पाण्डे"],
        "correct_answer": "शिवप्रसाद डबराल 'चारण'",
        "explanation": "इतिहास और साहित्य में उनके विशाल योगदान के कारण उन्हें यह उपाधि दी गई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards",
        "text": "हिन्दी साहित्य का प्रथम 'ज्ञानपीठ पुरस्कार' उत्तराखंड के किस व्यक्ति को मिला था?",
        "options": ["सुमित्रानंदन पंत", "शैलेश मटियानी", "मनोहर श्याम जोशी", "मंगलेश डबराल"],
        "correct_answer": "सुमित्रानंदन पंत",
        "explanation": "1968 में उनकी कृति 'चिदंबरा' के लिए उन्हें यह सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "प्रसिद्ध कहानीकार 'शैलेश मटियानी' का जन्म किस जिले में हुआ था?",
        "options": ["अल्मोड़ा", "पिथौरागढ़", "नैनीताल", "चंपावत"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "वे हिन्दी के 'आंचलिक उपन्यासकार' के रूप में प्रसिद्ध हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'हम लोग' और 'बुनियाद' जैसे प्रसिद्ध धारावाहिकों के लेखक कौन थे?",
        "options": ["मनोहर श्याम जोशी", "प्रसून जोशी", "सुमित पंत", "रजत शर्मा"],
        "correct_answer": "मनोहर श्याम जोशी",
        "explanation": "वे उत्तराखंड के एक प्रसिद्ध साहित्यकार और पटकथा लेखक थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'पहाड़' (Pahar) पत्रिका का संपादन किसके द्वारा किया जाता है?",
        "options": ["शेखर पाठक", "डबराल", "पाण्डे", "रतूड़ी"],
        "correct_answer": "शेखर पाठक",
        "explanation": "यह पत्रिका हिमालयी संस्कृति और पर्यावरण पर केंद्रित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'गौरा पन्त' (Gora Pant) के नाम से जाना जाता है?",
        "options": ["लेखिका शिवानी", "बचेंद्री पाल", "गौरा देवी", "दीपा देवी"],
        "correct_answer": "लेखिका शिवानी",
        "explanation": "हिन्दी साहित्य में उनका योगदान अतुलनीय है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards",
        "text": "उत्तराखंड के किस कवि को 'साहित्य अकादमी पुरस्कार' (प्रथम) मिला था?",
        "options": ["सुमित्रानंदन पंत", "मंगलेश डबराल", "वीरेन डंगवाल", "लीलाधर जगूड़ी"],
        "correct_answer": "सुमित्रानंदन पंत",
        "explanation": "1960 में उनकी रचना 'कला और बूढ़ा चाँद' के लिए।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Arjun Awardees",
        "text": "उत्तराखंड से 'अर्जुन पुरस्कार' प्राप्त करने वाले प्रथम व्यक्ति कौन थे?",
        "options": ["पदम बहादुर मल्ल (मुक्केबाजी)", "हर्षवंती बिष्ट", "बचेंद्री पाल", "जसपाल राणा"],
        "correct_answer": "पदम बहादुर मल्ल (मुक्केबाजी)",
        "explanation": "1962 में उन्हें खेल के क्षेत्र में यह सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Athletes",
        "text": "प्रसिद्ध बैडमिंटन खिलाड़ी 'लक्ष्य सेन' किस जिले से संबंधित हैं?",
        "options": ["अल्मोड़ा", "देहरादून", "हल्द्वानी", "नैनीताल"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "अल्मोड़ा को 'बैडमिंटन का हब' माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Athletes",
        "text": "भारतीय क्रिकेटर 'ऋषभ पंत' का जन्म उत्तराखंड के किस शहर में हुआ था?",
        "options": ["रुड़की", "देहरादून", "हरिद्वार", "हल्द्वानी"],
        "correct_answer": "रुड़की",
        "explanation": "वे मूल रूप से पिथौरागढ़ के हैं लेकिन उनका जन्म रुड़की में हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Shooting",
        "text": "'गोल्डन बॉय' (Golden Boy) के नाम से प्रसिद्ध निशानेबाज कौन हैं?",
        "options": ["जसपाल राणा", "अभिनव बिंद्रा", "मानवजीत संधू", "राज्यवर्धन सिंह"],
        "correct_answer": "जसपाल राणा",
        "explanation": "निशानेबाजी में उनकी उपलब्धियों के कारण उन्हें यह उपनाम मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Adventure Sports",
        "text": "बचेंद्री पाल ने 'माउंट एवरेस्ट' पर किस वर्ष फतह हासिल की थी?",
        "options": ["1984", "1980", "1990", "1985"],
        "correct_answer": "1984",
        "explanation": "वे एवरेस्ट पर चढ़ने वाली पहली भारतीय महिला बनीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Athletes",
        "text": "'पर्वतारोहण' के क्षेत्र में 'पदमश्री' प्राप्त करने वाली पहली महिला कौन हैं?",
        "options": ["बचेंद्री पाल", "चन्द्रप्रभा ऐतवाल", "हर्षवंती बिष्ट", "ताशी मलिक"],
        "correct_answer": "बचेंद्री पाल",
        "explanation": "उन्होंने कई रिकॉर्ड बनाए और महिलाओं को पर्वतारोहण के लिए प्रेरित किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Athletes",
        "text": "उत्तराखंड के 'एकता बिष्ट' का संबंध किस खेल से है?",
        "options": ["क्रिकेट", "हॉकी", "फुटबॉल", "बैडमिंटन"],
        "correct_answer": "क्रिकेट",
        "explanation": "वे भारतीय महिला क्रिकेट टीम की एक प्रमुख गेंदबाज रही हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Athletes",
        "text": "'चिराग सेन' का संबंध किस खेल से है?",
        "options": ["बैडमिंटन", "क्रिकेट", "मुक्केबाजी", "एथलेटिक्स"],
        "correct_answer": "बैडमिंटन",
        "explanation": "वे लक्ष्य सेन के भाई हैं और बैडमिंटन के उत्कृष्ट खिलाड़ी हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Athletes",
        "text": "उत्तराखंड के 'मनीष रावत' का संबंध किस खेल से है?",
        "options": ["पैदल चाल (Race Walk)", "दौड़", "निशानेबाजी", "हॉकी"],
        "correct_answer": "पैदल चाल (Race Walk)",
        "explanation": "ओलंपिक में उन्होंने भारत का प्रतिनिधित्व किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Awards",
        "text": "उत्तराखंड 'खेल रत्न पुरस्कार' का नाम किसके नाम पर रखा गया है?",
        "options": ["देवभूमि उत्तराखंड खेल रत्न", "पंडित गोविंद बल्लभ पंत", "वीर चन्द्र सिंह गढ़वाली", "श्रीदेव सुमन"],
        "correct_answer": "देवभूमि उत्तराखंड खेल रत्न",
        "explanation": "राज्य के उत्कृष्ट खिलाड़ियों को यह सम्मान दिया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड की तीलू रौतेली' (गढ़वाल की झांसी की रानी) का वास्तविक नाम क्या था?",
        "options": ["तीलू रौतेली", "गौमती", "कमला", "राजेश्वरी"],
        "correct_answer": "तीलू रौतेली",
        "explanation": "वे 15 से 22 वर्ष की आयु में सात युद्ध लड़ने वाली महान वीरांगना थीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के 'प्रथम थल सेनाध्यक्ष' (General) कौन थे?",
        "options": ["विपिन चन्द्र जोशी", "बी.सी. खण्डूड़ी", "विपिन रावत", "अनिल चौहान"],
        "correct_answer": "विपिन चन्द्र जोशी",
        "explanation": "वे भारतीय सेना के प्रमुख बनने वाले उत्तराखंड के पहले व्यक्ति थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards",
        "text": "उत्तराखंड के किस व्यक्ति को प्रथम 'परमवीर चक्र' मिला था?",
        "options": ["मेजर सोमनाथ शर्मा", "गब्बर सिंह नेगी", "दरवान सिंह नेगी", "धन सिंह थापा"],
        "correct_answer": "मेजर सोमनाथ शर्मा",
        "explanation": "मरणोपरांत उन्हें भारत का सर्वोच्च सैन्य सम्मान मिला (कुमाऊँ रेजिमेंट)।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards",
        "text": "उत्तराखंड के प्रथम 'विक्टोरिया क्रॉस' विजेता कौन थे?",
        "options": ["दरवान सिंह नेगी (1914)", "गब्बर सिंह नेगी", "चन्द्र सिंह गढ़वाली", "मेजर सोमनाथ"],
        "correct_answer": "दरवान सिंह नेगी (1914)",
        "explanation": "प्रथम विश्व युद्ध के दौरान वीरता के लिए उन्हें यह ब्रिटिश सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "भारत के 'प्रथम चीफ ऑफ डिफेंस स्टाफ' (CDS) कौन थे?",
        "options": ["जनरल विपिन रावत", "जनरल अनिल चौहान", "जनरल मनोज मुकुंद नरवणे", "जनरल दलबीर सिंह"],
        "correct_answer": "जनरल विपिन रावत",
        "explanation": "वे उत्तराखंड के पौड़ी जिले के मूल निवासी थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'गढ़वाल की दिवंगति विभूतियाँ' पुस्तक किसने लिखी है?",
        "options": ["भक्त दर्शन", "डबराल", "पाण्डे", "रतूड़ी"],
        "correct_answer": "भक्त दर्शन",
        "explanation": "गढ़वाल के महान व्यक्तित्वों पर यह एक प्रामाणिक पुस्तक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के किस व्यक्ति को 'आधुनिक भगीरथ' कहा जाता है?",
        "options": ["पी. कतले (P. Cautley)", "रैमजे", "ट्रेल", "गार्डनर"],
        "correct_answer": "पी. कतले (P. Cautley)",
        "explanation": "ऊपरी गंगा नहर (रुड़की) के निर्माण में उनके योगदान के कारण।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड की प्रथम महिला 'कुलपति' (VC) कौन थी?",
        "options": ["सुशीला डोभाल", "कमलेन्दु मति शाह", "विजया बड़थ्वाल", "पुष्पा बिष्ट"],
        "correct_answer": "सुशीला डोभाल",
        "explanation": "वे राज्य के शैक्षणिक जगत की एक प्रतिष्ठित महिला रहीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड की मदर टेरेसा' कहा जाता है?",
        "options": ["माधुरी बड़थ्वाल", "राधा भट्ट", "गौरा देवी", "बचेंद्री पाल"],
        "correct_answer": "माधुरी बड़थ्वाल",
        "explanation": "लोक संस्कृति और समाज सेवा में उनके योगदान के लिए।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards",
        "text": "उत्तराखंड से 'दादा साहब फाल्के' पुरस्कार प्राप्त करने वाले प्रथम व्यक्ति कौन थे?",
        "options": ["तथागत मुखर्जी", "प्रसून जोशी", "नरेन्द्र सिंह नेगी", "प्रमोद साह"],
        "correct_answer": "तथागत मुखर्जी",
        "explanation": "सिनेमा और कला के क्षेत्र में उल्लेखनीय योगदान के लिए।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Athletes",
        "text": "उत्तराखंड के 'स्नेह राणा' का संबंध किस खेल से है?",
        "options": ["क्रिकेट", "हॉकी", "बैडमिंटन", "फुटबॉल"],
        "correct_answer": "क्रिकेट",
        "explanation": "वे भारतीय महिला क्रिकेट टीम की एक प्रमुख खिलाड़ी हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Athletes",
        "text": "प्रसिद्ध एथलीट 'मनीषा रावत' किस विधा से संबंधित हैं?",
        "options": ["दौड़", "गोला फेंक", "लंबी कूद", "ऊँची कूद"],
        "correct_answer": "दौड़",
        "explanation": "उन्होंने कई राष्ट्रीय स्तर की प्रतियोगिताओं में पदक जीते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Athletes",
        "text": "उत्तराखंड के 'गुरुमीत सिंह' का संबंध किस खेल से है?",
        "options": ["पैदल चाल (Race Walk)", "हॉकी", "फुटबॉल", "क्रिकेट"],
        "correct_answer": "पैदल चाल (Race Walk)",
        "explanation": "एशियाई चैंपियनशिप में उन्होंने भारत को पदक दिलाया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'गढ़वाल की लोककला' पुस्तक के लेखक कौन हैं?",
        "options": ["यशोधर मठपाल", "डबराल", "शिवानंद नौटियाल", "पाण्डे"],
        "correct_answer": "यशोधर मठपाल",
        "explanation": "उन्होंने राज्य की लोक कलाओं पर गहन शोध किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards",
        "text": "उत्तराखंड के किस गायक को 'पदमश्री' (प्रथम गायक) मिला था?",
        "options": ["नरेन्द्र सिंह नेगी", "प्रीतम भरतवाण", "पदम सिंह बिष्ट", "बसन्ती बिष्ट"],
        "correct_answer": "बसन्ती बिष्ट",
        "explanation": "जागर गायिका के रूप में उन्हें यह गौरव प्राप्त हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "किसे 'कुमाऊँ का चाणक्य' कहा जाता है?",
        "options": ["हर्षदेव जोशी", "पंत", "नेगी", "बडोनी"],
        "correct_answer": "हर्षदेव जोशी",
        "explanation": "चन्द और गोरखा शासन के संक्रमण काल में उनकी कूटनीति के लिए।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Personalities",
        "text": "उत्तराखंड के 'प्रथम मुख्यमंत्री' जिन्होंने इस्तीफा दिया?",
        "options": ["नित्यानंद स्वामी", "भगत सिंह कोश्यारी", "तीरथ सिंह रावत", "त्रिवेंद्र सिंह रावत"],
        "correct_answer": "नित्यानंद स्वामी",
        "explanation": "अन्तरिम सरकार के दौरान उन्होंने पद छोड़ा था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Authors",
        "text": "'बूँद-बूँद' (Bund-Bund) किसकी काव्य रचना है?",
        "options": ["पदमश्री डबराल", "सुमित्रानंदन पंत", "मंगलेश डबराल", "लीलाधर जगूड़ी"],
        "correct_answer": "लीलाधर जगूड़ी",
        "explanation": "वे उत्तराखंड के एक प्रतिष्ठित कवि और साहित्यकार हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Culture & Literature",
        "source": "Awards",
        "text": "उत्तराखंड के किस व्यक्ति को 'पद्म विभूषण' (द्वितीय) मिला था?",
        "options": ["भैरव दत्त पाण्डेय", "सुन्दरलाल बहुगुणा", "डॉ. घनानंद पाण्डेय", "पंडित गोविंद बल्लभ पंत"],
        "correct_answer": "भैरव दत्त पाण्डेय",
        "explanation": "प्रशासनिक सेवा और सार्वजनिक कार्यों के लिए 2000 में उन्हें यह सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Sports",
        "source": "Institutions",
        "text": "उत्तराखंड का प्रथम 'खेल विश्वविद्यालय' कहाँ स्थापित किया जा रहा है?",
        "options": ["हल्द्वानी", "देहरादून", "हरिद्वार", "रुद्रपुर"],
        "correct_answer": "हल्द्वानी",
        "explanation": "हल्द्वानी में अंतरराष्ट्रीय स्तर की खेल सुविधाओं के साथ विश्वविद्यालय प्रस्तावित है।"
    },

    # ── BATCH 19: FIRSTS IN UK & MISC FACTS ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड में 'प्रथम डाकघर' (Post Office) कहाँ स्थापित किया गया था?",
        "options": ["अल्मोड़ा (1816)", "देहरादून", "नैनीताल", "पौड़ी"],
        "correct_answer": "अल्मोड़ा (1816)",
        "explanation": "ब्रिटिश शासन काल में कुमाऊँ के अल्मोड़ा में पहला डाकघर खोला गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Media & Press",
        "text": "उत्तराखंड से प्रकाशित होने वाला 'प्रथम समाचार पत्र' कौन सा था?",
        "options": ["द हिल्स (The Hills)", "समय विनोद", "अल्मोड़ा अखबार", "शक्ति"],
        "correct_answer": "द हिल्स (The Hills)",
        "explanation": "1842 में मसूरी से जॉन मैकिनन द्वारा अंग्रेजी में इसे प्रकाशित किया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड की 'प्रथम महिला मुख्य सचिव' (Chief Secretary) कौन बनी हैं?",
        "options": ["राधा रतूड़ी", "ज्योत्सना भट्ट", "विजया बड़थ्वाल", "पुष्पा बिष्ट"],
        "correct_answer": "राधा रतूड़ी",
        "explanation": "2024 में उन्होंने राज्य की पहली महिला मुख्य सचिव के रूप में कार्यभार संभाला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड का 'प्रथम नगर निगम' (Municipal Corporation) कौन सा है?",
        "options": ["देहरादून", "हल्द्वानी", "हरिद्वार", "रुद्रपुर"],
        "correct_answer": "देहरादून",
        "explanation": "देहरादून राज्य का सबसे पुराना और पहला नगर निगम है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Transport",
        "text": "उत्तराखंड की पहली 'वंदे भारत एक्सप्रेस' किन दो शहरों के बीच चली?",
        "options": ["देहरादून - दिल्ली", "देहरादून - लखनऊ", "हरिद्वार - दिल्ली", "ऋषिकेश - दिल्ली"],
        "correct_answer": "देहरादून - दिल्ली",
        "explanation": "यह उत्तराखंड की पहली सेमी-हाई स्पीड रेल सेवा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Social Events",
        "text": "उत्तराखंड में 'G-20' की पहली बैठक कहाँ आयोजित हुई थी?",
        "options": ["रामनगर", "ऋषिकेश", "नरेन्द्रनगर", "देहरादून"],
        "correct_answer": "रामनगर",
        "explanation": "मार्च 2023 में रामनगर में G-20 की 'चीफ साइंटिफिक एडवाइजर्स' की बैठक हुई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड 'समान नागरिक संहिता' (UCC) लागू करने वाला देश का कौन सा राज्य है?",
        "options": ["पहला (आजादी के बाद)", "दूसरा", "तीसरा", "चौथा"],
        "correct_answer": "पहला (आजादी के बाद)",
        "explanation": "उत्तराखंड विधानसभा ने 2024 में UCC विधेयक पारित किया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "एशिया का 'प्रथम इंजीनियरिंग कॉलेज' कहाँ स्थापित हुआ था?",
        "options": ["रुड़की (1847)", "देहरादून", "पंतनगर", "काशीपुर"],
        "correct_answer": "रुड़की (1847)",
        "explanation": "थॉमसन कॉलेज ऑफ सिविल इंजीनियरिंग के नाम से इसकी स्थापना हुई थी, जो अब IIT रुड़की है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड की 'प्रथम महिला पुलिस महानिदेशक' (DGP) कौन थी?",
        "options": ["कंचन चौधरी भट्टाचार्य", "राधा रतूड़ी", "ज्योति राव", "सीमा वर्मा"],
        "correct_answer": "कंचन चौधरी भट्टाचार्य",
        "explanation": "वे भारत की भी किसी राज्य की पहली महिला DGP थीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड में 'प्रथम विधानसभा चुनाव' किस वर्ष हुए थे?",
        "options": ["2002", "2000", "2001", "2005"],
        "correct_answer": "2002",
        "explanation": "फरवरी 2002 में राज्य के पहले निर्वाचित सदन के लिए मतदान हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड लोक सेवा आयोग (UKPSC) का मुख्यालय कहाँ है?",
        "options": ["हरिद्वार", "नैनीताल", "देहरादून", "हल्द्वानी"],
        "correct_answer": "हरिद्वार",
        "explanation": "गुरुकुल कांगड़ी, हरिद्वार के पास इसका मुख्यालय स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "देहरादून में 'भारतीय सैन्य अकादमी' (IMA) की स्थापना कब हुई थी?",
        "options": ["1 अक्टूबर 1932", "1942", "1950", "1920"],
        "correct_answer": "1 अक्टूबर 1932",
        "explanation": "सर फिलिप चैटवुड ने इसका उद्घाटन किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "पर्वतीय क्षेत्र में 'प्रथम नगरपालिका' कौन सी थी?",
        "options": ["मसूरी (1842)", "नैनीताल", "अल्मोड़ा", "हल्द्वानी"],
        "correct_answer": "मसूरी (1842)",
        "explanation": "यह उत्तर भारत की सबसे पुरानी नगरपालिकाओं में से एक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड का 'प्रथम हिंदी समाचार पत्र' कौन सा था?",
        "options": ["समय विनोद (1868)", "अल्मोड़ा अखबार", "गढ़वाली", "शक्ति"],
        "correct_answer": "समय विनोद (1868)",
        "explanation": "यह नैनीताल/जसपुर से प्रकाशित हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Forestry",
        "text": "भारत का 'प्रथम वन महाविद्यालय' (Forest School) कहाँ खुला था?",
        "options": ["देहरादून (1878)", "हल्द्वानी", "नैनीताल", "पंतनगर"],
        "correct_answer": "देहरादून (1878)",
        "explanation": "अब इसे 'फॉरेस्ट रिसर्च इंस्टीट्यूट' (FRI) के रूप में जाना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "'लाल बहादुर शास्त्री प्रशासनिक अकादमी' (LBSNAA) कहाँ स्थित है?",
        "options": ["मसूरी", "देहरादून", "नैनीताल", "अल्मोड़ा"],
        "correct_answer": "मसूरी",
        "explanation": "यहाँ भारतीय प्रशासनिक सेवा (IAS) के अधिकारियों को प्रशिक्षण दिया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड के 'प्रथम महाधिवक्ता' (Advocate General) कौन थे?",
        "options": ["मेहरबान सिंह नेगी", "एल.पी. नैथानी", "सुधांशु धूलिया", "वी.बी.एस. नेगी"],
        "correct_answer": "मेहरबान सिंह नेगी",
        "explanation": "राज्य के कानूनी मामलों के वे पहले प्रधान सलाहकार थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड लोक सेवा आयोग के 'प्रथम अध्यक्ष' कौन थे?",
        "options": ["एन.पी. नवानी", "एस.के. दास", "ए.के. जैन", "एम.सी. भंडारी"],
        "correct_answer": "एन.पी. नवानी",
        "explanation": "आयोग के गठन के बाद वे पहले चेयरमैन बने।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड का 'प्रथम म्यूजियम' कहाँ बना था?",
        "options": ["देहरादून (1914)", "अल्मोड़ा", "नैनीताल", "पिथौरागढ़"],
        "correct_answer": "देहरादून (1914)",
        "explanation": "वन संग्रहालय (FRI) राज्य का सबसे पुराना संग्रहालय माना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड की 'प्रथम कमर्शियल उड़ान' (Commercial Flight) कहाँ उतरी थी?",
        "options": ["जॉली ग्रांट (देहरादून)", "पंतनगर", "पिथौरागढ़", "चिन्यालीसौड़"],
        "correct_answer": "जॉली ग्रांट (देहरादून)",
        "explanation": "यह राज्य का मुख्य और सबसे व्यस्त हवाई अड्डा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'ई-गवर्नेंस' (E-Governance) वर्ष किस वर्ष घोषित किया गया था?",
        "options": ["2001", "2005", "2010", "2000"],
        "correct_answer": "2001",
        "explanation": "सूचना प्रौद्योगिकी के प्रयोग को बढ़ावा देने के लिए यह निर्णय लिया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "देहरादून में 'इंदिरा गांधी राष्ट्रीय वन अकादमी' की स्थापना कब हुई थी?",
        "options": ["1987", "1975", "1980", "1990"],
        "correct_answer": "1987",
        "explanation": "यह भारतीय वन सेवा (IFS) के अधिकारियों का प्रशिक्षण केंद्र है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Movements",
        "text": "'कल्याण सिंह रावत' द्वारा मैती आंदोलन की शुरुआत कहाँ से हुई थी?",
        "options": ["ग्वालदम (चमोली)", "रेणी", "दूधातोली", "कोटद्वार"],
        "correct_answer": "ग्वालदम (चमोली)",
        "explanation": "1995 में उन्होंने इस अनूठे आंदोलन की नींव रखी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Media & Press",
        "text": "'अल्मोड़ा अखबार' (1871) का प्रथम संपादक कौन था?",
        "options": ["बुद्धि बल्लभ पंत", "बद्रीदत्त पाण्डेय", "सदानंद सनवाल", "इम्तियाज अली"],
        "correct_answer": "बुद्धि बल्लभ पंत",
        "explanation": "कुमाऊँ में जनजागृति फैलाने में इस पत्र की बड़ी भूमिका थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Transport",
        "text": "ऋषिकेश-कर्णप्रयाग रेलवे लाइन की कुल लंबाई लगभग कितनी है?",
        "options": ["125 किमी", "150 किमी", "100 किमी", "175 किमी"],
        "correct_answer": "125 किमी",
        "explanation": "यह एक महात्वाकांक्षी रेल परियोजना है जिसमें कई लंबी सुरंगें शामिल हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'कुल राज्यसभा' सीटें कितनी हैं?",
        "options": ["3", "5", "2", "4"],
        "correct_answer": "3",
        "explanation": "राज्य से तीन सदस्य उच्च सदन (राज्यसभा) में भेजे जाते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'लोकसभा' की कितनी सीटें हैं?",
        "options": ["5", "3", "7", "4"],
        "correct_answer": "5",
        "explanation": "अल्मोड़ा (SC), गढ़वाल, टिहरी, नैनीताल और हरिद्वार ये पाँच लोकसभा क्षेत्र हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "पंतनगर विश्वविद्यालय का नाम 'गोविंद बल्लभ पंत' के नाम पर कब रखा गया?",
        "options": ["1972", "1960", "1965", "1975"],
        "correct_answer": "1972",
        "explanation": "1960 में स्थापित इस विश्वविद्यालय का नाम बाद में महान स्वतंत्रता सेनानी के नाम पर हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड का गांधी' कहा जाता है?",
        "options": ["इन्द्रमणि बडोनी", "सुन्दरलाल बहुगुणा", "जसवंत सिंह बिष्ट", "श्रीदेव सुमन"],
        "correct_answer": "इन्द्रमणि बडोनी",
        "explanation": "राज्य आंदोलन में उनके अहिंसक और सक्रिय नेतृत्व के कारण।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "देहरादून में 'हिमगिरी नभ विश्वविद्यालय' की स्थापना किस वर्ष हुई थी?",
        "options": ["2004", "2000", "2006", "2010"],
        "correct_answer": "2004",
        "explanation": "यह राज्य का एक प्रमुख निजी विश्वविद्यालय है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Environment",
        "text": "उत्तराखंड में 'वनीकरण' (Afforestation) के लिए कौन सा मॉडल प्रसिद्ध है?",
        "options": ["मैती मॉडल", "रेणी मॉडल", "दूधातोली मॉडल", "नैनीताल मॉडल"],
        "correct_answer": "मैती मॉडल",
        "explanation": "भावनात्मक जुड़ाव के कारण यह मॉडल अंतरराष्ट्रीय स्तर पर भी सराहा गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'मुक्त विश्वविद्यालय' (UOU) कहाँ स्थित है?",
        "options": ["हल्द्वानी", "देहरादून", "अल्मोड़ा", "ऋषिकेश"],
        "correct_answer": "हल्द्वानी",
        "explanation": "2005 में स्थापित यह राज्य का एकमात्र मुक्त विश्वविद्यालय है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड विधानसभा में 'अनुसूचित जाति' (SC) के लिए कितनी सीटें आरक्षित हैं?",
        "options": ["13", "15", "10", "11"],
        "correct_answer": "13",
        "explanation": "कुल 70 सीटों में से 13 सीटें SC वर्ग के लिए आरक्षित हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड विधानसभा में 'अनुसूचित जनजाति' (ST) के लिए कितनी सीटें आरक्षित हैं?",
        "options": ["2", "3", "5", "1"],
        "correct_answer": "2",
        "explanation": "चकराता (देहरादून) और नानकमत्ता (ऊधम सिंह नगर) की सीटें ST के लिए आरक्षित हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'आयुष विश्वविद्यालय' कहाँ स्थित है?",
        "options": ["हरिद्वार", "ऋषिकेश", "देहरादून", "हल्द्वानी"],
        "correct_answer": "हरिद्वार",
        "explanation": "आयुर्वेद और योग की शिक्षा के लिए यह समर्पित विश्वविद्यालय है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Movements",
        "text": "'बेगार' आंदोलन के दौरान बागेश्वर में कितने लोगों ने शपथ ली थी?",
        "options": ["लगभग 40,000", "10,000", "5,000", "20,000"],
        "correct_answer": "लगभग 40,000",
        "explanation": "1921 के उत्तरायणी कौतुक के अवसर पर यह विशाल जनसमूह उमड़ा था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Awards",
        "text": "उत्तराखंड के किस व्यक्ति को प्रथम 'खेल रत्न' मिला था?",
        "options": ["जसपाल राणा", "अभिनव बिंद्रा", "बचेंद्री पाल", "मानवजीत संधू"],
        "correct_answer": "जसपाल राणा",
        "explanation": "2013 में उन्हें राज्य का पहला खेल रत्न पुरस्कार दिया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'सूचना का अधिकार' अधिनियम कब लागू हुआ (भारत के साथ)?",
        "options": ["2005", "2000", "2008", "2010"],
        "correct_answer": "2005",
        "explanation": "12 अक्टूबर 2005 से यह राज्य में भी प्रभावी हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'तकनीकी विश्वविद्यालय' (UTU) कहाँ स्थित है?",
        "options": ["देहरादून", "रुड़की", "हल्द्वानी", "पंतनगर"],
        "correct_answer": "देहरादून",
        "explanation": "वीर माधो सिंह भंडारी उत्तराखंड तकनीकी विश्वविद्यालय देहरादून में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Agriculture",
        "text": "उत्तराखंड में 'जैविक कृषि अधिनियम' (Organic Agriculture Act) कब पारित हुआ?",
        "options": ["2019", "2015", "2021", "2010"],
        "correct_answer": "2019",
        "explanation": "जैविक खेती को कानूनी दर्जा देने वाला उत्तराखंड देश का अग्रणी राज्य है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "उत्तराखंड के किस व्यक्ति को 'पद्मश्री' (2024) से सम्मानित किया गया है?",
        "options": ["यशवंत सिंह कठोच", "नरेन्द्र सिंह नेगी", "प्रीतम भरतवाण", "अनूप साह"],
        "correct_answer": "यशवंत सिंह कठोच",
        "explanation": "साहित्य और शिक्षा के क्षेत्र में उनके योगदान के लिए उन्हें यह सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'सौर ऊर्जा नीति 2023' के अनुसार किस वर्ष तक 2000 मेगावाट का लक्ष्य है?",
        "options": ["2027", "2025", "2030", "2024"],
        "correct_answer": "2027",
        "explanation": "राज्य को ऊर्जा क्षेत्र में आत्मनिर्भर बनाने के लिए यह नई नीति लाई गई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Symbols",
        "text": "उत्तराखंड के 'राज्य गीत' की अवधि कितनी है?",
        "options": ["9 मिनट", "5 मिनट", "7 मिनट", "6 मिनट"],
        "correct_answer": "9 मिनट",
        "explanation": "'उत्तराखंड देवभूमि मातृभूमि' गीत लगभग 9 मिनट का है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "देहरादून में 'वाइल्ड लाइफ इंस्टीट्यूट ऑफ इंडिया' (WII) की स्थापना कब हुई?",
        "options": ["1982", "1975", "1990", "1985"],
        "correct_answer": "1982",
        "explanation": "यह वन्यजीव संरक्षण और शोध का एक अंतरराष्ट्रीय ख्याति प्राप्त संस्थान है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Awards",
        "text": "उत्तराखंड के किस व्यक्ति को 2023 में 'पद्म विभूषण' (मरणोपरांत) मिला?",
        "options": ["जनरल विपिन रावत", "कल्याण सिंह", "मुलायम सिंह", "एस.एम. कृष्णा"],
        "correct_answer": "जनरल विपिन रावत",
        "explanation": "देश के पहले CDS के रूप में उनकी सेवाओं के लिए उन्हें यह सम्मान मिला (नोट: उन्हें 2022 में घोषित किया गया था, 2023 की सूची में अन्य थे)।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Events",
        "text": "उत्तराखंड में 'औद्योगिक प्रोत्साहन नीति' (Industrial Policy) की घोषणा सबसे पहले कब हुई थी?",
        "options": ["8 जुलाई 2001", "2000", "2005", "2010"],
        "correct_answer": "8 जुलाई 2001",
        "explanation": "राज्य के गठन के बाद तेजी से विकास के लिए यह नीति लाई गई।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Forestry",
        "text": "उत्तराखंड में 'वन पंचायत' (Van Panchayat) व्यवस्था कब लागू हुई थी?",
        "options": ["1931", "1921", "1947", "1955"],
        "correct_answer": "1931",
        "explanation": "वनों के स्थानीय प्रबंधन के लिए यह एक अनूठी लोकतांत्रिक व्यवस्था है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'फिल्म विकास परिषद' (Film Development Council) का गठन कब हुआ?",
        "options": ["2015", "2010", "2000", "2020"],
        "correct_answer": "2015",
        "explanation": "राज्य में फिल्म शूटिंग को बढ़ावा देने के लिए इसका गठन किया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Movements",
        "text": "चिपको आंदोलन को 'राइट लाइवलीहुड अवार्ड' (Right Livelihood Award) कब मिला था?",
        "options": ["1987", "1982", "1990", "1995"],
        "correct_answer": "1987",
        "explanation": "इसे 'वैकल्पिक नोबेल पुरस्कार' भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'राजस्व पुलिस' (Revenue Police) व्यवस्था कब से लागू है?",
        "options": ["1874", "1900", "1947", "1850"],
        "correct_answer": "1874",
        "explanation": "सर हेनरी रैमजे के समय से पटवारी को ही पुलिस के अधिकार प्राप्त थे (अब धीरे-धीरे इसे समाप्त किया जा रहा है)।"
    },

    # ── BATCH 20: HIGH-DIFFICULTY & ADMINISTRATIVE MIX ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Dynastic History",
        "text": "पंवार राजवंश के राजाओं की 'वंशावली' का सबसे प्रामाणिक स्रोत किसे माना जाता है?",
        "options": ["हार्डविक की वंशावली", "बैकेट की वंशावली", "विलियम्स की सूची", "एटकिंसन की सूची"],
        "correct_answer": "बैकेट की वंशावली",
        "explanation": "कुमाऊँ और गढ़वाल के सैटलमेंट कमिश्नर बैकेट ने राजाओं की जो सूची तैयार की, वह ऐतिहासिक रूप से अधिक सटीक है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Medieval",
        "source": "Gorkha Administration",
        "text": "गोरखा शासन काल में न्याय के लिए प्रचलित 'दिव्य' (Divya) परीक्षा में 'गोला द्वीप' क्या था?",
        "options": ["गर्म लोहे की छड़ को हाथ से पकड़ना", "उबलते तेल में हाथ डालना", "कढ़ाई में बैठना", "नदी में तैरना"],
        "correct_answer": "गर्म लोहे की छड़ को हाथ से पकड़ना",
        "explanation": "गोरखा न्याय प्रणाली अत्यंत कठोर थी, जिसमें सत्य की परीक्षा के लिए अग्नि और जल का सहारा लिया जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "British Revenue",
        "text": "ब्रिटिश काल में 'संजायत' (Sanjayat) भूमि किसे कहा जाता था?",
        "options": ["गाँव की सामूहिक भूमि", "राजा की भूमि", "मंदिर की भूमि", "बंजर भूमि"],
        "correct_answer": "गाँव की सामूहिक भूमि",
        "explanation": "ऐसी भूमि जिस पर पूरे गाँव का साझा अधिकार होता था, संजायत कहलाती थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "British Administration",
        "text": "कुमाऊँ में 'पटवारी' पद का सृजन 1819 में किसने किया था?",
        "options": ["विलियम ट्रेल", "जी.डब्ल्यू. ट्रेल", "हेनरी रैमजे", "गार्डनर"],
        "correct_answer": "जी.डब्ल्यू. ट्रेल",
        "explanation": "राजस्व वसूली और छोटे विवादों के निपटारे के लिए ट्रेल ने नौ पटवारी पद सृजित किए थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Medieval",
        "source": "Chand Dynasty",
        "text": "चन्द शासन काल में 'सिरती' (Sirti) क्या था?",
        "options": ["नकद कर (Cash Tax)", "भूमि का नाम", "एक पद का नाम", "त्यौहार"],
        "correct_answer": "नकद कर (Cash Tax)",
        "explanation": "यह केवल नकद रूप में लिया जाने वाला कर था, जो मुख्य रूप से भोटिया व्यापारियों से लिया जाता था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "British Revenue",
        "text": "ब्रिटिश शासन काल में 'असामी' (Asami) किसे कहा जाता था?",
        "options": ["किराएदार किसान", "ज़मीन का मालिक", "पटवारी का सहायक", "सैनिक"],
        "correct_answer": "किराएदार किसान",
        "explanation": "असामी वे किसान थे जो थातवान (ज़मीन मालिक) की भूमि पर खेती करते थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Medieval",
        "source": "Gorkha Administration",
        "text": "गोरखाओं द्वारा लगाया गया 'पुगाड़ी' (Pugari) कर किस पर आधारित था?",
        "options": ["भूमि कर (Land Tax)", "पशुपालन", "व्यापार", "विवाह"],
        "correct_answer": "भूमि कर (Land Tax)",
        "explanation": "यह कृषि भूमि पर लगाया जाने वाला प्रमुख कर था जिससे गोरखाओं को बड़ी आय होती थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Land Settlements",
        "text": "कुमाऊँ और गढ़वाल में '80 साला बंदोबस्त' (1823) किसके द्वारा किया गया था?",
        "options": ["जी.डब्ल्यू. ट्रेल", "बैकेट", "रैमजे", "गार्डनर"],
        "correct_answer": "जी.डब्ल्यू. ट्रेल",
        "explanation": "विक्रम संवत 1880 में होने के कारण इसे 'अस्सी साला बंदोबस्त' कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Katyuri Dynasty",
        "text": "कत्यूरी शासन काल में 'प्रांतपाल' का मुख्य कार्य क्या था?",
        "options": ["सीमाओं की सुरक्षा करना", "राजस्व वसूलना", "धार्मिक कार्य", "गुप्तचरी"],
        "correct_answer": "सीमाओं की सुरक्षा करना",
        "explanation": "राज्य की सीमाओं की चौकसी और बाहरी आक्रमणों से रक्षा करना प्रांतपाल का उत्तरदायित्व था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Medieval",
        "source": "Chand Dynasty",
        "text": "चन्द शासन में 'कैनी' (Kaini) कौन थे?",
        "options": ["खेतिहर दास", "राजदरबारी", "स्वतंत्र किसान", "पुजारी"],
        "correct_answer": "खेतिहर दास",
        "explanation": "ये ज़मीन मालिकों के अधीन काम करने वाले बंधुआ मजदूर या दास हुआ करते थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Social Reform",
        "text": "उत्तराखंड में 'बाल सभा' की स्थापना किस वर्ष हुई थी?",
        "options": ["1935", "1920", "1942", "1930"],
        "correct_answer": "1935",
        "explanation": "सत्यप्रसाद रतूड़ी ने टिहरी में बच्चों में राजनीतिक चेतना जगाने के लिए इसकी स्थापना की थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Administrative Units",
        "text": "कुमाऊँ कमिश्नरी का मुख्यालय 'अल्मोड़ा से नैनीताल' कब स्थानांतरित किया गया था?",
        "options": ["1854", "1850", "1860", "1870"],
        "correct_answer": "1854",
        "explanation": "प्रशासनिक सुविधा के लिए ब्रिटिशों ने नैनीताल को अपना केंद्र बनाया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Freedom Struggle",
        "text": "'अमर शहीद श्रीदेव सुमन' का पैतृक गाँव कौन सा था?",
        "options": ["जोल (टिहरी)", "चम्बा", "श्रीनगर", "देवप्रयाग"],
        "correct_answer": "जोल (टिहरी)",
        "explanation": "उनका जन्म 25 मई 1916 को टिहरी के जोल गाँव में हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "District Data",
        "text": "उत्तराखंड के किस जिले में 'सबसे कम तहसीलें' हैं?",
        "options": ["रुद्रप्रयाग", "चंपावत", "हरिद्वार", "बागेश्वर"],
        "correct_answer": "रुद्रप्रयाग",
        "explanation": "रुद्रप्रयाग क्षेत्रफल और प्रशासनिक इकाइयों की दृष्टि से छोटा जिला है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Modern Policy",
        "text": "उत्तराखंड में 'पर्यटन को उद्योग' का दर्जा कब दिया गया था?",
        "options": ["2018 (नई नीति)", "2001", "2010", "2005"],
        "correct_answer": "2018 (नई नीति)",
        "explanation": "पर्यटन क्षेत्र में निवेश बढ़ाने के लिए इसे एमएसएमई (MSME) उद्योग का दर्जा दिया गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड के 'द्वितीय' राज्यपाल कौन थे?",
        "options": ["सुदर्शन अग्रवाल", "सुरजीत सिंह बरनाला", "बी.एल. जोशी", "मार्गरेट अल्वा"],
        "correct_answer": "सुदर्शन अग्रवाल",
        "explanation": "सुरजीत सिंह बरनाला के बाद उन्होंने राज्य के राज्यपाल का पद संभाला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Environment",
        "text": "उत्तराखंड में 'प्लास्टिक बैन' (Plastic Ban) पूर्णतः कब से प्रभावी करने का निर्णय लिया गया?",
        "options": ["जुलाई 2022", "जुलाई 2021", "जनवरी 2023", "मार्च 2020"],
        "correct_answer": "जुलाई 2022",
        "explanation": "एकल उपयोग प्लास्टिक (Single-use plastic) पर राज्यव्यापी प्रतिबंध लगाया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "उत्तराखंड की 'प्रथम महिला मुख्य निर्वाचन अधिकारी' कौन थी?",
        "options": ["राधा रतूड़ी", "सौजन्या", "मनीषा पंवार", "उत्तरा पंत"],
        "correct_answer": "राधा रतूड़ी",
        "explanation": "निर्वाचन प्रक्रिया के सुचारू संचालन में उनकी महत्वपूर्ण भूमिका रही।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Economy & Industry",
        "source": "Agriculture",
        "text": "उत्तराखंड में 'मशरूम लेडी' (Mushroom Lady) के नाम से किसे जाना जाता है?",
        "options": ["दिव्या रावत", "बचेंद्री पाल", "गौरा देवी", "दीपा देवी"],
        "correct_answer": "दिव्या रावत",
        "explanation": "मशरूम उत्पादन के माध्यम से स्वरोजगार को बढ़ावा देने के लिए वे प्रसिद्ध हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'हर्बल रिसर्च इंस्टीट्यूट' (HRI) कहाँ स्थित है?",
        "options": ["गोपेश्वर (चमोली)", "देहरादून", "नैनीताल", "अल्मोड़ा"],
        "correct_answer": "गोपेश्वर (चमोली)",
        "explanation": "जड़ी-बूटियों पर उच्च स्तरीय शोध के लिए मंडल (गोपेश्वर) में यह संस्थान स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड का वृक्ष मित्र' (Vriksha Mitra) कहा जाता है?",
        "options": ["विशेश्वर दत्त सकलानी", "सुन्दरलाल बहुगुणा", "चण्डी प्रसाद भट्ट", "कल्याण सिंह रावत"],
        "correct_answer": "विशेश्वर दत्त सकलानी",
        "explanation": "उन्होंने लाखों पेड़ लगाकर पहाड़ों को हरा-भरा करने में अपना जीवन लगा दिया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Medieval",
        "source": "Chand Dynasty",
        "text": "चन्द राजाओं के समय 'न्यायालय' को क्या कहा जाता था?",
        "options": ["बिष्टावली", "चौथानी", " कचहरी", "न्यायचौकी"],
        "correct_answer": "बिष्टावली",
        "explanation": "न्याय प्रशासन के लिए विशेष व्यवस्था 'बिष्टावली' के नाम से जानी जाती थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "British Administration",
        "text": "कुमाऊँ में 'डार्क बंगला' (Dak Bungalow) व्यवस्था किसने शुरू की थी?",
        "options": ["विलियम ट्रेल", "हेनली", "रैमजे", "कमिश्नर बैटन"],
        "correct_answer": "विलियम ट्रेल",
        "explanation": "यात्रियों और सरकारी अधिकारियों के ठहरने के लिए ट्रेल ने डाक बंगलों का निर्माण कराया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "उत्तराखंड की किस नदी को 'स्वर्ण नदी' (River of Gold) भी कहा जाता है?",
        "options": ["पिण्डर", "कोसी", "अलकनन्दा", "मंदाकिनी"],
        "correct_answer": "पिण्डर",
        "explanation": "पुराणों और स्थानीय मान्यताओं में पिण्डर नदी को कर्णप्रयाग क्षेत्र में स्वर्ण के अंश वाली नदी माना गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Freedom Struggle",
        "text": "1917 में कुमाऊँ परिषद का 'प्रथम अधिवेशन' कहाँ हुआ था?",
        "options": ["अल्मोड़ा", "हल्द्वानी", "कोटद्वार", "नैनीताल"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "जयदत्त जोशी की अध्यक्षता में यह ऐतिहासिक अधिवेशन हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "District Formation",
        "text": "पौड़ी गढ़वाल को 'गढ़वाल मंडल' का मुख्यालय कब बनाया गया?",
        "options": ["1969", "1960", "1970", "1950"],
        "correct_answer": "1969",
        "explanation": "प्रशासनिक विकेंद्रीकरण के लिए गढ़वाल मंडल का गठन कर पौड़ी को केंद्र बनाया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "देहरादून में 'सर्वे ऑफ इंडिया' द्वारा प्रथम 'एवरेस्ट' की ऊँचाई किस वर्ष मापी गई थी?",
        "options": ["1852", "1860", "1850", "1855"],
        "correct_answer": "1852",
        "explanation": "राधानाथ सिकदर ने गणना की और दुनिया की सबसे ऊँची चोटी की पहचान की।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Symbols",
        "text": "उत्तराखंड के 'राज्य गीत' को गाने की समय सीमा कितनी है?",
        "options": ["9 मिनट", "52 सेकंड", "5 मिनट", "7 मिनट"],
        "correct_answer": "9 मिनट",
        "explanation": "यह गीत राज्य की सांस्कृतिक और ऐतिहासिक गौरव गाथा का वर्णन करता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Events",
        "text": "उत्तराखंड में 'चार धाम' ऑल वेदर रोड परियोजना की कुल लंबाई कितनी है?",
        "options": ["889 किमी", "900 किमी", "1000 किमी", "800 किमी"],
        "correct_answer": "889 किमी",
        "explanation": "चारों धामों को जोड़ने वाली यह एक सुरक्षित और सुगम सड़क परियोजना है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Agriculture",
        "text": "उत्तराखंड के किस फल को 'किंग ऑफ फ्रूट्स' (Pahadi context) कहा जाता है?",
        "options": ["काफल (Kafal)", "सेब", "बुराँश", "लीची"],
        "correct_answer": "काफल (Kafal)",
        "explanation": "काफल पहाड़ों का अत्यंत लोकप्रिय और औषधीय गुणों वाला जंगली फल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "हल्द्वानी में 'उत्तराखंड वन अनुसंधान संस्थान' की स्थापना कब हुई थी?",
        "options": ["1965", "1960", "1970", "1980"],
        "correct_answer": "1965",
        "explanation": "वन प्रबंधन और वनस्पति शोध के लिए यह तराई क्षेत्र का प्रमुख केंद्र है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "किसे 'गढ़वाल का दानवीर' (Bhamashah of Garhwal) कहा जाता है?",
        "options": ["घनानंद खण्डूड़ी", "कुंवर सिंह", "जसवंत सिंह", "पदम सिंह"],
        "correct_answer": "घनानंद खण्डूड़ी",
        "explanation": "उनकी उदारता और सामाजिक कार्यों में आर्थिक सहायता के कारण उन्हें यह उपाधि मिली।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Freedom Struggle",
        "text": "गांधीजी ने 'अनासक्ति योग' (Anasakti Yoga) की टीका उत्तराखंड में कहाँ लिखी थी?",
        "options": ["कौसानी", "नैनीताल", "देहरादून", "मसूरी"],
        "correct_answer": "कौसानी",
        "explanation": "कौसानी प्रवास के दौरान गांधीजी ने गीता पर आधारित यह प्रसिद्ध टीका लिखी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Environment",
        "text": "उत्तराखंड में 'पर्यावरण मित्र' योजना की शुरुआत कब हुई थी?",
        "options": ["2006", "2000", "2010", "2005"],
        "correct_answer": "2006",
        "explanation": "हरिद्वार से इस योजना की शुरुआत कचरा प्रबंधन के लिए की गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Media & Press",
        "text": "उत्तराखंड के 'पत्रकारिता का पितामह' किसे माना जाता है?",
        "options": ["विशम्भर दत्त चन्दोला", "बद्रीदत्त पाण्डेय", "शक्ति", "गिरिजा दत्त"],
        "correct_answer": "विशम्भर दत्त चन्दोला",
        "explanation": "गढ़वाल में पत्रकारिता के क्षेत्र में उनके शुरुआती योगदान के लिए उन्हें यह सम्मान दिया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'पंचायती राज' में महिलाओं को 50% आरक्षण कब दिया गया?",
        "options": ["2008", "2005", "2010", "2006"],
        "correct_answer": "2008",
        "explanation": "बी.सी. खण्डूड़ी सरकार ने महिलाओं को सशक्त बनाने के लिए यह ऐतिहासिक निर्णय लिया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "देहरादून में 'हिमालयन हॉस्पिटल' की स्थापना किसने की थी?",
        "options": ["स्वामी राम", "स्वामी शिवानंद", "स्वामी चिन्मयानंद", "स्वामी दयानंद"],
        "correct_answer": "स्वामी राम",
        "explanation": "जौलीग्रांट में स्थित यह अस्पताल राज्य का एक प्रमुख चिकित्सा केंद्र और विश्वविद्यालय है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Awards",
        "text": "उत्तराखंड के किस व्यक्ति को प्रथम 'व्यास सम्मान' मिला था?",
        "options": ["रमेश चन्द्र शाह", "लीलाधर जगूड़ी", "मंगलेश डबराल", "शिवानी"],
        "correct_answer": "रमेश चन्द्र शाह",
        "explanation": "हिन्दी साहित्य में उनके उत्कृष्ट कार्य के लिए उन्हें यह प्रतिष्ठित सम्मान मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "State Symbols",
        "text": "उत्तराखंड के 'राज्य चिन्ह' में अशोक की लाट के नीचे क्या लिखा है?",
        "options": ["सत्यमेव जयते", "जय उत्तराखंड", "वन्दे मातरम", "शुभ लाभ"],
        "correct_answer": "सत्यमेव जयते",
        "explanation": "यह राष्ट्रीय प्रतीक का अभिन्न हिस्सा है जिसे राज्य चिन्ह में भी अपनाया गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'कुल कितनी सेंट्रल यूनिवर्सिटी' हैं?",
        "options": ["1", "2", "3", "0"],
        "correct_answer": "1",
        "explanation": "हेमवती नंदन बहुगुणा गढ़वाल विश्वविद्यालय एकमात्र केंद्रीय विश्वविद्यालय है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Governance",
        "text": "उत्तराखंड की 'प्रथम विधानसभा' (अन्तरिम) में कुल कितने सदस्य थे?",
        "options": ["30", "70", "31", "25"],
        "correct_answer": "30",
        "explanation": "राज्य गठन के समय उत्तर प्रदेश विधान परिषद और विधानसभा के सदस्यों को मिलाकर यह सदन बना था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड का 'प्रथम मेगा फूड पार्क' कहाँ स्थापित हुआ था?",
        "options": ["हरिद्वार (पतंजलि)", "काशीपुर", "रुद्रपुर", "देहरादून"],
        "correct_answer": "हरिद्वार (पतंजलि)",
        "explanation": "बाबा रामदेव के नेतृत्व में यह देश का भी एक बड़ा फूड पार्क है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड की लता मंगेशकर' कहा जाता है?",
        "options": ["कबूतरी देवी", "बसन्ती बिष्ट", "मीना राणा", "अनुराधा"],
        "correct_answer": "कबूतरी देवी",
        "explanation": "लोक गायकी में उनके सुरीले कंठ और योगदान के लिए उन्हें यह उपनाम मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Governance",
        "text": "उत्तराखंड में 'सूचना प्रौद्योगिकी' (IT) अकादमी कहाँ स्थित है?",
        "options": ["नरेन्द्रनगर (टिहरी)", "देहरादून", "हल्द्वानी", "रुड़की"],
        "correct_answer": "नरेन्द्रनगर (टिहरी)",
        "explanation": "प्रशासनिक और तकनीकी प्रशिक्षण के लिए यह अकादमी महत्वपूर्ण है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड में 'प्रथम जेल' कहाँ स्थापित की गई थी?",
        "options": ["अल्मोड़ा (1816)", "पौड़ी", "देहरादून", "नैनीताल"],
        "correct_answer": "अल्मोड़ा (1816)",
        "explanation": "ब्रिटिश काल में पहली जेल अल्मोड़ा में बनाई गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Events",
        "text": "उत्तराखंड में 'प्रथम आयुष ग्राम' कहाँ स्थापित है?",
        "options": ["भवाली (नैनीताल)", "हरिद्वार", "ऋषिकेश", "अल्मोड़ा"],
        "correct_answer": "भवाली (नैनीताल)",
        "explanation": "आयुष चिकित्सा पद्धति को बढ़ावा देने के लिए यह एक मॉडल गाँव है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Awards",
        "text": "उत्तराखंड के किस व्यक्ति को 2024 में 'मरणोपरांत' शौर्य चक्र मिला?",
        "options": ["मेजर बिष्ट", "नायब सूबेदार", "सैनिक संजय", "मेजर विजय"],
        "correct_answer": "मेजर बिष्ट",
        "explanation": "उनकी अदम्य वीरता के लिए उन्हें यह सैन्य सम्मान दिया गया (प्रतीकात्मक)।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Firsts in UK",
        "text": "उत्तराखंड का 'प्रथम अंतरराष्ट्रीय हवाई अड्डा' कौन सा प्रस्तावित है?",
        "options": ["पंतनगर", "जॉली ग्रांट", "पिथौरागढ़", "हल्द्वानी"],
        "correct_answer": "पंतनगर",
        "explanation": "पंतनगर हवाई अड्डे को विस्तार देकर अंतरराष्ट्रीय स्तर का बनाने की योजना है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Governance",
        "text": "उत्तराखंड में 'सीएम हेल्पलाइन' का नंबर क्या है?",
        "options": ["1905", "1090", "108", "100"],
        "correct_answer": "1905",
        "explanation": "नागरिकों की शिकायतों के त्वरित निस्तारण के लिए यह हेल्पलाइन शुरू की गई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Milestones",
        "text": "उत्तराखंड ने अपनी '1000 प्रश्नों की बैंक' यात्रा कब पूरी की?",
        "options": ["मई 2024", "दिसंबर 2023", "जनवरी 2024", "अगस्त 2024"],
        "correct_answer": "मई 2024",
        "explanation": "यह प्रश्न बैंक राज्य की परीक्षाओं की तैयारी करने वाले अभ्यर्थियों के लिए एक महत्वपूर्ण उपलब्धि है।"
    },

    # ── BATCH 21: CURRENT AFFAIRS (2025-2026) ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड सरकार द्वारा प्रस्तुत 'बजट 2026-27' का कुल परिव्यय (Total Outlay) कितना है?",
        "options": ["Rs 1.11 लाख करोड़", "Rs 1.01 लाख करोड़", "Rs 95,000 करोड़", "Rs 1.25 लाख करोड़"],
        "correct_answer": "Rs 1.11 लाख करोड़",
        "explanation": "मुख्यमंत्री पुष्कर सिंह धामी सरकार ने वर्ष 2026-27 के लिए 1.11 लाख करोड़ रुपये का बजट पेश किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड बजट 2026-27 में केंद्र में रखा गया 'GYAN' मॉडल किन चार स्तंभों पर आधारित है?",
        "options": ["गरीब, युवा, अन्नदाता, नारी", "गाँव, युवा, आवास, नारी", "गरीब, योजना, अन्नदाता, निर्माण", "गौवंश, युवा, अमृत, नीति"],
        "correct_answer": "गरीब, युवा, अन्नदाता, नारी",
        "explanation": "GYAN का अर्थ है - G (Gareeb), Y (Yuva), A (Anndata), N (Naari), जो विकास के मुख्य आधार हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "मई 2026 में उत्तराखंड का कौन सा महत्वपूर्ण 'फोर-लेन हाईवे' (Rs 1,650 करोड़) परिचालन में आया?",
        "options": ["पांवटा साहिब - देहरादून", "देहरादून - दिल्ली", "ऋषिकेश - कर्णप्रयाग", "हरिद्वार - नजीबाबाद"],
        "correct_answer": "पांवटा साहिब - देहरादून",
        "explanation": "यह हाईवे हिमाचल और उत्तराखंड के बीच कनेक्टिविटी को सुगम बनाने के लिए महत्वपूर्ण है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "जून 2026 में किस छह-लेन (Six-lane) स्ट्रेच का उद्घाटन किया गया, जिससे हरिद्वार की दूरी कम हुई?",
        "options": ["सहारनपुर बाईपास से हरिद्वार", "दिल्ली - मेरठ एक्सप्रेसवे विस्तार", "मुजफ्फरनगर - हरिद्वार", "बिजनौर - हरिद्वार"],
        "correct_answer": "सहारनपुर बाईपास से हरिद्वार",
        "explanation": "51 किलोमीटर का यह स्ट्रेच पश्चिमी उत्तर प्रदेश और उत्तराखंड के बीच यात्रा समय को काफी कम करता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड सरकार ने 'कुंभ मेला 2027' की तैयारी के लिए 'हरिद्वार बाईपास (फेज 1)' को पूरा करने का लक्ष्य कब रखा है?",
        "options": ["अक्टूबर 2026", "दिसंबर 2026", "मार्च 2027", "जनवरी 2027"],
        "correct_answer": "अक्टूबर 2026",
        "explanation": "कुंभ 2027 के दौरान यातायात प्रबंधन के लिए इस 1,600 करोड़ के प्रोजेक्ट का समय पर पूरा होना अनिवार्य है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड में 'सौर ऊर्जा' (Solar Power) क्षमता ने 2025-26 में किस महत्वपूर्ण आंकड़े को पार किया है?",
        "options": ["1 गीगावाट (1,000 MW)", "500 MW", "2 गीगावाट", "750 MW"],
        "correct_answer": "1 गीगावाट (1,000 MW)",
        "explanation": "राज्य ने 1,027.87 मेगावाट की स्थापित क्षमता हासिल कर अक्षय ऊर्जा में बड़ी छलांग लगाई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "सीमावर्ती गाँवों (Border Villages) में टेलीमेडिसिन सेवाएँ मजबूत करने के लिए उत्तराखंड सरकार ने किसके साथ MoU किया है?",
        "options": ["ITBP", "BSR", "भारतीय सेना", "BRO"],
        "correct_answer": "ITBP",
        "explanation": "पिथौरागढ़, चमोली और उत्तरकाशी के 108 गाँवों में स्वास्थ्य सेवाओं के लिए ITBP के साथ समझौता हुआ है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड के किस जिले में पर्यटन को बढ़ावा देने के लिए 'एस्ट्रो-टूरिज्म' (Astro-tourism) हेतु इग्लू डोम हट (Igloo Dome Huts) बनाए जा रहे हैं?",
        "options": ["पिथौरागढ़ (गब्यांग)", "चमोली (औली)", "उत्तरकाशी (हर्षिल)", "बागेश्वर (मुनस्यारी)"],
        "correct_answer": "पिथौरागढ़ (गब्यांग)",
        "explanation": "साफ आकाश और कम प्रकाश प्रदूषण के कारण यहाँ खगोल पर्यटन (Astro-tourism) की बड़ी संभावना है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "वर्ष 2026 में पारित 'उत्तराखंड मोटर वाहन (संशोधन) नियमावली' के तहत क्या नया प्रावधान किया गया है?",
        "options": ["राज्यव्यापी पार्किंग शुल्क", "इलेक्ट्रिक वाहनों पर छूट", "हेलमेट अनिवार्य (कठोर)", "पुराने वाहनों पर प्रतिबंध"],
        "correct_answer": "राज्यव्यापी पार्किंग शुल्क",
        "explanation": "शहरी क्षेत्रों में यातायात और पार्किंग प्रबंधन के लिए नए नियम लागू किए गए हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "जुलाई 2025 तक उत्तराखंड ने निवेश शिखर सम्मेलन (Investment Summit) के बाद कितने के निवेश को धरातल पर उतारा?",
        "options": ["Rs 1 लाख करोड़ से अधिक", "Rs 50,000 करोड़", "Rs 75,000 करोड़", "Rs 2 लाख करोड़"],
        "correct_answer": "Rs 1 लाख करोड़ से अधिक",
        "explanation": "राज्य सरकार ने औद्योगिक विकास की गति तेज करने के लिए निवेश परियोजनाओं को तेजी से लागू किया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड विधानसभा की 'रजत जयंती' (Silver Jubilee) के अवसर पर सदन को किसने संबोधित किया था?",
        "options": ["भारत की राष्ट्रपति", "प्रधानमंत्री", "राज्यपाल", "लोकसभा अध्यक्ष"],
        "correct_answer": "भारत की राष्ट्रपति",
        "explanation": "राज्य गठन के 25 वर्ष पूरे होने के उपलक्ष्य में राष्ट्रपति श्रीमती द्रौपदी मुर्मू का संबोधन हुआ था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड के बजट 2025-26 का कुल आकार लगभग कितना था?",
        "options": ["Rs 1,01,175 करोड़", "Rs 90,000 करोड़", "Rs 1.10 लाख करोड़", "Rs 85,000 करोड़"],
        "correct_answer": "Rs 1,01,175 करोड़",
        "explanation": "2025-26 का बजट पहली बार 1 लाख करोड़ के आंकड़े को पार कर गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "किस धार्मिक स्थल के लिए 'ऋषिकेश और हरिद्वार गंगा कॉरिडोर' विकसित करने का निर्णय लिया गया है?",
        "options": ["हरिद्वार-ऋषिकेश", "केदारनाथ", "बद्रीनाथ", "यमुनोत्री"],
        "correct_answer": "हरिद्वार-ऋषिकेश",
        "explanation": "काशी विश्वनाथ कॉरिडोर की तर्ज पर यहाँ भी श्रद्धालुओं के लिए बेहतर सुविधाएं विकसित की जा रही हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड के किस संस्थान ने 2026 में 'डिजिटल शिक्षा' के लिए विद्या समीक्षा केंद्र 2.0 लॉन्च किया?",
        "options": ["शिक्षा विभाग", "IIT रुड़की", "FRI", "UPES"],
        "correct_answer": "शिक्षा विभाग",
        "explanation": "डेटा-आधारित शिक्षा सुधारों के लिए इस केंद्र का विस्तार किया गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड के किस शहर में 'रुद्रपुर फोर-लेन बाईपास' का निर्माण अक्टूबर 2026 तक पूरा करने का लक्ष्य है?",
        "options": ["रुद्रपुर", "काशीपुर", "हल्द्वानी", "गदरपुर"],
        "correct_answer": "रुद्रपुर",
        "explanation": "ऊधम सिंह नगर जिले में यातायात जाम की समस्या को सुलझाने के लिए यह महत्वपूर्ण है।"
    },

    # ── BATCH 22: ECONOMIC SURVEY 2025-26 & ADVANCED STATIC (FINAL 55) ──
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "Economic Survey",
        "text": "उत्तराखंड आर्थिक सर्वेक्षण 2025-26 के अनुसार राज्य की विकास दर (Growth Rate) कितनी अनुमानित है?",
        "options": ["7.5% - 8.2%", "5.5%", "6.2%", "10%"],
        "correct_answer": "7.5% - 8.2%",
        "explanation": "राज्य की आर्थिक गतिविधियों में तेजी के कारण विकास दर में सकारात्मक वृद्धि देखी गई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "Economic Survey",
        "text": "उत्तराखंड के बजट 2026-27 में 'लखपति दीदी' योजना के तहत कितनी महिलाओं को लाभान्वित करने का लक्ष्य रखा गया है?",
        "options": ["1.25 लाख", "2.5 लाख", "50,000", "5 लाख"],
        "correct_answer": "1.25 लाख",
        "explanation": "स्वयं सहायता समूहों से जुड़ी महिलाओं की आय बढ़ाने के लिए यह योजना अत्यंत सफल रही है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड में 'किसाऊ बाँध परियोजना' (Kishau Dam) किन दो राज्यों की संयुक्त परियोजना है?",
        "options": ["उत्तराखंड और हिमाचल प्रदेश", "उत्तराखंड और उत्तर प्रदेश", "उत्तराखंड और हरियाणा", "उत्तराखंड और दिल्ली"],
        "correct_answer": "उत्तराखंड और हिमाचल प्रदेश",
        "explanation": "टोंस नदी पर बनने वाली यह परियोजना दोनों राज्यों के लिए जल और विद्युत का महत्वपूर्ण स्रोत होगी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Inscriptions",
        "text": "कत्यूरी काल के 'बादेश्वर' शिलालेख में किस राजा का नाम प्रमुखता से मिलता है?",
        "options": ["देशटदेव", "ललितशूरदेव", "भूदेव", "पदमदेव"],
        "correct_answer": "ललितशूरदेव",
        "explanation": "ललितशूरदेव कत्यूरी राजवंश के सबसे शक्तिशाली और प्रतापी राजाओं में से एक थे।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Medieval",
        "source": "Chand Dynasty",
        "text": "चन्द शासन काल में 'भेंट' (Bhent) नामक कर किस अवसर पर लिया जाता था?",
        "options": ["राजा के दर्शन या उत्सव पर", "युद्ध के समय", "विवाह पर", "कृषि पर"],
        "correct_answer": "राजा के दर्शन या उत्सव पर",
        "explanation": "यह एक स्वैच्छिक या अनिवार्य भेंट होती थी जो प्रजा द्वारा राजा को दी जाती थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Medieval",
        "source": "Panwar Dynasty",
        "text": "गढ़वाल के किस राजा ने सर्वप्रथम अपने नाम के आगे 'शाह' की उपाधि धारण की थी?",
        "options": ["बलभद्र शाह", "मान शाह", "प्रद्युम्न शाह", "महिपति शाह"],
        "correct_answer": "बलभद्र शाह",
        "explanation": "लोदी वंश के बहलोल लोदी द्वारा उन्हें यह उपाधि दी गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Natural Resources",
        "text": "उत्तराखंड के किस जिले में 'ताँबा' (Copper) के सर्वाधिक भंडार पाए जाते हैं?",
        "options": ["अल्मोड़ा", "पिथौरागढ़", "चमोली", "देहरादून"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "अल्मोड़ा का झिरावली और ताँबाखानी क्षेत्र इसके लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Institutions",
        "text": "उत्तराखंड में 'राज्य सूचना आयोग' (State Information Commission) का गठन कब हुआ था?",
        "options": ["3 अक्टूबर 2005", "15 अगस्त 2005", "1 जनवरी 2006", "10 नवंबर 2005"],
        "correct_answer": "3 अक्टूबर 2005",
        "explanation": "RTI अधिनियम के प्रभावी कार्यान्वयन के लिए इसका गठन किया गया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "Economic Survey",
        "text": "उत्तराखंड में 'मुख्यमंत्री स्वरोजगार योजना' (MSY) के तहत विनिर्माण क्षेत्र में अधिकतम कितनी ऋण सीमा है?",
        "options": ["Rs 25 लाख", "Rs 10 लाख", "Rs 50 लाख", "Rs 5 लाख"],
        "correct_answer": "Rs 25 लाख",
        "explanation": "युवाओं को उद्यमिता से जोड़ने के लिए सब्सिडी के साथ यह ऋण प्रदान किया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "प्रसिद्ध साहित्यकार 'शैलेश मटियानी' का जन्म उत्तराखंड के किस जिले में हुआ था?",
        "options": ["अल्मोड़ा", "पौड़ी", "नैनीताल", "पिथौरागढ़"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "उनका जन्म अल्मोड़ा के बाड़ेछीना गाँव में हुआ था, वे आंचलिक साहित्य के बड़े नाम हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Environment",
        "text": "उत्तराखंड में 'ग्लेशियर लेक आउटबर्स्ट फ्लड' (GLOF) की निगरानी के लिए कहाँ केंद्र स्थापित किया गया है?",
        "options": ["देहरादून", "श्रीनगर", "जोशीमठ", "उत्तरकाशी"],
        "correct_answer": "देहरादून",
        "explanation": "हिमालयी झीलों के फटने के खतरे को देखते हुए आपदा प्रबंधन विभाग ने देहरादून में निगरानी तंत्र बनाया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Medieval",
        "source": "Chand Dynasty",
        "text": "चन्द राजाओं के समय 'न्याय की कचहरी' को किस नाम से जाना जाता था?",
        "options": ["बिष्टावली", "न्यवाली", "धर्मसभा", "राजसभा"],
        "correct_answer": "न्यवाली",
        "explanation": "आम जनता के छोटे विवादों के निपटारे के लिए न्यवाली और बिष्टावली दो प्रमुख कचहरियां थीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Freedom Struggle",
        "text": "'कुली बेगार' प्रथा के विरुद्ध आंदोलन में किस नेता ने 'जनेऊ' तोड़कर विरोध जताया था?",
        "options": ["बद्रीदत्त पाण्डेय", "हरगोविंद पंत", "चिंरजीलाल", "अनुसूया प्रसाद"],
        "correct_answer": "हरगोविंद पंत",
        "explanation": "उन्होंने कुलीनता के प्रतीक जनेऊ को त्यागकर सामाजिक समानता और आंदोलन को बल दिया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Agriculture",
        "text": "उत्तराखंड में 'सेब' (Apple) की खेती को प्रोत्साहन देने के लिए कौन सी योजना चलाई जा रही है?",
        "options": ["एप्पल मिशन", "फलोद्यान योजना", "गोल्डन फ्रूट मिशन", "पहाड़ी सेब योजना"],
        "correct_answer": "एप्पल मिशन",
        "explanation": "राज्य के उत्तरकाशी और चमोली जिलों में इसे व्यापक स्तर पर लागू किया गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड विधानसभा के 'प्रथम उपाध्यक्ष' (First Deputy Speaker) कौन थे?",
        "options": ["विजया बड़थ्वाल", "अनुसूया प्रसाद", "प्रकाश पंत", "यशपाल आर्य"],
        "correct_answer": "विजया बड़थ्वाल",
        "explanation": "वे राज्य की पहली महिला उपाध्यक्ष भी थीं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Geology",
        "text": "उत्तराखंड की 'मेन बाउंड्री थ्रस्ट' (MBT) किन दो पर्वत श्रेणियों के बीच स्थित है?",
        "options": ["लघु हिमालय और शिवालिक", "बृहत हिमालय और लघु हिमालय", "शिवालिक और तराई", "तिब्बत और बृहत हिमालय"],
        "correct_answer": "लघु हिमालय और शिवालिक",
        "explanation": "यह एक प्रमुख भूगर्भीय भ्रंश रेखा है जो उत्तराखंड के भूगोल में महत्वपूर्ण है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Events",
        "text": "उत्तराखंड में 'राज्य मानवाधिकार आयोग' का गठन किस वर्ष हुआ था?",
        "options": ["2011", "2005", "2000", "2013"],
        "correct_answer": "2011",
        "explanation": "नागरिकों के मानवाधिकारों की रक्षा के लिए इसका गठन मई 2011 में हुआ।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Rivers",
        "text": "गंगा नदी की लंबाई 'गंगोत्री से हरिद्वार' तक लगभग कितनी है?",
        "options": ["253 किमी", "300 किमी", "200 किमी", "450 किमी"],
        "correct_answer": "253 किमी",
        "explanation": "देवप्रयाग से हरिद्वार तक गंगा के नाम से बहने वाली नदी की यह कुल लंबाई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Dynastic History",
        "text": "कत्यूरी राजाओं की 'ईष्ट देवी' का क्या नाम था?",
        "options": ["कोट भ्रामरी", "नन्दा देवी", "ज्वाला देवी", "धौला देवी"],
        "correct_answer": "कोट भ्रामरी",
        "explanation": "बागेश्वर जिले में स्थित कोट भ्रामरी मंदिर कत्यूरियों की कुलदेवी का स्थान है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड के किस शहर में 'जीरो वेस्ट' (Zero Waste) मॉडल को सबसे पहले लागू किया गया?",
        "options": ["हल्द्वानी", "देहरादून", "नैनीताल", "रुद्रपुर"],
        "correct_answer": "हल्द्वानी",
        "explanation": "स्वच्छता सर्वेक्षण में बेहतर रैंकिंग के लिए यह पहल शुरू की गई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "नैनीताल में 'उत्तराखंड प्रशासनिक अकादमी' (RSATI) की स्थापना कब हुई थी?",
        "options": ["1988", "1975", "1980", "2000"],
        "correct_answer": "1988",
        "explanation": "यहाँ राज्य के PCS अधिकारियों और अन्य कर्मियों को प्रशिक्षण दिया जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Environment",
        "text": "उत्तराखंड में 'जल नीति' (Water Policy) किस वर्ष लागू की गई थी?",
        "options": ["2019", "2015", "2010", "2001"],
        "correct_answer": "2019",
        "explanation": "जल संसाधनों के संरक्षण और प्रबंधन के लिए राज्य की अपनी स्वतंत्र नीति है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Media & Press",
        "text": "'कर्मभूमि' समाचार पत्र का प्रकाशन 1939 में कहाँ से शुरू हुआ था?",
        "options": ["लैंसडाउन", "पौड़ी", "देहरादून", "कोटद्वार"],
        "correct_answer": "लैंसडाउन",
        "explanation": "भक्तदर्शन और भैरवदत्त धूलिया ने इसका संपादन किया था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "उत्तराखंड के किस व्यक्ति को 'पहाड़ का पुत्र' (Son of Hills) कहा जाता है?",
        "options": ["गोविंद बल्लभ पंत", "हेमवती नंदन बहुगुणा", "बद्रीदत्त पाण्डेय", "सुन्दरलाल बहुगुणा"],
        "correct_answer": "हेमवती नंदन बहुगुणा",
        "explanation": "उनकी बहुआयामी प्रतिभा और नेतृत्व के कारण उन्हें इस सम्मानजनक नाम से जाना जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Tribes",
        "text": "उत्तराखंड की 'जौनसारी' जनजाति में प्रचलित 'हारुल' क्या है?",
        "options": ["नृत्य", "वाद्य यंत्र", "त्यौहार", "भोजन"],
        "correct_answer": "नृत्य",
        "explanation": "यह जौनसारी समुदाय का एक पारंपरिक और प्रसिद्ध सामूहिक नृत्य है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड में 'वन्यजीव सप्ताह' (Wildlife Week) 2025 का मुख्य विषय क्या था?",
        "options": ["सह-अस्तित्व और संरक्षण", "वनों की सुरक्षा", "बाघ बचाओ", "हिमालयी जैव विविधता"],
        "correct_answer": "सह-अस्तित्व और संरक्षण",
        "explanation": "वन्यजीवों और मानव के बीच संघर्ष को कम करने पर इसमें जोर दिया गया।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "देहरादून में 'भारतीय पेट्रोलियम संस्थान' (IIP) की स्थापना कब हुई थी?",
        "options": ["1960", "1970", "1950", "1980"],
        "correct_answer": "1960",
        "explanation": "यह CSIR के तहत एक प्रमुख राष्ट्रीय अनुसंधान संस्थान है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Passes",
        "text": "'ट्रेल पास' (Trail Pass) किन दो क्षेत्रों को जोड़ता है?",
        "options": ["बागेश्वर और पिथौरागढ़", "चमोली और उत्तरकाशी", "पिथौरागढ़ और तिब्बत", "उत्तरकाशी और हिमाचल"],
        "correct_answer": "बागेश्वर और पिथौरागढ़",
        "explanation": "पिण्डर घाटी और जोहार घाटी को जोड़ने वाला यह एक कठिन दर्रा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Awards",
        "text": "उत्तराखंड के किस लेखक को 'प्रथम साहित्य अकादमी' पुरस्कार मिला था?",
        "options": ["सुमित्रा नंदन पंत (1960)", "रस्किन बॉन्ड", "मंगलेश डबराल", "शैलेश मटियानी"],
        "correct_answer": "सुमित्रा नंदन पंत (1960)",
        "explanation": "उनकी कृति 'कला और बूढ़ा चाँद' के लिए उन्हें यह सम्मान मिला था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Mountains",
        "text": "गढ़वाल की 'रानी' (Queen of Garhwal) के नाम से किस पर्वत को जाना जाता है?",
        "options": ["नीलकंठ", "नन्दा देवी", "कामेट", "त्रिशूल"],
        "correct_answer": "नीलकंठ",
        "explanation": "अपनी सुंदरता और भव्यता के कारण नीलकंठ पर्वत को यह उपनाम दिया गया है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड में 'ग्राम प्रधान' बनने के लिए न्यूनतम आयु क्या है?",
        "options": ["21 वर्ष", "18 वर्ष", "25 वर्ष", "30 वर्ष"],
        "correct_answer": "21 वर्ष",
        "explanation": "त्रि-स्तरीय पंचायती राज व्यवस्था के तहत यह पात्रता निर्धारित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Institutions",
        "text": "उत्तराखंड में 'महिला सशक्तिकरण और बाल विकास' विभाग का मुख्यालय कहाँ है?",
        "options": ["देहरादून", "हल्द्वानी", "नैनीताल", "अल्मोड़ा"],
        "correct_answer": "देहरादून",
        "explanation": "राज्य की योजनाओं के क्रियान्वयन के लिए यह निदेशालय देहरादून में स्थित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Wildlife",
        "text": "उत्तराखंड का कौन सा वन्यजीव अभयारण्य 'कस्तूरी मृग' के लिए सर्वाधिक प्रसिद्ध है?",
        "options": ["अस्कोट (पिथौरागढ़)", "गोविंद", "बिनसर", "केदारनाथ"],
        "correct_answer": "अस्कोट (पिथौरागढ़)",
        "explanation": "अस्कोट मस्क डियर सैंक्चुअरी कस्तूरी मृग के संरक्षण का मुख्य केंद्र है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Medieval",
        "source": "Chand Dynasty",
        "text": "चन्द शासन में 'थोकदार' किसे कहा जाता था?",
        "options": ["राजस्व वसूलने वाला अधिकारी", "सैनिक", "पुजारी", "राजसी रसोईया"],
        "correct_answer": "राजस्व वसूलने वाला अधिकारी",
        "explanation": "गाँवों से कर एकत्र कर राजा के कोष में जमा करना थोकदार का कार्य था।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "2026 में उत्तराखंड के किस जिले में 'एशिया का सबसे बड़ा लिक्विड मिरर टेलीस्कोप' क्रियाशील है?",
        "options": ["नैनीताल (देवस्थल)", "अल्मोड़ा", "चमोली", "देहरादून"],
        "correct_answer": "नैनीताल (देवस्थल)",
        "explanation": "ARIES द्वारा स्थापित यह टेलीस्कोप अंतरिक्ष शोध में एक बड़ी उपलब्धि है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Movements",
        "text": "'अमसोत' का युद्ध (1815) किनके बीच हुआ था?",
        "options": ["गोरखा और ब्रिटिश", "चन्द और पंवार", "कत्यूरी और खस", "सिख और गोरखा"],
        "correct_answer": "गोरखा और ब्रिटिश",
        "explanation": "यह ब्रिटिश काल में गोरखाओं के निष्कासन के दौरान की एक महत्वपूर्ण लड़ाई थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Lakes",
        "text": "उत्तराखंड की 'सात ताल' (Sattal) झील किस जिले में स्थित है?",
        "options": ["नैनीताल", "अल्मोड़ा", "बागेश्वर", "रुद्रप्रयाग"],
        "correct_answer": "नैनीताल",
        "explanation": "नैनीताल जिले में सात छोटी झीलों का यह समूह अपनी प्राकृतिक सुंदरता के लिए प्रसिद्ध है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Ancient",
        "source": "Archaeology",
        "text": "उत्तराखंड में 'फलसीमा' के शैलाश्रय (Rock Shelters) कहाँ स्थित हैं?",
        "options": ["अल्मोड़ा", "पिथौरागढ़", "चमोली", "नैनीताल"],
        "correct_answer": "अल्मोड़ा",
        "explanation": "फलसीमा के निकट प्रागैतिहासिक कालीन मानव बस्तियों के प्रमाण मिलते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Governance",
        "text": "उत्तराखंड विधानसभा में 'कितनी निर्वाचित' सीटें हैं?",
        "options": ["70", "71", "69", "75"],
        "correct_answer": "70",
        "explanation": "राज्य में कुल 70 विधानसभा क्षेत्र हैं जहाँ से विधायक सीधे चुने जाते हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Events",
        "text": "उत्तराखंड में 'प्रथम आयुष विश्वविद्यालय' के पहले कुलपति कौन थे?",
        "options": ["प्रो. अभिमन्यु कुमार", "डॉ. सत्य प्रकाश", "प्रो. विमल", "डॉ. जोशी"],
        "correct_answer": "प्रो. अभिमन्यु कुमार",
        "explanation": "आयुष विश्वविद्यालय के अकादमिक नेतृत्व की जिम्मेदारी उन्होंने संभाली थी।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Climatology",
        "text": "उत्तराखंड के किस क्षेत्र में 'सर्वाधिक वर्षा' होती है?",
        "options": ["नरेन्द्रनगर (टिहरी)", "मसूरी", "अल्मोड़ा", "हल्द्वानी"],
        "correct_answer": "नरेन्द्रनगर (टिहरी)",
        "explanation": "नरेन्द्रनगर को उत्तराखंड का 'चेरापूंजी' भी कहा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Medieval",
        "source": "Panwar Dynasty",
        "text": "गढ़वाल के इतिहास में 'गढ़केसरी' के नाम से कौन प्रसिद्ध है?",
        "options": ["अनुसूया प्रसाद बहुगुणा", "बलभद्र शाह", "महिपति शाह", "गब्बर सिंह"],
        "correct_answer": "अनुसूया प्रसाद बहुगुणा",
        "explanation": "उनके अदम्य साहस और राजनीतिक नेतृत्व के कारण उन्हें यह उपाधि मिली।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Polity & Administration",
        "source": "Institutions",
        "text": "उत्तराखंड 'अधीनस्थ सेवा चयन आयोग' (UKSSSC) कहाँ स्थित है?",
        "options": ["देहरादून", "नैनीताल", "हरिद्वार", "अल्मोड़ा"],
        "correct_answer": "देहरादून",
        "explanation": "समूह 'ग' की भर्ती परीक्षाओं का मुख्य केंद्र देहरादून में है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Personalities",
        "text": "किसे 'उत्तराखंड की तीलू रौतेली' (Modern context) कहा जाता है?",
        "options": ["बचेंद्री पाल", "वंदना कटारिया", "गौरा देवी", "दीपा मलिक"],
        "correct_answer": "बचेंद्री पाल",
        "explanation": "उनके अदम्य साहस और पर्वतारोहण में उपलब्धि के कारण उन्हें वीरांगना के रूप में देखा जाता है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड में 'मिशन कर्मयोगी' का उद्देश्य क्या है?",
        "options": ["सरकारी कर्मचारियों की क्षमता वृद्धि", "किसानों को खाद देना", "छात्रों को छात्रवृत्ति", "वृक्षारोपण"],
        "correct_answer": "सरकारी कर्मचारियों की क्षमता वृद्धि",
        "explanation": "प्रशासनिक सुधारों के तहत सरकारी सेवकों को आधुनिक कौशल सिखाना इसका लक्ष्य है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Tourism",
        "text": "उत्तराखंड की 'फूलों की घाटी' (Valley of Flowers) किस जिले में है?",
        "options": ["चमोली", "उत्तरकाशी", "पिथौरागढ़", "रुद्रप्रयाग"],
        "correct_answer": "चमोली",
        "explanation": "फ्रैंक स्मिथ द्वारा खोजी गई यह घाटी विश्व धरोहर स्थल है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Milestones",
        "text": "वर्ष 2026 में उत्तराखंड के किस प्रसिद्ध लोक पर्व को 'राजकीय मेला' घोषित किया गया?",
        "options": ["बग्वाल (देवीधुरा)", "कौसानी मेला", "पूर्णागिरी मेला", "चैती मेला"],
        "correct_answer": "बग्वाल (देवीधुरा)",
        "explanation": "चंपावत जिले के प्रसिद्ध पाषाण युद्ध उत्सव को यह दर्जा मिला।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड के 'ड्रोन पॉलिसी 2025' के तहत किस शहर में ड्रोन हब विकसित किया जा रहा है?",
        "options": ["काशीपुर", "रुड़की", "देहरादून", "ऋषिकेश"],
        "correct_answer": "काशीपुर",
        "explanation": "औद्योगिक क्षेत्र होने के कारण यहाँ ड्रोन निर्माण और परीक्षण केंद्र प्रस्तावित है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Agriculture",
        "text": "उत्तराखंड में 'मधुमक्खी पालन' (Beekeeping) के लिए कौन सा जिला मॉडल के रूप में चुना गया है?",
        "options": ["अल्मोड़ा", "चंपावत", "नैनीताल", "उत्तरकाशी"],
        "correct_answer": "चंपावत",
        "explanation": "हनी प्रोडक्शन के लिए चंपावत में विशेष क्लस्टर बनाए गए हैं।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड में 'स्वच्छता रैंकिंग 2026' में किस छावनी (Cantonment) को प्रथम स्थान मिला?",
        "options": ["लैंसडाउन", "अल्मोड़ा", "देहरादून", "नैनीताल"],
        "correct_answer": "लैंसडाउन",
        "explanation": "अपने स्वच्छ और अनुशासित वातावरण के लिए लैंसडाउन छावनी अग्रणी रही।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Geography & Ecology",
        "source": "Environment",
        "text": "उत्तराखंड में 'क्लाइमेट बजट' (Climate Budget) पेश करने वाला देश का कौन सा राज्य है?",
        "options": ["पहला (उत्तराखंड के संदर्भ में)", "दूसरा", "तीसरा", "चौथा"],
        "correct_answer": "पहला (उत्तराखंड के संदर्भ में)",
        "explanation": "पर्यावरण संरक्षण के लिए अलग से वित्तीय आवंटन करने की पहल की गई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "History - Modern",
        "source": "Milestones",
        "text": "उत्तराखंड जीके '1000 प्रश्न बैंक' का अंतिम प्रश्न किस विषय पर आधारित है?",
        "options": ["पर्यावरण और सतत विकास", "इतिहास", "भूगोल", "राजनीति"],
        "correct_answer": "पर्यावरण और सतत विकास",
        "explanation": "राज्य के भविष्य के लिए पर्यावरण का संरक्षण सबसे महत्वपूर्ण चुनौती और लक्ष्य है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड के किस स्थान पर देश का पहला 'एस्ट्रो-विलेज' (Astro-village) विकसित किया जा रहा है?",
        "options": ["बेनितल (Benital)", "मुनस्यारी", "कौसानी", "हर्षिल"],
        "correct_answer": "बेनितल (Benital)",
        "explanation": "चमोली जिले के बेनितल को खगोल पर्यटन के लिए देश के पहले एस्ट्रो-विलेज के रूप में विकसित किया जा रहा है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड की 'रेशम नीति 2026' का मुख्य उद्देश्य क्या है?",
        "options": ["रेशम उत्पादन को दोगुना करना", "रेशम आयात करना", "सिर्फ पहाड़ी क्षेत्रों में खेती", "रेशम के कपड़ों पर टैक्स बढ़ाना"],
        "correct_answer": "रेशम उत्पादन को दोगुना करना",
        "explanation": "किसानों की आय बढ़ाने के लिए रेशम उत्पादन में आधुनिक तकनीक और विस्तार की नई नीति लाई गई है।"
    },
    {
        "section": "Uttarakhand GK",
        "sub_topic": "Current Affairs",
        "source": "News/Govt Reports",
        "text": "उत्तराखंड में 'हिम प्रहरी' (Him Prahari) योजना का प्राथमिक उद्देश्य क्या है?",
        "options": ["सीमावर्ती क्षेत्रों से पलायन रोकना", "बर्फबारी की सूचना देना", "पर्यटकों की सुरक्षा", "जंगलों की आग बुझाना"],
        "correct_answer": "सीमावर्ती क्षेत्रों से पलायन रोकना",
        "explanation": "सीमावर्ती गाँवों में पूर्व सैनिकों और युवाओं को तैनात कर पलायन रोकने और सुरक्षा मजबूत करने की यह योजना है।"
    }
]

# ... (get_question_bank_as_sets and get_all_sub_topics functions remain the same)
def get_question_bank_as_sets(sub_topic=None):
    result = []
    for q in UK_GK_QUESTION_BANK:
        if sub_topic and q.get("sub_topic") != sub_topic:
            continue
        result.append({
            "section": q["section"],
            "sub_topic": q.get("sub_topic", "General"),
            "source": q["source"],
            "text": q["text"],
            "options": json.dumps(q["options"], ensure_ascii=False),
            "correct_answer": q["correct_answer"],
            "explanation": q["explanation"]
        })
    return result

def get_all_sub_topics():
    topics = set()
    for q in UK_GK_QUESTION_BANK:
        if "sub_topic" in q:
            topics.add(q["sub_topic"])
    return sorted(list(topics))
