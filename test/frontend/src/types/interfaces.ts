export interface Service {
  ServiceID: number
  CategoryID: number
  Title: string
  Description: string
  DatePosted: string // or Date
  CleanerID: number
  LikeCount: number
  ViewCount: number
  MatchCount: number
  Price: number
  ImageLink: string
}
//this user is for the own Logged in User
export interface User {
  Address: string
  Email: string
  Experience: number
  IsActive: boolean
  Phone: string
  Privilege: string
  UPActive: boolean
  UserID: number
  UserProfile: number
  UserProfileName: string
  Username: string
}
//this UserAccount is for useradmin view UserAccounts type
export interface UserAccount {
  UserID: number
  Username: string
  Email: string
  Phone: string
  IsActive: boolean
  UserProfile: number
  Address: boolean
  Experience: string | null
}
export interface CustomUserAccount {
  UserProfileName: string
  Privilege: string
  UPActive: boolean
  UserID: number
  Username: string
  Email: string
  Phone: string
  IsActive: boolean
  UserProfile: number
  Address: string | null
  Experience: number
}
export interface UserProfile {
  UserProfileID: number
  Name: string
  Privilege: string
  Is_Active: boolean
}
export interface CreateUserType {
  username: string
  email: string
  phone: string
  address: string
  Experience: number
  UserProfileID: number
}
export interface UpdateUserType {
  username: string
  email: string
  phone: string
  IsActive: boolean
  UserID: number
  address: string
  Experience: number
  UserProfileID: number
}
// Inherit from Service
export interface CustomService extends Service {
  // Category details
  CatTitle: string
  CatDesc: string
  CatActive: boolean

  // Cleaner/User details
  Username: string
  Email: string
  Phone: string
  UActive: boolean
  Experience: number
}

// Inherit from CustomService, which already includes Service fields
//remove Username as we want it to be cleanerName instead
//email phone will be assuumed to be blonging to cleaner
export type CustomMatch = Omit<CustomService, 'Username'> & {
  CleanerName: string
  //HomeOwnerDetails
  HomeOwnerName: string
  Address: string
  // Match details
  DealPrice: number
  DealDate: string
  ImageLink: string
}
export interface SimpleMatch {
  ServiceID: number
  Title: string
  Price: number
  ImageLink: string
  MatchID: number
  DealPrice: number
  DealDate: string // or Date, depending on how you're parsing it in the frontend
}

export function getRandomImgurLink() {
  const imgurLinks = [
    'https://i.imgur.com/hLNZVyO.jpeg',
    'https://i.imgur.com/lqQeSfx.jpeg',
    'https://i.imgur.com/xVkYiuZ_d.webp?maxwidth=1520&fidelity=grand',
    'https://i.imgur.com/Vz0hwqb.jpeg',
  ]

  const randomIndex = Math.floor(Math.random() * imgurLinks.length)
  return imgurLinks[randomIndex]
}
