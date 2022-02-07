<template>
  <div class="main__wrapp">
    <!-- Page header -->
    <header class="header">
      <div class="head__container">
        <h1 class="text-center">Найти вакансии</h1>
        <p class="lead text-center">Воспользуйтесь полями ниже для поиска подходящей работы</p>
      </div>

      <div class="filter__container">
        <form action="#">

          <div class="filter__container_header">
            <div class="form-group col-xs-12 col-sm-4">
              <input type="text" class="form-control"
                placeholder="Ключевые слова: название должности, требования к навыкам, название компании">
            </div>

            <div class="form-group col-xs-12 col-sm-4">
              <input type="text" class="form-control" placeholder="Местоположение: город, область или почтовый индекс">
            </div>

            <div class="form-group col-xs-12 col-sm-4">
              <select class="form-control selectpicker" multiple>
                <option selected>Все категории</option>
                <option>Разработка</option>
                <option>Дизайн</option>
                <option>Работа с клиентами</option>
                <option>Финансы</option>
                <option>Здравоохранение</option>
                <option>Продажи</option>
                <option>Строительство</option>
                <option>Маркетинг</option>
                <option>Информационные технологии</option>
                <option>Другое</option>
              </select>
            </div>
          </div>
          <div class="filter__container_footer">

            <div class="form-group col-xs-12 col-sm-4">
              <h6>Режим работы</h6>
              <div class="checkall-group">
                <div class="checkbox">
                  <input type="checkbox" id="contract1" name="contract" checked>
                  <label for="contract1">Любой</label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="contract2" name="contract">
                  <label for="contract2">Полная занятость <small>(354)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="contract3" name="contract">
                  <label for="contract3">Частичная занятость <small>(284)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="contract4" name="contract">
                  <label for="contract4">Стажировка <small>(169)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="contract5" name="contract">
                  <label for="contract5">Фриланс <small>(480)</small></label>
                </div>
              </div>
            </div>


            <div class="form-group col-xs-12 col-sm-4">
              <h6>Оплата в час</h6>
              <div class="checkall-group">
                <div class="checkbox">
                  <input type="checkbox" id="rate1" name="rate" checked>
                  <label for="rate1">Любая</label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="rate2" name="rate">
                  <label for="rate2">$0 - $50 <small>(364)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="rate3" name="rate">
                  <label for="rate3">$50 - $100 <small>(684)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="rate4" name="rate">
                  <label for="rate4">$100 - $200 <small>(195)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="rate5" name="rate">
                  <label for="rate5">$200+ <small>(39)</small></label>
                </div>
              </div>
            </div>


            <div class="form-group col-xs-12 col-sm-4">
              <h6>Ученая степень</h6>
              <div class="checkall-group">
                <div class="checkbox">
                  <input type="checkbox" id="degree1" name="degree" checked>
                  <label for="degree1">Все</label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="degree2" name="degree">
                  <label for="degree2">Ассистент <small>(216)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="degree3" name="degree">
                  <label for="degree3">Бакалавр <small>(569)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="degree4" name="degree">
                  <label for="degree4">Магистр <small>(439)</small></label>
                </div>

                <div class="checkbox">
                  <input type="checkbox" id="degree5" name="degree">
                  <label for="degree5">Докторская степень <small>(84)</small></label>
                </div>
              </div>
            </div>

          </div>

          <div class="button-group">
            <div class="action-buttons">
              <button class="btn btn-primary">Применить фильтр</button>
            </div>
          </div>

        </form>

      </div>

    </header>
    <!-- END Page header -->


    <!-- Main container -->
    <main class="vacancy">
      <section class="vacancy__list">
        <div class="vacancy__container">
          <div class="vacancy__container_head">
            <div class="vacancy__container_head-title">
              <br>
              <h5>Мы нашли <strong>357</strong> совпадений, вы смотрите от <i>10</i> до <i>20</i></h5>
            </div>
          </div>
          <!-- Job item -->

          <div class="vacancy-item" v-for="(item, id) in testVacancyList" :key="id">
            <nuxt-link :to="`/vacancies/${item.id}`" style="textDecoration:none">
              <div class="vacancy-item__block">
                <div class="vacancy-item__img"><img class="company-logo" :src="item.img" alt=""></div>
                <div class="vacancy-item__info">
                  <div class="vacancy-item__info_main">
                    <div class="vacancy-item__info_main-name">{{ item.title }}</div>
                    <div class="vacancy-item__info_main-time">{{ item.vacancyTime}}</div>
                  </div>
                  <div class="vacancy-item__info_add">
                    <div class="vacancy-item__info_add-name">{{ item.company }}</div>
                    <div class="vacancy-item__info_add-time">{{ item.worktime}}</div>
                  </div>
                  <div class="vacancy-item__info_descr"><p class="vacancy-item__info_description">{{ item.descr }}</p></div>
                  <div class="vacancy-item__info_footer">
                    <div class="vacancy-item__info_footer-city">{{ item.location }}</div>
                    <div class="vacancy-item__info_footer-salary">{{ item.salary }}</div>
                    <div class="vacancy-item__info_footer-education">{{ item.educ }}</div>
                  </div>
                </div>
              </div>
            </nuxt-link>
          </div>
          <!-- END Job item first-->

          <!-- Page navigation -->
          <nav class="text-center">
            <ul class="pagination">
              <li>
                <a href="#" aria-label="Previous">
                  <i class="ti-angle-left"></i>
                </a>
              </li>
              <li><a href="#">1</a></li>
              <li class="active"><a href="#">2</a></li>
              <li><a href="#">3</a></li>
              <li><a href="#">4</a></li>
              <li>
                <a href="#" aria-label="Next">
                  <i class="ti-angle-right"></i>
                </a>
              </li>
            </ul>
          </nav>
          <!-- END Page navigation -->
        </div>
      </section>
    </main>
    <!-- END Main container -->
  </div>
</template>

<script>
export default {
  data () {
    return {
      loading: false,
      vacancyList: [],
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
  methods: {
    onSubmit () {
      this.login()
    },
    onSearch () {
      console.log('Уже ищу!!!')
    }
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
  }
}
</script>

<style lang="scss">
.main__wrapp {
  display: flex;
  max-width: 100%;
  flex-direction: column;
}
.header {
  display: flex;
  height: 700px;
  flex-direction: column;
  background: url('~/assets/img/bg-banner2.jpg') no-repeat bottom center;
  background-size: cover;
  align-items: center;
}
.head__container {
  max-width: 1800px;
  margin-top: 150px;
}
.filter__container {
  display: flex;
  flex-direction: column;
  width: 90%;
  &_header {
    display: flex;
  }
  &_footer {
    display: flex;
  }
}
.vacancy {
  display: flex;
  flex-direction: column;
  max-width: 1800px;
  align-self: center;
  &__list {
    display: flex;
    flex-direction: column;
  }
  &__container {
    &_head {
      display: flex;
      justify-content: center;
      &-title {
        display: flex;
        justify-content: center;
      }
    }
  }
}
.vacancy-item {
  &__block {
    display: flex;
    cursor: pointer;
    width: 100%;
    justify-content: space-around;
    margin: 30px 0;
    transition-property: border;
    transition-duration: .2s;
    // &:hover {
    //   border: 1px solid #29aafe;
    // }
  }

  &__img {
    display: flex;
    padding: 0 30px;
    align-items: center;
    max-width: 300px;
    img {
      width: 240px;
    }
  }
  &__info {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    width: 100%;
    padding: 0 30px;
    color: dimgray;
    &_main {
      display: flex;
      justify-content: space-between;
      &-name {
        font-size: 36px;
        line-height: 40px;
        color: #55595c;
        font-family: Arial, sans-serif;
        font-weight: 400;
      }
      &-city {
        color: #96a2b2;
        line-height: 35px;
        font-size: 30px;
      }
    }
    &_add {
      display: flex;
      justify-content: space-between;
      &-company {
        font-size: 30px;
        color: #96a2b2;
      }
      &-worktime {
        text-transform: uppercase;
        letter-spacing: 1px;
        font-size: 30px;
        color: white;
        font-weight: 400;
        border-radius: 0;
        padding: 4px 6px;
        margin-top: 6px;
        margin-left: 16px;
        opacity: .85;
        background-color: #5cb85c;
      }
    }
    &_footer {
      display: flex;
      justify-content: space-between;
      max-width: 50%;
    }
  }
}

</style>
