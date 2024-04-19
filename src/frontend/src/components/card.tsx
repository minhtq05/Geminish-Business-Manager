import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { Button } from "./ui/button";
import { cn } from "@/lib/utils";
interface CardUIProps {
  heading?: string;
  subheading?: string;
  className?: string;
  children?: React.ReactNode | React.ReactNode[];
  footer?: React.ReactNode;
  props?: React.ComponentPropsWithoutRef<"div">;
  colorScheme?: {
    bgColor: string | "text-current";
    textColor: string | "bg-current";
  };
}

const CardUI: React.FC<CardUIProps> = ({
  heading,
  subheading,
  children,
  className,
  colorScheme,
  footer,
  ...props
}: CardUIProps) => {
  const { bgColor, textColor } = colorScheme
    ? colorScheme
    : { bgColor: "text-current", textColor: "bg-current" };
  return (
    <Card
      className={cn(
        "drop-shadow-lg subpixel-antialiased rounded-md",
        className
      )}
      {...props}
    >
      <CardHeader className={cn("rounded-t-md", bgColor)}>
        <CardTitle className={cn("text-4xl", textColor)}>{heading}</CardTitle>
        <p className={cn("text-4xl", textColor)}>{subheading}</p>
      </CardHeader>
      <CardContent className={cn("py-10 rounded-b-md", bgColor, textColor)}>
        {children}
      </CardContent>
      {footer ? <CardFooter>{footer}</CardFooter> : null}
    </Card>
  );
};
export default CardUI;
