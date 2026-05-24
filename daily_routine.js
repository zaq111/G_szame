// daily_routine.js (DI GITHUB ANDA)
async function runDailyRoutine(bagian) {
    const tunggu = (ms) => new Promise(resolve => setTimeout(resolve, ms));
    
    // Fungsi pembantu agar log terlihat rapi
    const logBagian = (no, nama) => console.log(`%c[Daily] ─── MEMULAI BAGIAN ${no}: ${nama} ───`, 'color: #ff00ff; font-weight: bold;');

    // ==========================================
    // LOGIKA SELEKSI BAGIAN
    // ==========================================
    
    // JIKA MEMILIH BAGIAN 1 (atau jalankan semua)
    if (bagian === 1 || bagian === undefined) {
        logBagian(1, "Raid Boss & Dungeon Daily");
        kirimPerintah("Raid Boss", [255,221,6,0,108,189,67,208,86,0,0,0,53,83]);
        await tunggu(500);
        kirimPerintah("Challenge - Dungeon Daily", [255,221,7,0,103,58,38,138,32,8,0,0,53,68,1]);
        await tunggu(500);
        kirimPerintah("Raid - Dungeon Daily", [255,221,7,0,248,229,216,19,54,8,0,0,53,68,2]);
        await tunggu(500);
    }

    // JIKA MEMILIH BAGIAN 2 (atau jalankan semua)
    if (bagian === 2 || bagian === undefined) {
        logBagian(2, "Abyss Operations");
        kirimPerintah("Abyss - Reset Confirm", [255,221,6,0,143,71,126,108,186,27,0,0,53,32]);
        await tunggu(500);
		kirimPerintah("Abyss - Quick Raid", [255,221,10,0,169,182,45,131,120,8,0,0,0,32,44,0,0,0]);
        await tunggu(500);
		kirimPerintah("Abyss - Quick Raid Confirm", [255,221,6,0,236,101,82,170,141,8,0,0,53,33]);
        await tunggu(500);
		kirimPerintah("Claim Gift Teritory", [255,221,6,0,70,187,104,162,197,0,0,0,11,6]);
        await tunggu(500);
		kirimPerintah("Chat Cross Server", [255,221,15,0,57,165,90,172,37,12,0,0,59,1,10,0,0,0,0,1,0,97,0]);
        await tunggu(500);
		kirimPerintah("Buy Dark Spirit Ethereal Realm", [255,221,6,0,184,175,234,159,229,1,0,0,68,35],50)
        await tunggu(500);
		kirimPerintah("Claim Dark Spirit Ethereal Realm 1", [255,221,7,0,19,57,164,237,228,8,0,0,68,36,1]);
		kirimPerintah("Claim Dark Spirit Ethereal Realm 2", [255,221,7,0,19,57,164,237,228,8,0,0,68,36,2]);
		kirimPerintah("Claim Dark Spirit Ethereal Realm 3", [255,221,7,0,19,57,164,237,228,8,0,0,68,36,3]);
		kirimPerintah("Claim Dark Spirit Ethereal Realm 4", [255,221,7,0,19,57,164,237,228,8,0,0,68,36,4]);
		kirimPerintah("Claim Dark Spirit Ethereal Realm 5", [255,221,7,0,19,57,164,237,228,8,0,0,68,36,5]);
		kirimPerintah("Claim VIP13 Reward", [255,221,6,0,155,88,193,131,59,2,0,0,19,7]);
        await tunggu(500);
		kirimPerintah("Diaz Donate Guild", [255,221,10,0,47,173,9,230,229,29,0,0,62,13,1,0,0,0],500);
		kirimPerintah("Gold Donate Guild", [255,221,10,0,47,173,9,230,229,29,0,0,62,13,2,0,0,0],100);
        await tunggu(20000);
		kirimPerintah("Enhance Gear", [255,221,7,0,87,17,135,83,71,0,0,0,52,1,0]);
		kirimPerintah("Upgrade Skill", [255,221,8,0,245,242,128,19,5,1,0,0,2,4,7,0]);
		kirimPerintah("Train Avatar", [255,221,6,0,124,222,183,88,89,2,0,0,57,32]);
		kirimPerintah("Train Mercenary", [255,221,6,0,216,240,70,155,178,13,0,0,57,12]);
		kirimPerintah("AFK Raid", [255,221,7,0,126,24,103,6,167,7,0,0,53,7,2]);
		kirimPerintah("Inv Guild Team Challenge", [255,221,6,0,69,113,27,184,5,16,0,0,67,26]);
		kirimPerintah("Start Guild Team Challenge", [255,221,6,0,252,31,178,53,71,16,0,0,67,13]);
		await tunggu(8000);
		kirimPerintah("Open Rune Essence", [255,221,15,0,164,42,62,163,238,28,0,0,3,6,11,226,4,0,1,0,0,0,1],100);
		kirimPerintah("Open Rune Essence", [255,221,15,0,127,90,139,27,173,29,0,0,3,6,10,226,4,0,1,0,0,0,1],100);
		kirimPerintah("Open Rune Essence", [255,221,15,0,127,90,139,27,173,30,0,0,3,6,12,226,4,0,1,0,0,0,1],100);
		await tunggu(1000);
		kirimPerintah("Open Box", [255,221,15,0,67,141,71,195,145,30,0,0,3,6,57,196,9,0,1,0,0,0,1],20)
		kirimPerintah("Open Box Territory War", [255,221,15,0,101,4,124,151,85,31,0,0,3,6,239,89,5,0,1,0,0,0,1],20)
		kirimPerintah("Open Box Premium Circle", [255,221,15,0,169,229,236,104,228,31,0,0,3,6,65,187,4,0,1,0,0,0,1],20)
		kirimPerintah("Up Dark Spirit", [255,221,6,0,79,239,158,140,127,12,0,0,68,31],2000)
		await tunggu(10000);
		kirimPerintah("Buy Sprite Organite 1", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,1,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 2", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,2,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 3", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,3,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 4", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,4,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 5", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,5,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 6", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,6,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 7", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,7,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 8", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,8,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 9", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,9,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 10", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,10,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 11", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,11,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 12", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,12,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 13", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,13,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 14", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,14,0,1,0,0,0]);
		kirimPerintah("Buy Sprite Organite 15", [255,221,13,0,100,151,204,7,86,1,0,0,61,28,1,15,0,1,0,0,0]);
		await tunggu(3000);
		kirimPerintah("Claim Benefit Hall 2min", [255,221,8,0,194,215,83,64,89,12,0,0,36,31,1,0]);
		kirimPerintah("Claim Benefit Hall 5min", [255,221,8,0,59,220,189,231,124,12,0,0,36,31,2,0]);
		kirimPerintah("Claim Benefit Hall 10min", [255,221,8,0,59,220,189,231,124,12,0,0,36,31,3,0]);
		kirimPerintah("Claim Benefit Hall 20min", [255,221,8,0,59,220,189,231,124,12,0,0,36,31,4,0]);
		kirimPerintah("Claim Benefit Hall 30min", [255,221,8,0,59,220,189,231,124,12,0,0,36,31,5,0]);
		kirimPerintah("Claim Benefit Hall 40min", [255,221,8,0,59,220,189,231,124,12,0,0,36,31,6,0]);
		kirimPerintah("Claim Benefit Hall 50min", [255,221,8,0,59,220,189,231,124,12,0,0,36,31,7,0]);
		kirimPerintah("Claim Benefit Hall 60min", [255,221,8,0,59,220,189,231,124,12,0,0,36,31,8,0]);
		kirimPerintah("Claim Benefit Hall 90min", [255,221,8,0,125,35,239,94,195,6,0,0,36,31,9,0]);
		kirimPerintah("Claim Benefit Hall 120min", [255,221,8,0,59,220,189,231,124,12,0,0,36,31,10,0]);
		kirimPerintah("Claim Benefit Hall 150min", [255,221,8,0,59,220,189,231,124,12,0,0,36,31,11,0]);
		kirimPerintah("Claim Benefit Hall 180min", [255,221,8,0,59,220,189,231,124,12,0,0,36,31,12,0]);
		await tunggu(2000);
		kirimPerintah("Claim Login Gift", [255,221,7,0,99,61,207,116,19,20,0,0,36,41,1]);
		kirimPerintah("Claim Login Gift", [255,221,7,0,99,61,207,116,19,20,0,0,36,41,2]);
		kirimPerintah("Claim Login Gift", [255,221,7,0,99,61,207,116,19,20,0,0,36,41,3]);
		kirimPerintah("Claim Login Gift", [255,221,7,0,99,61,207,116,19,20,0,0,36,41,4]);
		kirimPerintah("Claim Login Gift", [255,221,7,0,99,61,207,116,19,20,0,0,36,41,5]);
		kirimPerintah("Claim Login Gift", [255,221,7,0,99,61,207,116,19,20,0,0,36,41,6]);
		await tunggu(2000);
		kirimPerintah("Gear Hunt", [255,221,9,0,193,72,160,192,210,20,0,0,6,2,1,1,0],2);
		kirimPerintah("Soul Gear Hunt", [255,221,9,0,51,40,176,139,204,21,0,0,6,2,2,1,0],2);
		kirimPerintah("Rune Hunt", [255,221,9,0,193,72,160,192,210,20,0,0,6,2,3,1,0],2);
		kirimPerintah("Peak Hunt", [255,221,9,0,193,72,160,192,210,20,0,0,6,2,4,1,0],2);
		kirimPerintah("Deity Hunt", [255,221,9,0,193,72,160,192,210,20,0,0,6,2,5,1,0],2);
		kirimPerintah("Spirit Gear Hunt", [255,221,9,0,193,72,160,192,210,20,0,0,6,2,6,1,0],2);
    }

    // JIKA MEMILIH BAGIAN 3 (atau jalankan semua)
    if (bagian === 3 || bagian === undefined) {
        logBagian(3, "Stealth Tower");
        kirimPerintah("Buy Dark Spirit Ethereal Realm", [255,221,6,0,184,175,234,159,229,1,0,0,68,35], 50);
        await tunggu(3000); 

        for (let i = 1; i <= 5; i++) {
            kirimPerintah(`Claim Dark Spirit Ethereal Realm ${i}`, [255,221,7,0,19,57,164,237,228,8,0,0,68,36,i]);
            await tunggu(400);
        }
        await tunggu(1500);
		console.log("[Bot - Bagian 3] Memulai perulangan Stealth Tower (5x)...");
		for (let siklus = 1; siklus <= 5; siklus++) {
            console.log(`  └─ Stealth Tower - Putaran ke-${siklus}`);
            
            kirimPerintah(`Stealth Tower [P${siklus}]`, [255,221,6,0,131,22,227,188,230,3,0,0,53,164]);
            await tunggu(200); // delay 1 detik
            
            kirimPerintah(`RainStealth Tower [P${siklus}]`, [255,221,6,0,9,180,76,247,61,3,0,0,53,168]);
            await tunggu(200); // delay 1 detik
            
            kirimPerintah(`Claim Stealth Tower [P${siklus}]`, [255,221,6,0,121,60,39,103,168,3,0,0,53,165]);
            await tunggu(200); // delay 1 detik
        }
    }

    // JIKA MEMILIH BAGIAN 4 (atau jalankan semua)
    // JIKA MEMILIH BAGIAN 4 (atau jalankan semua)
    if (bagian === 4 || bagian === undefined) {
        logBagian(4, "Quest");

        // Pembungkus utama agar semua alur berjalan berurutan dari atas ke bawah
        await (async function eksekusiQuestMaksimal() {
            // Pindahkan helper tunggu ke paling atas agar bisa dipakai di mana saja
            const tunggu = (ms) => new Promise(resolve => setTimeout(resolve, ms));

            // ==========================================
            // TAHAP 1: LOCH TEMPLE ROUTINE
            // ==========================================
            console.log("[Bot] Memulai urutan perintah Loch Temple...");

            kirimPerintah("Beli Loch Temple Attempt", [255,221,6,0,5,91,202,158,19,4,0,0,53,200], 6);
            await tunggu(1000); // Jeda sebentar setelah beli

            kirimPerintah("Loch Temple M11 R4", [255,221,8,0,126,56,17,215,189,0,0,0,53,194,19,0]);
            await tunggu(80000);
            kirimPerintah("Loch Temple M11 R2", [255,221,8,0,126,56,17,215,189,0,0,0,53,194,18,0]);
            await tunggu(80000);
            kirimPerintah("Loch Temple M10 R4", [255,221,8,0,126,56,17,215,189,0,0,0,53,194,17,0]);
            await tunggu(80000);
            kirimPerintah("Loch Temple M10 R2", [255,221,8,0,126,56,17,215,189,0,0,0,53,194,16,0]);
            await tunggu(80000);
            kirimPerintah("Loch Temple M9 R4", [255,221,8,0,126,56,17,215,189,0,0,0,53,194,15,0]);
            await tunggu(80000);

            kirimPerintah("Loch Temple M9 R2", [255,221,8,0,126,56,17,215,189,0,0,0,53,194,14,0]);
            await tunggu(80000);

            kirimPerintah("Loch Temple M8 R4", [255,221,8,0,126,56,17,215,189,0,0,0,53,194,13,0]);
            await tunggu(80000);

            kirimPerintah("Loch Temple M8 R2", [255,221,8,0,126,56,17,215,189,0,0,0,53,194,12,0]);
            await tunggu(80000);

            kirimPerintah("Loch Temple M7 R4", [255,221,8,0,126,56,17,215,189,0,0,0,53,194,11,0]);
            await tunggu(80000);

            kirimPerintah("Loch Temple M7 R2", [255,221,8,0,126,56,17,215,189,0,0,0,53,194,10,0]);
            console.log("[Bot] Semua urutan perintah Loch Temple selesai! Bersiap transisi...");
            
            // Jeda transisi setelah Loch Temple selesai sebelum masuk Combat Area
            await tunggu(5500);

            // ==========================================
            // TAHAP 2: SIKLUS COMBAT MASSAL (3X)
            // ==========================================
            console.log("[Bot] 🚀 Memulai Otomasi Combat: Total 3 Siklus Berturut-turut...");

            for (let siklus = 1; siklus <= 3; siklus++) {
                console.log(`%c[Bot] ─── MEMULAI SIKLUS KE-${siklus} ───`, 'color: #00ffff; font-weight: bold;');

                // 1. Ke Combat Area
                kirimPerintah("Ke Combat Area", [255,221,10,0,43,225,48,55,224,31,0,0,0,30,0,0,0,0]);
                console.log(`[Bot - S${siklus}] Perintah 'Ke Combat Area' dikirim. Menunggu memuat 20 detik...`);
                await tunggu(20000);

                // 2. Kill & ATK Monster ke-1
                kirimPerintah("Kill Monster ke-1 Legendary Combat Area", [255,221,7,0,96,114,80,178,253,31,0,0,79,4,9]);
                kirimPerintah("ATK Monster ke-1 Legendary Combat Area", [255,221,7,0,169,11,44,108,227,32,0,0,79,9,9]);
                console.log(`[Bot - S${siklus}] Perintah Kill & ATK dikirim. Menunggu pertarungan 45 detik...`);
                await tunggu(45000);

                // 3. Proses Claim Reward 1 sampai 12
                console.log(`[Bot - S${siklus}] Memulai Claim Reward 1-12 dengan jeda 0.3 detik...`);
                for (let i = 1; i <= 12; i++) {
                    const labelClaim = `Claim-${i} Legendary Combat Area (Siklus ${siklus})`;
                    const bytesClaim = [255, 221, 7, 0, 13, 55, 240, 159, 75, 34, 0, 0, 79, 6, i];
                    
                    kirimPerintah(labelClaim, bytesClaim);
                    await tunggu(300);
                }
                
                console.log(`[Bot - S${siklus}] Semua reward selesai diklaim. Jeda akhir siklus 5 detik...`);
                await tunggu(5000);
                
                console.log(`%c[Bot] ✅ Siklus ke-${siklus} Selesai!`, 'color: #00ff88;');
            }

            console.log("%c[Bot] 🎉 LUAR BIASA! Seluruh 3 siklus otomatis telah selesai dijalankan!", 'color: #ffcc00; font-weight: bold;');
            await tunggu(6000);

            // ==========================================
            // TAHAP 3: AKHIR INSTANCE
            // ==========================================
            kirimPerintah("Keluar dari Instance", [255,221,6,0,221,149,149,69,63,4,0,0,53,43]);
            console.log("[Bot] Perintah 'Keluar dari Instance' berhasil dikirim.");
            await tunggu(2000);

        })(); // Akhir dari fungsi eksekusi otomatis
    }
    // JIKA MEMILIH BAGIAN 5 (atau jalankan semua)
    if (bagian === 5 || bagian === undefined) {
        logBagian(5, "VIP & Guild Donations");
        kirimPerintah("Claim VIP13 Reward", [255,221,6,0,155,88,193,131,59,2,0,0,19,7]);
        await tunggu(2000);
        kirimPerintah("Diaz Donate Guild", [255,221,10,0,47,173,9,230,229,29,0,0,62,13,1,0,0,0], 500);
        await tunggu(2000);
        kirimPerintah("Gold Donate Guild", [255,221,10,0,47,173,9,230,229,29,0,0,62,13,2,0,0,0], 100);
    }

    // JIKA MEMILIH BAGIAN 6 (atau jalankan semua)
    if (bagian === 6 || bagian === undefined) {
        logBagian(6, "Character Training & AFK");
        await tunggu(5000); // Menunggu jeda setelah donasi selesai diproses internal
        kirimPerintah("Enhance Gear", [255,221,7,0,87,17,135,83,71,0,0,0,52,1,0]);
        kirimPerintah("Upgrade Skill", [255,221,8,0,245,242,128,19,5,1,0,0,2,4,7,0]);
        kirimPerintah("Train Avatar", [255,221,6,0,124,222,183,88,89,2,0,0,57,32]);
        kirimPerintah("Train Mercenary", [255,221,6,0,216,240,70,155,178,13,0,0,57,12]);
        kirimPerintah("AFK Raid", [255,221,7,0,126,24,103,6,167,7,0,0,53,7,2]);
        await tunggu(3000);
        kirimPerintah("Inv Guild Team Challenge", [255,221,6,0,69,113,27,184,5,16,0,0,67,26]);
        kirimPerintah("Start Guild Team Challenge", [255,221,6,0,252,31,178,53,71,16,0,0,67,13]);
    }

    // JIKA MEMILIH BAGIAN 7 (atau jalankan semua)
    if (bagian === 7 || bagian === undefined) {
        logBagian(7, "Open Chests & Up Dark Spirit");
        await tunggu(5000);
        kirimPerintah("Open Rune Essence", [255,221,15,0,164,42,62,163,238,28,0,0,3,6,11,226,4,0,1,0,0,0,1], 100);
        kirimPerintah("Open Rune Essence", [255,221,15,0,127,90,139,27,173,29,0,0,3,6,10,226,4,0,1,0,0,0,1], 100);
        kirimPerintah("Open Rune Essence", [255,221,15,0,127,90,139,27,173,30,0,0,3,6,12,226,4,0,1,0,0,0,1], 100);
        
        kirimPerintah("Open Box", [255,221,15,0,67,141,71,195,145,30,0,0,3,6,57,196,9,0,1,0,0,0,1], 20);
        kirimPerintah("Open Box Territory War", [255,221,15,0,101,4,124,151,85,31,0,0,3,6,239,89,5,0,1,0,0,0,1], 20);
        kirimPerintah("Open Box Premium Circle", [255,221,15,0,169,229,236,104,228,31,0,0,3,6,65,187,4,0,1,0,0,0,1], 20);
        
        kirimPerintah("Up Dark Spirit", [255,221,6,0,79,239,158,140,127,12,0,0,68,31], 2000);
        await tunggu(20000);
    }

    // JIKA INGIN MENAMBAH BAGIAN 8 BESOK, TINGGAL PASTE DI BAWAH SINI:
    // if (bagian === 8 || bagian === undefined) { ... }

    console.log(`%c[Daily] ✅ Eksekusi bagian [${bagian || 'ALL'}] Selesai!`, "color: #00ff88; font-weight: bold;");
}
