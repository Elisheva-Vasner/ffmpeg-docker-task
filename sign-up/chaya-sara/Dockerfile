FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app
COPY  src/strongPassword ./strongPassword
RUN javac strongPassword/StrongPassword.java
CMD ["java","strongPassword.StrongPassword"]


# /*src/strongPassword/StrongPassword.java StrongPassword.java*/