import datetime, calendar,pdb

head_data = """

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {box-sizing:border-box;}
ul {list-style-type: none;}
body {
  font-family: Helvetica,sans-serif;
  background-color: #F0F3F5;
}

.month {
    padding: 20px 25px;
    width: 100%;
    background: #ccc;
}

.month ul {
    margin: 0;
    padding: 0;
}

.month ul li {
    color: #2D6891;
    font-size: 20px;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-weight: bold;
}

.weekdays {
    margin: 0;
    padding: 10px 0;
    background-color: #ddd;
}

.weekdays li {
    display: inline-block;
    width: 13.6%;
    color: #666;
    text-align: center;
}

.days {
    padding: 10px 0;
    background: #eee;
    margin: 0;
}

.days li {
    list-style-type: none;
    display: inline-block;
    width: 13.6%;
    text-align: center;
    margin-bottom: 5px;
    font-size:12px;
    color: #777;
    padding-top: 10px;
}

.days li .active {
    padding: 5px;
    background: #2D6891;
    color: white !important
}

/* Add media queries for smaller screens */
@media screen and (max-width:720px) {
    .weekdays li, .days li {width: 13.1%;}
}

@media screen and (max-width: 420px) {
    .weekdays li, .days li {width: 12.5%;}
    .days li .active {padding: 2px;}
}

@media screen and (max-width: 290px) {
    .weekdays li, .days li {width: 12.2%;}
}
button.accordion {
    background-color: #ddd;
    color: #2D6891;
    cursor: pointer;
    padding: 18px;
    width: 100%;
    border: none;
    text-align: left;
    outline: none;
    font-size: 16px;
    transition: 0.4s;
    font-weight: bold;
}

button.accordion.active, button.accordion:hover {
    background-color: #ddd;
}

button.accordion:after {
    content: '+';
    font-size: 16px;
    color: #2D6891;
    float: right;
    margin-left: 5px;
}

button.accordion.active:after {
    content: "-";
    color: #2D6891;
    font-size: 16px;
}

div.panel {
    padding: 0 18px;
    background-color: white;
    max-height: 0;
    overflow: hidden;
    transition: 0.6s ease-in-out;
    opacity: 0;
}

div.panel.show {
    opacity: 1;
    max-height: 10000px;
}

a, a:hover, a:active, a:visited {
  color: #70A0BF;
}

.sectionWrapper {
  margin-bottom: 20px;
  border: 1px solid #CFDADE;
}

.sectionHeader {
  text-align: center;
  color: #fff;
  font-size: 26px;
  margin: 0;
  padding: 20px;
  background-color: #2D6891;
  font-weight: normal;
}

.postWrapper {
  margin-bottom: 30px;
}
.postAuthor {
  font-weight: bold;
}

.postTime {
  font-style: italic;
}
</style>
</head>
"""
today = datetime.date.today()
monday = today - datetime.timedelta(days=today.weekday())
daterange = list(range(monday.day,monday.day + 7))
dateposition = daterange.index(today.day)
daterange[dateposition] = "<span class='active'>{}</span>".format(today.day)
calendar = """
<body>
<div class="sectionWrapper">

<h1 class="sectionHeader">Calendar</h1>

<div class="month">
  <ul>
    <li style="text-align:center">
      {}<br>
      <span style="font-size:18px">2016</span>
    </li>
  </ul>
</div>

<ul class="weekdays">
  <li>Mo</li>
  <li>Tu</li>
  <li>We</li>
  <li>Th</li>
  <li>Fr</li>
  <li>Sa</li>
  <li>Su</li>
</ul>

<ul class="days">
  <li>{}</li>
  <li>{}</li>
  <li>{}</li>
  <li>{}</li>
  <li>{}</li>
  <li>{}</li>
  <li>{}</li>
</ul>
</div>
<div class="sectionWrapper">

<h1 class="sectionHeader">News Posts</h1>
""".format(calendar.month_name[today.month],daterange[0],daterange[1],daterange[2],daterange[3],daterange[4],daterange[5],daterange[6])

ending_html = """
</div>
</div>
<script>
var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("show");
  }
}
</script>
</body>

</html>
"""
