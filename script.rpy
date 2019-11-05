# Определение персонажей игры.
# Главная героиня, которая ни слова не скажет за всю игру(автор пиздабол, она пиздит и не затыкается)))
define a = Character('Аня Мяу', who_color="#c8ffc8")
define a_shout = Character('Аня Мяу', who_color="#c8ffc8", what_size=34)
define am = Character('мысли Ани Мяу', who_color="#c8ffc8")
# Команда AMfans studio
define nik = Character('Ника Рулетова', who_color="#7d2087")
define slu = Character('SlugGous', who_color = "#2c2e0c")
define k = Character('Кустик', who_color = "#059fff")
define p = Character('Пчола', who_color = "#ffdc2e")
define s = Character('SandManager', who_color = "#b3b854")
define at = Character('Анитошка', who_color = "#kfkfkf")
define al = Character('Алемарт', who_color = "#2E8B57")
define nm = Character('Никита Мапко', who_color = "#ffffff")

#герои новеллы


#### Любовники
define morg = Character('Морган', who_color = "#ffffff")
define sos = Character('Cосидж', who_color="#ffffff")
#### чат и другие персонажи
define ch = Character('Чат', who_color = "#050505")
define nn = Character('Неизвестный покупатель', who_color = "#7d2087")
define al1 = Character('Кассир Макдональдса', who_color = "#2E8B57")
# фрики давай поженимся
define gob = Character('Андрей Гобзавр', who_color = "#ffffff")
define g1 = Character('Геннадий Горин', who_color = "#ffffff")
define fil = Character('Дима Философ', who_color = "#ffffff")
define ls = Character('Толян', who_color = "#ffffff")
define sr = Character('Сергей Резников', who_color = "#ffffff")
define vn = Character('Виталик', who_color = "#ffffff")
## Друзья Гобза
define ll = Character('Людмила Людмурик', who_color = "#ffffff")
## Друзья философа
define m = Character('Максимка', who_color = "#ffffff")
define l = Character('Лёшка', who_color = "#ffffff")
## Друзья Витали
define an = Character('Ангелина', who_color = "#ffffff")
define sv = Character('Гульнара', who_color = "#ffffff")
define bv = Character('Руслан', who_color = "#ffffff")
## Друзья Горина
define g2 = Character('Гешка Горин', who_color = "#ffffff")
define g3 = Character('Гена Горин', who_color = "#ffffff")
## друзья Резникова
define rg = Character('Голуби', who_color = "#ffffff")
## Ведущие шоу
define dg = Character('Лариса Гузеева', who_color = "#ffffff")
define dg_shout = Character('Лариса Гузеева', who_color = "ffffff", what_size = 25)
define ds = Character('Роза Сябитова', who_color = "#ffffff")
define dv = Character('Василиса Володина', who_color = "#ffffff")
#никому не нужные пидоры
define doc = Character('Доктор', who_color = "#ffffff")
define med = Character('Медсестра', who_color = "#ffffff")

###размещение
transform right_down_corner:
    xpos 1.0
    ypos 0.4

transform head:
    xpos 0.5
    ypos 0.2

transform down:
    xpos 0.2
    ypos 1.0
transform rightly:
    xalign 0.8
    yalign 1.0
#видео в главно меню
#init -2:
#    image lofi = Movie(play="gui/main_menu.webm",size=(1280,720))

#label main_menu:
#    scene lofi
#    jump main_menu_screen

# заставка
label splashscreen:
    image bg black = "#000000"
    scene bg black with dissolve
    pause 2
    scene bg logo with dissolve
    pause 1
    scene bg black with dissolve
    pause 2
    scene bg title with dissolve
    pause 3
    scene bg black with dissolve
    pause 1
return
#главное меню ролик


#начало игры
label start:
    play music "music/main.mp3"
    scene bg black
    "Стоял хороший летний день. "
    "Анна Мяу только что закончила трансляцию на своем любимом ютубчике."

    scene bg stream with dissolve
    a "Ну вот я закончила очередной стрим."
    a "Интересно, Артём ещё стримит?"
    a "Надо было сказать всем идти к нему."
    play sound "sounds/keyword.mp3"
    play sound "sounds/clicks1.wav"
    scene bg morgyt
    a "Странно"
    a "Он час назад закончил и до сих пор даже не позвонил сказать, что освободился и скоро приедет."
    a "Ну раз я тоже освободилась, то поеду за ним сама."
    a "Сделаю ему сюрприз."
    scene bg black with dissolve

    pause 2

    play sound "sounds/shagi.mp3"
    play sound "sounds/opencar.mp3"
    play sound "sounds/closecar.mp3"

    pause 2

    scene bg civic
    a "..."
    a "Что-то тихо в машине"
    menu:
        "Включить музыку":
            jump music_in_a_car
        "Не включать музыку":
            jump nomusic_in_a_car

label nomusic_in_a_car:
    $ car_flag = False
    "Как хорошо сидеть в тишине."
    "Особенно после такого тяжёлого дня."
    jump mono_car

label music_in_a_car:
    $ car_flag = True
    a "Включу-ка музыку"
    play music "music/ogonek.mp3"
    jump mono_car

label mono_car:
    a "Надо бы Паппи корм купить по дороге назад."
    a "Когда уже умрёт эта говноедка..."
    a "Интересно, чем там Артём занят?"
    a "Скорее всего видео монтирует новое."
    a "Он как раз говорил, что с Сосиджем собирается что-то снимать."
    a "Но обычно он предупреждает о таком..."
    a "Возможно, слишком углубился в рабочий процесс и про всё позабыл."
    a "..."
    a "О, Мак."
    a "Может заехать? Наверняка Артём проголодался."
    menu:
        "Заехать в мак":
            jump mac
        "Ехать дальше в студию":
            jump drive_to_study

label mac:
    $ mac_flag = True
    stop music
    scene bg black with dissolve
    pause 1
    scene bg mac with dissolve
    play music "music/macin.mp3"
    a "Какой-то уродский макдональдс, у которого не работает МакАвто."
    a "Теперь придётся торчать в этой ужасной очереди!"
    a "Благо она не такая уж и длинная."
    a "Так, чтобы взять..."
    show nika good with dissolve
    nn "Здарова, Карина!"
    al1 "Ика, снова ты?"
    al1 "Что тебе тут нужно, снова издеваться пришла?"
    nn "Конечно же нет."
    nn "Как я могу издеваться над своей любимой подругой, которая работает в МакДональдсе?"
    nn "Что за глупости ты говоришь?"
    nn "Кстати, подружка!"
    nn "Скажи, пожалуйста, \"Свободная касса\""
    al1 "Вика, иди уже отсюда!"
    nn "Никуда я не пойду, пока не получу свой Биг Мак и диетическую колу!"
    al1 "Хочешь Биг Мак?"
    al1 "Держи!"
    show big mak at right_down_corner with moveinright
    show big mak at head with move
    show nika angry
    show big mak at down with move
    hide big mak with moveoutbottom
    al1 "Запить дать?"
    nn "ПРИНЕСИ МНЕ КНИГУ ЖАЛОБ!!!"
    al1 "Её конь съел"
    nn "Ну всё блин, пока-пока, любительница хорс фейлов."
    al1 "Проваливай уже."
    hide nika angry with moveoutleft
    al1 "Здравствуйте, чего желаете?"
    a "Здравствуйте"
    a "Мне большое маккомбо с двойным Биг Маком и диетическую колу"
    al1 "Вот ваш заказ, всего хорошего!"
    a "До свидания!"
    al1 "До свидания!"
    scene bg black
    stop music
    play music "music/main.mp3"
    a "Ну и ну, странный мак какой-то попался..."
    a "Надо поскорее отправится к Артёму"
    jump nude_studio

label drive_to_study:
    $ mac_flag = False
    a "Не, не хочу, дома лучше чего-ниудь закажем."
    a "Или в KFC заедем."
    a "Потом решим."
    jump morg_studio

label morg_studio:
    stop music
    play music "music/main.mp3"
    scene bg black
    a "Ну вот я на месте"
    play sound "sounds/opendoor.mp3"
    a "Привет, Моргунис"
    scene bg yaoi with dissolve
    play music "music/sad.mp3"
    a "Морг..."
    scene bg studio with dissolve
    show sosig nervous at rightly with dissolve
    show morg shok at center with dissolve
    a_shout "Артёёёёёёёёём"
    a_shout "Какого хуя тут происходит?????"
    morg "А-Аня"
    morg "Эт-это не то, о чём ты подумала"
    a_shout "Артём, ты ахуел?"
    morg "Никита, скажи ей, что она всё неправильно поняла"
    show sosig neutral
    sos "Аня, ты всё неправильно поняла"
    show sosig nervous
    a_shout "Что я неправильно поняла?"
    a_shout "Вы тут, значит, сосались, пока меня не было, да?"
    show morg serious
    morg "Нет, Аня, нет"
    a_shout "Артём, ты меня не обманешь!"
    a_shout "Я всё видела!"
    #show morg
    morg "Ну да, мы поцеловались разок"
    morg "Но это ничего не значит!"
    show sosig neutral
    sos "Вот именно, всего разок, Аня!"
    show sosig nerv
    a "А что делают презервативы на полу..."
    a "Только не говорите, что вы..."
    show sosig nerv
    a "..."
    morg "..."
    sos "..."
    sos "Я пожалуй пойду"
    hide sosig with moveoutright
    play sound "sounds/closedoor.mp3"
    show morg shok
    a "..."
    morg "..."
    sos "..."
    a "Артём, скажи, пожалуйста, что это не то, о чём я подумала"
    show morg serious
    morg "Аня..."
    morg "Я пытался это всячески скрыть"
    morg "Аня, прости"
    a "..."
    morg "Мы с Никитой очень давно..."
    show morg shok
    a "Артём, не продолжай"
    a "Я всё поняла"
    a "Можешь не возвращаться домой!"
    a "Я тебе привезу потом вещи"
    a "Прощай..."
    #show morg
    morg "Аня..."
    scene bg black
    play sound "sounds/opendoor.mp3"
    play sound "sounds/closedoor.mp3"
    jump sad

label nude_studio:


    scene bg black
    a "Ну вот я на месте"
    play sound "sounds/opendoor.mp3"
    a "Привет, Моргунис"
    scene bg yaoi with dissolve
    a "Морг..."
    play music "music/sad.mp3"
    scene bg studio with dissolve
    show sosig nervous at rightly with dissolve
    show nude shok at center with dissolve
    a_shout "Артёёёёёёёёёёём"
    a_shout "Какого хуя тут происходит?????"
    a_shout "И почему ты блять голый?"
    morg "А-Аня"
    morg "Эт-это не то, о чём ты подумала"
    a_shout "Артём, ты ахуел?"
    morg "Никита, скажи ей, что она всё неправильно поняла"
    show sosig neutral
    sos "Аня, ты всё неправильно поняла"
    show sosig nerv
    a_shout "Что я неправильно поняла?"
    a_shout "Что вы тут делали, пока меня не было?"
    show nude serious
    morg "Н-ничего"

    show nude shok

    a_shout "Артём, ты меня не обманешь!"
    a_shout "Почему ты голый?!"
    a_shout "И почему вы целовались?!"
    show nude serious
    morg "Ну да, мы поцеловались разок"
    morg "Но это ничего не значит!"
    show sosig nervous
    sos "Вот именно, всего разок, Аня!"
    show sosig nerv
    show nude shok
    a "А что делают презервативы на полу..."
    a "Только не говорите, что вы..."
    show sosig nervous
    a "..."
    morg "..."
    sos "..."
    sos "Я пожалуй пойду"
    hide sosig with moveoutright
    play sound "sounds/closedoor.mp3"

    a "Артём, скажи, пожалуйста, что это не то, о чём я подумала"
    show nude nervsad
    morg "Аня..."
    morg "Я не знал, как это сказать..."
    morg "Аня, прости"
    a "Как давно?..."
    morg "С первого бухлострима..."
    show nude sad
    a "Ясно"
    a "Всё хорошо"
    morg "Аня..."
    a "Я всё поняла"
    a "Можешь не возвращаться домой!"
    morg "Аня я..."
    a "Я тебе привезу потом вещи"
    a "Прощай..."

    morg "Аня..."
    scene bg black
    play sound "sounds/closedoor.mp3"
    jump sad

label sad:
    a "..."
    a "Как он мог"
    a "Мы были вместе 5 лет..."
    a "И тут так внезапно"
    a "Почему?..."
    "*Плачет*"
    jump future

label future:
    play music "music/main.mp3"
    show text "прошло 3 месяца"
    pause 2
    hide text
    pause 2
    play sound "sounds/alarm.mp3"
    play sound "sounds/alarm.mp3"
    a "Выключись, зараза"
    #play sound "sounds/punchalarm.mp3"
    pause 0.5
    stop sound
    scene bg room
    a "Доброе утро, Аня"
    a "Говорю я сама себе уже третий месяц"
    a "Ладно, что я сегодня такая траурная..."
    a "Надо бы встать и принять хотя бы душ."
    a "Паппи, Паппи, туруруруруру"
    a "Иди сюда лапочка"
    a "Хм?"
    a "Паппи, почему рот в говне?"
    a "Тебе что, нормальной еды не хватает?"
    a "А..."
    a "Точно, я же её так и не купила..."
    a "Да и себе надо что-нибудь купить покушать."
    a "А денег нет..."
    a "Как я могла все 40.000 долларов проесть за 3 месяца..."
    a "Мне что, снова придётся стримить?"
    a "Эх..."
    a "Так уж и быть."
    a "Наверное, мои заечки соскучились там по мне"
    a "А то после расставания с Артёмом я ни разу так и не запустила стрим"
    a "Интересно, про меня ещё помнят?"
    a "Надо бы сегодня подготовиться к стриму основательно"
    a "И сделать пост в группу."
    a "Но это чуть позже."
    a "А сейчас, Паппи, пошли будем тебе рот мыть"
    scene bg black
    pause 1
    scene bg mainyt
    a "Так, надо бы выбрать видео, которые мы будем смотреть!"
    a "Столько новых видео, многие воскресли даже"
    a "Эх, столько контента."
    a "Всех не сможем посмотреть."
    a "Придётся выбирать."
    a "Так, кто там первые у нас на очереди?"
    menu:
        "Силена Свей":
            jump silena
        "Марина Морлок":
            jump morlok
label silena:
    a "Эх, давно Силеночку не смотрели"
    a "Посмотрим что нового продают в фикспрайсе"
    jump vibor_2
label morlok:
    a "О, у Морлок новое видео!"
    a "Надеюсь, не получу бан."
    jump vibor_2
label vibor_2:

    a "Так, выбрали, дальше"
    menu:
        "Гена Горин":
            jump Gorin
        "Андрей Гобзавр":
            jump Gobz
label Gorin:
    $ gena_gobz_flag = True
    a "Геночка!"
    a "Я так по нему скучала."
    a "Интересно, он ещё снимает видео с бомжами?"
    a "Вот как раз и посмотрим"
    jump vibor_3
label Gobz:
    $ gena_gobz_flag = False
    a "Ой, Андрюша, мой любимый урод."
    a "До сих пор стримит."
    a "Людка ещё не сдохла, интересно?"
    jump vibor_3

label vibor_3:
    a "Два есть, ещё."
    menu:
        "Виталик":
            jump vitalik_yt
        "Философ":
            jump filosof_yt
label vitalik_yt:
    $ vit_fil_flag = True
    a "Ну как же без Виталика и его Ангелины"
    a "И их кукольных котят."
    a "В каком теперь городе они живут?"
    a "Или снова в какой-то развалюхе обосновались?"
    a "Хочим посмотреть."
    jump vibor_4
label filosof_yt:
    $ vit_fil_flag = False
    a "Философ, мой сладенький"
    a "Вот этот вот с Геночкой гуляет"
    a "Помирился ли он с бомжами или нет?"
    jump vibor_4
label vibor_4:
    a "Думаю ещё пару и хватит."
    menu:
        "Вован":
            jump vova
        "Бига Егоров":
            jump biga
label vova:
    a "Так, Вован, ну посмотрим, что у него нового."
    jump vibor_5
label biga:
    a "Посмотрим Бигу Егорова."
    a "Главное, на кукольное порно случайно не попасть."
    jump vibor_5

label vibor_5:
    a "В конце надо бы посмотреть какой-нибудь обжор."
    menu:
        "Резников":
            jump reznik_yt
        "Толян":
            jump tola_yt
label reznik_yt:
    $ rez_tola_flag = True
    a "Серёжа, мой не первый и не последний московский видеоблогер."
    a "С пропиской в центре Москвы."
    a "Завидую прям в сопливую тряпчку."
    a "Вот бы тоже прописку."
    jump stream
label tola_yt:
    $ rez_tola_flag = False
    a "Ахуеть, Толян воскрес!"
    a "Так много обжоров снял."
    a "Надо будет заценить с моими любимыми зрителями подписчиками канала {a=https://www.youtube.com/user/ANNAMEOWCHANNEL/featured}Anna Meow{/a}."
    jump stream

label stream:
    a "Ну что ж, видео выбрали, осталось сделать анонс в группе."
    a "И в 6 часиков подрублю."
    scene bg black with dissolve
    pause 1
    show text "18:00"
#    if gena_gobz_flag:
#        if vit_fil_flag:
#            if rez_tola_flag:
#                show text "Вы выбрали Гену, Виталика и Резникова."
#                pause 2
#            else:
#                show text "Вы выбрали Гену, Виталика и Толяна."
#                pause 2
#        elif rez_tola_flag:
#            show text "Вы выбрали Гену, Философа и Резникова."
#            pause 2
#        else:
#            show text "Вы выбрали Гену, Философа и Толяна."
#            pause 2
#    elif vit_fil_flag:
#        if rez_tola_flag:
#            show text "Вы выбрали Гобзавра, Виталика и Резникова."
#            pause 2
#        else:
#            show text "Вы выбрали Гобзавра, Виталика и Толяна."
#            pause 2
#    elif rez_tola_flag:
#        show text "Вы выбрали Гобзавра, Философа и Резникова."
#        pause 2
#    else:
#        show text "Вы выбрали Гобзавра, Философа и Толяна."
#        pause 4
#    show text "Конец демо версии."
#    pause 3
#    show text "Спасибо за игру! <3"
#    pause 3
    show bg stream with dissolve
    a "Всем привет, привет всем."
    a "Как дела чатик?"
    ch "\"ToshkaGirl :3: приветик, пупси @deadclementine @Твистер. @Мемили Фиор @Pavs\""
    ch "\"пчола: ОГО, АНЯ, ТЫ ЖИВА!\""
    ch "\"Анитошка: девкам куни пацанам сосуни\""
    ch "\"xan46: Аня, пошли смотреть звуки пуков :)\""
    a "..."
    a "Ау, ау, ау, я тут тоже есть"
    a "Здороваются тут сами с собой, а со мной никто..."
    ch "\"Ника Рулетова: привет ан ВоронИна в поп мокоронИна\""
    ch "\"Анитошка: Здарова, Аня\""
    ch "\"Ника Рулетова: давай посмотрим видео про драку в макдональдсе!\""
    ch "\"AlemArtRu: Аня, давай посмотрим https://www.youtube.com/watch?v=-xsT-ViO4e8\""
    ch "\"Aiko Dark: У самой шкафы тоооо.....\""
    ch "\"Вежливый Лось: Если вы чувствуете, что охрипли, возможно, кто-то оглох.\""
    ch "\"Кто-то из чата1: @Вежливый Лось, ахахаххахаххахах\""
    ch "\"никита марко: Аня, какой сегодня парик?\""
    ch "\"Ивангай: заходите, у меня стрим!!!\""
    ch "\"Ивангай: заходите, у меня стрим!!!\""
    ch "\"Ивангай: заходите, у меня стрим!!!\""
    ch "\"пчола: модераторы ау\""
    ch "\"Анитошка: модераторы ау\""
    ch "\"Ника Рулетова: Госпади, отъебитесь от меня\""
    a "Ужас, чат, вы ахуели?"
    a "Только Ника и Анитошка поздаровались."
    a "Я в шоках."
    ch "\"Твистер.: also cringe no cap :weirdchamp:\""
    ch "\"Шнапсик: а что происходит?\""
    ch "\"Midori_: господи помилуй, господи помилуй, господи помилуй\""
    a "Мидори, спасибо за ссылку."
    a "Так, погнали смотреть с вами видосики"
    a "Я сегодня много чего подготовила."
    a "Так, снова смска от яндекс переводчика"
    ch "\"don someone: да, я да\""
    #define donat = Movies("videos/donat.webm", size=(200, 200)) # "Viktor NSK: Привет, Аня, я вот слышал, что ты рассталась с Артёмом, не хочешь пройти анкету на давай"
    a "Нет, Виктор, такого я точно проходить не буду."
    ch "\"Кто-то из чата1: Аня, где Морган?\""
    ch "\"Кто-то из чата2: зайди на стрим к Моргану, у них там бухлострим!\""
    a "Отстаньте со своим Морганом!"
    a "Ещё один вопрос про него и я закончу стрим!"
    #show donat
    a "Спасибо за донат Виктор, всем пока..."
    #стрим закончен
    a "Да уж, всё настроение испортили со своим Морганом."
    a "Зря запускала стрим."
    a "Что там Виктор НСК в донате скинул."
    a "Мммм, анкета на \"Давай поженимся\"."
    a "Ну можно по-приколу заполнить."
    a "Почему бы нет."
    play sound "sounds/clicks1.wav"
    scene bg anketa
    a "Что тут вообще за вопросы есть?"
    a "\"Фамилия, имя, отчество\""
    a "А есть поинтереснее вопросы?"
    a "\"Дата рождения\""
    a "Вы серьёзно?"
    a "\"Знак зодиака\""
    a "А это важно? Ну скорпион"
    a "Так"
    a "\"Какое приданое и чем вы готовы поделиться с избранником?\""
    menu:
        "Мощный игровой компьютер, машина и две вонючки животных":
            jump trupi
        "жИр":
            jump zhir

label trupi:
    $ trupi_zhir_flag = True
    jump anketa1

label zhir:
    $ trupi_zhir_flag = False
    jump anketa1

label anketa1:
    a "Что там дальше?"
    a "\"Есть ли у вас дети и сколько им лет\""
    menu:
        "Паппи и Китти":
            jump animals
        "Нет детей":
            jump childfree
label animals:
    $ animechild_flag = True
    jump anketa2
label childfree:
    $ animechild_flag = False
    jump anketa2
    a "\"О чём вы хотите предупредить своего избранника и с чем ему придётся смириться в браке\""
    menu:
        "Стримлю, не работаю":
            jump streams
        "В весе, с противным голосом":
            jump fat

label streams:
    $ strem_fat_flag = True
    jump anketa3

label fat:
    $ strem_fat_flag = False
    jump anketa3

label anketa3:
    a "\"Ваш мужской идеал\""
    menu:
        "С хорошим чувством юмора, верный, старше и толще меня самой":
            jump ideal1
        "Худой, успешный и самодостаточный":
            jump ideal2

label ideal1:
    $ ideal_flag = True
    jump anketa4
label ideal2:
    $ ideal_flag = False
    jump anketa4

label anketa4:
    a "\"Что вы категорически не приемлите в партнёре\""
    menu:
        "Зависимость от матери, слабоволие, враньё":
            jump kriterii1
        "Волосатую спину, глисты и нормальное поведение":
            jump kriterii2

label kriterii1:
    $ kriterii_flag = True
    jump dluc

label kriterii2:
    $ kriterii_flag = False
    jump dluc

label dluc:
    a "Анкету заполнили."
    a "Отправляем."
    a "Уверена, что я не пройду."
    a "Зачем я вообще её заполняла."
    a "Зря время потратила."
    #play sound "sounds/notification.mp3"
    a "М?"
    a "На почту письмо какое-то пришло."
    a "Так, посмотрим."
    play sound "sounds/keyword.mp3"
    play sound "sounds/clicks1.mp3"
    #scene bg gmail
    a "Что?"
    a "Вы что рофлите?"
    "\"Уважаемая, Воронина Анна Николаевна, Ваша анкета была рассмотрена. Просим вас явиться на съёмочную площадку по адресу г. Москва, ул. такая то, лялялялялял, 8.11.2019 года к 8:15.\""
    a "Это же в эту пятницу."
    a "Даже не знаю, идти или нет."
    a "Нуу, в принципе."
    a "Почему бы и нет."
    a "Я от этого ничего в принципе не теряю."
    a "Пойти что ли готовиться"
    a "Осталось не так уж и много времени"
    a "Всего два дня."
    a "Надеюсь, всё хорошо пройдёт"
    scene bg black with dissolve
    show text "Пятница, 8.09.2019, 8:12"
    pause 2
    #scene bg street
    a "Так, я на месте."
    a "Наверное, надо зайти внутрь."
    play sound "sounds/opendoor.mp3"
    #scene bg grim with dissolve
    play sound "sounds/closedoor.mp3"
    a "Тут кто-нибудь есть?"
    dg "Да, милочка, есть."
    #show larisa smile
    dg "Я Лариса Гузеева."
    dg "Приятно познакомиться."
    dg "А ты, как я понимаю наша героиня сегодняшняя?"
    dg "Как там тебя, Аня, да?"
    a "Да."
    dg "До начала съёмок осталось несколько минут."
    dg "Надеюсь, ты готова."
    dg "Если что можешь тут привести себя в порядок тут."
    dg "А я пойду готовиться к выходу."
    dg "Будем ждать через пару минут у сцены."
    dg "Пока."
    #hide larisa smile with dissolve
    a "Хм, привести себя в порядок или нет?"
    menu:
        "Да":
            jump mirror
        "Нет":
            jump preshow
label mirror:
    $ mirror_flag = True
    show bg mirror
    a "Хороший мейк сделала."
    a "Выгляжу просто прекрасно."
    a "Все женихи будут моими."
    jump shoow

label preshow:
    $ mirror_flag = False
    a "У меня и так всё хорошо с макияжем."
    jump kulisi

label kulisi:
    a "Пойду к Гузеевой."
    #scene bg scena with dissolve
    #show larisa smile
    dg "Привет, милочка."
    if mirror_flag:
        show larisa happy
        "Я смотрю ты всё же меня послушала и сделала нормальный макияж."
        "Молодец."
    else:
        show larisa nedovolna
        "Смотрю меня ты решила не слушать и оставить этот уродский макияж."
        "Если четсно, то ты больше похожа на какую-то экскортницу из Азейрбаджана."
        "Ну ладно."

    #show larisa smile
    dg "Давай расскажу тебе что сейчас делать."
    dg "Сейчас я выхожу на сцену, объявляю начало программы"
    dg "А потом выходишь ты."
    dg "Всё поняла"
    menu:
        "Да":
            jump yes
        "Нет":
            jump no
label yes:
    $ stupid = False
    #show larisa happy
    dg "Какая ты молодец, радуюсь не нарадуюсь."
    if !mirror_flag:
        dg "Вот бы ещё послушала меня и сменила бы макияж."
        dg "Цены бы не было."
    jump shoow
label no:
    $ stupid = True
    #show larisa angry
    dg "Я не понимаю, ты совсем что ли вся такая дурочка из себя?"
    dg "Знаешь, с таким умом тебе никогда не найти хорошего мужа."
    dg "В общем, выйдешь, когда я объявлю тебя."
    dg "Даже постараюсь произнести твоё имя погромче, чтобы услышала."
    jump shoow

label shoow:
    dg "Так, начинаем."
    #hide larisa smile
    #scene bg scena
    dg "Вы смотрите этот выпуск на {a=https://www.youtube.com/channel/UCvyma1G7ca7TQ7VtX2pPVug}официальном канале YouTube{/a}"
    dg "Не забудьте поставить лайк и нажать на колокольчик, чтобы не пропускать новые выпуски."
    hide larisa smile
    define zastavka = Movie(play="video/zastavka.webm", size=(1280, 720))
    show zastavka
    #scene bg stol with dissolve
    #show larisa smile with dissolve
    dg "Я Лариса Гузеева, это \"Давай поженимся\", добрый день."
    dg "Сегодня наши женихи:"
    #hide larisa smile
    #scene bg divan
    if gena_gobz_flag:
        show geshka smile at rightly
        show gena smile at center
        show gennadii smile at left
        dg "Гена!"
        hide geshka smile
        hide gena smile
        hide gennadii smile
    else:
        #show gobz at center
        #show luda at left
        dg "Андрей!"
        #hide gobz
        #hide luda
    if vit_fil_flag:
        #show vitalik smile at center
        show gulnara smile at left
        show rus smile at right
        dg "Виталик!"
        #hide vitalik smile
        hide gulnara smile
        hide rus smile
    else:
        show filosof smile at center
        show maks smile at left
        show lexa smile at right
        dg "Дмитрий!"
        hide filosof smile
        hide maks smile
        hide lexa smile

    if rez_tola_flag:
        show reznik smile at center
        #show golub at left
        dg "Сергей!"
        hide reznik smile
        #hide golub
    else:
        show tola smile
        dg "Анатолий!"
        hide tola smile
    show bg stol
    show larisa smile
    dg "А вот и наша героиня."
    if stupid:
        dg_shout "Аня!"
    else:
        dg "Аня."
    #play sound "sounds/aplodismenti.mp3"
    pause 2
    hide larisa smile
    show roza smile
    pause 1
    hide roza smile
    show vasilisa smile
    pause 1
    hide vasilisa
    stop sound
    if ideal_flag:
        if kriterii_flag:
            define anna_1 = Movie(play="video/anna1", size=(1280, 720))
            show anna_1
        else:
            define anna_2 = Movie(play="video/anna2", size=(1280, 720))
            show anna_2
    elif kriterii_flag:
        define anna_3 = Movie(play="video/anna3", size=(1280, 720))
        show anna_3
    else:
        define anna_4 = Movie(play="video/anna4", size=(1280, 720))
        show anna_4
    #проверить потом правильность видео!!!!!
    #play sound "sounds/aplodismenti.mp3"
    #show bg stol
    #show larisa smile at center
    dg "Здравствуй, малышка."
    dg "Хотя, судя по твоим формам, так нельзя сказать."
    dg "Скажи честно, любишь кушать по ночам?"
    a "Если честно, то да."
    dg "Заметно."
    dg "Чем ты вот вообще занимаешься в свои 21?"
    dg "Учишься или работаешь?"
    a "Работаю на ютубе."
    a "В основном занимаюсь стримингом."
    dg "А что это такое?"
    dg "Расскажи, пожалуйста, старому поколению."
    a "Ну это потоковое вещание в прямом эфире."
    a "В основном на таких эфирах я смотрю видеоролики."
    ds "И сколько ты зарабатываешь, если не секрет?"
    a "Ну всегда по-разному, зависит от настроения донатеров."
    a "Ну в среднем выходит около 5000 рублей за один такой эфир"
    dg "Давали б мне деньги, чтоб смотреть видеокарточки, а не на вас маргиналов пялиться..."
    a "Что простите?"
    dg "Ничего, милочка."
    dg "Расскажи лучше кто такие донатеры?"
    dg "Раз весь заработок зависит от них, то это важные люди скорее всего."
    a "Ну, это добрые зрители, котрые помогают материально."
    a "Закидывают деньги там."
    dg "То есть основной заработок идёт с попрошайничества?"
    dg "Хорошая профессия, ничего не скажешь."
    dg "Каждый раз в метро вижу пару стримеров безногих."
    dg "А у вас, надеюсь, конечности все на месте?"
    a "Всё на месте, можете не беспокойиться."
    show larisa smile at center_down with move
    show roza smile at right with dissolve
    ds "А у тебя есть вообще какое-нибудь образование?"
    show roza smile at right_down with move
    show larisa smile at center with move
    if animechild_flag:
        dg "Вот у тебя уже есть дети."
        dg "С очень необычными именами Паппи и Китти."
        dg "Сколько им лет?"
        dg "Их ровесники не обижают там?"
        dg "А то мало ли что."
        dg "Просто в моём детстве и не за такое унижали."
        dg "И не боишься ли ты, что мужчины не возьмут тебя с таким прицепом?"
        dg "Вроде 21, а уже 2 ребёнка на руках."
        a "Во-первых, Паппи и Китти - это мои домашние питомцы."
        a "Которые мне как родные дети."
        a "Во-вторых, хочется сразу сказать, что детей прям детей я заводить не собираюсь ещё лет 10."
        a "А что насчёт образования."
    else:
        dg "Уже дети не за горами."
        dg "Одним попрошайничеством ты их всю жизнь кормить не сможешь."
        dg "Знаешь, а мне ведь никто не помогал, когда я родила своего."
        a "Знаете, детей я не очень люблю."
        a "И в моих планах пока не заводить их ближайшие 10 лет уж точно."
        dg "Ты что одна из этих?"
        dg "Которые против детей?"
        a "Да, я чайлдфри."
        a "Не очень люблю детей."
        dg "Почему?"
        dg "Дети же это святое"
        dg "Как же без ребёночка?"
        dg "Зачем тогда жить?"
        a "Ну я живу для себя."
        a "Тем более у меня есть два домашних питомца, за которыми нужно следить!"
        a "Если у меня появится ребёнок, то я этого не вынесу."
        a "Не готова ещё к такой ответственности."
        dg "Ну, милочка моя, замужество - это всё тоже очень ответственно."
        dg "Чего пришла-то такая неподготовленая сюда?"
        dg "Да и дети всё же важно."
        dg "А то время летит так быстро."
        dg "Что не успеешь оглянуться, а тут уже и климакс прилетит."
        dg "А детей-то всё равно захочется."
        dg "Придётся детей брать из детдома, которых, возможно, бросили какие-то алкаши, наркоманы."
        dg "А гены-то не изменишь."
        dg "Задумайся о будущем."
        dg "Я просто волнуюсь за тебя."
        dg "Вижу ты нормальная."
        dg "Я уже прожила жизнь и знаю много"
        dg "Хотелось бы лучшего для тебя."
        dg "Ты вообще учишься где-нибудь?"
    a "Ну, у меня есть среднее профессиональное."
    a "Училась в университете."
    a "Ну как училась."
    a "Поступила из-за родителей."
    a "На занятия не ходила, курсовые в конце года покупала и сдавала, чтобы не отчислили."
    a "В итоге с пятого курса решила отчислиться."
    a "Поняла, что мне это ничего не даст в жизни особо."
    dg "А на кого училась-то, дорогуша?"
    a "На видеомонтажёра."
    dg "Уже работала?"
    a "Нет."
    a "Я работаю на ютубе и занимаюсь стримингом уже много лет."
    dg "Ну и что же ты будешь, если это всё закроют?"
    a "Ну хотя опыт попрошайничества точно поможет"
    а "Я непонимаю почему вы меня постоянно унижаете."
    a "Я для этого могу почитать свой чат!"
    dg "Анна пойми, я просто хочу вставить тебе мозги на место!"
    dg "Я очень прониклась твоей историей за эти 5 минут и просто хочу помочь"
    dg "Ты не глупая девочка ведь!"
    а "Какой историей?"
    a "Я даже не начинала говорить про свою жизнь"
    dg "Это защитный механизм, можешь врать себе и успокаивать, что выпрашивать деньги нормально."
    dg "Желаю найти тебе выйти замуж за богатенького мужика."
    a "Вы считаете я не смогу сама себя обеспечить?"
    a "Я смогу найти работу, если это понадобится, Я СИЛЬНАЯ И НЕЗАВИСИМАЯ!"
    dg "Я вижу, что вы горды собой и без комплексов."
    dg "Мужчины не всегда любят таких темпераментных женщин."
    a "Зачем мне молодой человек, который не будет меня уважать и мой жир с противным голосом."
    а "Я не надеюсь найти принца, главное чтоб уважал и не изменял..."
    dg "Скажите, а что случилось с вашим прошлым партнёром, это же связано с вашими словами про измену?"
    a "Моего бывшего звали Артём Морган, может вы про него слышали.."
    a "У нас были грандиозные планы, мы хотели кардинально изменить свою жизнь."
    a "Собирались переехать в Эквадор."
    a "Не спрашивайте, почему именно туда!"
    a "Мы собирали деньги, почти расписались."
    a "Но вот 3 месяца назад я случайно его застала с другим мужчиной."
    a "Я знала, что они были близки, но не настолько."
    a "И знаете, меня всю охватила печаль."
    a "Я плакала, наверное, недели 2."
    a "И ещё недель 7 просто лежала в кровати."
    a "Это расставание было слишком болезненным для меня."
    dg "Боже.."
    dg "Малышка моя, мне так жаль..."
    dg "ВОТ ЖЕ ПИДАРАС! ПИДАРАСИНА!"
    dg "Как он мог променять такую красивую девочку на парня."
    dg "Забудь про него, милая, он тебя не достоин."
    dg "Найдём тебе нового, не переживай."
    dg "Давайте посмотрим на первого нашего жениха."
    dg "Иди, встречай."
    play sound "sounds/aplodismenti.mp3"
    pause
    if vit_fil_flag:
        jump vitalik
    else:
        jump filosof

label filosof:
    play music "music/dp.mp3"
    show bg red_scena
    pause 3
    show vitalik smile
    fil "Привет, меня зовут Дмитрий."
    fil "Я тоже работаю на ютубе, расчитываю на коллаб."
    fil "Пройдём."

    define filosof_anketa = Movie(play="video/filosof.webm", size=(1280, 720))
    show filosof_anketa

    jump spletni_vit
label vitalik:
    play music "music/dp.mp3"
    show bg red_scena
    pause 3
    show vitalik smile
    fil "Привет, меня зовут Дмитрий."
    fil "Я тоже работаю на ютубе, расчитываю на коллаб."
    fil "Пройдём."
    hide vitalik smile
    define vitalik_anketa = Movie(play="video/vitalya.webm", size=(1280, 720))
    show vitalik_anketa
    scene bg stol
    show larisa smile
    dg "Привет, Виталик."
    dg "Ну что, рассказывай, кто ты."
    hide larisa smile
    show vitalik smile
    vn "Ну я блоггер, снимал видео со своей женой."
    hide vitalik smile
    show larisa smile
    dg "Женой?"
    dg "Если у тебя есть жена..."
    dg "Прости, но что ты тут тогда делаешь?"
    hide larisa smile
    show vitalik smile
    vn "Ну, короче, это..."
    vn "Мы поссорились с ней."
    vn "Короче, я стримил, пил с другом."
    vn "А она с нихуя выключила мне стрим."
    vn "И начала меня орать."
    vn "Какая муха её укусила, я не понимаю."
    vn "Я всё для неё делал, ёпт."
    vn "А она не понимала."
    vn "Я даже цветы ей купил, чтобы она меня простила."
    vn "А она меня избила ими, гадина."
    vn "Ну... короче да она до меня она ещё не доросла."
    hide vitalik smile
    show larisa smile
    dg "Ну, Виталий, на сколько я знаю, избивали Ангелину вы, а не она вас."
    hide larisa smile
    show vitalik smile
    vn "Я?!"
    vn "Да я бы никогда никогда не поднял на неё руку!"
    vn "Да я не бил её никогда."
    vn "Я её поцеловать хотел."
    vn "Да, Ангелина?"
    show vitalik angry at right with move
    show angelina smile at center with dissolve
    play sound "sounds/sverchki.mp3"
    an "..."
    vn "Чо по чём, Ангелина, ты чего молчишь, э?"
    vn "Ты чо язык проглотила, а?"
    vn "Хуя, тебе что, э, кукольная что ли?"
    hide angelina smile with moveoutleft
    show vitalik smile at center with move
    hide vitalik smile
    show larisa smile
    dg "Мальчик мой, что это за мешок с картошкой?"
    dg "С какого огорода ты эту картошку принёс?"
    dg "И зачем?"
    hide larisa smile
    show vitalik angry
    vn "Э, какой мешок, чё по чём..."
    vn "Какой нахуй мешок?"
    vn "Я чо сюда пришёл, чтобы меня хуями крыли?"
    hide vitalik smile
    show larisa smile
    dg "Виталий, успокойтесь, ведите себя адекватно."
    dg "Вы тут не на пьянку пришли."
    dg "Аня, посмотри на него."
    dg "Алкаш, пьяница, куряга, небось и наркоман."
    dg "Тебе нужно такое будущее?"
    dg "Тебе это надо?"
    dg "Вот я всё знаю, я всё это пережила."
    dg "Вот мой бывший муж."
    dg "Царствие ему небесное."
    dg "Он бил меня по виску гантелей, чтобы посмотреть, как расширяются мои зрачки."
    dg "Вот поверь, с ним тебя ждёт тоже самое."
    dg "Я не могу врать, я желаю тебе самого лучшего."
    hide larisa smile
    show vitalik angry
    vn "Э, вы чо нахуй."
    vn "Кто нахуй?"
    vn "Я нахуй?"
    vn "Я бросил вообще-то"
    vn "Уже 2 дня не пью, зуб даю, отвечаю короче."
    vn "Всего 2 сигареты за день скурил."
    vn "Э, блин, пойду короче сюрприз показывать, заебали блять."

    define vit_surprize = Movie(play="video/vitsur.webm", size=(1280, 720))
    show vit_surprize
    show larisa smile
    dg "Можешь пройти к себе в комнату."
    jump spletni_vit


label spletni_fil:

    if gena_gobz_flag:
        jump gennadii
    else:
        jump gobzavr

label spletni_vit:

    if gena_gobz_flag:
        jump gennadii
    else:
        jump gobzavr

label gennadii:
    jump spletni_gena
label gobzavr:
    play music "music/dp.mp3"
    show bg red_scena
    pause 3
    show gobz smile
    gob "Привет, я Аааааааандрей Гооооооообзавр!"
    gob "Привет, Аня Мяу."
    gob "Надеюсь, ты выберешь меня, ведь мы давно знакомы, и я знаю, что я тебе нравлюсь."
    gob "Пройдём."
    hide gobz smile
    define gobz_anketa = Movie(play="video/gobz.webm", size=(1280, 720))
    show gobz_anketa
    scene bg stol
    show larisa smile
    dg "Привет, милый мой."
    dg "Ты такой красивый и весёлый."
    dg "Настроение даже поднял."
    dg "С кем пришёл, мой сладкий?"
    hide larisa smile
    show gobz smile
    gob "Я пришёл со своей любимой мамочкой."
    gob "Людмилой Людмурик."
    dg "Как я понимаю, вы с мамой ведёте канал вместе? Что снимаете то?"
    gob "Ой... Мама моя оочень любит анекдотики вот.. наши дорогие телезрители ещё донатят нам на клипы и мы вот очень любим под них танцевать да!"
    ll "Вот бы ты это вот это блин ну не забирал себе эта деньги все, я же я.. я всё для стримов эээ делаю вот это вот!! 
    ll "И картинки блин днями вот и ночами вырезаю это вот лучшие самые смешные мои, а ему бы хоть что, тварь..."
    ll "Знаете, а вот это у меня вот уже несколько книг этаа с анекдотами.. А что он??? Он то ЧТО сделал то а? Нихую не делает, сидит и пьет как свинья"
    gob "Мама... что ты тут такое говоришь??? Не негативь, Мама"
    dg "Боже, так разговаривать с матерью, ну вы что, дорогой??! С ума сошли?"
    dg "Неужели на стримах вы тоже так обращаетесь с матерью? Ну это же просто недопустимо!"
    ll "Понимаете, вы просто мою маму не знаете"
    ll "Попробовали б вы с ней пожить хотя бы день!"
    ll "Мама пьёт
    
    
    show gobz smile at right with move
    show luda smile at center with moveinleft
    ll "Всем привет."
    ll "Я так рада побывать на этом шоу, вот честно."
    ll "Плачу."
    
    show gobz smile at center with move
    show luda smile at left with move



    jump spletni_gobz

label spletni_gena:
    if rez_tola_flag:
        jump reznikov
    else:
        jump tola

label spletni_gobz:
    if rez_tola_flag:
        jump reznikov
    else:
        jump tola

label reznikov:
    jump spletni_rez
label tola:
    play music "music/dp.mp3"
    show bg red_scena
    pause 3
    show tola smile
    ls "Привет, я Толя."
    ls "Я бывший ютубер, занимался ютубом, мой канал LinkinSimpson на ютубе, вот."
    ls "Знаешь, вот, надеюсь, у нас будет очень сильная любовь, вот"
    ls "Очень сильная и крепкая любовь."
    ls "Знаешь, давай пройдём."
    define tola_anketa = Movie(play="video/tola.webm", size=(1280, 720))
    show tola_anketa
    scene bg stol
    show larisa smile at center
    dg "Ну привет, Анатолий."
    dg "Как такой красивый, скромный и обоятельный мужчина, а до сих девственник."
    hide larisa smile
    show tola smile
    ls "Знаете, я не хочу просто секса, просто секс мне не нужен, я вот знаете."
    ls "Я на самом деле очень романтичный и хрупкий человек."
    ls "Хоть по мне и не скажешь."
    ls "И я вот романтичный и очень сильно люблю."
    ls "И хочу секс только по любви, понимаете."
    ls "Никак иначе."
    hide tola smile
    show larisa kakaya-to
    dg "Толя, хватит, ты уже повторяешься, остановись."
    dg "Ты так нудишь, что задушить хочется."
    dg "Тебя не беспокоит, что ты всё ещё живёшь с мамой?"
    dg "Тебе уже 30 лет."
    dg "Пора уже найти работу."
    dg "Съехать от матери."
    hide larisa smile
    show tola smile
    ls "Ну понимаете, я не хочу работать."
    ls "Вот знаете, я всю жизнь любил сидеть дома."
    ls "Но родители меня всё время заставляли учиться."
    ls "И говорили, что работа никуда не денется, лучше сначала отучиться."
    ls "Работа не убежит, и вот забрали меня из ПТУ."
    ls "Заставили учиться в колледже, вот."
    ls "Но я не хотел учиться, я хотел дома сидеть, понимаете."
    ls "И вот у меня нет желания работать, да."
    ls "У меня есть мама, бабушка, они достаточно зарабатывают."
    ls "Мы не бедные, мама бабушка меня всем обеспечивает, вот"
    ls "Мама говорит, что ничего мне не должна."
    ls "Но я считаю, что она должна принять меня таким, какой я есть."
    ls "Ну не хочу я работать, да"
    ls "И знаете, я уверен, что каждый должен принять своих близких такими, какими они должны быть, вот да."
    ls "Надеюсь, Аня поймёт меня и примет меня таким, какой я есть, вот."
    hide tola smile

    show roza smile
    ds "Что ж.. Вы очень интересная личность, как я вижу."
    ds "А чем вы сможете очаровать, что можете дать?"
    hide roza smile
    show tola smile
    ls "Я могу многое."
    ls "Например, я хорошо танцую."
    ls "Знаете, я очень сильно люблю, и когда люблю, мне не важны недостатки."
    ls "Я и сам очень красивый."
    ls "Вот не хочу хвастаться, но у меня член стоит, как скала."
    ls "Вот знаете, я дрочу и уже всё, а он стоит и я не знаю, что с ним делать."
    ls "А ещё будем гулять по моим любимым местам."
    ls "Качаться на качелях во дворе на улице парковая 15, между домами 42 и 52 корпус 2."

    ls "Слушать моих любимых исполнителей, слушать Майли Сайкус старые песни."
    ls "Ханну Монтану 1, Ханну Монтану 2, вот."
    ls "Так люблю Майли Сайрус, правда старые её песни только."
    ls "Сейчас она какая-то развратная шлюха."
    ls "Образ её мне не нравится."
    ls "А ещё, вот знаете, почему я LinkinSimpson."
    ls "Я был фанатом Линкин парк, когда ещё вышел альбом метеор, я стал фанатом в те времена 2001, 2002, 2003 годы."
    am "О, Линкин Парк."
    am "Я тоже его обожала."
    am "Мы с Артёмом благодаря их музыке познакомились."
    am "Так... не надо о плохом."
    ls "Я их просто обожал, был огромным фанатом, как вы можете заметить."
    ls "А ещё вот я любил да и люблю очень сильно сейчас."
    ls "Эшли Симпсон, ну вообще правильно Ашли в Америке называют, но в России Эшли, но ладно."
    ls "Я её люблю вот очень сильно, могу часами её слушать и смотреть на неё."
    ls "Всё в ней люблю, кроме её пения."
    ls "Люблю, как женщину в общем."
    hide tola smile
    show larisa smile
    dg "То есть ты любишь знаменитостей?"
    dg "А ничего, что вы никогда не сможете быть вместе?"
    hide larisa smile
    show tola smile
    ls "Ну почему?"
    ls "Мы все люди, и каждый человек может быть с другим человеком, главное, чтобы они нравились друг другу."
    ls "Вот знаете, если бы у меня была возможность попасть в Америку и встретиться с, например, той же Ашли Симпсон."
    ls "И если мы могли бы быть вместе, если бы друг другу понравились, всё зависит от человека."
    ls "Мы же люди, все люди могут всречаться с кем могут."
    hide tola smile
    show larisa smile
    dg "А ты смотрел на девушек в жизни, не пытался пробовать встречаться с ними?"
    hide larisa smile
    show tola smile
    ls "Да, и я встречался."
    ls "У меня было 2 девушки."
    ls "Вот знаете, первая."
    ls "Вот мы встречались, влюблялись в друг друга потихоньку."
    ls "Но в один момент, она говорит, что вот у неё бывший отучился, бизнес завёл, и ушла к нему."
    ls "Ну и не надо!"
    ls "А со второй, вот"
    ls "Знаете, я первый её бросил, вот разлюбил."
    ls "И больше отношений не заводил, вернулся к знаменитостям."
    hide tola smile
    show vasilisa smile
    dv "Анатолий, вы у нас телец."
    dv "Когда любит мужчина Телец, то ему свойственно проявлять – рассудительность, спокойствие и здравый смысл."
    dv "На жизнь он смотрит реалистично, приземленно."
    dv "Однако, несмотря на некоторую сдержанность чувств, эмоций."
    dv "Это не мешает ему увлекаться чувственными аспектами любви и вести себя как истинный гурман в любовных отношениях."
    dv "Вы у нас гурман в еде, значит и с женщиной вы будете обходительны."
    hide vasilisa smile
    show larisa smile
    dg "Толя, у меня ещё один вопрос к тебе."
    dg "Вот ты снимал раньше ролики, но потом почему-то ушёл на время."
    dg "Почему?"
    hide larisa smile
    show tola smile
    ls "Ну я, знаете."
    ls "Меня достали хейтеры, они доставали меня, облили дверь краской, вот"
    ls "Знаете, узнали мой адрес, облили краской дверь, и я решил, что лучше уйти."
    ls "Понимаете, это был вот лучший, наверное, выход."
    ls "Страшно сказать, что они могли дальше сделать, вот."
    hide tola smile
    show larisa smile
    dg "Ладно, Толя."
    dg "Мы всё поняли."
    dg "Я так тебя понимаю."
    dg "Вот меня тоже эти хейтеры в соц сетях достали."
    dg "Называют алкоголичкой."
    dg "В общем, показывай сюрприз."
    hide larisa smile
    show tola smile
    ls "Хорошо, у меня вот видеосюрприз."
    ls "Ане, надеюсь очень сильно понравится."
    hide tola smile
    define surprize_tola = Movie(play="video/surtola.webm", size=(1280, 720))
    show surprize_tola
    pause 2
    show larisa smile
    dg "Ну чтож Толя, можешь проходить в свою комнату."

    jump spletni_tola

label spletni_rez:
    jump choice_husband
label spletni_tol:
    jump choice_husband

label choice_husband:
    if gena_gobz_flag:
        if vit_fil_flag:
            if rez_tola_flag:
                menu:
                    "Геннадий":
                        jump gena_end
                    "Виталик":
                        jump vit_end
                    "Резников":
                        jump rez_end

            else:
                menu:
                    "Геннадий":
                        jump gena_end
                    "Виталик":
                        jump vit_end
                    "Толя":
                        jump tola_end
        elif rez_tola_flag:
            menu:
                "Геннадий":
                    jump gena_end
                "Философ":
                    jump fil_end
                "Резников":
                    jump rez_end
        else:
            menu:
                "Геннадий":
                    jump gena_end
                "Философ":
                    jump fil_end
                "Толя":
                    jump tola_end
    elif vit_fil_flag:
        if rez_tola_flag:
            menu:
                "Андрей":
                    jump gobz_end
                "Виталик":
                    jump vit_end
                "Резников":
                    jump rez_end
        else:
            menu:
                "Андрей":
                    jump gobz_end
                "Виталик":
                    jump vit_end
                "Толя":
                    jump tola_end
    elif rez_tola_flag:
        menu:
            "Андрей":
                jump gobz_end
            "Философ":
                jump fil_end
            "Резников":
                jump rez_end
    else:
        menu:
            "Андрей":
                jump gobz_end
            "Философ":
                jump vit_end
            "Толя":
                jump tola_end


label gobz_end:
    if gobz_flag:
        jump gobz_good_end
    else:
        jump gobz_bad_end

label gena_end:
    if gena_flag:
        jump gena_good_end
    else:
        jump gena_bad_end

label vit_end:
    if vit_flag:
        jump vit_good_end
    else:
        jump vit_bad_end
label fil_end:
    if fil_flag:
        jump fil_good_end
    else:
        jump fil_bad_end
label rez_end:
    if rez_flag:
        jump rez_good_end
    else:
        jump rez_bad_end

label tola_end:
    scene bg black
    show text "Исчезнувшая концовка."
    jump titri

label gobz_good_end:
    scene bg black
    show text "Хорошая концовка Гобзавра."
    jump titri
label gobz_bad_end:
    scene bg black
    show text "Плохая концовка Гобзавра."
    jump titri

label gena_good_end:
    scene bg black
    show text "Реальная концовка."
    jump titri
label gena_bad_end:
    scene bg black
    show text "Плохая концовка Гены."
    jump titri

label vit_good_end:
    scene bg black
    show text "Кукольная концовка."
    jump titri

label vit_bad_end:
    scene bg black
    show text "Плохая концовка для Ангелины."
    jump titri

label rez_good_end:
    scene bg black
    show text "Улётная концовка."
    jump titri
label rez_bad_end:
    scene bg black
    show text "Завидуем в сопливую тряпочку счастью голубя и Резникова."
    jump titri

label fil_good_end:
    scene bg black
    show text "Концовка с бомжами."
    jump titri

label fil_bad_end:
    scene bg black
    show text "\"Я даже не удивлён\" концовка."
    if mac_flag:
        if mirror_flag:
            jump secret_end
    jump titri

label secret_end:
    jump titri

label titri:
    return
