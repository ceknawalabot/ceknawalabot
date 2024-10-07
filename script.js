    <script>
        $(document).ready(function() {
            $('button[id^='toggle-']').on('click', function() {
                var keyword = $(this).attr('id').replace('toggle-', '');
                var resultsDiv = $('#proxy-check-results-' + keyword);
                if (resultsDiv.css('display') === 'none') {
                    resultsDiv.show();
                    $(this).text('Hide Proxy Check Results');
                } else {
                    resultsDiv.hide();
                    $(this).text('Show Proxy Check Results');
                }
            });
        });
    </script>
