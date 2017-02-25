(function () {'use strict';}()); // don't touch this line


var recent5notesAPI = '/api/5recentnotes/';
var recent5notebooksAPI = '/api/5recentnotebooks/';


var menuItem = function (title,id) {
  return '<li role="presentation"><a role="menuitem" tabindex="-1" href="/wowCS/'+id+'/">'+title+'</a></li>';
};

var getRecentNotes = function(){
  $.getJSON(recent5notesAPI, {}).done(
    function (data) {
      //console.log(data);
      for (i = 0; i < data.length; i++)
      {$('.recent-notes').append(menuItem(data[i].note_title,'note/'+data[i].id));}
    }
);};

var getRecentNotebooks = function(){
  $.getJSON(recent5notebooksAPI, {}).done(
    function (data) {
      console.log(data);
      for (i = 0; i < data.length; i++)
      {$('.recent-notebooks').append(menuItem(data[i].notebook_title,'notebook/'+data[i].notebook_title));}
    }
);};

$(document).ready(
  function() {
    //console.log('ready!');
    getRecentNotes();
    getRecentNotebooks();
  }
);
