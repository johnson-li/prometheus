load('/Users/johnson/PycharmProjects/prometheus/matlab/resources/tcp_traffic_ratio_per_target.mat')

hold on
% errorbar(1:5, http1_response_ratios_50, http1_response_ratios_50 - http1_response_ratios_5, http1_response_ratios_95 - http1_response_ratios_50, 'x')
errorbar(1:5, http2_response_ratios_50, http2_response_ratios_50 - http2_response_ratios_5, http2_response_ratios_95 - http2_response_ratios_50, 'x')

ylim([0.9 5])
