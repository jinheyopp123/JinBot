const { Client, GatewayIntentBits, EmbedBuilder, PermissionsBitField } = require('discord.js');
const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent
    ]
});
const version = 'v.alpha-1.0-714';
// 공지 채널 설정 저장을 위한 딕셔너리
const announcementChannels = new Map();

client.once('ready', () => {
    console.log(`bot_name: ${client.user.tag}`);
    console.log(`bot_ID: ${client.user.id}`);
    console.log(`bot_version: ${version}`);
    console.log('bot_ready_complete');
});

client.on('messageCreate', async message => {
    if (message.author.bot) return;

    if (message.content === '안녕') {
        await message.channel.send('안녕하세요!');
    }

    if (message.content.toLowerCase() === '디도스') {
        await message.channel.send('ㄴㄴㄴㄴㄴ');
    }

    if (message.content.toLowerCase() === '임베드') {
        const embed = new EmbedBuilder().setTitle('테스트').setDescription('테스트중입니다');
        await message.channel.send({ embeds: [embed] });
    }

    if (message.content.toLowerCase() === '임베드2') {
        const embed = new EmbedBuilder().setTitle('없는데요?').setDescription('없다고요');
        await message.channel.send({ embeds: [embed] });
    }
});

client.on('interactionCreate', async interaction => {
    if (!interaction.isCommand()) return;

    const { commandName } = interaction;

    if (commandName === 'hello') {
        await interaction.reply('안녕하세요!');
    }

    if (commandName === '라이선스') {
        await interaction.reply('[GitHub](https://github.com/SEKA-TEAM/JinBot)');
    }

    if (commandName === 'ddos') {
        await interaction.reply('절대 안돼요');
    }

    if (commandName === '개발자') {
        await interaction.reply('SEKA TEAM 개발자분들이 제작하였습니다');
    }

    if (commandName === '개발내역') {
        await interaction.reply(`버전 ${version}`);
    }

    if (commandName === '비밀메세지') {
        await interaction.reply('DM으로 비밀번호 요청을 하였습니다!');
        await interaction.user.send('비밀번호를 입력해주세요');

        const filter = dmMessage => dmMessage.author.id === interaction.user.id;
        const dmChannel = await interaction.user.createDM();

        try {
            const collected = await dmChannel.awaitMessages({ filter, max: 1, time: 60000, errors: ['time'] });
            const dmMessage = collected.first();

            if (dmMessage.content === '0821') {
                await dmChannel.send('확인되었습니다.');
                const embed = new EmbedBuilder().setTitle('비밀 메세지').setDescription('알아서 하세요');
                await interaction.followUp({ embeds: [embed] });
            } else {
                await interaction.followUp('비밀번호가 틀렸습니다.');
            }
        } catch (error) {
            await interaction.followUp('시간이 초과되었습니다. 다시 시도해주세요.');
        }
    }

    if (commandName === '추방') {
        const member = interaction.options.getMember('user');
        const reason = interaction.options.getString('reason') || null;

        if (interaction.member.permissions.has(PermissionsBitField.Flags.KickMembers)) {
            if (member) {
                await member.kick(reason);
                await interaction.reply(`${member.user.tag}을(를) 추방합니다.`);
            } else {
                await interaction.reply('추방할 멤버를 멘션해주세요.');
            }
        } else {
            await interaction.reply('권한이 부족합니다.');
        }
    }

    if (commandName === '밴') {
        const member = interaction.options.getMember('user');
        const reason = interaction.options.getString('reason') || null;

        if (interaction.member.permissions.has(PermissionsBitField.Flags.BanMembers)) {
            if (member) {
                await member.ban({ reason });
                await interaction.reply(`${member.user.tag}을(를) 밴합니다.`);
            } else {
                await interaction.reply('밴할 멤버를 멘션해주세요.');
            }
        } else {
            await interaction.reply('권한이 부족합니다.');
        }
    }

    if (commandName === '공지채널설정') {
        const channel = interaction.options.getChannel('channel');

        if (interaction.member.permissions.has(PermissionsBitField.Flags.Administrator)) {
            announcementChannels.set(interaction.guild.id, channel.id);
            await interaction.reply(`공지 채널이 ${channel}으로 설정되었습니다!`);
        } else {
            await interaction.reply('권한이 부족합니다.');
        }
    }

    if (commandName === '힘들다') {
        await interaction.reply('무슨 고민 있으신가요?');
    }
});

client.login('YOUR_BOT_TOKEN');
