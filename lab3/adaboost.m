function [mu, sigma, p, alpha, classes] = adaboost(data, T)
w = ones(size(data, 1),1) ./ size(data, 1);
bayes(data)
bayes_weight(data, w)