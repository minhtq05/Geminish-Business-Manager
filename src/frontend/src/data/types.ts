export type Email = {
  id: string;
  date: string;
  category: "feedback" | "client" | "spam" | "others";
  email: string;
  content: string;
};
export type AnalyticText = {
  heading: string;
  subheading?: string;
  content: string;
};
export type NavLink = {
  name: string;
  url: string;
};
export type feedbackType = {
  email: string;
  id: string;
  time: string;
  content: string;
  user: { name: string; imgHref: string };
  tags: string[];
};
