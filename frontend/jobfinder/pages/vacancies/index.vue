<template>
  <div class="main__wrapp">
    <!-- Page header -->
    <header class="page-header bg-img">
      <div class="head__container">
        <h1 class="text-center">Найти вакансии</h1>
        <p class="lead text-center">Воспользуйтесь полями ниже для поиска подходящей работы</p>
      </div>

      <div class="container">
        <form action="#">

          <div class="row">
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
    <main>
      <section class="no-padding-top bg-alt">
        <div class="container">
          <div class="row">

            <div class="col-xs-12">
              <br>
              <h5>Мы нашли <strong>357</strong> совпадений, вы смотрите от <i>10</i> до <i>20</i></h5>
            </div>

            <!-- Job item -->
            <div class="col-xs-12">
              <a class="item-block" href="job-detail.html">
                <header>
                  <img src="assets/img/logo-google.jpg" alt="">
                  <div class="hgroup">
                    <h4>Старший фронт-энд девелопер</h4>
                    <h5>Google <span class="label label-success">Full-time</span></h5>
                  </div>
                  <time datetime="2016-03-10 20:00">34 min ago</time>
                </header>

                <div class="item-body">
                  <p>A rapidly growing, well established marketing firm is looking for an experienced web developer for a
                    full-time position. In this role, you will develop websites, apps, emails and other forms of digital
                    electronic media, all while maintaining brand standards across design projects and other marketing
                    communication materials.</p>
                </div>

                <footer>
                  <ul class="details cols-3">
                    <li>
                      <i class="fa fa-map-marker"></i>
                      <span>Menlo Park, CA</span>
                    </li>

                    <li>
                      <i class="fa fa-money"></i>
                      <span>$90,000 - $110,000 / year</span>
                    </li>

                    <li>
                      <i class="fa fa-certificate"></i>
                      <span>Master or Bachelor</span>
                    </li>
                  </ul>
                </footer>
              </a>
            </div>
            <!-- END Job item -->


            <!-- Job item -->
            <div class="col-xs-12">
              <a class="item-block" href="job-detail.html">
                <header>
                  <img src="assets/img/logo-linkedin.png" alt="">
                  <div class="hgroup">
                    <h4>Software Engineer (Entry or Senior)</h4>
                    <h5>Linkedin <span class="label label-warning">Part-time</span></h5>
                  </div>
                  <time datetime="2016-03-10 20:00">8 hours ago</time>
                </header>

                <div class="item-body">
                  <p>The Special Programs Department II is seeking to hire a Computer Scientist to augment our software
                    development team. Members of the software development team are expected to follow established software
                    engineering principles to methodically deliver mission application software.</p>
                </div>

                <footer>
                  <ul class="details cols-3">
                    <li>
                      <i class="fa fa-map-marker"></i>
                      <span>Livermore, CA</span>
                    </li>

                    <li>
                      <i class="fa fa-money"></i>
                      <span>$60,000 - $75,000 / year</span>
                    </li>

                    <li>
                      <i class="fa fa-certificate"></i>
                      <span>Master or Bachelor</span>
                    </li>
                  </ul>
                </footer>
              </a>
            </div>
            <!-- END Job item -->


            <!-- Job item -->
            <div class="col-xs-12">
              <a class="item-block" href="job-detail.html">
                <header>
                  <img src="assets/img/logo-envato.png" alt="">
                  <div class="hgroup">
                    <h4>Full Stack Web Developer</h4>
                    <h5>Envato <span class="label label-info">Freelance</span></h5>
                  </div>
                  <time datetime="2016-03-10 20:00">2 days ago</time>
                </header>

                <div class="item-body">
                  <p>We're seeing a driven, curious, passionate full-stack web developer to help change how people learn
                    creative skills and effortlessly create the images they imagine. You’ll be part of a new rapid
                    prototyping and development team helping to apply lean startup development methodologies and modern
                    web technologies to shape the future of Creative Cloud.</p>
                </div>

                <footer>
                  <ul class="details cols-3">
                    <li>
                      <i class="fa fa-map-marker"></i>
                      <span>San Francisco, CA</span>
                    </li>

                    <li>
                      <i class="fa fa-money"></i>
                      <span>$105,000 / year</span>
                    </li>

                    <li>
                      <i class="fa fa-certificate"></i>
                      <span>Master</span>
                    </li>
                  </ul>
                </footer>
              </a>
            </div>
            <!-- END Job item -->


            <!-- Job item -->
            <div class="col-xs-12">
              <a class="item-block" href="job-detail.html">
                <header>
                  <img src="assets/img/logo-facebook.png" alt="">
                  <div class="hgroup">
                    <h4>Web Applications Developer</h4>
                    <h5>Facebook <span class="label label-danger">Internship</span></h5>
                  </div>
                  <time datetime="2016-03-10 20:00">Feb 26, 2016</time>
                </header>

                <div class="item-body">
                  <p>Client needs a back-end Java developer who has worked mainly on Java, J2EE, Spring, Web Services, and
                    other Java related technologies.</p>
                </div>

                <footer>
                  <ul class="details cols-3">
                    <li>
                      <i class="fa fa-map-marker"></i>
                      <span>Lexington, MA</span>
                    </li>

                    <li>
                      <i class="fa fa-money"></i>
                      <span>$130,000 - $150,000 / year</span>
                    </li>

                    <li>
                      <i class="fa fa-certificate"></i>
                      <span>Ph.D. or Master</span>
                    </li>
                  </ul>
                </footer>
              </a>
            </div>
            <!-- END Job item -->


            <!-- Job item -->
            <div class="col-xs-12">
              <a class="item-block" href="job-detail.html">
                <header>
                  <img src="assets/img/logo-microsoft.jpg" alt="">
                  <div class="hgroup">
                    <h4>Sr. SQL Server Developer</h4>
                    <h5>Microsoft <span class="label label-success">Remote</span></h5>
                  </div>
                  <time datetime="2016-03-10 20:00">Feb 16, 2016</time>
                </header>

                <div class="item-body">
                  <p>Understand and model complex business requirements into database schemas and work with existing
                    databases in SQL and NOSQL data stores. Develop high performance stored procedures, triggers and other
                    database level code to provide data services to other teams.</p>
                </div>

                <footer>
                  <ul class="details cols-3">
                    <li>
                      <i class="fa fa-map-marker"></i>
                      <span>Palo Alto, CA</span>
                    </li>

                    <li>
                      <i class="fa fa-money"></i>
                      <span>$125,000 - $140,000 / year</span>
                    </li>

                    <li>
                      <i class="fa fa-certificate"></i>
                      <span>Ph.D. or Master</span>
                    </li>
                  </ul>
                </footer>
              </a>
            </div>
            <!-- END Job item -->

          </div>


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
          id: 1, title: 'Помощник бухгалтера', img: require('~/assets/img/companyIcons/Marvel.jpg'), company: 'ГК Марвел', location: 'Санкт-Петербург', worktime: 'Full-Time', link: 'job-detail.html', salary: '50 050', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Официальное трудоустройство с первого рабочего дня в соответствии с ТК РФ. Уютный офис в шаговой доступности от метро Фрунзенская .Расширенный компенсационный пакет. Скидки на продукцию партнеров компании.', category: 'Финансы'
        },
        {
          id: 2, title: 'Python Developer', img: require('~/assets/img/companyIcons/KPMG.svg'), company: 'KPMG', location: 'Москва', worktime: 'Full-Time', link: 'job-detail.html', salary: 'от 80 000', educ: 'Высшее', vacancyTime: '01.02.2022', descr: 'Решать задачи проектирования и разработки компонентов продукта. Проводить код-ревью решений коллег, предоставлять аргументированную критику. Уточнять и документировать собственные решения. Самостоятельность, способность анализировать и предлагать новые, возможно неочевидные, решения. Способность донести свои предложения и решения до команды, объяснить их плюсы.', category: 'Разработка'
        },
        {
          id: 3, title: 'Дизайнер-верстальщик', img: require('~/assets/img/companyIcons/Zebra.svg'), company: 'Зебра-ПР', location: 'Москва', worktime: 'Full-Time', link: 'job-detail.html', salary: '70 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Верстка русско- и англоязычных макетов многополосных изданий на основе утвержденных дизайн-макетов. Разработка инфографики (графики, схемы, иконки и т.п.) Углубленные знания пакета Adobe (InDesign, Illustrator, Photoshop, Acrobat). Чувство композиции и прекрасного. Портфолио. Обязателен опыт работы с многополосными изданиями', category: 'Дизайн'
        },
        {
          id: 4, title: 'Менеджер по работе с клиентами', img: require('~/assets/img/companyIcons/Bankirro.jpg'), company: 'БАНКИРРО', location: 'Саранск', worktime: 'Удаленно', link: 'job-detail.html', salary: 'до 100 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Проводить первичную консультацию клиентов, и передавать их в отдел продаж для визита на консультацию в офис (только горячие клиенты, входящий...Если Вы уверены, что способны показывать твердые результаты в продажах, Вас не пугают вызовы и готовность ставить перед собой большие цели', category: 'Работа с клиентами'
        },
        {
          id: 5, title: 'Медицинская сестра', img: require('~/assets/img/companyIcons/gemotest.jpg'), company: 'Гемотест', location: 'Ангарск', worktime: 'Full-Time', link: 'job-detail.html', salary: 'от 45 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Взятие биоматериала (венозной и капиллярной крови, гинекологических и урологических мазков). Информирование пациентов об оказываемых услугах, их стоимости, сроках исполнения, правилах сбора биоматериала, подготовке к исследованиям и т.п. Оформление медицинской документации', category: 'Здравоохранение'
        },
        {
          id: 6, title: 'Производитель работ/начальник участка', img: require('~/assets/img/companyIcons/oilberg.jpg'), company: 'OILBERG', location: 'Москва', worktime: 'Full-Time', link: 'job-detail.html', salary: 'от 80 000', educ: 'Высшее', vacancyTime: '03.02.2022', descr: 'Организация общестроительных и электромонтажных работ на объекте. Технический надзор за выполнением работ, приемка работ, консультация. Организация доставки инструментов и оборудования на объект. Опыт работы прорабом или начальником участка от 3 лет. Чтение схем и чертежей. ', category: 'Строительство'
        },
        {
          id: 7, title: 'Менеджер по продажам', img: require('~/assets/img/companyIcons/5M.jpg'), company: '5M', location: 'Екатеринбург', worktime: 'Полная занятость', link: 'job-detail.html', salary: '48 000 - 72 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Продавать веб-сервисы по телефону. База предоставляется. Общаться с клиентами: руководителями, бухгалтерами, специалистами по безопасности. Вести весь цикл общения с клиентом. Грамотно и четко излагаешь свои мысли. Умеешь работать с информацией: запоминать, анализировать, понимать, как использовать в работе.', category: 'Продажи'
        },
        {
          id: 8, title: 'Маркетолог-аналитик', img: require('~/assets/img/companyIcons/arkont.jpg'), company: 'АРКОНТ', location: 'Волгоград', worktime: 'Частичная занятость', link: 'job-detail.html', salary: '50 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Маркетолог-аналитик работает на стыке двух профессий, применяя аналитический подход и инструментарий в маркетинговой сфере. Маркетолог-аналитик собирает и анализирует информацию. Личные качества: Аналитическое мышление. Знания в области интернет-маркетинга. Технические компетенции и знание инструментов анализа. Знания: Аналитическое мышление. Google Analytics.', category: 'Маркетинг'
        },
        {
          id: 9, title: 'Системный администратор', img: require('~/assets/img/companyIcons/rarus.png'), company: '1C-Рарус', location: 'Новосибирск', worktime: 'Full-Time', link: 'job-detail.html', salary: 'от 50 000', educ: 'Высшее', vacancyTime: '01.02.2022', descr: 'Принимать заявки от первой линии поддержки. Диагностировать проблему и предлагать ряд решений. Обеспечивать безопасность и сохранность данных клиента.Опыт работы от 1 года. Интерес к технологиям. Способность разбираться в проблеме и копать до ее сути, решать проблему.', category: 'Информационные технологии'
        },
        {
          id: 10, title: 'Помощник руководителя', img: require('~/assets/img/companyIcons/tapp.jpg'), company: 'Открытые технологии', location: 'Белгород', worktime: 'Full-Time', link: 'job-detail.html', salary: '40 000', educ: 'Высшее', vacancyTime: '26.01.2022', descr: 'Контроль исполнения всех распоряжений и приказов генерального директора ответственными лицами. Планирование, координация и ведение рабочего графика руководителя. Организация внешних и внутренних встреч. Высшее профессиональное образование. Опыт работы в должности "помощник руководителя" на производственном предприятии не менее 1 года. Обязательное знание программ Excel.', category: 'Другое'
        },
        {
          id: 11, title: 'Бухгалтер', img: require('~/assets/img/companyIcons/bsg.png'), company: 'BGS Group', location: 'Санкт-Петербург', worktime: 'Full-Time', link: 'job-detail.html', salary: 'от 70 000', educ: 'Высшее', vacancyTime: '04.02.2022', descr: 'Участие в ежемесячном закрытии периода, помощь в подготовке и сдаче бухгалтерской и налоговой отчетности. Выполнение поручений главного бухгалтера и руководства.Опыт работы с кадровым делопроизводствам. Знание бухгалтерского и налогового учета. Знание 1С: Предприятие 8.2. ЗУП 8.2', category: 'Финансы'
        },
        {
          id: 12, title: 'Программист-разработчик Python', img: require('~/assets/img/companyIcons/lightmans.png'), company: 'Lightmans', location: 'Москва', worktime: 'Полная занятость', link: 'job-detail.html', salary: 'до 100 000', educ: 'Высшее', vacancyTime: '02.02.2022', descr: 'Наша компания работает над развитием действующего портала по поиску работы и персонала. Обязанности: Бэкенд-разработка. Работа по ТЗ Заказчика.Опыт бэкенд-разработки на языке программирования python, владение фреймворками Django. Владение веб-серверами вроде Nginx, uwsgi/gunicorn. Владение SQL-базами', category: 'Разработка'
        },
        {
          id: 13, title: 'Дизайнер презентаций', img: require('~/assets/img/companyIcons/sbs.png'), company: 'SBS Consulting', location: 'Москва', worktime: 'Частичная занятость', link: 'job-detail.html', salary: 'от 30 000', educ: 'Высшее', vacancyTime: '25.01.2022', descr: 'Переработка сложных данных, большого количества контента и систематизация информации Работа с графиками, таблицами, дашбордами и схемами. Подбор качественных изображений, фото.Учитесь на 4 курсе бакалавриата или 1-2 курсе магистратуры профильного направления. Вам необходима практика или стажировка. Умееет соблюдать сроки. ', category: 'Дизайн'
        },
        {
          id: 14, title: 'Оператор (консультант) колл-центра в банк, удалённо (входящие обращения в чате / входящие звонки)', img: require('~/assets/img/companyIcons/startjob.png'), company: 'Start-Job', location: 'Севастополь', worktime: 'Частичная занятость', link: 'job-detail.html', salary: 'от 25 000', educ: 'Высшее', vacancyTime: '03.02.2022', descr: 'Консультировать клиентов банка по телефону и в чате (входящие обращения, без продаж и обзвонов). Проводить простые банковские операции.Вы сами выбираете удобное время работы и согласовываете с руководителем. Грамотная речь. Умение вежливо разговаривать с клиентами. Для работы нужен компьютер и гарнитура', category: 'Работа с клиентами'
        },
        {
          id: 15, title: 'Врач-хирург', img: require('~/assets/img/companyIcons/pavlovmed.png'), company: 'МЦ Павлов Мед', location: 'Ростов-на-Дону', worktime: 'Полная занятость', link: 'job-detail.html', salary: '30 000 - 100 000', educ: 'Высшее', vacancyTime: '28.01.2022', descr: 'Амбулаторный прием пациентов (первичный, повторный). Выполнение различных хирургических операций и манипуляций в рамках амбулаторной хирургии. Ведение необходимой правовой и медицинской...Образование - высшее профессиональное медицинское. Обязательно наличие действующего сертификата на осуществление медицинской деятельности по специальности. Опыт работы по специальности не менее 3-х лет', category: 'Здравоохранение'
        },
        {
          id: 16, title: 'Автор студенческих работ по промышленному гражданскому строительству (удаленно)', img: require('~/assets/img/companyIcons/magistr.jpg'), company: 'ГК Магистр', location: 'Казань', worktime: 'Удаленно', link: 'job-detail.html', salary: 'до 50 000', educ: 'Высшее', vacancyTime: '01.02.2022', descr: 'Выполнение уникальных студенческих работ в соответствии с требованиями клиента (контрольные, лабораторные и курсовые работы, решение задач, выполнение упражнений и расчетов. Давайте знакомиться! Zaochnik - образовательный сервис с 20 летним опытом работы на рынке СНГ и Европы. Мы помогаем студентам.', category: 'Строительство'
        },
        {
          id: 17, title: 'Продавец консультант', img: require('~/assets/img/companyIcons/express.png'), company: 'ЭКСПРЕСС', location: 'Краснодар', worktime: 'Полная занятость', link: 'job-detail.html', salary: 'до 40 000', educ: 'Высшее', vacancyTime: '04.02.2022', descr: 'Работать в торговом зале. Консультировать покупателей. Разбирать поставки. Работать в примерочных. Работать на кассе. Быть честным и открытым. Быть ответственным и целеустремленным. Быть активным и трудолюбивым.', category: 'Продажи'
        },
        {
          id: 18, title: 'SMM-менеджер/таргетолог/маркетолог', img: require('~/assets/img/companyIcons/anima.png'), company: 'Анима', location: 'Сочи', worktime: 'Частичная занятость', link: 'job-detail.html', salary: 'до 50 000', educ: 'Высшее', vacancyTime: '05.02.2022', descr: 'Разработка и реализация SMM стратегии продвижения в Instagramm. Создание контента. Привлечение целевой аудитории, увеличение количества подписчиков. Проведение активностей (розыгрыши, опросы).Высшее образование. Опыт работы в маркетинге и рекламе (желательно в Бьюти-сфере). Креативность, творческий подход. Орфографическая и стилистическая грамотность.', category: 'Маркетинг'
        },
        {
          id: 19, title: 'Чат-менеджер в офис', img: require('~/assets/img/companyIcons/aliexpress.jpg'), company: 'Алиэкспресс Россия', location: 'Нижний Новгород', worktime: 'Удаленно', link: 'job-detail.html', salary: 'до 36 000', educ: 'Высшее', vacancyTime: '31.01.2022', descr: 'Работа в чатах, оказание онлайн поддержки продавцов AliExpress Россия. Консультирование по работе с платформой (это не тех поддержка). Опыт работы в контактных или call-центрах различных компаний. Готовность к постоянному развитию и активным действиям при исполнении трудовых обязанностей', category: 'Информационные технологии'
        },
        {
          id: 20, title: 'Офис-менеджер', img: require('~/assets/img/companyIcons/hilink.jpg'), company: 'ХайЛинк', location: 'Иркутск', worktime: 'Full-Time', link: 'job-detail.html', salary: '25 000 - 30 000', educ: 'Высшее', vacancyTime: '23.01.2022', descr: 'Встреча посетителей в офисе. Работа с входящей/исходящей корреспонденцией (регистрация, учёт, хранение, архивирование). Организация деловых встреч и переговоров руководства. Высшее юридическое образование (рассмотрим выпускников без опыта работы, студентов в т.ч.). Уверенный пользователь ПК, знание программ MS Office.', category: 'Другое'
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
    },
    async getVacancy () {
      try {
        const response = await this.$axios.get('/api/v1/vacancy')
        this.vacancyList = response.data.data
        // eslint-disable-next-line no-console
        console.log(this.vacancyList)
      } catch (e) {
        this.$toast.error(e.response.data)
      }
    },
  }
}
</script>

<style lang="scss">
.main-container {
  display: flex;
  max-width: 100%;
}
.page-header {
  display: flex;
  height: 700px;
  flex-direction: column;
  background: url('~/assets/img/bg-banner2.jpg') no-repeat bottom center;
  background-size: cover;
}
.head__container {
  max-width: 1800px;
  margin-top: 150px;
}
// .site-header {
//   display: flex;
//   height: 700px;
// }
// .header-job-search {
//   display: flex;
//   justify-content: center;
// }
// .wsearch-btn {
//   height: 100%;
//   border: none;
// }
// .main__wrapp {
//   width: 100%;
// }
// .main-window__header {
//   font-size: 46px;
//   font-family: Arial,sans-serif;
//   margin: 16px 0;
//   line-height: 1.4;
//   color: white;
//   font-weight: 800;
// }
// .site-header mark {
//   color: #29aafe;;
//   background-color: transparent;
//   font-weight: 700;
// }
// .body-header {
//   padding-top: 80px;
//   display: flex;
//   flex-direction: column;
//   align-items: center;
//   &__new {
//     color: #84878a;
//     font-family: Arial,sans-serif;
//     font-size: 20px;
//     letter-spacing: 2px;
//     text-transform: uppercase;
//   }
//   &__head {
//     padding: 48px 0;
//     display: flex;
//     flex-direction: column;
//     align-items: center;
//     font-size: 46px;
//     font-family: Arial,sans-serif;
//     color: #55595c;
//     text-transform: capitalize;
//     margin: 16px 0;
//     line-height: 1.4;
//     font-weight: 800;
//     &::after {
//       content: "";
//       width: 60px;
//       height: 2px;
//       background-color: #29aafe;
//       margin-top: 50px;
//     }

//   }
// }
// body {
//   font-family: Arial,sans-serif;
//   font-size: 16px;
//   line-height: 28px;
//   color: #7e8890;
// }
// .body {
//   &__container {
//     display: flex;
//     flex-direction: column;
//     align-items: center;
//     &_vacancy {
//       display: flex;
//       flex-direction: column;
//       align-items: center;
//       width: 90%;

//     }
//   }
// }
// .vacancy-item {
//   display: flex;
//   cursor: pointer;
//   width: 100%;
//   justify-content: space-around;
//   margin: 30px 0;
//   transition-property: border;
//   transition-duration: .2s;
//   &:hover {
//     border: 1px solid #29aafe;
//   }
//   &__img {
//     display: flex;
//     padding: 0 30px;
//   }
//   &__info {
//     display: flex;
//     flex-direction: column;
//     justify-content: space-around;
//     width: 100%;
//     padding: 0 30px;
//     &_main {
//       display: flex;
//       justify-content: space-between;
//       &-name {
//         font-size: 36px;
//         line-height: 40px;
//         color: #55595c;
//         font-family: Arial, sans-serif;
//         font-weight: 400;
//       }
//       &-city {
//         color: #96a2b2;
//         line-height: 35px;
//         font-size: 30px;
//       }
//     }
//     &_add {
//       display: flex;
//       justify-content: space-between;
//       &-company {
//         font-size: 30px;
//         color: #96a2b2;
//       }
//       &-worktime {
//         text-transform: uppercase;
//         letter-spacing: 1px;
//         font-size: 30px;
//         color: white;
//         font-weight: 400;
//         border-radius: 0;
//         padding: 4px 6px;
//         margin-top: 6px;
//         margin-left: 16px;
//         opacity: .85;
//         background-color: #5cb85c;
//       }
//     }
//   }
// }
// .header-meta {
//   display: flex;
//   flex-direction: column;
//   justify-content: space-between;
//   height: 100%;
// }
// .nav-menu {
//   margin: 0;
//   padding: 0;
//   display: flex;
//   text-align: center;
//   list-style-type: none;
//   width: 65%;
//   justify-content: space-between;
//   align-items: center;
//   &__ul {
//     &_el {
//       display: none;
//     }
//   }
// }
// .btn-more {
//     width: 250px;
//     height: 50px;
//     color: #fff;
//     background-color: #5bb7ed;
//     border-color: #5bb7ed;
//     align-items: center;
//     display: flex;
//     justify-content: center;
// }
// .text__container {
//   display: flex;
//   justify-content: space-around;
//   &_left {
//     width: 40%;
//     &-title {
//       display: flex;
//       flex-direction: column;
//       &--text {
//         color: #84878a;
//         font-family: Arial,sans-serif;
//         font-size: 20px;
//         letter-spacing: 2px;
//         text-transform: uppercase;
//       }
//       &--head {
//         padding: 48px 0;
//         display: flex;
//         flex-direction: column;
//         align-items: center;
//         font-size: 46px;
//         font-family: Arial,sans-serif;
//         color: #55595c;
//         text-transform: capitalize;
//         margin: 16px 0;
//         line-height: 1.4;
//         font-weight: 800;
//       }
//     }
//   }
// }
// .category__container {
//   display: flex;
//   flex-direction: column;
//   align-items: center;
//   &_header {
//     display: flex;
//     flex-direction: column;
//     align-items: center;
//     &-title {
//       color: #84878a;
//       font-family: Arial,sans-serif;
//       font-size: 20px;
//       letter-spacing: 2px;
//       text-transform: uppercase;
//     }
//     &-head {
//       padding: 48px 0;
//       display: flex;
//       flex-direction: column;
//       align-items: center;
//       font-size: 46px;
//       font-family: Arial,sans-serif;
//       color: #55595c;
//       text-transform: capitalize;
//       margin: 16px 0;
//       line-height: 1.4;
//       font-weight: 800;
//       &::after {
//         content: "";
//         width: 60px;
//         height: 2px;
//         background-color: #29aafe;
//         margin-top: 50px;
//       }
//     }
//     &-note {
//       color: #84878a;
//       font-family: Arial,sans-serif;
//       font-size: 20px;
//       letter-spacing: 2px;
//       text-transform: uppercase;
//     }
//   }
// }
// .category__block {
//   display: flex;
//   flex-wrap: wrap;
//   width: 100%;
//   padding: 30px;
//   justify-content: space-around;
// }
// .category__item {
//   display: flex;
//   flex-direction: column;
//   width: 30%;
//   align-items: center;
//   padding: 30px;
//   transition-property: background-color;
//   transition-duration: .5s;
//   &_img {
//     width: 185px;
//   }
//   &_title {
//     display: flex;
//     font-size: 28px;
//     font-family: Arial,sans-serif;
//     color: #55595c;
//     text-transform: capitalize;
//     padding: 24px;
//     line-height: 1.4;
//     font-weight: 600;
//     transition-property: color;
//     transition-duration: .5s;
//   }
//   &_descr {
//     display: flex;
//     padding: 24px;
//     text-align: center;
//     color: #96a2b2;
//     font-size: 20px;
//     line-height: 30px;
//     transition-property: color;
//     transition-duration: .5s;
//   }
// }
// .category__item:hover {
//   background-color: #29aafe;
// }
// .category__item:hover .category__item_title{
//   color: white;
// }
// .category__item:hover .category__item_descr{
//   color: white;
// }

</style>
