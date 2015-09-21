function g = discriminant(data, mu, sigma, p)
for i=1:2
    g_i = log(p(i));
    tmp_1 = 0;
    tmp_2 = 0;
    
    for n=1:2
        tmp_1 = tmp_1 + log(sigma(i,n));
        tmp_2 = tmp_2 + (data(:,n) - mu(i,n)).^2/(2*sigma(i,n)^2);
    end
    g_i = g_i - tmp_1 - tmp_2;
    g(i,:) = g_i;
end
g = transpose(g);
    