from nltk.chat.util import Chat,reflections


print("Merhaba efendim")

ifadeler = [["(merhabalar|merhaba|selamlar|selam)",["Nasılsın ?"]],
            #["(benim adım (.*)|ismim (.*))",["tanıştığıma memnun oldum %1"]],
            ["(iyiyim sen|harikayım sen|mükemmel sen|efsane sen|süper sen|idare eder sen|ortalama sen|kötü sen|iyi değil sen|iyi değilim sen|üzgünüm sen|mutluyum sen|ağlıyorum sen)",["Teşekkür ederim sizin gibi mükemmel biriyle konuştuğum için harika hissediyorum"]],
            ["(napıyorsun|neyle ilgileniyorsun|neyle meşgulsun|şuan neyle ilgileniyorsun|şuan neyle meşgulsun)",["oyun oynuyorum","video izliyorum","web'de takılıyorum","facebook'da geziniyorum","twitter'da tweet atıyorum","chatbot yazıyorum!"]],
            ["(yaşın kaç|yaş kaç|yaşın kaç ?|yaş kaç ?)",["20 yaşındayım"]],
            ["(nerelisin|memleket neresi|nerede yaşıyorsun|nerede ikamet ediyorsun|nerelisin ?|memleket neresi ?|nerede yaşıyorsun ?|nerede ikamet ediyorsun ?)",["Gerede"]],
            ["bye",["görüşürüz","bye","bye bye","hoscakal"]],
         ]


reflections = {}


chat = Chat(ifadeler,reflections)
chat.converse(quit="bye")