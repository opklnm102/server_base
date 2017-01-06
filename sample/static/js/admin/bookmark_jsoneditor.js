(function ($) {
    $(document).ready(function () {
        var $data_input = $("#id_data");
        var $jsoneditor = $("<div id='jsoneditor' style='width:100%;height:400px;margin-bottom:20px;'></div>");
        $data_input.hide().after($jsoneditor);
        var container = document.getElementById("jsoneditor");
        var options = {};
        var editor = new JSONEditor(container, options);
        editor.set(JSON.parse($data_input.val()));
        $data_input.parents('form').submit(function (event) {
            try {
                $data_input.val(JSON.stringify(editor.get()));
            } catch (error) {
                alert('json 양식이 잘못되었습니다.');
                event.preventDefault();
            }
        });
    });
})(django.jQuery);
