from __future__ import print_function

import sys
import cdp.cdp_parameter


class ACMEParameter(cdp.cdp_parameter.CDPParameter):
    def __init__(self):
        self.case_id = ''
        # The user must define these, so don't give any defaults.
        # self.reference_data_path = ''
        # self.test_data_path = ''

        self.sets = ['zonal_mean_xy', 'zonal_mean_2d', 'lat_lon', 'polar', 'cosp_histogram']
        self.dataset = ''
        self.run_type = 'model_vs_obs'
        self.variables = []
        self.seasons = ['ANN', 'DJF', 'MAM', 'JJA', 'SON']
        self.regions = ['global']
        self.regrid_tool = 'esmf'
        self.regrid_method = 'conservative'
        self.plevs = []

        # Plotting related.
        self.main_title = ''
        self.backend = 'mpl'
        self.save_netcdf = False
        self.output_format = ['png']
        self.output_format_subplot = []
        self.canvas_size_w = 1212
        self.canvas_size_h = 1628
        self.figsize = [8.5, 11.0]
        self.dpi = 150
        self.arrows = True
        self.logo = False

        self.contour_levels = []
        self.test_name = ''
        self.short_test_name = ''
        self.test_title = ''
        self.test_colormap = 'cet_rainbow.rgb'
        self.test_units = ''

        self.reference_name = ''
        self.reference_title = ''
        self.reference_colormap = 'cet_rainbow.rgb'
        self.reference_units = ''

        self.diff_name = ''
        self.diff_title = 'Model - Observation'
        self.diff_colormap = 'diverging_bwr.rgb'
        self.diff_levels = []
        self.diff_units = ''

        self.multiprocessing = False
        self.distributed = False
        self.num_workers = 4

        self.no_viewer = False
        self.debug = False

        self.granulate = ['variables', 'seasons', 'regions', 'plevs']
        self.selectors = ['sets', 'seasons']
        self.viewer_descr = {}

    def check_values(self):
        must_have_params = ['reference_data_path', 'test_data_path', 'results_dir']

        for param in must_have_params:
            if not hasattr(self, param):
                msg = 'You need to specify {p} in the parameters file or via the command line using --{p}'.format(p=param)
                raise RuntimeError(msg)
