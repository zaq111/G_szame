// daily_routine.js
async function runDailyRoutine() {
    const tunggu = (ms) => new Promise(resolve => setTimeout(resolve, ms));
    console.log("%c[Bot] ☀️ Memulai Rutinitas Harian dari GitHub...", "color: #ff00ff; font-weight: bold;");

    // 1. Raid Boss & Dungeon Daily
    kirimPerintah("Raid Boss", [255,221,6,0,108,189,67,208,86,0,0,0,53,83]);
    await tunggu(500);
    kirimPerintah("Challenge - Dungeon Daily", [255,221,7,0,103,58,38,138,32,8,0,0,53,68,1]);
    await tunggu(500);
    kirimPerintah("Raid - Dungeon Daily", [255,221,7,0,248,229,216,19,54,8,0,0,53,68,2]);
    await tunggu(500);

    // 2. Abyss Operations
    kirimPerintah("Abyss - Reset Confirm", [255,221,6,0,143,71,126,108,186,27,0,0,53,32]);
    await tunggu(500);
    kirimPerintah("Abyss - Quick Raid", [255,221,10,0,169,182,45,131,120,8,0,0,0,32,44,0,0,0]);
    await tunggu(500);
    kirimPerintah("Abyss - Quick Raid Confirm", [255,221,6,0,236,101,82,170,141,8,0,0,53,33]);
    await tunggu(000);

    // 3. Territory & Social Interaction
    kirimPerintah("Claim Gift Teritory", [255,221,6,0,70,187,104,162,197,0,0,0,11,6]);
    await tunggu(1500);
    kirimPerintah("Chat Cross Server", [255,221,15,0,57,165,90,172,37,12,0,0,59,1,10,0,0,0,0,1,0,97,0]);
    await tunggu(2000);

    // 4. Dark Spirit Realm (Buy & Claim 1-5)
    kirimPerintah("Buy Dark Spirit Ethereal Realm", [255,221,6,0,184,175,234,159,229,1,0,0,68,35], 50);
    await tunggu(3000); 

    for (let i = 1; i <= 5; i++) {
        kirimPerintah(`Claim Dark Spirit Ethereal Realm ${i}`, [255,221,7,0,19,57,164,237,228,8,0,0,68,36,i]);
        await tunggu(400);
    }
    await tunggu(1500);

    // 5. VIP Rewards
    kirimPerintah("Claim VIP13 Reward", [255,221,6,0,155,88,193,131,59,2,0,0,19,7]);
    await tunggu(2000);

    // 6. Guild Donations (Diaz & Gold)
    kirimPerintah("Diaz Donate Guild", [255,221,10,0,47,173,9,230,229,29,0,0,62,13,1,0,0,0], 500);
    await tunggu(2000);
    kirimPerintah("Gold Donate Guild", [255,221,10,0,47,173,9,230,229,29,0,0,62,13,2,0,0,0], 100);

    console.log("%c[Bot] ✅ Rutinitas Harian Selesai Terpanggil!", "color: #00ff88; font-weight: bold;");
    await tunggu (50000)
    kirimPerintah("Enhance Gear", [255,221,7,0,87,17,135,83,71,0,0,0,52,1,0]);
    kirimPerintah("Upgrade Skill", [255,221,8,0,245,242,128,19,5,1,0,0,2,4,7,0]);
    kirimPerintah("Train Avatar", [255,221,6,0,124,222,183,88,89,2,0,0,57,32]);
    kirimPerintah("Train Mercenary", [255,221,6,0,216,240,70,155,178,13,0,0,57,12]);
    kirimPerintah("AFK Raid", [255,221,7,0,126,24,103,6,167,7,0,0,53,7,2]);
    await tunggu (3000)
    kirimPerintah("Inv Guild Team Challenge", [255,221,6,0,69,113,27,184,5,16,0,0,67,26])
    kirimPerintah("Start Guild Team Challenge", [255,221,6,0,252,31,178,53,71,16,0,0,67,13])
    await tunggu (5000)
    kirimPerintah("Open Rune Essence", [255,221,15,0,164,42,62,163,238,28,0,0,3,6,11,226,4,0,1,0,0,0,1],100)
    kirimPerintah("Open Rune Essence", [255,221,15,0,127,90,139,27,173,29,0,0,3,6,10,226,4,0,1,0,0,0,1],100)
    kirimPerintah("Open Rune Essence", [255,221,15,0,127,90,139,27,173,30,0,0,3,6,12,226,4,0,1,0,0,0,1],100)
    
    kirimPerintah("Open Box", [255,221,15,0,67,141,71,195,145,30,0,0,3,6,57,196,9,0,1,0,0,0,1],20)
    kirimPerintah("Open Box Territory War", [255,221,15,0,101,4,124,151,85,31,0,0,3,6,239,89,5,0,1,0,0,0,1],20)
    kirimPerintah("Open Box Premium Circle", [255,221,15,0,169,229,236,104,228,31,0,0,3,6,65,187,4,0,1,0,0,0,1],20)
    
    kirimPerintah("Up Dark Spirit", [255,221,6,0,79,239,158,140,127,12,0,0,68,31],2000)
    await tunggu (20000)
}

// Daftarkan fungsi ke objek global game setelah skrip ini dimuat oleh browser
if (window.CMD) {
    window.CMD.daily = runDailyRoutine;
} else {
    window.runDailyRoutine = runDailyRoutine;
}
