function [mu, sigma] = bayes_weight(data, w)
mu = zeros(2,2);
sigma = zeros(2,2);

for i=1:2
    for n=1:2
        wsum = 0;
        for m=1:size(data)
            if(data(m,3) == i-1)
                mu(i,n) = mu(i,n) + w(m)*data(m,n);
                wsum = wsum + w(m);
            end
        end
        mu(i,n) = mu(i,n) / wsum;
    end
end

for i=1:2
    for n=1:2
        wsum = 0;
        for m=1:size(data)
            if(data(m,3) == i-1)
                sigma(i,n) = sigma(i,n) + w(m)*(data(m,n) - mu(i,n))^2;
                wsum = wsum + w(m);
            end
        end
        sigma(i,n) = sqrt(sigma(i,n) / wsum);
    end
end