export type Email = {
  id: string;
  date: string;
  category: "feedback" | "client" | "spam" | "others";
  email: string;
  content: string;
};
export type TextCard = {
  heading: string;
  subheading?: string;
  content: string;
};
