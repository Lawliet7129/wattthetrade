% BlackScholes.m
function [callPrice, putPrice] = BlackScholes(S, K, T, r, sigma)
    d1 = (log(S / K) + (r + 0.5 * sigma^2) * T) / (sigma * sqrt(T));
    d2 = d1 - sigma * sqrt(T);

    callPrice = S * normcdf(d1) - K * exp(-r * T) * normcdf(d2);
    putPrice = K * exp(-r * T) * normcdf(-d2) - S * normcdf(-d1);

    optionPrices = struct('callPrice', callPrice, 'putPrice', putPrice);
    savejson('', optionPrices, 'optionPrices.json');
end
