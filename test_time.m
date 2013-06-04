Y1 = [0.3174290657043457;1.6768231391906738;3.4251248836517334;8.374122858047485;15.609631061553955];
Y2 = [0.20072007179260254; 0.9606108665466309; 1.9028711318969727; 4.9337849617004395; 9.712602853775024];
X = [1:5]';
plot(X, X, X,Y2,X,X .^ log(X), X,Y1, X, X .^ 2);
xlabel("number of triples, |I|");
ylabel("Execution time, sec");
legend("Linear", "Storing", "Linearithmic", "No storing", "Quadratic");

