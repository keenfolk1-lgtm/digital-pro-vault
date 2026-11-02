# ⚡ STEAM HOURBOOST 24/7 (НАКРУТКА ЧАСОВ В ДОТЕ, CS2, RUST — ДО 32 ИГР ОДНОВРЕМЕННО)

Полная инструкция и готовый скрипт для безопасной накрутки часов в Steam 24/7 (без запуска самих игр и нагрузки на видеокарту — потребляет всего 15 МБ ОЗУ!).

---

## Вариант 1: Готовый скрипт на Node.js (`steam-user`)

1. Установите Node.js с официального сайта `nodejs.org`.
2. Создайте папку `hourboost`, откройте в ней терминал и выполните:
   ```bash
   npm init -y
   npm install steam-user readline-sync
   ```
3. Создайте файл `boost.js`:
   ```javascript
   const SteamUser = require('steam-user');
   const readline = require('readline-sync');

   const client = new SteamUser();
   const username = readline.question('Steam Login: ');
   const password = readline.question('Steam Password: ', { hideEchoBack: true });

   // ID игр для одновременного буста: 730 = CS2, 570 = Dota 2, 252490 = Rust, 440 = TF2, 271590 = GTA V
   const GAMES_TO_BOOST = [730, 570, 252490, 440, 271590];

   client.logOn({ accountName: username, password: password });

   client.on('loggedOn', () => {
     console.log('✅ Успешный вход в Steam! Запускаем буст часов в играх:', GAMES_TO_BOOST);
     client.setPersona(SteamUser.EPersonaState.Online);
     client.gamesPlayed(GAMES_TO_BOOST);
   });
   ```
4. Запустите: `node boost.js`, введите код Steam Guard — и часы пойдут во всех играх одновременно!