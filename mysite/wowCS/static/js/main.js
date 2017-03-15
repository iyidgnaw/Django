(function () {'use strict';}()); // don't touch this line


var recent10notesAPI = '/api/10recentnotes/';
var recent10notebooksAPI = '/api/10recentnotebooks/';
var getcatagoryAPI = '/api/usercatagory/';
var getcatalistAPI = '/api/notesin/';

var menuItem = function (title,id) {
  return '<li role="presentation"><a role="menuitem" tabindex="-1" href="/wowCS/'+id+'/">'+title+'</a></li>';
};

var cataItem = function(title) {
    return '<li class=""><a class="dropdown-toggle side-cata" data-toggle="dropdown" href=""> <span class="glyphicon" aria-hidden="true"></span>'+title+'</a><ul class="dropdown-menu" role="menu" aria-labelledby="menu4">'+'</ul></li>';

  // var html = '<li class=""><a class="dropdown-toggle side-cata" data-toggle="dropdown" href=""> <span class="glyphicon" aria-hidden="true"></span>'+title+'</a><ul class="dropdown-menu" role="menu" aria-labelledby="menu4">'
  //   data = $.getJSON(getcatalistAPI+title+'/',{});
  //   for (i=0;i<data.length;i++){
  //       html+=menuItem(data[i].note_title,'note/'+data[i].id)}
  //
  //
  //   return html+'</ul></li>';
    // return html+'</ul></li>'
};

// var cataList = function(title,html){
//     $.getJSON(getcatalistAPI+title+'/',{}).done(
//        function(data,html){
//            console.log(data);
//            for (i = 0;i<data.length;i++)
//            {html+=menuItem(data[i].note_title,'note/'+data[i].id)}
//         return html;
//        }
//     );
// };

var getRecentNotes = function(){
  $.getJSON(recent10notesAPI, {}).done(
    function (data) {
      //console.log(data);
      for (i = 0; i < data.length; i++)
      {$('.recent-notes').append(menuItem(data[i].note_title,'note/'+data[i].id));}
    }
);};

var getRecentNotebooks = function(){
  $.getJSON(recent10notebooksAPI, {}).done(
    function (data) {
      // console.log(data);
      for (i = 0; i < data.length; i++)
      {$('.recent-notebooks').append(menuItem(data[i].notebook_title,'notebook/'+data[i].notebook_title));}
    }
);};

var getCatagory = function(){
    $.getJSON(getcatagoryAPI,{}).done(
        function(data){
            for (i=0;i<data.length;i++)
            {$('.notebooklist').append(cataItem(data[i].notebook_title));}
        }
);};


$('#confirm-delete').click(function(e){
  e.stopPropagation();
  $.getJSON('/delete/note/'+e.target.getAttribute('noteid'),{});
  location.reload();
});

$('#edit-note').click(function(e){
  e.stopPropagation();
  console.log($(this).attr('href'));
  window.location.replace($(this).attr('href'));
});
/*
$('#modal-from-dom').on('show', function() {
    var noteID = $(this).data('noteID');
    var removeBtn = $(this).find('.danger');

    removeBtn.click(function(){
      $.getJSON('/delete/note/'+noteID,{});
      location.reload();
    });

    //$('#debug-url').html('Delete URL: <strong>' + removeBtn.attr('href') + '</strong>');
});

$('.confirm-delete').on('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    var noteID = e.target.getAttribute('noteid');
    console.log(noteID);
    $('#modal-from-dom').data('noteID', noteID).modal('show');
});
*/
$('#confirm-delete').on('click', '.btn-ok', function(e) {
    e.stopPropagation();
    var $modalDiv = $(e.delegateTarget);
    var id = $(this).data('recordId');
    $.getJSON('/delete/note/'+id,{});
    location.reload();
    $modalDiv.addClass('loading');
    setTimeout(function() {
        $modalDiv.modal('hide').removeClass('loading');
    }, 1000);
});
$('#confirm-delete').on('click', function(e) {

      e.stopPropagation();
    var data = $(e.relatedTarget).data();
    $('.title', this).text(data.recordTitle);
    $('.btn-ok', this).data('recordId', data.recordId);
});

$('.btn--default').click(function(e){
  if ($(this).hasClass('btn--favorite')){ return; }
  $(this).removeClass('btn--default').addClass('btn--favorite');
  var favoriteCountE = $(this).children(":first");
  var favoriteCount = parseInt(favoriteCountE.text());
  console.log($(this));
  favoriteCountE[0].innerText = (favoriteCount+1);
  var noteID = $(this).attr('noteid');
  console.log(noteID);
  $.getJSON('/favorite/'+noteID,{});
});

function hideBDPageHeader(){
  var user = $('#menu3')[0];
  console.log(user.innerText);
  if (! user.innerText.includes('Sign in')){
    document.getElementById('bd-pageheader').style.display = 'none';
  }
}

/*
$('#confirm-delete').on('show.bs.modal', function(e) {
  e.stopPropagation();
  $(this).find('.btn-ok').attr('href', $(e.relatedTarget).data('href'));

  $('.debug-url').html('Delete URL: <strong>' + $(this).find('.btn-ok').attr('href') + '</strong>');
});
*/
$(document).ready(
  function() {
    hideBDPageHeader();
    console.log('document ready! enjoy.');
    getRecentNotes();
    getRecentNotebooks();
    getCatagory();
  }
);
