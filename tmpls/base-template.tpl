<!DOCTYPE html>
<html>
<head>
  <title>{% if page_title %}{{ page_title }}{% else %}SodTheQuest{% endif %}</title>
  <meta content="Manage Your RPG Campaign" name="description">
  <meta content="width=device-width, initial-scale=1.0, maximum-scale=2" name="viewport">
  <link href="static/css/style.css" rel="stylesheet" type="text/css">
  <script src="static/js/vendor/custom.modernizr.js"></script>
</head>
<body>
  <nav class="top-bar">
    <ul class="title-area">
      <li class="name">
        <h1 class="header-logo">
          <a href="/" style="height:45px;">
            <span>STQ<span class="hide-for-small"> RPG Manager</span></span>
          </a>
        </h1>
      </li>
    </ul>
  </nav>
  {% block searchbar %}
  <div class="shaded top-bar-attached search-box">
    <div class="row">
      <div class="large-8 columns">
        <form action="/characters" class="custom basic-search">
          <div class="stretcher">
            <input class="no-bottom-margin" id="main-search" name="character" placeholder="Search by character name" type="text" {% if query %}value="{{ query }}"{% endif %}/>
            <button class="button radius no-bottom-margin">
              <i class="icon-search">Search!</i>
            </button>
          </div>
        </form>
      </div>
      <div class="large-8 columns">
        <span>{% if query %}You just searched for: {{ query }}{% else %}Try searching for a character!{% endif %}</span>
      </div>
    </div>
    <div class="row">
      <div class="large-8 columns">
        <a href="/create_character" class="button" id="form-button">Make a New Character</a>
      </div>
    </div>
  </div>
  {% endblock %}
  {% block content %}
  {% endblock %}
  <script src="static/js/jquery.js"></script>
  <script src="static/js/foundation.min.js"></script>
  <script src="static/js/application.js" type="text/javascript"></script>
  <script>
  window.onload = function() {
      var search_box = document.getElementById('main-search');
      search_box.focus();
      // The following line resets the search_box value to itself to move the cursor to the end 
      // of the query text, the actual value is set in the templating layer before page load.
      search_box.value = search_box.value;
    }
  </script>
  {% block scripts %}
  {% endblock %}
</body>
</html>

