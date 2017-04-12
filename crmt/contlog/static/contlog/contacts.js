$(function () {

  $(".js-create-cnt").click(function () {
    $.ajax({
      url: '/create_contact/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-cnt").modal("show");
      },
      success: function (data) {
        $("#modal-cnt .modal-content").html(data.html_form);
      }
    });
  });

});