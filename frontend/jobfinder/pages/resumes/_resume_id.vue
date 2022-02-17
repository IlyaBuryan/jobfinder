<template>
  <div class="vacancy_wrapp">
      <!-- Page header -->
    <header class="page-header">
      <div class="container">
        <div class="header-detail">
          <div class="header-detail__head">
            <img class="logo" :src="vacancy.img" alt="">
            <div class="header-detail__head_main">
              <div class="hgroup">
                <h1>{{ vacancy.title}}</h1>
                <h3><a href="#">{{ vacancy.company }}</a></h3>
              </div>
              <div class="header-detail__head_main-time">{{ vacancy.vacancyTime }}</div>
            </div>
          </div>
          <hr>
          <p class="header-detail__head_main-descr">{{ vacancy.descr }}.</p>
          <div class="header-detail__footer">
            <ul class="header-detail__head_main-params">
              <li>
                <i class="fa fa-map-marker"></i>
                <span>{{ vacancy.location }}</span>
              </li>

              <li>
                <i class="fa fa-briefcase"></i>
                <span>{{ vacancy.worktime }}</span>
              </li>

              <li>
                <i class="fa fa-money"></i>
                <span>{{ vacancy.salary }}</span>
              </li>
            </ul>
            <ul class="header-detail__head_main-params">
              <li>
                <i class="fa fa-clock-o"></i>
                <span>40h / week</span>
              </li>

              <li>
                <i class="fa fa-flask"></i>
                <span>2+ years experience</span>
              </li>

              <li>
                <i class="fa fa-certificate"></i>
                <a href="#">{{ vacancy.educ }}</a>
              </li>
            </ul>
          </div>

          <div class="button-group">
            <ul class="social-icons">
              <li class="title">Разместить на</li>
              <li><a class="facebook" href="#"><i class="fa fa-facebook"></i></a></li>
              <li><a class="google-plus" href="#"><i class="fa fa-google-plus"></i></a></li>
              <li><a class="twitter" href="#"><i class="fa fa-twitter"></i></a></li>
              <li><a class="linkedin" href="#"><i class="fa fa-linkedin"></i></a></li>
            </ul>

            <div class="action-buttons">
              <a class="btn btn-primary" href="#">Разместить на linkedin</a>
              <a class="btn btn-success" href="#">Откликнуться</a>
            </div>
          </div>

        </div>
      </div>
    </header>
    <!-- END Page header -->


    <!-- Main container -->
    <main>

      <!-- Job detail -->
      <section class="vacancy-info">
        <div class="vacancy-info__container">

          <p>Google is and always will be an engineering company. We hire people with a broad set of technical skills who
            are ready to tackle some of technology's greatest challenges and make an impact on millions, if not billions,
            of users. At Google, engineers not only revolutionize search, they routinely work on massive scalability and
            storage solutions, large-scale applications and entirely new platforms for developers around the world. From
            AdWords to Chrome, Android to YouTube, Social to Local, Google engineers are changing the world one
            technological achievement after another.</p>

          <br>
          <h4>Responsibilities</h4>
          <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec odio. Quisque volutpat mattis eros. Nullam
            malesuada erat ut turpis. Suspendisse urna nibh, viverra non.</p>
          <ul>
            <li>Build next-generation web applications with a focus on the client side.</li>
            <li>Redesign UI's, implement new UI's, and pick up Java as necessary.</li>
            <li>Explore and design dynamic and compelling consumer experiences.</li>
            <li>Design and build scalable framework for web applications.</li>
          </ul>

          <br>
          <h4>Minimum qualifications</h4>
          <ul>
            <li>BA/BS degree in a technical field or equivalent practical experience. </li>
            <li>2 years of relevant work experience in software development.</li>
            <li>Programming experience in C, C++ or Java.</li>
            <li>Experience with AJAX, HTML and CSS.</li>
          </ul>

          <br>
          <h4>Preferred qualifications</h4>
          <ul>
            <li>Interest in user interface design.</li>
            <li>Web application development experience.</li>
            <li>Experience working on cross-browser platforms.</li>
            <li>Development experience designing object-oriented JavaScript.</li>
            <li>Experience with user interface frameworks such as XUL, Flex and XAML.</li>
            <li>Knowledge of user interface design.</li>
          </ul>

        </div>
      </section>
      <!-- END Job detail -->

    </main>
    <!-- END Main container -->
  </div>
</template>

<script>
export default {
  data () {
    return {
      loading: false,
      workerList: [],
      worker: {},
      workerId: '',
      resumeId: '',
      resumeList: [],
      resume: {},
      testVacancyList: [
        {
          id: 1, title: 'Помощник бухгалтера', img: require('~/assets/img/companyIcons/Marvel.jpeg'), company: 'ГК Марвел', location: 'Санкт-Петербург', worktime: 'Full-Time', link: 'job-detail.html', salary: 'ЗП: 50 050', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Официальное трудоустройство с первого рабочего дня в соответствии с ТК РФ. Уютный офис в шаговой доступности от метро Фрунзенская .Расширенный компенсационный пакет. Скидки на продукцию партнеров компании.', category: 'Финансы'
        },
        {
          id: 2, title: 'Python Developer', img: require('~/assets/img/companyIcons/KPMG.svg'), company: 'KPMG', location: 'Москва', worktime: 'Full-Time', link: 'job-detail.html', salary: 'ЗП: от 80 000', educ: 'Высшее', vacancyTime: '01.02.2022', descr: 'Решать задачи проектирования и разработки компонентов продукта. Проводить код-ревью решений коллег, предоставлять аргументированную критику. Уточнять и документировать собственные решения. Самостоятельность, способность анализировать и предлагать новые, возможно неочевидные, решения. Способность донести свои предложения и решения до команды, объяснить их плюсы.', category: 'Разработка'
        },
        {
          id: 3, title: 'Дизайнер-верстальщик', img: require('~/assets/img/companyIcons/Zebra.png'), company: 'Зебра-ПР', location: 'Москва', worktime: 'Full-Time', link: 'job-detail.html', salary: 'ЗП: 70 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Верстка русско- и англоязычных макетов многополосных изданий на основе утвержденных дизайн-макетов. Разработка инфографики (графики, схемы, иконки и т.п.) Углубленные знания пакета Adobe (InDesign, Illustrator, Photoshop, Acrobat). Чувство композиции и прекрасного. Портфолио. Обязателен опыт работы с многополосными изданиями', category: 'Дизайн'
        },
        {
          id: 4, title: 'Менеджер по работе с клиентами', img: require('~/assets/img/companyIcons/Bankirro.jpeg'), company: 'БАНКИРРО', location: 'Саранск', worktime: 'Удаленно', link: 'job-detail.html', salary: 'ЗП: до 100 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Проводить первичную консультацию клиентов, и передавать их в отдел продаж для визита на консультацию в офис (только горячие клиенты, входящий...Если Вы уверены, что способны показывать твердые результаты в продажах, Вас не пугают вызовы и готовность ставить перед собой большие цели', category: 'Работа с клиентами'
        },
        {
          id: 5, title: 'Медицинская сестра', img: require('~/assets/img/companyIcons/gemotest.jpeg'), company: 'Гемотест', location: 'Ангарск', worktime: 'Full-Time', link: 'job-detail.html', salary: 'ЗП: от 45 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Взятие биоматериала (венозной и капиллярной крови, гинекологических и урологических мазков). Информирование пациентов об оказываемых услугах, их стоимости, сроках исполнения, правилах сбора биоматериала, подготовке к исследованиям и т.п. Оформление медицинской документации', category: 'Здравоохранение'
        },
        {
          id: 6, title: 'Производитель работ/начальник участка', img: require('~/assets/img/companyIcons/oilberg.jpeg'), company: 'OILBERG', location: 'Москва', worktime: 'Full-Time', link: 'job-detail.html', salary: 'ЗП: от 80 000', educ: 'Высшее', vacancyTime: '03.02.2022', descr: 'Организация общестроительных и электромонтажных работ на объекте. Технический надзор за выполнением работ, приемка работ, консультация. Организация доставки инструментов и оборудования на объект. Опыт работы прорабом или начальником участка от 3 лет. Чтение схем и чертежей. ', category: 'Строительство'
        },
        {
          id: 7, title: 'Менеджер по продажам', img: require('~/assets/img/companyIcons/5M.png'), company: '5M', location: 'Екатеринбург', worktime: 'Полная занятость', link: 'job-detail.html', salary: 'ЗП: 48 000 - 72 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Продавать веб-сервисы по телефону. База предоставляется. Общаться с клиентами: руководителями, бухгалтерами, специалистами по безопасности. Вести весь цикл общения с клиентом. Грамотно и четко излагаешь свои мысли. Умеешь работать с информацией: запоминать, анализировать, понимать, как использовать в работе.', category: 'Продажи'
        },
        {
          id: 8, title: 'Маркетолог-аналитик', img: require('~/assets/img/companyIcons/arkont.jpeg'), company: 'АРКОНТ', location: 'Волгоград', worktime: 'Частичная занятость', link: 'job-detail.html', salary: 'ЗП: 50 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Маркетолог-аналитик работает на стыке двух профессий, применяя аналитический подход и инструментарий в маркетинговой сфере. Маркетолог-аналитик собирает и анализирует информацию. Личные качества: Аналитическое мышление. Знания в области интернет-маркетинга. Технические компетенции и знание инструментов анализа. Знания: Аналитическое мышление. Google Analytics.', category: 'Маркетинг'
        },
        {
          id: 9, title: 'Системный администратор', img: require('~/assets/img/companyIcons/rarus.png'), company: '1C-Рарус', location: 'Новосибирск', worktime: 'Full-Time', link: 'job-detail.html', salary: 'ЗП: от 50 000', educ: 'Высшее', vacancyTime: '01.02.2022', descr: 'Принимать заявки от первой линии поддержки. Диагностировать проблему и предлагать ряд решений. Обеспечивать безопасность и сохранность данных клиента.Опыт работы от 1 года. Интерес к технологиям. Способность разбираться в проблеме и копать до ее сути, решать проблему.', category: 'Информационные технологии'
        },
        {
          id: 10, title: 'Помощник руководителя', img: require('~/assets/img/companyIcons/tapp.jpeg'), company: 'Открытые технологии', location: 'Белгород', worktime: 'Full-Time', link: 'job-detail.html', salary: 'ЗП: 40 000', educ: 'Высшее', vacancyTime: '26.01.2022', descr: 'Контроль исполнения всех распоряжений и приказов генерального директора ответственными лицами. Планирование, координация и ведение рабочего графика руководителя. Организация внешних и внутренних встреч. Высшее профессиональное образование. Опыт работы в должности "помощник руководителя" на производственном предприятии не менее 1 года. Обязательное знание программ Excel.', category: 'Другое'
        },
        {
          id: 11, title: 'Бухгалтер', img: require('~/assets/img/companyIcons/bsg.png'), company: 'BGS Group', location: 'Санкт-Петербург', worktime: 'Full-Time', link: 'job-detail.html', salary: 'ЗП: от 70 000', educ: 'Высшее', vacancyTime: '04.02.2022', descr: 'Участие в ежемесячном закрытии периода, помощь в подготовке и сдаче бухгалтерской и налоговой отчетности. Выполнение поручений главного бухгалтера и руководства.Опыт работы с кадровым делопроизводствам. Знание бухгалтерского и налогового учета. Знание 1С: Предприятие 8.2. ЗУП 8.2', category: 'Финансы'
        },
        {
          id: 12, title: 'Программист-разработчик Python', img: require('~/assets/img/companyIcons/lightmans.png'), company: 'Lightmans', location: 'Москва', worktime: 'Полная занятость', link: 'job-detail.html', salary: 'ЗП: до 100 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Наша компания работает над развитием действующего портала по поиску работы и персонала. Обязанности: Бэкенд-разработка. Работа по ТЗ Заказчика.Опыт бэкенд-разработки на языке программирования python, владение фреймворками Django. Владение веб-серверами вроде Nginx, uwsgi/gunicorn. Владение SQL-базами', category: 'Разработка'
        },
        {
          id: 13, title: 'Дизайнер презентаций', img: require('~/assets/img/companyIcons/sbs.png'), company: 'SBS Consulting', location: 'Москва', worktime: 'Частичная занятость', link: 'job-detail.html', salary: 'ЗП: от 30 000', educ: 'Высшее', vacancyTime: '25.01.2022', descr: 'Переработка сложных данных, большого количества контента и систематизация информации Работа с графиками, таблицами, дашбордами и схемами. Подбор качественных изображений, фото.Учитесь на 4 курсе бакалавриата или 1-2 курсе магистратуры профильного направления. Вам необходима практика или стажировка. Умееет соблюдать сроки. ', category: 'Дизайн'
        },
        {
          id: 14, title: 'Оператор (консультант) колл-центра в банк, удалённо (входящие обращения в чате / входящие звонки)', img: require('~/assets/img/companyIcons/startjob.png'), company: 'Start-Job', location: 'Севастополь', worktime: 'Частичная занятость', link: 'job-detail.html', salary: 'ЗП: от 25 000', educ: 'Высшее', vacancyTime: '03.02.2022', descr: 'Консультировать клиентов банка по телефону и в чате (входящие обращения, без продаж и обзвонов). Проводить простые банковские операции.Вы сами выбираете удобное время работы и согласовываете с руководителем. Грамотная речь. Умение вежливо разговаривать с клиентами. Для работы нужен компьютер и гарнитура', category: 'Работа с клиентами'
        },
        {
          id: 15, title: 'Врач-хирург', img: require('~/assets/img/companyIcons/pavlovmed.png'), company: 'МЦ Павлов Мед', location: 'Ростов-на-Дону', worktime: 'Полная занятость', link: 'job-detail.html', salary: 'ЗП: 30 000 - 100 000', educ: 'Высшее', vacancyTime: '28.01.2022', descr: 'Амбулаторный прием пациентов (первичный, повторный). Выполнение различных хирургических операций и манипуляций в рамках амбулаторной хирургии. Ведение необходимой правовой и медицинской...Образование - высшее профессиональное медицинское. Обязательно наличие действующего сертификата на осуществление медицинской деятельности по специальности. Опыт работы по специальности не менее 3-х лет', category: 'Здравоохранение'
        },
        {
          id: 16, title: 'Автор студенческих работ по промышленному гражданскому строительству (удаленно)', img: require('~/assets/img/companyIcons/magistr.jpeg'), company: 'ГК Магистр', location: 'Казань', worktime: 'Удаленно', link: 'job-detail.html', salary: 'ЗП: до 50 000', educ: 'Высшее', vacancyTime: '01.02.2022', descr: 'Выполнение уникальных студенческих работ в соответствии с требованиями клиента (контрольные, лабораторные и курсовые работы, решение задач, выполнение упражнений и расчетов. Давайте знакомиться! Zaochnik - образовательный сервис с 20 летним опытом работы на рынке СНГ и Европы. Мы помогаем студентам.', category: 'Строительство'
        },
        {
          id: 17, title: 'Продавец консультант', img: require('~/assets/img/companyIcons/express.png'), company: 'ЭКСПРЕСС', location: 'Краснодар', worktime: 'Полная занятость', link: 'job-detail.html', salary: 'ЗП: до 40 000', educ: 'Высшее', vacancyTime: '04.02.2022', descr: 'Работать в торговом зале. Консультировать покупателей. Разбирать поставки. Работать в примерочных. Работать на кассе. Быть честным и открытым. Быть ответственным и целеустремленным. Быть активным и трудолюбивым.', category: 'Продажи'
        },
        {
          id: 18, title: 'SMM-менеджер/таргетолог/маркетолог', img: require('~/assets/img/companyIcons/anima.png'), company: 'Анима', location: 'Сочи', worktime: 'Частичная занятость', link: 'job-detail.html', salary: 'ЗП: до 50 000', educ: 'Высшее', vacancyTime: '05.02.2022', descr: 'Разработка и реализация SMM стратегии продвижения в Instagramm. Создание контента. Привлечение целевой аудитории, увеличение количества подписчиков. Проведение активностей (розыгрыши, опросы).Высшее образование. Опыт работы в маркетинге и рекламе (желательно в Бьюти-сфере). Креативность, творческий подход. Орфографическая и стилистическая грамотность.', category: 'Маркетинг'
        },
        {
          id: 19, title: 'Чат-менеджер в офис', img: require('~/assets/img/companyIcons/aliexpress.jpeg'), company: 'Алиэкспресс Россия', location: 'Нижний Новгород', worktime: 'Удаленно', link: 'job-detail.html', salary: 'ЗП: до 36 000', educ: 'Высшее', vacancyTime: '31.01.2022', descr: 'Работа в чатах, оказание онлайн поддержки продавцов AliExpress Россия. Консультирование по работе с платформой (это не тех поддержка). Опыт работы в контактных или call-центрах различных компаний. Готовность к постоянному развитию и активным действиям при исполнении трудовых обязанностей', category: 'Информационные технологии'
        },
        {
          id: 20, title: 'Офис-менеджер', img: require('~/assets/img/companyIcons/hilink.jpeg'), company: 'ХайЛинк', location: 'Иркутск', worktime: 'Full-Time', link: 'job-detail.html', salary: 'ЗП: 25 000 - 30 000', educ: 'Высшее', vacancyTime: '23.01.2022', descr: 'Встреча посетителей в офисе. Работа с входящей/исходящей корреспонденцией (регистрация, учёт, хранение, архивирование). Организация деловых встреч и переговоров руководства. Высшее юридическое образование (рассмотрим выпускников без опыта работы, студентов в т.ч.). Уверенный пользователь ПК, знание программ MS Office.', category: 'Другое'
        },

      ],
    }
  },
  mounted () {
    this.getVacancy()
  },
  // created () {
  //   this.getVacancies()
  // },
  methods: {
    onSubmit () {
      this.login()
    },
    onSearch () {
      console.log('Уже ищу!!!')
    },
    // async getVacancies () {
    //   try {
    //     const response = await this.$axios.get('/api/v1/vacancies')
    //     this.vacancyList = response.data.data
    //     // eslint-disable-next-line no-console
    //     console.log(this.vacancyList)
    //   } catch (e) {
    //     this.$toast.error(e.response.data)
    //   }
    // },
    getVacancy () {
      this.vacancyId = this.$route.params.vacancy_id
      this.vacancy = this.testVacancyList[this.vacancyId-1]
    }
    //   try {
    //     const response = await this.$axios.get('/api/v1/shop/vacancy', { params: { package_id: this.productId } })
    //     this.vacancy = response.data.data

    //   } catch (e) {
    //     this.$toast.error(e.response.data)
    //   }
    // },
  }
}
</script>

<style lang="scss">
.main__wrapp {
  display: flex;
  max-width: 100%;
  flex-direction: column;
}
.page-header {
  display: flex;
  height: 700px;
  flex-direction: column;
  background: url('~/assets/img/bg-banner2.jpg') no-repeat top center;
  background-size: cover;
  align-items: center;
  justify-content: center;
}
.container {
  justify-content: center;
  max-width: 100%;
  margin-top: 100px;
  display: flex;
}
.header-detail {
  width: 80%;
  background-color: white;
  &__head {
    display: flex;
    padding-top: 10px;
    &_main {
      display: flex;
      justify-content: space-between;
      width: 75%;
      &-time {
        margin-right: 10px;
        display: flex;
        align-items: center;
      }
      &-descr {
        display: flex;
        padding: 10px;
      }
      &-params {
        display: flex;
        li {
          width: 30%;
        }
      }
    }
  }
}
.button-group {
  display: flex;
  padding: 20px;
  justify-content: space-between;
}
.logo {
  display: flex;
  padding: 0 10px;
  align-items: center;
  max-width: 300px;
  img {
    width: 240px;
  }
}
.vacancy-info {
  display: flex;
  justify-content: center;
  &__container {
    display: flex;
    flex-direction: column;
    padding: 50px;
    max-width: 90%;
  }
}

</style>
