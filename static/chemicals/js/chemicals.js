function messagesTimeout(wait){
    setTimeout(function() {
        $('#messages').children().slideUp();
    }, wait);
}

function removeForm() {
    $(this).closest('tr').addClass('hidden');
    $(this).parent().find('.hidden').find('input').prop('checked', true);
}

function addForm() {
    var selector = $(this).closest('form').find(".form-template").last(); 
    var id = $(this).attr('id').slice(12);
    var type = selector.data('form-type')
    var total = $('#id_' + type + '-TOTAL_FORMS').val();
    template = selector.clone(true);
    template.removeClass('form-template');
    template.html(function(index, content) {
        return content.replace(/__prefix__/g, total);
    });
    template.find('.location').find("[value='" + id + "']").prop('selected', true);
    template.find('.actions').find('button').on('click', removeForm);
    selector.before(template);
    total++;
    $('#id_' + type + '-TOTAL_FORMS').val(total);
}


$(document).ready(function () {
    // Let the messages disappear after a certain time
    messagesTimeout(10000)

    // Prevent Users from changing the location in the form
    $('.location select').prop("disabled", true);
    $('#stockform').on("submit", function() {
        // Only the active forms should be enabled
        $('.location select').prop("disabled", false);
    });

    // Highlight or remove rows that are selected for removal
    $('.actions').find('input:checked').closest('tr').toggleClass('danger');
    $('.actions').find('input[type="checkbox"]').on('click', function(){
        $(this).closest('tr').toggleClass('danger')
    });
    $('.actions').find('button').on('click', removeForm)
    $('.actions').find('.hidden').find('input:checked').closest('tr').addClass('hidden');

    // Provide an opportunity to add further forms to the formset
    $('#location_list').find('a').on("click", addForm);
});
