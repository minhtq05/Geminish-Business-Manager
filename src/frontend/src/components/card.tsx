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
  heading: string;
  subheading?: string;
  className?: string;
  children: React.ReactNode;
  props?: React.ComponentPropsWithoutRef<"div">;
}

const CardUI: React.FC<CardUIProps> = ({
  heading,
  subheading,
  children,
  className,
  ...props
}: CardUIProps) => {
  return (
    <Card
      className={cn("drop-shadow-sm subpixel-antialiased", className)}
      {...props}
    >
      <CardHeader>
        <CardTitle className="text-4xl text-gray-800">{heading}</CardTitle>
        <CardDescription className="text-gray-600text-gray-600">
          {subheading}
        </CardDescription>
      </CardHeader>
      <Separator />
      <CardContent>{children}</CardContent>
      <CardFooter>
        <Button>Learn more</Button>
      </CardFooter>
    </Card>
  );
};
export default CardUI;
