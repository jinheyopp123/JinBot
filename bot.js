const { Client, Intents, MessageEmbed } = require('discord.js');
const client = new Client({ 
    intents: [
        Intents.FLAGS.GUILDS,
        Intents.FLAGS.GUILD_MESSAGES,
        Intents.FLAGS.MESSAGE_CONTENT // MESSAGE CONTENT INTENT 활성화
    ] 
});

// 봇 준비 이벤트
client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
});

// 메시지 이벤트
client.on('messageCreate', async message => {
    if (message.author.bot) return;

    if (message.content === '안녕') {
        await message.channel.send('안녕하세요!');
    }

    if (message.content.toLowerCase() === '디도스') {
        await message.channel.send('ㄴㄴㄴㄴㄴ');
    }

    if (message.content.toLowerCase() === '임베드') {
        const embed = new MessageEmbed()
            .setTitle('테스트')
            .setDescription('테스트중입니다');
        await message.channel.send({ embeds: [embed] });
    }
});

// 명령어 핸들러
client.on('messageCreate', async message => {
    if (message.content.startsWith('!')) {
        const args = message.content.slice(1).trim().split(/ +/);
        const command = args.shift().toLowerCase();

        if (command === 'hello') {
            await message.channel.send('Hello!');
        } else if (command === '라이선스') {
            await message.channel.send('https://github.com/jinheyopp123/JinBot | GitHub MIT라이선스라 자유입니다 :)');
        } else if (command === 'ddos') {
            await message.channel.send('절대 안돼요');
        } else if (command === '개발자') {
            await message.channel.send('김진혁 제작');
        }
    }
});

// 하드코딩된 봇 토큰으로 봇 실행
const TOKEN = 'YOUR_TOKEN';
client.login(TOKEN);

