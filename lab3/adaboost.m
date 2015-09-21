function [mu, sigma, p, alpha, classes] = adaboost(data, T)
mu = [];
sigma = [];
p = [];
alpha = [];
classes = [0,1];

w = ones(size(data, 1),1) ./ size(data, 1);

for t=1:T
    [mu(:,:,t), sigma(:,:,t)] = bayes_weight(data, w);
    p(t,:) = prior(data, w);
    g = discriminant(data(:,1:2), mu(:,:,t), sigma(:,:,t), p(t,:));
    [dummy class] = max(g, [], 2);

    class = class - 1;
    epsilon = 1.0-sum(w.*(class == data(:,end)));

    alpha(t) = 1/(2*log((1-epsilon)/epsilon));
    alph = (data(:,end) == class)*-1;
    w = w.*exp(alph.*alpha(t));
    w = w./sum(w);
end