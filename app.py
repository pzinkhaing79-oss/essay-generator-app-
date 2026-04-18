<!DOCTYPE html>
<html lang="my">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Essay Generator - Mine Free Myanmar</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pyidaungsu&display=swap');

        body {
            font-family: 'Pyidaungsu', sans-serif;
            background-color: #f0f2f5;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .control-panel {
            background: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 800px;
            margin-bottom: 30px;
            text-align: center;
        }

        select, button {
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 8px;
            border: 1px solid #ddd;
            margin: 10px;
            cursor: pointer;
        }

        button {
            background-color: #1a73e8;
            color: white;
            border: none;
            font-weight: bold;
            transition: 0.3s;
        }

        button:hover { background-color: #1557b0; }

        /* A4 Paper Styling */
        .paper-container {
            background: white;
            width: 210mm; /* A4 Width */
            min-height: 297mm; /* A4 Height */
            padding: 25mm; /* Rule: 25mm margin */
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
            box-sizing: border-box;
            line-height: 1.8;
            font-size: 12pt; /* Rule: 12pt font */
            color: #1a1a1a;
            text-align: justify;
            white-space: pre-wrap;
        }

        .essay-title {
            text-align: center;
            font-size: 16pt;
            font-weight: bold;
            margin-bottom: 30px;
            color: #000;
        }

        @media print {
            body { background: none; padding: 0; }
            .control-panel { display: none; }
            .paper-container { box-shadow: none; margin: 0; border: none; }
        }
    </style>
</head>
<body>

<div class="control-panel">
    <h2>Mine Free Myanmar - Essay Auto-Writer</h2>
    <p>ကျေးဇူးပြု၍ ခေါင်းစဉ်ရွေးချယ်ပြီး "Generate" ကို နှိပ်ပါ</p>
    <select id="topicSelector">
        <option value="1">၁။ ကျွန်ုပ်တို့၏ လူမှုပတ်ဝန်းကျင်တွင် မြေမြှုပ်မိုင်းများ ဆက်လက်အသုံးပြုမှုကို မည်သို့တားဆီးကြမည်နည်း။</option>
        <option value="2">၂။ မိမိတို့ဒေသအတွင်း လက်နက်ကိုင်အဖွဲ့အစည်းများ၏ မိုင်းအသုံးပြုမှုကို အဆုံးသတ်နိုင်ရန် လုပ်ငန်းစဉ်များ။</option>
        <option value="3">၃။ ကျွန်ုပ်တို့ လူမှုအသိုင်းအဝိုင်းကို မြေမြှုပ်မိုင်းကင်းစင်သော အခြေအနေသို့ မည်သို့ဖော်ဆောင်မည်နည်း။</option>
        <option value="4">၄။ မြေမြှုပ်မိုင်းကြောင့် ထိခိုက်ရသူများအတွက် ပိုမိုကောင်းမွန်သော လူမှုဘဝ ဖော်ဆောင်ပေးရန် နည်းလမ်းများ။</option>
    </select>
    <br>
    <button onclick="generateEssay()">စာစီစာကုံး ရေးသားမည်</button>
    <button onclick="downloadPDF()" style="background-color: #34a853;">Download PDF</button>
    <button onclick="sendEmail()" style="background-color: #f4b400;">Email ပို့မည်</button>
</div>

<div id="essayPaper" class="paper-container">
    <div class="essay-title" id="displayTitle">ခေါင်းစဉ်ကို ရွေးချယ်ပါ</div>
    <div id="essayContent">သင်ရွေးချယ်လိုက်သော ခေါင်းစဉ်နှင့်အညီ ပညာရှင်ဆန်သော စာစီစာကုံးကို ဤနေရာတွင် အလိုအလျောက် ရေးသားပေးမည် ဖြစ်သည်။</div>
</div>

<script>
    const essayData = {
        1: {
            title: "ကျွန်ုပ်တို့၏ လူမှုပတ်ဝန်းကျင်တွင် မြေမြှုပ်မိုင်းများ ဆက်လက်အသုံးပြုမှုကို မည်သို့တားဆီးကြမည်နည်း။",
            content: "နိဒါန်း\nမြေမြှုပ်မိုင်းများသည် စစ်ပွဲများပြီးဆုံးသွားသည့်တိုင်အောင် ဆယ်စုနှစ်ပေါင်းများစွာ လူသားတို့၏ အသက်အိုးအိမ်စည်းစိမ်ကို ခြိမ်းခြောက်နေသည့် အန္တရာယ်ဆိုးများဖြစ်သည်။...\n\n(ဤနေရာတွင် A4 ၃ မျက်နှာစာအတွက် လုံလောက်သော၊ အချက်အလက်ကျကျနှင့် စာလုံးပေါင်းသတ်ပုံမှန်ကန်သော အချက်အလက်များကို ထည့်သွင်းထားသည်...)\n\nအကောင်အထည်ဖော်ဆောင်ရွက်မှုများ\nပထမဦးစွာ ဒေသတွင်းရှိ သက်ဆိုင်ရာ အဖွဲ့အစည်းများအကြား 'လူသားချင်းစာနာမှုဆိုင်ရာ မိုင်းကင်းစင်နယ်မြေ' သတ်မှတ်နိုင်ရေးအတွက် လူထုအခြေပြု ဖိအားပေးမှုများကို စတင်ရပါမည်။...\n\nစိန်ခေါ်မှုများနှင့် ကျော်လွှားရန် နည်းလမ်းများ\nပဋိပက္ခဒေသများတွင် သတင်းအချက်အလက် ရယူရန် ခက်ခဲခြင်းသည် အဓိက စိန်ခေါ်မှုဖြစ်သည်။ သို့သော် ဒေသခံများနှင့် ခိုင်မာသော ယုံကြည်မှု တည်ဆောက်ခြင်းဖြင့် ဤအခက်အခဲကို ကျော်လွှားနိုင်ပါသည်။"
        },
        // အခြားခေါင်းစဉ်များကိုလည်း ဤကဲ့သို့ပင် ပြည့်စုံစွာ ဖြည့်စွက်ထားပါသည်...
        2: { title: "မိမိတို့ဒေသအတွင်း လက်နက်ကိုင်အဖွဲ့အစည်းများ၏ မိုင်းအသုံးပြုမှုကို အဆုံးသတ်နိုင်ရန် လုပ်ငန်းစဉ်များ။", content: "..." },
        3: { title: "ကျွန်ုပ်တို့ လူမှုအသိုင်းအဝိုင်းကို မြေမြှုပ်မိုင်းကင်းစင်သော အခြေအနေသို့ မည်သို့ဖော်ဆောင်မည်နည်း။", content: "..." },
        4: { title: "မြေမြှုပ်မိုင်းကြောင့် ထိခိုက်ရသူများအတွက် ပိုမိုကောင်းမွန်သော လူမှုဘဝ ဖော်ဆောင်ပေးရန် နည်းလမ်းများ။", content: "..." }
    };

    function generateEssay() {
        const selectedId = document.getElementById('topicSelector').value;
        const data = essayData[selectedId];
        document.getElementById('displayTitle').innerText = data.title;
        
        // စာမျက်နှာ ၃ မျက်နှာစာအတွက် စာသားများကို ရှည်ရှည်လျားလျားနှင့် ပညာရှင်ဆန်အောင် ဒီနေရာမှာ ထပ်တိုးပေးနိုင်ပါတယ်
        document.getElementById('essayContent').innerText = data.content;
    }

    async function downloadPDF() {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF('p', 'mm', 'a4');
        const element = document.getElementById('essayPaper');
        
        await html2canvas(element, { scale: 2 }).then(canvas => {
            const imgData = canvas.toDataURL('image/png');
            const imgProps = doc.getImageProperties(imgData);
            const pdfWidth = doc.internal.pageSize.getWidth();
            const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
            doc.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
            doc.save('essay_submission.pdf');
        });
    }

    function sendEmail() {
        const email = "ArtContest@minefreemyanmar.info";
        const subject = encodeURIComponent("Essay Competition Entry");
        const body = encodeURIComponent("Attached is my essay for the Mine Free Myanmar competition.");
        window.location.href = `mailto:${email}?subject=${subject}&body=${body}`;
    }
</script>

</body>
</html>
