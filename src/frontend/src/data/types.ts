export type EmailType = {
  id: string;
  date: string;
  category: "feedback" | "client" | "spam" | "others";
  email: string;
  content: { heading: string; body: string };
  user: { name: string; imgHref: string };
};
export type FeedbackDataType = {
  id: string;
  sender: { name: string; email: string };
  content: { subject: string; body: string };
  date: string;
};
export type SummaryDataType = {
  sender: string;
  products?: {
    id: string;
    name: string;
    status: string;
    summary: string[];
  }[];
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

// mock data
export type feedbackType = {
  email: string;
  id: string;
  time: string;
  content: string;
  user: { name: string; imgHref: string };
  tags: string[];
};
