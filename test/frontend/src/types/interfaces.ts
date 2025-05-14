export interface Service {
  ServiceID: number
  CategoryID: number
  Title: string
  Description: string
  DatePosted: string // or `Date` if you parse it before use
  CleanerID: number
  LikeCount: number
  ViewCount: number
  MatchCount: number
  Price: number
  ImageLink: string
}
export interface User {
  Address: string
  Email: string
  Experience: number
  IsActive: boolean
  Phone: string
  Privilege: string // narrow this union if there are other known values
  UPActive: boolean
  UserID: number
  UserProfile: number
  UserProfileName: string
  Username: string
}
