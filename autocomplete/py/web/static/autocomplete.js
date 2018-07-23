$(function() {
    $("#query").on("input", function() {
        var query = $("#query").val();
        $.ajax({
            url: "/search?q=" + query
        }).done(function(response) {
            $("#results").html(
                "<div>Results for " + response.query + "</div>" +
                    "<div>" + response.results.join("<br/>") + "</div>");
        });
    });
});
