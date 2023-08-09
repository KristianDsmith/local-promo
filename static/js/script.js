$(document).ready(function () {
    $(".article-card").on("click", function () {
        var articleId = $(this).find(".article-details").attr("id").split("-")[2];
        var articleTitle = $(this).find(".overlay .card-title").text();
        var articleContent = $(this).find(".article-details p").text();

        $("#articleModalLabel").text(articleTitle);
        $("#articleModalBody").html("<p>" + articleContent + "</p>");

        $("#articleModal").modal("show");
    });
});


