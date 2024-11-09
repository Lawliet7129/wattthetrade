% BlackScholes.m
function [callPrice, putPrice] = BlackScholes(S, K, T, r, sigma)
    % Calculate d1 and d2
    d1 = (log(S / K) + (r + sigma^2 / 2) * T) / (sigma * sqrt(T));
    d2 = d1 - sigma * sqrt(T);

    % Calculate call and put prices
    callPrice = S * normcdf(d1) - K * exp(-r * T) * normcdf(d2);
    putPrice = K * exp(-r * T) * normcdf(-d2) - S * normcdf(-d1);

    % Save results to JSON for use in backend
    optionPrices = struct('callPrice', callPrice, 'putPrice', putPrice);
    savejson('', optionPrices, 'optionPrices.json');
end
