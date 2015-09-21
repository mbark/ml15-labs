function [s] = subset(data, i, c)
ind = find(data(:,i) == c);
s = data(ind,:);