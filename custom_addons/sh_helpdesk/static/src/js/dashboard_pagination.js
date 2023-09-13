odoo.define('sh_helpdesk.pagination', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var _t = core._t;

    // Get the current page number
    var currentPage = 1;

    // Define the number of records to display per page
    var recordsPerPage = 1;

    // Function to fetch records for a specific page
    function fetchRecords(page) {
        ajax.jsonRpc('/sh_helpdesk/get_records', 'call', { page: page, per_page: recordsPerPage })
            .then(function (data) {
                // Update the table with the new records
                updateTable(data.records);

                // Update the pagination controls
                updatePagination(data.total_records, page);
            });
    }

    // Function to update the table with fetched records
    function updateTable(records) {
        var $tableBody = $('.o_list_view tbody');
        $tableBody.empty();

        records.forEach(function (record) {
            var $row = $('<tr>');
            $row.append('<td>' + record.ticket_no + '</td>');
            $row.append('<td>' + record.partner_name + '</td>');
            $row.append('<td>' + record.partner_mobile + '</td>');
            $row.append('<td>' + record.create_date + '</td>');
            $row.append('<td>' + record.write_date + '</td>');
            $row.append('<td>' + record.user_id + '</td>');
            // Add other columns as needed
            $tableBody.append($row);
        });
    }

    // Function to update pagination controls
    function updatePagination(totalRecords, currentPage) {
        var totalPages = Math.ceil(totalRecords / recordsPerPage);
        var $pagerValue = $('.o_pager_value');
        var $pagerPrevious = $('.o_pager_previous');
        var $pagerNext = $('.o_pager_next');

        $pagerValue.text(currentPage + '/' + totalPages);

        if (currentPage === 1) {
            $pagerPrevious.addClass('disabled');
        } else {
            $pagerPrevious.removeClass('disabled');
        }

        if (currentPage === totalPages) {
            $pagerNext.addClass('disabled');
        } else {
            $pagerNext.removeClass('disabled');
        }
    }

    // Function to handle the "Previous" button click
    function prevPage() {
        if (currentPage > 1) {
            currentPage--;
            fetchRecords(currentPage);
        }
    }

    // Function to handle the "Next" button click
    function nextPage() {
        var totalPages = Math.ceil(totalRecords / recordsPerPage);
        if (currentPage < totalPages) {
            currentPage++;
            fetchRecords(currentPage);
        }
    }

    // Bind click events to pagination controls
    $('.o_pager_previous').on('click', prevPage);
    $('.o_pager_next').on('click', nextPage);

    // Initial fetch of records for the first page
    fetchRecords(currentPage);
});
