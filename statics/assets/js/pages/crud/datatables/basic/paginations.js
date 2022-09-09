/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/*!******************************************************************!*\
  !*** ../demo1/src/js/pages/crud/datatables/basic/paginations.js ***!
  \******************************************************************/

var KTDatatablesBasicPaginations = function() {

	var initTable1 = function() {
		var table = $('#kt_datatable');

		// begin first table
		table.DataTable({
			responsive: true,
			pagingType: 'full_numbers',
			language: {
            	url: "//cdn.datatables.net/plug-ins/1.10.16/i18n/Spanish.json"
        	},
		});
	};

	return {

		//main function to initiate the module
		init: function() {
			initTable1();
		},

	};

}();

jQuery(document).ready(function() {
	KTDatatablesBasicPaginations.init();
});

/******/ })()
;
//# sourceMappingURL=paginations.js.map