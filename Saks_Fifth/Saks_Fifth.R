library(RJSONIO)

df <- fromJSON("https://saksfifthavenue.brickworksoftware.com/en/api/v3/stores.json?upcoming_events=true")


data <- df[['stores']]

name <- vector()
address <- vector()
city <- vector()
state <- vector()
zip <- vector()
telephone <- vector()
URL <- vector()
image_url <- vector()
manager <- vector()
Sunday_Open <- vector()
Sunday_Close <- vector()
Monday_Open <- vector()
Monday_Close <- vector()
Tuesday_Open <- vector()
Tuesday_Close <- vector()
Wednesday_Open <- vector()
Wednesday_Close <- vector()
Thursday_Open <- vector()
Thursday_Close <- vector()
Friday_Open <- vector()
Friday_Close <- vector()
Saturday_Open <- vector()
Saturday_Close <- vector()
phone <- vector()
a <- vector()

for (i in 1:46){
  name[i] <- paste("Saks Fifth Haven in", data[i][[1]]$name, sep = " ")
  address[i] <- trimws(paste(data[i][[1]]$address_1,data[i][[1]]$address_2, data[i][[1]]$address_3, sep = " "))
  city[i] <- data[i][[1]]$city
  state[i] <- ifelse(data[i][[1]]$state != "", data[i][[1]]$state, data[i][[1]]$country_code)
  zip[i] <- data[i][[1]]$postal_code
  phone[i] <- data[i][[1]]$phone_number
  URL[i] <- paste("https://www.saksfifthavenue.com/locations/s/", data[i][[1]]$slug, sep = "")
  image_url[i] <- data[i][[1]]$store_hero_images[1][[1]]$url
  manager[i] <- "None"
  if (i != 42){
    Sunday_Open[i]<- data[i][[1]]$regular_hours[[1]]$display_start_time
    Sunday_Close[i] <- data[i][[1]]$regular_hours[[1]]$display_end_time
    Monday_Open[i] <- data[i][[1]]$regular_hours[[2]]$display_start_time
    Monday_Close[i] <- data[i][[1]]$regular_hours[[2]]$display_end_time
    Tuesday_Open[i] <- data[i][[1]]$regular_hours[[3]]$display_start_time
    Tuesday_Close[i] <- data[i][[1]]$regular_hours[[3]]$display_end_time
    Wednesday_Open[i] <- data[i][[1]]$regular_hours[[4]]$display_start_time
    Wednesday_Close[i] <- data[i][[1]]$regular_hours[[4]]$display_end_time
    Thursday_Open[i] <- data[i][[1]]$regular_hours[[5]]$display_start_time
    Thursday_Close[i] <- data[i][[1]]$regular_hours[[5]]$display_end_time
    Friday_Open[i] <- data[i][[1]]$regular_hours[[6]]$display_start_time
    Friday_Close[i] <- data[i][[1]]$regular_hours[[6]]$display_end_time
    Saturday_Open[i] <- data[i][[1]]$regular_hours[[7]]$display_start_time
    Saturday_Close[i] <- data[i][[1]]$regular_hours[[7]]$display_end_time
  }
  if (i == 42){  
    Sunday_Open[i] <- "Closed"
    Sunday_Close[i] <- "Closed"
    Monday_Open[i] <- "Closed"
    Monday_Close[i] <- "Closed"
    Tuesday_Open[i] <- "Closed"
    Tuesday_Close[i] <- "Closed"
    Wednesday_Open[i] <- "Closed"
    Wednesday_Close[i] <- "Closed"
    Thursday_Open[i] <- "Closed"
    Thursday_Close[i] <- "Closed"
    Friday_Open[i] <- "Closed"
    Friday_Close[i] <- "Closed"
    Saturday_Open[i] <- "Closed"
    Saturday_Close[i] <- "Closed"}
}

telephone <- ifelse(str_detect(phone, "\\d{3}.\\d{3}.\\d{4}"),
                    paste("(", str_extract(phone, "\\d{3}"), ")", str_extract(phone, "(?<=\\d{3}.)\\d{3}"), "-", str_extract(phone, "\\d{4}"), sep = ""),
                    phone)

store_name <- "Saks Fifth Avenue"
Saks_Fifth <- as.data.frame(cbind(store_name, name, address, city, state, zip, telephone, manager, URL, image_url, Sunday_Open,
                                  Sunday_Close, Monday_Open, Monday_Close, Tuesday_Open, Tuesday_Close, Wednesday_Open, 
                                  Wednesday_Close, Thursday_Open, Thursday_Close, Friday_Open, Friday_Close, Saturday_Open,
                                  Saturday_Close))
Saks_Fifth <- Saks_Fifth %>%
  mutate_all(as.character)

Saks_Fifth[is.na(Saks_Fifth) == TRUE] <- "NA"
Saks_Fifth[Saks_Fifth == ""] <- "NA"
Saks_Fifth$state <- state.abb[match(Saks_Fifth$state, state.name)]
Saks_Fifth$X1 <- NULL
Saks_Fifth[Saks_Fifth == "None"] <- "NA"

write.csv(Saks_Fifth, "C:\\Users\\switkowski\\Documents\\FreeLance\\luxury_stores\\Saks_Fifth\\Saks_Fifth_Stores.csv")
