function [mu, sigma] = bayes(data)
mu = zeros(2,2);
sigma = zeros(2,2);

for i=1:2
    data_sub = subset(data, 3, i-1);
    for n=1:2
        mu(i,n) = mean(data_sub(:,n));
    end
end

for i=1:2
    data_sub = subset(data, 3, i-1);
    for n=1:2
        sigma(i,n) = std(data_sub(:,n));
    end
end

mu
sigma


