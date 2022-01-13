# library
install.packages("ggplot2")
install.packages("dplyr")
install.packages("tidyr")
install.packages("lubridate")
install.packages("gganimate")
install.packages("broom.mixed")
install.packages("gifski")
install.packages("av")


library(ggplot2)
library(dplyr)
library(tidyr)
library(lubridate)
library(gganimate)
library(broom.mixed)
library(gifski)
library(av)

data <- read.csv(file.choose(), header = T)
summary(data)


head(data$date_confirmation)

#handling data

datanew <- data %>%
  mutate(date_confirmation = dmy(date_confirmation))
datanew %>% group_by(date_confirmation) %>% 
  summarise(count = n()) %>% 
  mutate(cuml = cumsum(count)) %>% 
  ggplot(aes(x = date_confirmation, y = cuml)) +
  geom_line(color = 'red') +
  geom_point(size = 1.5) +
  geom_area(fill = 'red') +
  theme_bw() +
  ggtitle('Daily Commulative Cases') +
  transition_reveal(cuml)

head(datanew$date_confirmation)
head(data$date_confirmation)

# saving animation
anim_save('CumlPlot')

# data completion
datanew$day <- day(datanew$date_confirmation)
datanew$month <- month(datanew$date_confirmation)
new <- datanew %>%
  filter(month == 3) %>%
  group_by(day, country) %>%
  summarise(count = n())
new <- data.frame(complete(new, day, country,
                           fill = list(count = 0)))
new
# Animated daily line plot
new %>% filter(country == 'United States' |
                 country == 'France' |
                 country == 'United Kingdom' |
                 country == 'Germany') %>%
  ggplot(aes(x = day, y = count, group = country,
             color = country)) +
  geom_line() +
  
  geom_point() +
  
  ggtitle('Animated daily plot') +
  transition_reveal(day)
# Data for bar plot
new <- datanew %>% 
  filter(country == 'United States' |
           country == 'France' |
           country == 'United Kingdom' |
           country == 'Germany') %>% 
  filter(month == 2| month == 3) %>% 
  group_by(country, month) %>% 
  summarise(count = n())
# bar plot
p <- new %>% ggplot(aes(x = country, 
                        y = count,
                        fill = country)) +
  geom_bar(stat = 'identity') +
  geom_point(size = 1.5) +
  #scale_y_log10() +
  theme_bw() +
  guides(fill = "none")

# Animated bar plot by month
p + transition_time(as.integer(month)) +
  labs(title = 'Animated Bar Plot by Month',
       subtitle = 'Month: {frame_time}')

# Animated bar plot by country
p + transition_states(count) +
  labs(title = 'Animated bar plot by countries') +
  shadow_mark() +
  enter_grow()




